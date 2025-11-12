# -*- coding: utf-8 -*-
"""
CODESYS IronPython Integration Example
Generates CODESYS-compatible variable lists from JSON configurations

Usage:
    python codesys_import_example.py --input=/path/to/json/configs [--plc=IO043]
    
Examples:
    # Process all PLCs in directory
    python codesys_import_example.py --input=/usr/src/app/misc/besecke/outputs
    
    # Process specific PLC
    python codesys_import_example.py --input=/usr/src/app/misc/besecke/outputs --plc=IO251
"""

import sys
import json
import os
import argparse
import glob


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='CODESYS IronPython Integration - JSON Config Importer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Process all PLCs
    python codesys_import_example.py --input=/path/to/configs
    
    # Process specific PLC
    python codesys_import_example.py --input=/path/to/configs --plc=IO251
        """
    )
    
    parser.add_argument(
        '--input',
        required=True,
        help='Path to directory containing JSON config files'
    )
    
    parser.add_argument(
        '--plc',
        default=None,
        help='Specific PLC name to process (e.g., IO251). If not specified, all PLCs are processed.'
    )
    
    return parser.parse_args()


def find_json_configs(config_dir):
    """Find all PLC JSON configuration files in directory"""
    pattern = os.path.join(config_dir, 'PLC_*_config.json')
    json_files = glob.glob(pattern)
    
    configs = []
    for json_file in sorted(json_files):
        basename = os.path.basename(json_file)
        # Extract PLC name from filename: PLC_IO251_config.json -> IO251
        plc_name = basename.replace('PLC_', '').replace('_config.json', '')
        configs.append({
            'plc_name': plc_name,
            'filepath': json_file
        })
    
    return configs


def load_plc_config(json_file):
    """Load PLC configuration from JSON file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"ERROR: Could not load JSON: {str(e)}")
        return None


def create_variable_list(config, output_file):
    """
    Creates variable list in IEC 61131-3 format
    Can be imported into CODESYS
    """
    plc_info = config['PLC_Info']
    plc_name = plc_info['Name']
    plc_type = plc_info['Type']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"(* Variable List for PLC: {plc_name} *)\n")
        f.write(f"(* PLC Type: {plc_type} *)\n")
        f.write(f"(* IP Address: {plc_info['IP_Address']} *)\n")
        f.write(f"(* Location: {plc_info['Location']} *)\n")
        f.write(f"(* Generated from JSON configuration *)\n\n")
        f.write("VAR_GLOBAL\n")
        
        for module in config['IO_Modules']:
            module_type = module['Module_Type']
            signals = module['Signals']
            f.write(f"\n  (* Module: {module_type} - {len(signals)} signals *)\n")
            
            for signal in signals:
                object_name = signal['Object_Name']
                signal_type = signal['Signal_Type']
                terminal = signal['Terminal']
                signal_spec = signal['Signal']
                
                # Determine data type and direction based on signal type
                if signal_type.upper() == 'I':
                    var_type = "BOOL"
                    direction = "AT %I*"
                elif signal_type.upper() == 'O':
                    var_type = "BOOL"
                    direction = "AT %Q*"
                else:
                    # For special types like RS485, RS232, etc.
                    var_type = "BOOL"
                    direction = ""
                
                # Write variable declaration
                comment = f"{terminal} - {signal_spec}"
                if direction:
                    f.write(f"  {object_name} {direction} : {var_type}; (* {comment} *)\n")
                else:
                    f.write(f"  {object_name} : {var_type}; (* {signal_type}: {comment} *)\n")
        
        f.write("\nEND_VAR\n")
    
    print(f"  Generated: {os.path.basename(output_file)}")
    return output_file


def print_config_summary(config):
    """Print configuration summary"""
    plc_info = config['PLC_Info']
    stats = config['Statistics']
    metadata = config.get('Metadata', {})
    
    print("\n" + "="*70)
    print(f"PLC Configuration: {plc_info['Name']}")
    print("="*70)
    print(f"Type:          {plc_info['Type']}")
    print(f"IP Address:    {plc_info['IP_Address']}")
    print(f"Location:      {plc_info['Location']}")
    print(f"IO Box:        {plc_info['IO_Box']}")
    print("-"*70)
    print(f"Modules:       {stats['Total_Modules']}")
    print(f"Signals:       {stats['Total_Signals']}")
    print(f"  - Inputs:    {stats['Input_Signals']}")
    print(f"  - Outputs:   {stats['Output_Signals']}")
    print("-"*70)
    if metadata:
        print(f"Generated:     {metadata.get('Generated', 'N/A')}")
        print(f"Source File:   {metadata.get('Source_File', 'N/A')}")
    print("="*70)


