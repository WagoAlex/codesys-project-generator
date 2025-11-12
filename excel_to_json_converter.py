# -*- coding: utf-8 -*-
"""
WAGO PLC Configuration Extractor
Extracts PLC configurations from Excel and generates JSON config files
"""

import pandas as pd
import json
import os
import re
from datetime import datetime
from collections import defaultdict


class PLCConfigExtractor:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.plcs = {}
        self.validation_log = []
        self.stats = {
            'total_plcs': 0,
            'total_signals': 0,
            'total_modules': 0,
            'warnings': 0,
            'errors': 0
        }
        
    def log_warning(self, message):
        """Log a warning message"""
        self.validation_log.append(f"[WARNING] {message}")
        self.stats['warnings'] += 1
        print(f"WARNING: {message}")
    
    def log_error(self, message):
        """Log an error message"""
        self.validation_log.append(f"[ERROR] {message}")
        self.stats['errors'] += 1
        print(f"ERROR: {message}")
    
    def log_info(self, message):
        """Log an info message"""
        self.validation_log.append(f"[INFO] {message}")
        print(f"INFO: {message}")
    
    def validate_ip_address(self, ip):
        """Validate IP address format only"""
        if not ip or pd.isna(ip):
            return False, "IP address is empty"
        
        ip_str = str(ip).strip()
        
        # Check IP format
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        match = re.match(pattern, ip_str)
        
        if not match:
            return False, f"Invalid IP format: {ip_str}"
        
        octets = [int(x) for x in match.groups()]
        
        # Check valid range (0-255 for each octet)
        if any(o < 0 or o > 255 for o in octets):
            return False, f"IP octets out of range: {ip_str}"
        
        return True, ip_str
    
    def extract_plc_type(self, type_str):
        """
        Extract PLC type from string.
        Looks for patterns like 750-8xxx
        
        Examples:
            "750-8210" -> "750-8210"
            "750-8212" -> "750-8212"
            "750-8210/025-000" -> "750-8210/025-000"
            "PFC200 750-8210" -> "750-8210"
        """
        if not type_str or pd.isna(type_str):
            return None
        
        type_str = str(type_str).strip()
        
        # Pattern to match 750-8xxx with optional /xxx-xxx suffix
        pattern = r'750-8\d{3}(?:/\d{3}-\d{3})?'
        match = re.search(pattern, type_str)
        
        if match:
            return match.group(0)
        
        return None
    
    def extract_plcs_from_io_boxes(self):
        """Extract PLC information from IO-Boxen sheet"""
        self.log_info(f"Reading IO-Boxen sheet from {os.path.basename(self.excel_file)}...")
        
        try:
            # Try reading with header=0 first (new format)
            df = pd.read_excel(self.excel_file, sheet_name='IO-Boxen', header=0)
            
            # Check if we have the expected columns
            if 'PLC' not in df.columns or 'IP-Adress' not in df.columns:
                # Try with header=3 (old format)
                df = pd.read_excel(self.excel_file, sheet_name='IO-Boxen', header=3)
            
            # Clean column names
            df.columns = df.columns.str.strip()
            
            self.log_info(f"Found {len(df)} rows in IO-Boxen sheet")
            
            # Process each row
            plc_count = 0
            for idx, row in df.iterrows():
                # Skip if PLC column is empty
                if pd.isna(row.get('PLC')) or str(row.get('PLC')).strip() == '':
                    continue
                
                plc_name = str(row['PLC']).strip()
                
                # Skip placeholder text rows
                if plc_name.lower() == 'text':
                    continue
                
                # Extract data
                io_box = str(row.get('IO BOX', '')).strip() if not pd.isna(row.get('IO BOX')) else ''
                location = str(row.get('Location', '')).strip() if not pd.isna(row.get('Location')) else ''
                ip_address = str(row.get('IP-Adress', '')).strip() if not pd.isna(row.get('IP-Adress')) else ''
                
                # Validate IP
                ip_valid, ip_result = self.validate_ip_address(ip_address)
                
                if not ip_valid:
                    self.log_error(f"PLC {plc_name}: {ip_result}")
                    continue
                
                # Extract PLC type from available columns
                plc_type = '750-8210'  # Default
                
                # Method 1: Check for columns with PLC type names (e.g., '750-8210', '750-8212')
                # Look for an 'X' marker in these columns
                plc_type_columns = [col for col in df.columns if re.match(r'750-8\d{3}', str(col))]
                
                if plc_type_columns:
                    # Check which column has an 'X' marker for this row
                    for type_col in plc_type_columns:
                        cell_value = row.get(type_col, '')
                        
                        # Handle both NaN and string 'NAN'
                        if pd.isna(cell_value):
                            continue
                        
                        cell_value_str = str(cell_value).strip().upper()
                        
                        # Check for 'X' marker (ignore 'NAN' strings)
                        if cell_value_str == 'X':
                            # Extract the PLC type from the column name
                            extracted_type = self.extract_plc_type(type_col)
                            if extracted_type:
                                plc_type = extracted_type
                                break
                
                # Method 2: Check common column names for PLC type
                if plc_type == '750-8210':  # Only if not found via X marker
                    for col in ['Type', 'PLC Type', 'Device Type', 'Gerätetyp', 'Typ']:
                        if col in df.columns and not pd.isna(row.get(col)):
                            extracted_type = self.extract_plc_type(row.get(col))
                            if extracted_type:
                                plc_type = extracted_type
                                break
                
                # Method 3: If still not found, check all column values
                if plc_type == '750-8210':
                    for col_value in row.values:
                        if pd.isna(col_value):
                            continue
                        extracted_type = self.extract_plc_type(col_value)
                        if extracted_type:
                            plc_type = extracted_type
                            break
                
                # Create PLC entry
                if plc_name not in self.plcs:
                    self.plcs[plc_name] = {
                        'PLC_Info': {
                            'Name': plc_name,
                            'Type': plc_type,
                            'IP_Address': ip_result,
                            'Location': location,
                            'IO_Box': io_box
                        },
                        'IO_Modules': {},
                        'Statistics': {
                            'Total_Modules': 0,
                            'Total_Signals': 0,
                            'Input_Signals': 0,
                            'Output_Signals': 0
                        }
                    }
                    plc_count += 1
                    self.log_info(f"Added PLC: {plc_name} ({ip_result}) - Type: {plc_type}")
                else:
                    self.log_warning(f"Duplicate PLC entry found: {plc_name}")
            
            self.stats['total_plcs'] = plc_count
            self.log_info(f"Successfully extracted {plc_count} PLCs from IO-Boxen")
            
        except Exception as e:
            self.log_error(f"Failed to read IO-Boxen sheet: {str(e)}")
            raise
    
    def extract_signals_from_signallist(self):
        """Extract signals from SIGNALLIST sheet and assign to PLCs"""
        self.log_info(f"Reading SIGNALLIST sheet...")
        
        try:
            # Read SIGNALLIST sheet - header is in row 1 (index 0)
            df = pd.read_excel(self.excel_file, sheet_name='SIGNALLIST', header=0)
            
            # Clean column names
            df.columns = df.columns.str.strip()
            
            self.log_info(f"Found {len(df)} rows in SIGNALLIST")
            
            signal_count = 0
            unassigned_count = 0
            
            for idx, row in df.iterrows():
                # Skip rows without PLC assignment
                if pd.isna(row.get('PLC')) or str(row.get('PLC')).strip() == '':
                    continue
                
                plc_name = str(row['PLC']).strip()
                
                # Skip placeholder text
                if plc_name.lower() == 'text':
                    continue
                
                # Check if PLC exists
                if plc_name not in self.plcs:
                    if unassigned_count == 0:
                        self.log_warning(f"Signal found for unknown PLC: {plc_name}")
                    unassigned_count += 1
                    continue
                
                # Extract signal data
                module_type = str(row.get('Mode_Type', '')).strip() if not pd.isna(row.get('Mode_Type')) else ''
                terminal = str(row.get('PLC_terminal', '')).strip() if not pd.isna(row.get('PLC_terminal')) else ''
                object_name = str(row.get('Objektname', '')).strip() if not pd.isna(row.get('Objektname')) else ''
                signal_type = str(row.get('Type', '')).strip() if not pd.isna(row.get('Type')) else ''
                signal = str(row.get('Signal', '')).strip() if not pd.isna(row.get('Signal')) else ''
                
                # Skip if critical data is missing
                if not module_type or not terminal or not object_name:
                    continue
                
                # Create signal entry
                signal_entry = {
                    'Terminal': terminal,
                    'Object_Name': object_name,
                    'Signal_Type': signal_type,
                    'Signal': signal
                }
                
                # Add to PLC's modules (group by module type)
                if module_type not in self.plcs[plc_name]['IO_Modules']:
                    self.plcs[plc_name]['IO_Modules'][module_type] = {
                        'Module_Type': module_type,
                        'Signals': []
                    }
                
                self.plcs[plc_name]['IO_Modules'][module_type]['Signals'].append(signal_entry)
                
                # Update statistics
                self.plcs[plc_name]['Statistics']['Total_Signals'] += 1
                if signal_type.upper() == 'I':
                    self.plcs[plc_name]['Statistics']['Input_Signals'] += 1
                elif signal_type.upper() == 'O':
                    self.plcs[plc_name]['Statistics']['Output_Signals'] += 1
                
                signal_count += 1
            
            # Update module counts
            for plc_name, plc_data in self.plcs.items():
                plc_data['Statistics']['Total_Modules'] = len(plc_data['IO_Modules'])
            
            self.stats['total_signals'] = signal_count
            self.stats['total_modules'] = sum(len(plc['IO_Modules']) for plc in self.plcs.values())
            
            if unassigned_count > 0:
                self.log_warning(f"Total signals for unknown PLCs: {unassigned_count}")
            
            self.log_info(f"Successfully extracted {signal_count} signals")
            
        except Exception as e:
            self.log_error(f"Failed to read SIGNALLIST sheet: {str(e)}")
            raise
    
    def generate_json_files(self, output_dir):
        """Generate JSON configuration files for each PLC"""
        self.log_info(f"Generating JSON files in {output_dir}...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        generated_files = []
        
        for plc_name, plc_data in self.plcs.items():
            # Convert IO_Modules dict to list
            plc_output = plc_data.copy()
            plc_output['IO_Modules'] = list(plc_data['IO_Modules'].values())
            
            # Add metadata
            plc_output['Metadata'] = {
                'Generated': datetime.now().isoformat(),
                'Source_File': os.path.basename(self.excel_file),
                'Generator': 'WAGO PLC Config Extractor v2.0'
            }
            
            # Generate filename
            filename = f"PLC_{plc_name}_config.json"
            filepath = os.path.join(output_dir, filename)
            
            # Write JSON
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(plc_output, f, indent=2, ensure_ascii=False)
            
            generated_files.append(filename)
            self.log_info(f"Generated: {filename}")
        
        return generated_files
    
    def generate_summary(self, output_dir):
        """Generate summary.txt with overview of all PLCs"""
        summary_path = os.path.join(output_dir, 'summary.txt')
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("WAGO PLC Configuration - Summary Report\n")
            f.write("="*70 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source File: {os.path.basename(self.excel_file)}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"Total PLCs: {self.stats['total_plcs']}\n")
            f.write(f"Total IO Modules: {self.stats['total_modules']}\n")
            f.write(f"Total Signals: {self.stats['total_signals']}\n\n")
            
            f.write("PLC Overview:\n")
            f.write("-"*70 + "\n")
            
            for plc_name, plc_data in sorted(self.plcs.items()):
                info = plc_data['PLC_Info']
                stats = plc_data['Statistics']
                
                f.write(f"\n{plc_name}:\n")
                f.write(f"  Type: {info['Type']}\n")
                f.write(f"  IP Address: {info['IP_Address']}\n")
                f.write(f"  Location: {info['Location']}\n")
                f.write(f"  IO Box: {info['IO_Box']}\n")
                f.write(f"  Modules: {stats['Total_Modules']}\n")
                f.write(f"  Signals: {stats['Total_Signals']} (I: {stats['Input_Signals']}, O: {stats['Output_Signals']})\n")
        
        self.log_info(f"Generated: summary.txt")
        return summary_path
    
    def generate_validation_report(self, output_dir):
        """Generate validation_report.txt with warnings and errors"""
        report_path = os.path.join(output_dir, 'validation_report.txt')
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("WAGO PLC Configuration - Validation Report\n")
            f.write("="*70 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source File: {os.path.basename(self.excel_file)}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"Total Warnings: {self.stats['warnings']}\n")
            f.write(f"Total Errors: {self.stats['errors']}\n\n")
            
            if self.validation_log:
                f.write("Validation Log:\n")
                f.write("-"*70 + "\n")
                for log_entry in self.validation_log:
                    f.write(f"{log_entry}\n")
            else:
                f.write("No issues found.\n")
        
        self.log_info(f"Generated: validation_report.txt")
        return report_path
    
    def process(self, output_dir):
        """Main processing pipeline"""
        print("\n" + "="*70)
        print("WAGO PLC Configuration Extractor")
        print("="*70 + "\n")
        
        # Step 1: Extract PLCs
        self.extract_plcs_from_io_boxes()
        
        # Step 2: Extract Signals
        self.extract_signals_from_signallist()
        
        # Step 3: Generate JSON files
        json_files = self.generate_json_files(output_dir)
        
        # Step 4: Generate reports
        self.generate_summary(output_dir)
        self.generate_validation_report(output_dir)
        
        # Final summary
        print("\n" + "="*70)
        print("Processing Complete!")
        print("="*70)
        print(f"Generated {len(json_files)} PLC configuration files")
        print(f"Total signals processed: {self.stats['total_signals']}")
        print(f"Warnings: {self.stats['warnings']}")
        print(f"Errors: {self.stats['errors']}")
        print("="*70 + "\n")
        
        return json_files