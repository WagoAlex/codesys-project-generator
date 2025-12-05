# PLC Configuration Toolchain
Automated extraction, conversion, and CODESYS integration of PLC configurations
Version: 2.1  
Last Update: November 2025
---
## 📋 Table of Contents
- [General Overview](#-general-overview)
  - [What is this project?](#what-is-this-project)
  - [Key Features](#key-features)
  - [Who should use this tool?](#who-should-use-this-tool)
- [Architectural Overview & Usage Guide](#-architectural-overview--usage-guide)
  - [System Architecture](#system-architecture)
  - [Workflow Diagram](#workflow-diagram)
  - [Quick Start](#quick-start)
  - [Detailed Usage Guide](#detailed-usage-guide)
- [Developer Documentation](#-developer-documentation)
  - [Project Structure](#project-structure)
  - [Component Details](#component-details)
  - [Data Flow & Interfaces](#data-flow--interfaces)
  - [Extension & Customization](#extension--customization)
---
## 🎯 General Overview
### What is this project?
The WAGO PLC Configuration Toolchain is a comprehensive automation solution for managing and integrating WAGO PLC configurations. It transforms Excel-based measuring point lists into structured JSON configurations and CODESYS-compatible project files.
#### Problem Statement
In industrial automation projects, PLC configurations are often maintained in Excel documents:
- Hundreds to thousands of I/O signals per project
- Manual transfer into CODESYS is error-prone and time-consuming
- No central version control or validation
- Difficult traceability of changes
#### Solution
This toolchain automates the entire workflow:
1. Extraction: Reads structured data from Excel files
2. Validation: Checks IP addresses, module definitions, and signal consistency
3. Transformation: Generates JSON configurations and IEC 61131-3 variable lists
4. Integration: Creates complete CODESYS projects via IronPython ScriptEngine
### Key Features
#### ✅ Excel-to-JSON Conversion
- Automatic detection of up to 5 PLCs per project
- Extraction of I/O module configurations (750-4xx, 750-5xx, 750-6xx)
- Validation of IP addresses (172.16.46.x, 172.16.60.x)
- Generation of structured JSON files
#### ✅ CODESYS Integration
- Automatic project creation from template
- Configuration of K-Bus I/O modules
- Import of variable lists (IEC 61131-3 standard)
- IP address configuration of PLC devices
#### ✅ Quality Assurance
- Comprehensive validation reports
- Warnings for invalid entries
- Statistics per PLC (modules, signals, I/O types)
- Logging of all processing steps
### Who should use this tool?
#### 🎯 Target audiences
Automation Engineers
- Create PLC projects from plant documentation
- Rapid integration of new I/O configurations
- Consistent project structures
System Integrators
- Batch processing of multiple PLCs
- Standardized project templates
- Documentation and traceability
Project Managers
- Overview of project scope (number of signals, modules)
- Validation of planning data
- Quality assurance prior to commissioning
---
## 🏗️ Architectural Overview & Usage Guide
### System Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                         INPUT LAYER                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Excel file: LIST_OF_MEASURING_POINTS.xls                │   │
│  │  ┌──────────────┬──────────────┬───────────────────┐     │   │
│  │  │  IO Boxes    │  SIGNALLIST  │  LOCATION/LEGEND  │     │   │
│  │  │  (PLC info)  │  (signals)   │  (metadata)       │     │   │
│  │  └──────────────┴──────────────┴───────────────────┘     │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  batch_processor.py                                      │   │
│  │  ├─► excel_to_json_converter.py (PLCConfigExtractor)     │   │
│  │  │   ├─► Extract PLCs (IO Boxes sheet)                   │   │
│  │  │   ├─► Extract signals (SIGNALLIST sheet)              │   │
│  │  │   ├─► Validate IP addresses                           │   │
│  │  │   ├─► Group by module type                            │   │
│  │  │   └─► Calculate statistics                            │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT LAYER                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  JSON configurations                                     │   │
│  │  ├─► PLC_IO020_config.json                               │   │
│  │  ├─► PLC_IO043_config.json                               │   │
│  │  └─► PLC_IO251_config.json                               │   │
│  │                                                          │   │
│  │  IEC 61131-3 variable lists                              │   │
│  │  ├─► IO020_variables.txt                                 │   │
│  │  ├─► IO043_variables.txt                                 │   │
│  │  └─► IO251_variables.txt                                 │   │
│  │                                                          │   │
│  │  Reports                                                 │   │
│  │  ├─► summary.txt                                         │   │
│  │  └─► validation_report.txt                               │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CODESYS INTEGRATION LAYER                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  create_codesys_project.py (IronPython)                  │   │
│  │  ├─► Load template project (TEMPLATE_WAGO_750-8210)      │   │
│  │  ├─► Configure PLC device (750-8210)                     │   │
│  │  ├─► Add K-Bus I/O modules                               │   │
│  │  ├─► Import variables (GVL)                              │   │
│  │  ├─► Set IP address                                      │   │
│  │  └─► Save CODESYS project                                │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FINAL OUTPUT                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  CODESYS Projects (.project)                             │   │
│  │  ├─► IO020.project                                       │   │
│  │  ├─► IO043.project                                       │   │
│  │  └─► IO251.project                                       │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```
### Workflow Diagram
```
START
  │
  ├──► [1] Provide Excel file
  │     ├─ Check sheets: IO Boxes, SIGNALLIST
  │     └─ Validate structure (header rows)
  │
  ├──► [2] Start batch processing
  │     └─ python batch_processor.py --input=file.xls --output=./output
  │
  ├──► [3] Extraction & validation
  │     ├─ Parse IO Boxes (PLCs, IP addresses)
  │     ├─ Parse SIGNALLIST (signals, modules)
  │     ├─ Validate IP addresses
  │     └─ Group by PLC & module type
  │
  ├──► [4] JSON generation
  │     ├─ PLC_IO020_config.json
  │     ├─ PLC_IO043_config.json
  │     ├─ summary.txt
  │     └─ validation_report.txt
  │
  ├──► [5] Variable list generation
  │     └─ python codesys_import_example.py --input=./output
  │
  ├──► [6] CODESYS project creation (optional)
  │     ├─ Open CODESYS with ScriptEngine
  │     ├─ Run create_codesys_project.py
  │     └─ Generate .project files
  │
  └──► [7] Quality check
        ├─ Review validation_report.txt
        ├─ Check statistics
        └─ Test CODESYS import
  │
END
```
### Quick Start
#### Prerequisites
Python environment:
```bash
Python 3.8+
pandas >= 1.5.0
openpyxl >= 3.0.0  # For .xlsx support
xlrd >= 2.0.0      # For .xls support
```
CODESYS (optional for project generation):
```
CODESYS V3.5 SP19+
WAGO PFC200 Device Description
IronPython ScriptEngine enabled
```
#### Installation
```bash
# 1. Clone repository
git clone <repository-url>
cd codesys-project-generator
# 2. Install dependencies
pip install -r requirements.txt
# 3. Create directory structure
mkdir -p input output projects
```
#### First Steps
Step 1: Prepare the Excel file
```bash
# Copy your Excel file into the input directory
cp /path/to/LIST_OF_MEASURING_POINTS.xls ./input/
```
Step 2: Start batch processing
```bash
python batch_processor.py \
  --input=./input/LIST_OF_MEASURING_POINTS.xls \
  --output=./output
```
Step 3: Review results
```bash
# Show overview
cat ./output/summary.txt
# Check validation report
cat ./output/validation_report.txt
# View JSON files
ls -lh ./output/*.json
```
Step 4: Generate variable lists
```bash
python codesys_import_example.py \
  --input=./output
```
### Detailed Usage Guide
#### Excel File Format
Sheet: "IO-Boxes"
Header in row 4, data from row 5:
| Column | Name | Description | Example |
|--------|------|-------------|---------|
| 1 | IO BOX | Box number | 36140310.0 |
| 2 | Location | Location | I A 3 |
| 3 | PLC | PLC name | IO043 |
| 6 | IP-Adress | IP address | 172.16.60.043 |
Sheet: "SIGNALLIST"
Header in row 1, data from row 2:
| Column | Name | Description | Example |
|--------|------|-------------|---------|
| 5 | PLC | PLC assignment | IO045 |
| 6 | Type | Signal type | I (Input) / O (Output) |
| 11 | Signal | Signal kind | NC / 4-20mA / 24V DC |
| 62 | Mode_Type | IO module type | 750-432 / 750-554 |
| 69 | PLC_terminal | Terminal address | IX 65.3 -A3.5 |
| 72 | Objektname | Signal name | I0001_Me_MnCoolCmnAlrm |
#### Command Line Options
batch_processor.py
```bash
python batch_processor.py [OPTIONS]
Options:
  --input PATH   (required)  Path to the Excel file
  --output PATH  (required)  Path to the output directory
Examples:
  # Simple processing
  python batch_processor.py --input=data.xls --output=./configs
  # With absolute paths
  python batch_processor.py \
    --input=/home/user/data/measuring_points.xls \
    --output=/home/user/output/configs
```
codesys_import_example.py
```bash
python codesys_import_example.py [OPTIONS]
Options:
  --input PATH  (required)  Directory with JSON configurations
  --plc NAME    (optional)  Specific PLC (e.g., IO251)
Examples:
  # Process all PLCs
  python codesys_import_example.py --input=./output
  # Only a specific PLC
  python codesys_import_example.py --input=./output --plc=IO020
```
create_codesys_project.py
```bash
# Must be executed in CODESYS ScriptEngine
# Adjust configuration in file:
AUTO_DETECT_MODE = True  # Automatically finds all IO*_variables.txt
DEFAULT_PROJECT_PATH = r"D:\WAGO\CODESYS\projects"
DEFAULT_VARIABLES_PATH = r"D:\WAGO\CODESYS\outputs"
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210.project"
```
#### Output Files
JSON configuration (PLC_IO043_config.json)
```json
{
  "PLC_Info": {
    "Name": "IO043",
    "Type": "750-8210",
    "IP_Address": "172.16.60.043",
    "Location": "I A 3",
    "IO_Box": "36140310.0"
  },
  "IO_Modules": [
    {
      "Module_Type": "750-432",
      "Signals": [
        {
          "Terminal": "IX 65.3 -A3.5",
          "Object_Name": "I0001_Me_MnCoolCmnAlrm",
          "Signal_Type": "I",
          "Signal": "NC"
        }
      ]
    }
  ],
  "Statistics": {
    "Total_Modules": 5,
    "Total_Signals": 42,
    "Input_Signals": 25,
    "Output_Signals": 17
  },
  "Metadata": {
    "Generated": "2025-11-12T10:30:00",
    "Source_File": "measuring_points.xls",
    "Generator": "WAGO PLC Config Extractor v2.0"
  }
}
```
Variable list (IO043_variables.txt)
```iec61131-3
VAR_GLOBAL
    (* Digital Inputs - 750-432 *)
    I0001_Me_MnCoolCmnAlrm : BOOL;
    I0002_Me_CoolPumpAlrm : BOOL;
    (* Analog Outputs - 750-554 *)
    O0001_So_CoolValvePos : INT;
    O0002_So_PumpSpeed : INT;
END_VAR
```
Summary report (summary.txt)
```
======================================================================
WAGO PLC Configuration - Summary Report
======================================================================
Generated: 2025-11-12 10:30:00
Source File: measuring_points.xls
======================================================================
Total PLCs: 3
Total IO Modules: 15
Total Signals: 427
PLC Overview:
----------------------------------------------------------------------
IO020:
  Type: 750-8210
  IP Address: 172.16.46.020
  Location: I A 1
  IO Box: 36140308
  Modules: 4
  Signals: 669 (I: 7, O: 1)
IO043:
  Type: 750-8210
  IP Address: 172.16.60.043
  Location: I A 3
  IO Box: 36140310.0
  Modules: 5
  Signals: 42 (I: 25, O: 17)
```
Validation report (validation_report.txt)
```
======================================================================
WAGO PLC Configuration - Validation Report
======================================================================
Generated: 2025-11-12 10:30:00
Source File: measuring_points.xls
======================================================================
Total Warnings: 2
Total Errors: 0
Validation Log:
----------------------------------------------------------------------
[INFO] Reading IO-Boxen sheet from measuring_points.xls...
[INFO] Found 25 rows in IO-Boxen sheet
[INFO] PLC IO020: IP 172.16.46.020 valid
[WARNING] Row 15: Empty PLC field, skipping
[INFO] PLC IO043: IP 172.16.60.043 valid
[WARNING] PLC IO999: Module 750-999 not found in device descriptors
[INFO] Generated 3 PLC configuration files
```
## Execution (CLI)

### 1. Navigate to CODESYS Path
```powershell
cd "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
```

### 2. Run Script
```powershell
.\Codesys.exe --noUI --profile="CODESYS V3.5 SP21 Patch 1" --runscript="D:\path\to\script\create_codesys_project.py"
```

---

**Parameter:**
- `--noUI` - start CODESYS headless (without UI)
- `--profile` - installed CODESYS-Version
- `--runscript` - Path to IronPython-Script

## Configuration

### INI File: `WAGO_ProjectGenerator_Config.ini`

**Adjust paths:**
```ini
[CODESYS]
InstallPath=C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common
Profile=CODESYS V3.5 SP21 Patch 1

[PATHS]
ScriptDirectory=\scripts
ProjectDirectory=\projects
OutputDirectory=\outputs

[SCRIPTS]
DefaultScript=create_codesys_project_enhanced.py
```

---

### Python Script: `create_codesys_project_enhanced.py`

**Adjust paths :**
```python
# Paths
CONFIG_PATH = r"\configs\PLC_IO020_config.json"
TEMPLATE_PATH = r"\templates\WAGO_Template.project"
OUTPUT_DIR = r"\outputs"
LOG_DIR = r"\logs"
```

**Important:** 
- Replace `<YOUR_PROJECT_ROOT>` with your actual project directory
- All paths must be absolute and formatted with `r"..."`
- Use backslashes `\` for Windows paths

- 
#### Troubleshooting
Problem: "No PLC configuration files found"
```bash
# Solution 1: Check filename pattern
ls ./output/PLC_*_config.json
# Solution 2: Check permissions
chmod -R 755 ./output
# Solution 3: Run batch processor again
python batch_processor.py --input=data.xls --output=./output
```
Problem: "Invalid IP address format"
```python
# Check validation_report.txt:
cat ./output/validation_report.txt | grep "IP"
# Valid IP ranges:
# - 172.16.46.020 - 172.16.46.251
# - 172.16.60.001 - 172.16.60.255
```
Problem: "Module 750-XXX not found"
```python
# Check available modules in create_codesys_project.py:
# WAGO_DEVICE_DESCRIPTORS dictionary
# Supported modules (examples):
# - 750-402, 750-430, 750-432 (Digital Input)
# - 750-517, 750-530, 750-554 (Analog Output)
# - 750-610, 750-652 (Serial communication)
```


---
## 👨‍💻 Developer Documentation
### Project Structure
```
codesys-project-generator/
│
├── batch_processor.py              # CLI wrapper for Excel processing
├── excel_to_json_converter.py      # Core extraction logic
├── codesys_import_example.py       # Variable list generator
├── create_codesys_project.py       # CODESYS IronPython integration
│
├── input/                          # Input directory
│   └── LIST_OF_MEASURING_POINTS.xls
│
├── output/                         # Output directory
│   ├── PLC_IO020_config.json
│   ├── PLC_IO043_config.json
│   ├── PLC_IO251_config.json
│   ├── IO020_variables.txt
│   ├── IO043_variables.txt
│   ├── IO251_variables.txt
│   ├── summary.txt
│   └── validation_report.txt
│
├── projects/                       # CODESYS projects
│   ├── IO020.project
│   ├── IO043.project
│   └── IO251.project
│
├── TEMPLATE_WAGO_750-8210.project  # CODESYS template
│
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── WAGO_PLC_Schnittstellen_Dokumentation.md  # API reference
```
### Component Details
#### 1. batch_processor.py
Purpose: CLI entry point for batch processing
Main functions:
```python
def parse_arguments() -> argparse.Namespace
    """
    Parses command line arguments
    Returns:
        Namespace with 'input' and 'output' attributes
    """
def main() -> None
    """
    Main execution logic:
    1. Validate input file
    2. Create output directory
    3. Initialize PLCConfigExtractor
    4. Process Excel file
    5. Output summary
    """
```
Usage example:
```python
# Command line
python batch_processor.py --input=data.xls --output=./configs
# Programmatic call
from batch_processor import main
import sys
sys.argv = ['batch_processor.py', '--input=data.xls', '--output=./configs']
main()
```
#### 2. excel_to_json_converter.py
Purpose: Core extraction and conversion logic
Class: PLCConfigExtractor
```python
class PLCConfigExtractor:
    """
    Extracts PLC configurations from Excel and generates JSON
    Attributes:
        excel_file (str): Path to the Excel input file
        plcs (dict): Dictionary of all extracted PLCs
        validation_log (list): List of all log entries
        stats (dict): Processing statistics
    """
    def **init**(self, excel_file: str):
        """Initializes extractor with Excel file"""
    def extract_plcs_from_io_boxes(self) -> None:
        """
        Extracts PLC information from sheet 'IO-Boxen'
        Processing:
        1. Read sheet with pandas (header in row 3 or 0)
        2. Iterate over rows starting at row 5
        3. Extract: PLC name, IP, location, IO box
        4. Validate IP address
        5. Store in self.plcs
        """
    def extract_signals_from_signallist(self) -> None:
        """
        Extracts signals from sheet 'SIGNALLIST'
        Processing:
        1. Read sheet with pandas (header in row 0)
        2. Iterate over rows starting at row 2
        3. Group signals by PLC and module type
        4. Compute statistics (input/output counters)
        """
    def validate_ip_address(self, ip: str) -> tuple[bool, str]:
        """
        Validates IP address format
        Args:
            ip: IP address as string
        Returns:
            (is_valid, result_or_error_message)
        Validation rules:
        - Format: xxx.xxx.xxx.xxx
        - Each octet: 0-255
        - Not empty
        """
    def generate_json_files(self, output_dir: str) -> list:
        """
        Generates JSON configuration files
        Args:
            output_dir: Target directory
        Returns:
            List of generated filenames
        Format:
        - PLC_Info: Name, Type, IP, Location, IO_Box
        - IO_Modules: List of modules with signals
        - Statistics: Counters
        - Metadata: Generation info
        """
    def generate_summary(self, output_dir: str) -> str:
        """Generates summary.txt with overview"""
    def generate_validation_report(self, output_dir: str) -> str:
        """Generates validation_report.txt with warnings/errors"""
    def process(self, output_dir: str) -> list:
        """
        Main processing pipeline
        Args:
            output_dir: Output directory
        Returns:
            List of generated JSON files
        Workflow:
        1. extract_plcs_from_io_boxes()
        2. extract_signals_from_signallist()
        3. generate_json_files()
        4. generate_summary()
        5. generate_validation_report()
        """
```
Data structures:
```python
# self.plcs dictionary structure
{
    "IO043": {
        "PLC_Info": {
            "Name": "IO043",
            "Type": "750-8210",
            "IP_Address": "172.16.60.043",
            "Location": "I A 3",
            "IO_Box": "36140310.0"
        },
        "IO_Modules": {
            "750-432": {
                "Module_Type": "750-432",
                "Signals": [
                    {
                        "Terminal": "IX 65.3 -A3.5",
                        "Object_Name": "I0001_Me_MnCoolCmnAlrm",
                        "Signal_Type": "I",
                        "Signal": "NC"
                    }
                ]
            }
        },
        "Statistics": {
            "Total_Modules": 5,
            "Total_Signals": 42,
            "Input_Signals": 25,
            "Output_Signals": 17
        }
    }
}
# validation_log entries
[
    "[INFO] Reading IO-Boxen sheet...",
    "[WARNING] Row 15: Empty PLC field, skipping",
    "[ERROR] PLC IO999: Invalid IP format: 999.999.999.999"
]
# stats dictionary
{
    'total_plcs': 3,
    'total_signals': 427,
    'total_modules': 15,
    'warnings': 2,
    'errors': 0
}
```
#### 3. codesys_import_example.py
Purpose: Generates IEC 61131-3 variable lists from JSON
Main functions:
```python
def load_plc_config(json_file: str) -> dict:
    """
    Loads JSON configuration
    Args:
        json_file: Path to the JSON file
    Returns:
        Dictionary with PLC configuration or None on error
    """
def create_variable_list(config: dict, output_file: str) -> None:
    """
    Creates IEC 61131-3 variable list
    Args:
        config: PLC configuration from JSON
        output_file: Output file (e.g., IO043_variables.txt)
    Generates:
        VAR_GLOBAL
            (* Comments per module type *)
            variable_name : data_type;
        END_VAR
    Data type mapping:
        - "I" / "O" with "NC" / "NO" → BOOL
        - "I" / "O" with "4-20mA" / "0-10V" → INT
        - "RS485" / "RS232" → No variable (comment)
    """
def find_json_configs(directory: str) -> list:
    """
    Finds all PLC_*_config.json files
    Args:
        directory: Search directory
    Returns:
        List of dictionaries with:
        - plc_name: PLC identifier (e.g., "IO043")
        - filepath: Full path to the JSON file
    """
def process_plc(config_info: dict, output_dir: str) -> bool:
    """
    Processes a single PLC
    Args:
        config_info: Dict with plc_name and filepath
        output_dir: Output directory
    Returns:
        True on success, False on error
    Workflow:
    1. Load JSON configuration
    2. Show summary (PLC info, modules, signals)
    3. Generate variable list
    """
```
IEC 61131-3 output format:
```iec61131-3
VAR_GLOBAL
    (* ================================================ *)
    (* PLC: IO043 - 750-8210 *)
    (* IP: 172.16.60.043 *)
    (* Location: I A 3 *)
    (* Generated: 2025-11-12 10:30:00 *)
    (* ================================================ *)
    (* -------------------------------- *)
    (* Module: 750-432 (4DI 24 VDC 3ms 2-wire) *)
    (* Total Signals: 4 *)
    (* -------------------------------- *)
    I0001_Me_MnCoolCmnAlrm : BOOL;           (* IX 65.3 -A3.5 | NC *)
    I0002_Me_CoolPumpAlrm : BOOL;            (* IX 65.4 -A3.6 | NC *)
    I0003_Me_TempSensorAlrm : BOOL;          (* IX 65.5 -A3.7 | NC *)
    I0004_Me_FlowSensorAlrm : BOOL;          (* IX 65.6 -A3.8 | NC *)
    (* -------------------------------- *)
    (* Module: 750-554 (4AO 0-20mA 12bit single-ended *)
    (* Total Signals: 2 *)
    (* -------------------------------- *)
    O0001_So_CoolValvePos : INT;             (* QW 3 -A5.2 | 4-20mA *)
    O0002_So_PumpSpeed : INT;                (* QW 5 -A5.4 | 4-20mA *)
END_VAR
``]
#### 4. create_codesys_project.py
Purpose: CODESYS project creation via IronPython ScriptEngine
Important constants:
```python
# Path configuration
DEFAULT_PROJECT_PATH = r"D:\WAGO\CODESYS\projects"
DEFAULT_VARIABLES_PATH = r"D:\WAGO\CODESYS\outputs"
DEFAULT_CONFIG_PATH = r"D:\WAGO\CODESYS\outputs"
# Template project
USE_TEMPLATE = True
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210.project"
# Auto-detect mode
AUTO_DETECT_MODE = True  # Automatically finds all IO*_variables.txt
# Manual configuration (if AUTO_DETECT_MODE = False)
SPECIFIC_VARIABLES_FILE = r"...\IO020_variables.txt"
SPECIFIC_CONFIG_FILE = r"...\PLC_IO020_config.json"
```
WAGO Device Descriptors:
```python
WAGO_DEVICE_DESCRIPTORS = {
    "750-432": {
        "device_id": 32776,
        "descriptor": "8401_0750043200000000",
        "version": "2.0.0.11",
        "name": "750-432",
        "description": "4DI 24 VDC 3ms 2-wire"
    },
    "750-554": {
        "device_id": 32776,
        "descriptor": "8401_0750055400000000",
        "version": "2.0.0.11",
        "name": "750-554",
        "description": "4AO 0-20mA 12bit single-ended"
    },
    # ... more modules
}
```
Main functions:
```python
def create_project_from_template(plc_name: str, project_path: str,
                                  template_path: str) -> tuple:
    """
    Creates a CODESYS project from a template
    Args:
        plc_name: PLC identifier (e.g., "IO043")
        project_path: Target directory
        template_path: Path to the template project
    Returns:
        (project_object, full_path)
    Workflow:
    1. Copy template to {plc_name}.project
    2. Open project with ScriptEngine
    3. Return project object
    """
def find_plc_device(proj) -> object:
    """
    Finds PLC device (type 4096)
    Args:
        proj: CODESYS Project Object
    Returns:
        Device object or None
    Search strategy:
    1. Search all devices recursively
    2. Check device_identification.type == 4096
    3. Return first match
    """
def find_kbus(device) -> object:
    """
    Finds K-Bus under the PLC device
    Args:
        device: PLC Device Object
    Returns:
        K-Bus object or None
    """
def add_io_modules_to_kbus(kbus, config: dict) -> None:
    """
    Adds I/O modules to the K-Bus
    Args:
        kbus: K-Bus Device Object
        config: JSON configuration
    Workflow:
    1. Iterate over config['IO_Modules']
    2. For each module:
       a. Get device descriptor from WAGO_DEVICE_DESCRIPTORS
       b. Create device with create_device()
       c. Set name and position
    """
def configure_device_ip(proj, device, ip_address: str) -> None:
    """
    Configures IP address of the PLC device
    Args:
        proj: Project Object
        device: PLC Device Object
        ip_address: IP as string (e.g., "172.16.60.043")
    Workflow:
    1. Find Ethernet adapter under device
    2. Set IP, subnet, gateway
    """
def create_gvl_with_variables(app, gvl_name: str, var_block: str):
    """
    Creates Global Variable List (GVL)
    Args:
        app: Application Object
        gvl_name: Name of the GVL (e.g., "GVL_IO043")
        var_block: IEC 61131-3 VAR_GLOBAL block
    Workflow:
    1. Create GVL with app.create_gvl()
    2. Set textual_declaration to var_block
    """
def create_single_project(var_file: str, config_file: str,
                         plc_name: str) -> bool:
    """
    Creates a complete CODESYS project
    Args:
        var_file: Path to IO043_variables.txt
        config_file: Path to PLC_IO043_config.json
        plc_name: PLC identifier
    Returns:
        True on success, False on error
    Workflow:
    1. Parse variable list and JSON config
    2. Create project from template
    3. Find Application and PLC device
    4. Configure IP address
    5. Add I/O modules to K-Bus
    6. Create GVL with variables
    7. Save and close project
    """
def main() -> None:
    """
    Main execution logic
    Workflow:
    1. Show available device descriptors
    2. Collect files (auto-detect or manual)
    3. For each PLC pair (variables.txt + config.json):
       - Create CODESYS project
       - Log success/error
    4. Show summary
    """
```
ScriptEngine API usage:
```python
# CODESYS ScriptEngine namespace
from ScriptEngine import projects
from ScriptEngine.HostAccess import ScriptTypes
# Open project
proj = projects.open(filepath, None, True)
# Find Application
app = proj.find("Application", True)[0]
# Create device
device = kbus.create_device(device_descriptor)
# Create GVL
gvl = app.create_gvl("GVL_IO043")
gvl.textual_declaration.replace(var_block)
# Save project
proj.save()
proj.close()
```
### Data Flow & Interfaces
#### Data Flow Diagram (detailed)
```
┌─────────────────────────────────────────────────────────────────────┐
│ EXCEL: LIST_OF_MEASURING_POINTS.xls                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Sheet: IO-Boxen (header row 4)                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ IO BOX | Location | PLC   | ... | IP-Adress      | Type        │ │
│  ├────────────────────────────────────────────────────────────────┤ │
│  │ 361403 | I A 3    | IO043 | ... | 172.16.60.043  | 750-8210    │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  Sheet: SIGNALLIST (header row 1)                                   │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ PLC | Type | Signal | Mode_Type | PLC_terminal | Objektname    │ │
│  ├────────────────────────────────────────────────────────────────┤ │
│  │IO043│  I   │  NC    │  750-432  │ IX 65.3-A3.5 │ I0001_Me..    │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ pandas.read_excel()
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.extract_plcs_from_io_boxes()                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  DataFrame → row iteration → validation                             │
│                                                                     │
│  self.plcs["IO043"] = {                                             │
│      "PLC_Info": {                                                  │
│          "Name": "IO043",                                           │
│          "Type": "750-8210",                                        │
│          "IP_Address": "172.16.60.043",                             │
│          "Location": "I A 3",                                       │
│          "IO_Box": "36140310.0"                                     │
│      },                                                             │
│      "IO_Modules": {},  # still empty                               │
│      "Statistics": {...}                                            │
│  }                                                                  │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.extract_signals_from_signallist()                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  DataFrame → grouping by (PLC, Module_Type)                         │
│                                                                     │
│  self.plcs["IO043"]["IO_Modules"]["750-432"] = {                    │
│      "Module_Type": "750-432",                                      │
│      "Signals": [                                                   │
│          {                                                          │
│              "Terminal": "IX 65.3 -A3.5",                           │
│              "Object_Name": "I0001_Me_MnCoolCmnAlrm",               │
│              "Signal_Type": "I",                                    │
│              "Signal": "NC"                                         │
│          }                                                          │
│      ]                                                              │
│  }                                                                  │
│                                                                     │
│  Update statistics:                                                 │
│  - Total_Modules++                                                  │
│  - Total_Signals++                                                  │
│  - Input_Signals++ / Output_Signals++                               │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.generate_json_files()                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  For each PLC in self.plcs:                                         │
│      1. Convert IO_Modules dict → list                              │
│      2. Add metadata                                                │
│      3. json.dump() → PLC_IO043_config.json                         │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: JSON files                                                  │
├─────────────────────────────────────────────────────────────────────┤
│  PLC_IO043_config.json                                              │
│  PLC_IO020_config.json                                              │
│  PLC_IO251_config.json                                              │
│  summary.txt                                                        │
│  validation_report.txt                                              │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ codesys_import_example.py
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ create_variable_list()                                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  For each PLC:                                                      │
│      For each module in IO_Modules:                                 │
│          For each signal:                                           │
│              Map Signal_Type → IEC data type                        │
│              Generate declaration                                   │
│                                                                     │
│  VAR_GLOBAL                                                         │
│      (* Module: 750-432 *)                                          │
│      I0001_Me_MnCoolCmnAlrm : BOOL;                                 │
│  END_VAR                                                            │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: Variable lists                                              │
├─────────────────────────────────────────────────────────────────────┤
│  IO043_variables.txt                                                │
│  IO020_variables.txt                                                │
│  IO251_variables.txt                                                │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ create_codesys_project.py (IronPython)
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ create_single_project()                                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Load IO043_variables.txt → var_block (string)                   │
│  2. Load PLC_IO043_config.json → config (dict)                      │
│  3. Copy template → IO043.project                                   │
│  4. Open project with ScriptEngine                                  │
│  5. Find PLC device (type 4096)                                     │
│  6. Configure IP address                                            │
│  7. Find K-Bus                                                      │
│  8. Add I/O modules:                                                │
│      For each module in config['IO_Modules']:                       │
│          descriptor = WAGO_DEVICE_DESCRIPTORS[Module_Type]          │
│          device = kbus.create_device(descriptor['descriptor'])      │
│  9. Create GVL:                                                     │
│      gvl = app.create_gvl("GVL_IO043")                              │
│      gvl.textual_declaration.replace(var_block)                     │
│  10. Save & close project                                           │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: CODESYS projects                                            │
├─────────────────────────────────────────────────────────────────────┤
│  projects/IO043.project                                             │
│  projects/IO020.project                                             │
│  projects/IO251.project                                             │
└─────────────────────────────────────────────────────────────────────┘
```
#### Interface Definition
Python → JSON (excel_to_json_converter.py)
Input: Excel file with defined sheets
Output: JSON with the following schema:
```json
{
  "PLC_Info": {
    "Name": "string",           // PLC identifier (e.g., "IO043")
    "Type": "string",           // PLC type (e.g., "750-8210")
    "IP_Address": "string",     // IP in format xxx.xxx.xxx.xxx
    "Location": "string",       // Location
    "IO_Box": "string"          // Box number
  },
  "IO_Modules": [               // List of all I/O modules
    {
      "Module_Type": "string",  // WAGO module type (e.g., "750-432")
      "Signals": [              // List of all signals of this module
        {
          "Terminal": "string", // Terminal address (e.g., "IX 65.3 -A3.5")
          "Object_Name": "string", // Signal name
          "Signal_Type": "string", // "I", "O", "SI", "SO", "RS485", etc.
          "Signal": "string"    // Signal kind (e.g., "NC", "4-20mA")
        }
      ]
    }
  ],
  "Statistics": {
    "Total_Modules": "integer",    // Number of modules
    "Total_Signals": "integer",    // Number of signals
    "Input_Signals": "integer",    // Number of inputs
    "Output_Signals": "integer"    // Number of outputs
  },
  "Metadata": {
    "Generated": "ISO 8601 datetime",
    "Source_File": "string",
    "Generator": "string"
  }
}
```
JSON → IEC 61131-3 (codesys_import_example.py)
Input: JSON as defined above
Output: Text file in IEC 61131-3 format
Mapping rules:
| Signal_Type | Signal | IEC Data Type | Example |
|-------------|--------|---------------|---------|
| I | NC / NO | BOOL | `I0001_Signal : BOOL;` |
| O | NC / NO | BOOL | `O0001_Signal : BOOL;` |
| I | 4-20mA / 0-10V | INT | `I0001_Signal : INT;` |
| O | 4-20mA / 0-10V | INT | `O0001_Signal : INT;` |
| SI | INT | INT | `I0001_Signal : INT;` |
| SO | INT | INT | `O0001_Signal : INT;` |
| RS485 / RS232 | - | (comment) | `(* Serial Module *)` |
IEC 61131-3 + JSON → CODESYS (create_codesys_project.py)
Input:
- IO043_variables.txt (IEC 61131-3 text)
- PLC_IO043_config.json (JSON)
- TEMPLATE_WAGO_750-8210.project (CODESYS template)
Output:
- IO043.project (CODESYS project)
API Calls:
```python
# CODESYS ScriptEngine API
projects.open(filepath) → Project
Project.find(name, recursive) → List[Object]
Project.active_application → Application
Device.create_device(descriptor) → Device
Application.create_gvl(name) → GVL
GVL.textual_declaration.replace(text) → None
Project.save() → None
```
### Extension & Customization
#### Add new I/O modules
1. Determine device descriptor:
```python
# In CODESYS:
# 1. Open Device Repository
# 2. Search WAGO module (e.g., 750-456)
# 3. Right-click → Properties → Device Identification
# 4. Note: Device ID, descriptor string, version
```
2. Add to WAGO_DEVICE_DESCRIPTORS:
```python
# In create_codesys_project.py
WAGO_DEVICE_DESCRIPTORS = {
    # ... existing modules
    "750-456": {
        "device_id": 32776,                 # From CODESYS
        "descriptor": "8401_0750045600000000",  # From CODESYS
        "version": "2.0.0.10",              # From CODESYS
        "name": "750-456",
        "description": "4DO 24VDC 0.5A"    # Description
    },
}
```
3. Test:
```python
# Process Excel with 750-456 module
python batch_processor.py --input=test.xls --output=./output
# Check if module is recognized
cat ./output/validation_report.txt | grep "750-456"
```
#### Add new signal types
In codesys_import_example.py:
```python
def map_signal_to_datatype(signal_info):
    """Map signal information to IEC 61131-3 data type"""
    signal_type = signal_info.get('Signal_Type', '')
    signal = signal_info.get('Signal', '')
    # Existing mappings...
    # ADD NEW MAPPINGS:
    if signal_type in ['AI'] and 'PT100' in signal:
        return 'REAL'  # Temperature as floating point
    if signal_type in ['AO'] and 'PWM' in signal:
        return 'WORD'  # PWM as 16-bit word
    # Default
    return 'INT'
```
#### Custom validation rules
In excel_to_json_converter.py:
```python
class PLCConfigExtractor:
    def custom_validation(self, plc_data):
        """Add custom validations"""
        # Example 1: Maximum number of modules per PLC
        if plc_data['Statistics']['Total_Modules'] > 64:
            self.log_warning(
                f"PLC {plc_data['PLC_Info']['Name']}: "
                f"More than 64 modules ({plc_data['Statistics']['Total_Modules']})"
            )
        # Example 2: Check for duplicate terminal addresses
        terminals = []
        for module in plc_data['IO_Modules']:
            for signal in module['Signals']:
                terminal = signal['Terminal']
                if terminal in terminals:
                    self.log_error(
                        f"Duplicate terminal address: {terminal}"
                    )
                terminals.append(terminal)
        # Example 3: Check naming convention
        for module in plc_data['IO_Modules']:
            for signal in module['Signals']:
                name = signal['Object_Name']
                if not name.startswith(('I', 'O')):
                    self.log_warning(
                        f"Signal {name}: Does not follow naming convention"
                    )
    def process(self, output_dir):
        """Extended processing with custom validation"""
        # ... existing code
        # Run custom validations
        for plc_name, plc_data in self.plcs.items():
            self.custom_validation(plc_data)
        # ... continue as before
```
#### Adjust template project
1. Create new template:
```
1. Open CODESYS
2. Create new project with WAGO PFC200 (750-8210)
3. Configure:
   - Ethernet settings (default IP)
   - Task configuration
   - Libraries (e.g., Standard, Util)
4. Save as: TEMPLATE_WAGO_750-8210_v2.project
```
2. Update in create_codesys_project.py:
```python
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210_v2.project"
```
3. Template-specific customizations:
```python
def customize_template_project(proj, config):
    """Template-specific adjustments after creation"""
    # Example: Set project information
    proj.set_project_information("Author", "Automation Team")
    proj.set_project_information("Company", config['PLC_Info'].get('Location', ''))
    # Example: Configure task
    app = proj.active_application
    tasks = app.find("Task Configuration", True)
    if tasks:
        task = tasks[0]
        # Set cycle time to 10ms
        task.cycle_time = 10000  # microseconds
```
#### Batch processing with filtering
```python
# Extend in batch_processor.py
def process_with_filter(input_file, output_dir, plc_filter=None):
    """
    Process only specific PLCs
    Args:
        plc_filter: List of PLC names (e.g., ['IO020', 'IO043'])
    """
    extractor = PLCConfigExtractor(input_file)
    extractor.extract_plcs_from_io_boxes()
    extractor.extract_signals_from_signallist()
    # Filtering
    if plc_filter:
        filtered_plcs = {
            name: data for name, data in extractor.plcs.items()
            if name in plc_filter
        }
        extractor.plcs = filtered_plcs
    # Further processing
    json_files = extractor.generate_json_files(output_dir)
    # ...
```
Usage:
```python
# Process only specific PLCs
process_with_filter(
    'measuring_points.xls',
    './output',
    plc_filter=['IO020', 'IO043']
)
```
#### Extend logging
```python
import logging
# In excel_to_json_converter.py
class PLCConfigExtractor:
    def **init**(self, excel_file):
        # ... existing code
        # Configure logger
        self.logger = logging.getLogger('PLCExtractor')
        handler = logging.FileHandler('extraction.log')
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    def log_info(self, message):
        self.logger.info(message)
        print(f"INFO: {message}")
    def log_debug(self, message):
        self.logger.debug(message)
        # Do not print to console
```
---
## 📚 Additional Resources
### External Documentation
- CODESYS ScriptEngine: See ScriptEngine.md in the project directory
- WAGO PLC Documentation: WAGO_PLC_Interfaces_Documentation.md
- Workflow Description: PROGRAM_EXECUTION_FLOW.md

### Support & Contact
If you have questions or issues:
1. Check validation_report.txt for warnings/errors
2. Consult this README
3. Check log files in the output directory
### License & Copyright
© 2025 - All rights reserved
---
Version: 2.1  
Status: November 2025  