def print_module_summary(config):
    """Print summary of modules and signal types"""
    print("\nModule Summary:")
    print("-"*70)
    
    for module in config['IO_Modules']:
        module_type = module['Module_Type']
        signals = module['Signals']
        
        # Count signal types
        signal_types = {}
        for signal in signals:
            stype = signal['Signal_Type']
            signal_types[stype] = signal_types.get(stype, 0) + 1
        
        signal_summary = ", ".join([f"{count} {stype}" for stype, count in signal_types.items()])
        print(f"  {module_type}: {len(signals)} signals ({signal_summary})")


def process_plc(config_info, output_dir):
    """Process a single PLC configuration"""
    plc_name = config_info['plc_name']
    json_file = config_info['filepath']
    
    print(f"\nProcessing PLC: {plc_name}")
    print(f"Source: {os.path.basename(json_file)}")
    
    # Load configuration
    config = load_plc_config(json_file)
    if not config:
        print(f"ERROR: Failed to load configuration for {plc_name}")
        return False
    
    # Print summary
    print_config_summary(config)
    print_module_summary(config)
    
    print("\nGenerating output files...")
    
    # Generate IEC 61131-3 variable list
    var_list_file = os.path.join(output_dir, f"{plc_name}_variables.txt")
    create_variable_list(config, var_list_file)
    
    return True


def main():
    """Main function"""
    
    # Parse arguments
    args = parse_arguments()
    
    config_dir = args.input
    specific_plc = args.plc
    
    # Validate input directory
    if not os.path.exists(config_dir):
        print(f"ERROR: Input directory not found: {config_dir}")
        sys.exit(1)
    
    # Output directory is same as input directory
    output_dir = config_dir
    
    print("\n" + "="*80)
    print("CODESYS IronPython Integration - Variable List Generator")
    print("="*80)
    print(f"Input Directory: {config_dir}")
    print(f"Output Directory: {output_dir}")
    
    # Find all JSON configurations
    all_configs = find_json_configs(config_dir)
    
    if not all_configs:
        print(f"\nERROR: No PLC configuration files found in {config_dir}")
        print("Looking for files matching pattern: PLC_*_config.json")
        sys.exit(1)
    
    # Filter for specific PLC if requested
    if specific_plc:
        configs_to_process = [c for c in all_configs if c['plc_name'] == specific_plc]
        if not configs_to_process:
            print(f"\nERROR: PLC '{specific_plc}' not found")
            print(f"\nAvailable PLCs:")
            for cfg in all_configs:
                print(f"  - {cfg['plc_name']}")
            sys.exit(1)
        print(f"Processing specific PLC: {specific_plc}")
    else:
        configs_to_process = all_configs
        print(f"Found {len(all_configs)} PLC configuration(s)")
        print("Processing all PLCs...")
    
    # Process each PLC
    success_count = 0
    failed_count = 0
    
    for config_info in configs_to_process:
        try:
            if process_plc(config_info, output_dir):
                success_count += 1
            else:
                failed_count += 1
        except Exception as e:
            print(f"\nERROR: Failed to process {config_info['plc_name']}: {str(e)}")
            import traceback
            traceback.print_exc()
            failed_count += 1
    
    # Print final summary
    print("\n" + "="*80)
    print("PROCESSING COMPLETE")
    print("="*80)
    print(f"Total PLCs processed: {success_count + failed_count}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"\nOutput directory: {output_dir}")
    print("\nGenerated files:")
    print(f"  - *_variables.txt (IEC 61131-3 variable lists)")
    print("="*80 + "\n")
    
    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    # Check if running in CODESYS context
    try:
        if 'projects' in dir():
            print("INFO: CODESYS context detected - full import possible")
        else:
            print("INFO: Standalone mode - file generation only")
    except:
        print("INFO: Standalone mode - file generation only")
    
    main()
