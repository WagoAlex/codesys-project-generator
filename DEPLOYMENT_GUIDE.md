# Deployment Guide

**Version:** 0.8.2  
**Author:** Alexander Fugmann  
**Last Updated:** 2024-12-11

---

## Overview

This guide covers the deployment and setup of the CODESYS Project Generator for WAGO PLCs. The system supports both local development and production deployment with a unified configuration approach.

---

## Prerequisites

### Software Requirements
- **CODESYS V3.5 SP16+** (tested with SP21 Patch 1)
- **Windows 10/11** (for ANSI color support in console)
- **WAGO Device Descriptor packages** installed in CODESYS
- **MQTT Client SL** and other required libraries (see Configuration)

### Hardware Requirements
- WAGO PFC200 controller (750-8210 series recommended)
- Network connection for gateway discovery (IP configuration)

### File Access
- Read/write permissions in project directory
- Access to CODESYS installation folder

---

## Installation

### Step 1: Create Directory Structure

```bash
# Base directory
mkdir "D:\WAGO\CODESYS\scripting\project generator"
cd "D:\WAGO\CODESYS\scripting\project generator"

# Subdirectories
mkdir files
mkdir files\exports
mkdir files\outputs
mkdir files\projects
mkdir files\logs
```

**Directory Purpose:**
```
project generator/
├── codesys_project_generator_local.py    # Main script
├── project_config.json                   # Configuration file
├── WAGO_ProjectGenerator.bat             # Batch launcher
└── files/
    ├── exports/                          # PLCopenXML files (.xml)
    ├── outputs/                          # Variable files (.txt) and PLC configs (.json)
    ├── projects/                         # Generated CODESYS projects (.project)
    └── logs/                             # Execution logs (auto-created)
```

### Step 2: Copy Script Files

Place these files in the root directory:
1. `codesys_project_generator_local.py` - Main generator script
2. `project_config.json` - Configuration file
3. `WAGO_ProjectGenerator.bat` - Batch launcher (optional)

### Step 3: Configure Paths

The script uses these default paths (configured in script header):
```python
BASE_PATH = r"D:\WAGO\CODESYS\scripting\project generator\files"
DEFAULT_PROJECT_PATH = os.path.join(BASE_PATH, "projects")
DEFAULT_VARIABLES_PATH = os.path.join(BASE_PATH, "outputs")
DEFAULT_CONFIG_PATH = os.path.join(BASE_PATH, "outputs")
CONFIG_JSON_PATH = os.path.join(BASE_PATH, "project_config.json")
TEMPLATE_PROJECT = os.path.join(BASE_PATH, "TEMPLATE_WAGO_750-8210.project")
```

**To customize paths**: Edit `BASE_PATH` in `codesys_project_generator_local.py` line 17.

---

## Configuration

### project_config.json Structure

```json
{
  "configuration": {
    "description": "CODESYS Project Generator Configuration",
    "version": "0.8.2",
    "namespace_mapping": {
      "MQTT Client SL": "MQTT",
      "JSON Utilities SL": "JSON",
      "WagoSysString": "WagoSysString"
    }
  },
  
  "libraries": {
    "items": [
      {
        "name": "MQTT Client SL",
        "vendor": "CODESYS",
        "version": "1.10.0.0",
        "namespace": "MQTT",
        "required": false
      },
      {
        "name": "WagoSysString",
        "vendor": "WAGO",
        "version": null,
        "namespace": "WagoSysString",
        "required": false
      }
    ]
  },
  
  "function_blocks": {
    "items": [
      {
        "library": "MQTT Client SL",
        "library_namespace": "MQTT",
        "fb_type": "MQTT.MQTTClient",
        "instance": "oMQTTClient",
        "params": {
          "xEnable": "xEnable",
          "sHostname": "sHostname",
          "uiPort": "uiPort"
        }
      }
    ]
  },
  
  "xml_imports": {
    "auto_detect": {
      "enabled": true,
      "directory": "exports",
      "pattern": "*.xml",
      "exclude_patterns": ["*_backup.xml", "*_old.xml"],
      "default_conflict_resolve": "replace",
      "treat_all_as_optional": false
    },
    "manual_files": []
  },
  
  "import_settings": {
    "default_conflict_resolve": "replace",
    "save_after_import": true,
    "continue_on_error": true
  }
}
```

### Configuration Sections

**libraries.items[]**
- `name`: Library display name in CODESYS (e.g., "MQTT Client SL")
- `vendor`: Library vendor - "CODESYS", "WAGO", or "3S"
- `version`: Specific version or `null` for latest
- `namespace`: Internal namespace for FB references (e.g., "MQTT")
- `required`: If `true`, project generation fails if library not found

**function_blocks.items[]**
- `fb_type`: Fully qualified type (e.g., "MQTT.MQTTClient")
- `instance`: Variable name (e.g., "oMQTTClient")
- `params`: Dictionary of parameter assignments

**xml_imports.auto_detect**
- `enabled`: Enable automatic XML file detection
- `directory`: Directory to scan (relative to BASE_PATH)
- `pattern`: File pattern (e.g., "*.xml")
- `exclude_patterns`: List of patterns to skip
- `default_conflict_resolve`: "replace", "copy", or "skip"

---

## Input Files

### Variable Files
**Format:** `IO{NUMBER}_variables.txt`
**Location:** `files/outputs/`
**Example:** `IO020_variables.txt`

**Content:**
```
VAR_GLOBAL
    IO020_Input_01 AT %IX0.0 : BOOL;
    IO020_Input_02 AT %IX0.1 : BOOL;
    IO020_Analog_01 AT %IW2 : INT;
END_VAR
```

### PLC Configuration Files
**Format:** `PLC_IO{NUMBER}_config.json`
**Location:** `files/outputs/`
**Example:** `PLC_IO020_config.json`

**Content:**
```json
{
  "PLC_Info": {
    "Name": "IO020",
    "Type": "750-8210",
    "IP_Address": "172.16.46.020",
    "Location": "Cabinet A3"
  },
  "IO_Modules": [
    {
      "Module_Type": "750-432",
      "Signals": [
        {
          "Terminal": "IX 0.0",
          "Object_Name": "IO020_Input_01",
          "Signal_Type": "I",
          "Signal": "24V DC"
        }
      ]
    }
  ]
}
```

### XML Files
**Format:** PLCopenXML or CODESYS Project XML
**Location:** `files/exports/`
**Extensions:** `.xml`

**Supported Formats:**
- PLCopenXML (IEC 61131-3 standard)
- CODESYS Project XML
- **NOT supported:** .export files (requires ISVNode)

---

## Execution

### Method 1: Batch Launcher (Recommended)

**File:** `WAGO_ProjectGenerator.bat`

```batch
@echo off
cd /d "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI --profile="CODESYS V3.5 SP21 Patch 1" --runscript="D:\WAGO\CODESYS\scripting\project generator\codesys_project_generator_local.py"
pause
```

**Usage:**
```bash
# Double-click batch file or run from command line
WAGO_ProjectGenerator.bat
```

### Method 2: Direct Execution

```bash
cd "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI --profile="CODESYS V3.5 SP21 Patch 1" --runscript="D:\WAGO\CODESYS\scripting\project generator\codesys_project_generator_local.py"
```

### Method 3: ScriptEngine Test Mode

```bash
# Test script syntax without full execution
ScriptEngine.exe --check "D:\WAGO\CODESYS\scripting\project generator\codesys_project_generator_local.py"
```

---

## Process Flow

### 13-Step Generation Process

For each PLC (IO020, IO021, etc.):

1. **Load JSON Configuration**
   - Parse `project_config.json`
   - Extract libraries, function blocks, XML imports

2. **Parse Input Files**
   - Read variable file: `IO020_variables.txt`
   - Read PLC config: `PLC_IO020_config.json`

3. **Create CODESYS Project**
   - Copy template: `TEMPLATE_WAGO_750-8210.project`
   - Open with `projects.open()`

4. **Find Application**
   - Locate Application node in project tree

5. **Install Libraries**
   - Search in repository: `librarymanager.repositories`
   - Add via Library Manager: `libman.add_library(lib)`

6. **Import XML Files**
   - Auto-detect files in exports folder (if enabled)
   - Import to Application: `app.import_xml(conflict_mode, filepath, True)`

7. **Find PLC Device**
   - Search for Device node: `proj.find('Device', True)`

8. **Configure IP Address**
   - Get gateway object: `get_first_gateway()`
   - Set IP: `device.set_gateway_and_ip_address(gateway, ip)`

9. **Configure K-Bus with IO Modules**
   - Find K-Bus: `device.find('Kbus', True)`
   - Add modules: `kbus.add(name, id, descriptor, version)`

10. **Find/Update PLC_PRG**
    - Locate or create PLC_PRG POU

11. **Instantiate Function Blocks**
    - Add VAR declarations
    - Add implementation calls

12. **Create GVL with Variables**
    - Create GVL: `app.create_gvl('GVL_IO020')`
    - Insert variable declarations

13. **Save Project**
    - Save: `proj.save()`
    - Close: `proj.close()`

**Total Duration:** ~3-5 seconds per project

---

## Output Files

### Generated Projects
**Location:** `files/projects/`
**Format:** `IO{NUMBER}.project`
**Example:** `IO020.project`

**Contents:**
- Configured PLC device with IP address
- K-Bus with IO modules
- Installed libraries
- Imported POUs from XML files
- Function block instances in PLC_PRG
- Global variable list (GVL_IO020)

### Log Files
**Location:** `files/logs/`
**Format:** `codesys_project_generator_local_log_YYYYMMDD_HHMMSS.txt`
**Example:** `codesys_project_generator_local_log_20241211_143052.txt`

**Content:**
```
[2024-12-11 14:30:52] [INFO] STEP 1/13: Load JSON Configuration
[2024-12-11 14:30:52] [SUCCESS]   [OK] Configuration loaded
[2024-12-11 14:30:52] [INFO] STEP 5/13: Install Libraries
[2024-12-11 14:30:53] [SUCCESS]   [FOUND] MQTT Client SL, 1.10.0.0 (CODESYS)
[2024-12-11 14:30:53] [SUCCESS]   [NAMESPACE] MQTT
```

---

## Troubleshooting

### Common Issues

**Issue 1: "Library not found"**
```
[ERROR] Library Manager not available
[ERROR] 'SystemImpl' object has no attribute 'librarymanager'
```
**Solution:** This is fixed in v0.8.1+. Update to latest version.

**Issue 2: "Kbus module creation failed"**
```
[ERROR] 'ScriptObject' object has no attribute 'create_child'
```
**Solution:** This is fixed in v0.8.1+. Uses `kbus.add()` method now.

**Issue 3: "IP configuration GUID error"**
```
[WARNING] GUID muss 32 Ziffern mit 4 Bindestrichen enthalten
```
**Solution:** This is fixed in v0.8.1+. Uses gateway object instead of string.

**Issue 4: "XML file not found"**
```
[ERROR] Not found (required) - ERROR
```
**Solution:**
- Check file exists in `files/exports/`
- Verify path in `project_config.json`
- Set `optional: true` if file is not critical

**Issue 5: "Template not found"**
```
[ERROR] Template not found!
```
**Solution:**
- Create template project manually in CODESYS
- Save as: `files/TEMPLATE_WAGO_750-8210.project`
- Must contain at least: Application, Device (750-8210), K-Bus

### Debug Mode

Enable detailed logging in `project_config.json`:
```json
{
  "debugging": {
    "enable_detailed_logging": true,
    "log_language": "en"
  }
}
```

### Validation

**Check Configuration:**
```python
import json
with open('project_config.json', 'r') as f:
    config = json.load(f)
    print("Libraries:", len(config['libraries']['items']))
    print("Function Blocks:", len(config['function_blocks']['items']))
    print("Auto-detect XML:", config['xml_imports']['auto_detect']['enabled'])
```

**Test XML Import:**
```python
# Create test script to verify XML files
import os
import glob

exports_dir = r"D:\WAGO\CODESYS\scripting\project generator\files\exports"
xml_files = glob.glob(os.path.join(exports_dir, "*.xml"))
print(f"Found {len(xml_files)} XML files:")
for xml_file in xml_files:
    print(f"  - {os.path.basename(xml_file)}")
```

---

## Performance

### Benchmarks

**Single Project Generation:**
- Template copy: ~0.5s
- Library installation: ~0.5-1.0s per library
- XML import: ~0.3-0.5s per file
- K-Bus configuration: ~0.1s per module
- GVL creation: ~0.2s
- **Total:** ~3-5 seconds

**Batch Processing:**
- 3 PLCs: ~9-15 seconds
- 10 PLCs: ~30-50 seconds
- 78 PLCs: ~6-7 minutes (production environment)

### Optimization Tips

1. **Use SSD storage** for project files
2. **Disable antivirus** scanning on project directory temporarily
3. **Close CODESYS IDE** during batch processing
4. **Pre-install libraries** in CODESYS (automatic discovery is faster)
5. **Use template** with pre-configured libraries (skip installation step)

---

## Backup & Recovery

### Backup Strategy

**Before Batch Processing:**
```bash
# Backup existing projects
xcopy "files\projects" "files\projects_backup_%date%" /E /I /Y

# Backup configuration
copy "project_config.json" "project_config_%date%.json.bak"
```

**Automated Backup Script:**
```batch
@echo off
set TIMESTAMP=%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%
set BACKUP_DIR=D:\WAGO\CODESYS\scripting\project generator\backups\%TIMESTAMP%
mkdir "%BACKUP_DIR%"
xcopy "files\projects\*.project" "%BACKUP_DIR%\projects\" /Y
copy "project_config.json" "%BACKUP_DIR%\"
echo Backup completed: %BACKUP_DIR%
```

### Recovery

**Restore Projects:**
```bash
# Restore from backup
xcopy "files\projects_backup_20241211\*" "files\projects\" /E /Y
```

**Re-run Failed Projects:**
1. Check log file for failed PLC IDs
2. Delete incomplete project files
3. Re-run script (auto-detect will skip existing valid projects)

---

## Security Considerations

### File Permissions
- **Read-only template:** Prevents accidental modification
- **Restricted logs:** Contains IP addresses and network topology
- **Secure config:** May contain library licenses or API keys

### Network Security
- Gateway discovery requires network access
- IP configuration exposes PLC addresses
- Consider VPN for remote execution

### Best Practices
1. Store configuration in version control (Git)
2. Use environment variables for sensitive paths
3. Restrict execution permissions on production systems
4. Audit log files regularly
5. Encrypt backups if stored remotely

---

## Maintenance

### Regular Tasks

**Weekly:**
- Review log files for errors
- Verify template project integrity
- Check for CODESYS updates

**Monthly:**
- Update library versions in configuration
- Clean old log files (>30 days)
- Test batch processing with sample projects

**Quarterly:**
- Review and update device descriptor database
- Audit namespace mapping
- Optimize configuration for performance

### Version Updates

**To update from 0.8.1 to 0.8.2:**
1. Backup current files
2. Replace `codesys_project_generator_local.py`
3. Update `project_config.json` (add auto_detect section)
4. Test with single PLC before batch processing
5. Review changelog in VERSION_HISTORY.md

---

## Support & Resources

### Documentation
- **README.md** - User guide and quick start
- **VERSION_HISTORY.md** - Complete changelog
- **PROGRAM_EXECUTION_FLOW.md** - Detailed process flow
- **WAGO_PLC_Interfaces_Documentation.md** - Technical reference

### Community
- **Repository:** https://github.com/WagoAlex/codesys-project-generator
- **Issues:** https://github.com/WagoAlex/codesys-project-generator/issues
- **Author:** Alexander Fugmann

### Getting Help

1. Check troubleshooting section above
2. Review log files for error details
3. Consult VERSION_HISTORY.md for known issues
4. Submit issue on GitHub with:
   - Version number (0.8.2)
   - Log file excerpt
   - Configuration file (redact sensitive data)
   - Steps to reproduce

---

## Appendix A: Complete Example

### Minimal Setup

**1. Directory structure:**
```
D:\WAGO\CODESYS\scripting\project generator\
├── codesys_project_generator_local.py
├── project_config.json
└── files\
    ├── exports\
    │   └── MyProgram.xml
    ├── outputs\
    │   ├── IO020_variables.txt
    │   └── PLC_IO020_config.json
    └── projects\
```

**2. Minimal project_config.json:**
```json
{
  "libraries": {
    "items": []
  },
  "function_blocks": {
    "items": []
  },
  "xml_imports": {
    "auto_detect": {
      "enabled": true,
      "directory": "exports"
    }
  }
}
```

**3. Execute:**
```bash
cd "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI --runscript="D:\WAGO\CODESYS\scripting\project generator\codesys_project_generator_local.py"
```

**4. Result:**
- Project created: `files\projects\IO020.project`
- XML imported from exports folder
- Variables added to GVL_IO020
- Log file: `files\logs\codesys_project_generator_local_log_*.txt`

---

**Document Version:** 0.8.2  
**Last Updated:** 2024-12-11  
**Maintained By:** Alexander Fugmann
