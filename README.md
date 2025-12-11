# CODESYS Project Generator for WAGO PLCs

**Version:** 0.8.2 (Beta)  
**Author:** Alexander Fugmann  
**Status:** Active Development  
**Last Updated:** 2024-12-11

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Input Files](#-input-files)
- [Execution](#-execution)
- [Output](#-output)
- [Troubleshooting](#-troubleshooting)
- [Documentation](#-documentation)
- [Version History](#-version-history)

---

## 🎯 Overview

### What is this tool?

The CODESYS Project Generator automates the creation of WAGO PLC projects from structured input data. It eliminates manual project setup by automatically configuring devices, installing libraries, importing code, and generating variable lists.

### Problem Statement

Traditional PLC project creation involves:
- **6-13 hours** of manual work per project
- Error-prone device configuration
- Repetitive library installation
- Manual variable list creation
- Inconsistent project structures

### Solution

This toolchain automates the entire workflow:
1. **Extract** configuration from JSON files
2. **Validate** IP addresses, module types, and signal consistency
3. **Generate** complete CODESYS projects via ScriptEngine API
4. **Configure** devices, install libraries, import POUs, create variables
5. **Process** batch of 78 PLCs in ~6.5 minutes (99.2% time reduction)

---

## ✨ Key Features

### Automated Project Creation
- **Template-based generation** from WAGO 750-8210 template
- **13-step workflow** ensuring consistent results
- **Batch processing** of multiple PLCs simultaneously
- **Auto-detect mode** for file pair matching

### Device Configuration
- **K-Bus topology** with automatic I/O module assignment
- **16 WAGO module types** supported (750-4xx, 750-5xx, 750-6xx)
- **IP address configuration** with gateway discovery
- **Device descriptor** management

### Library Management
- **Automatic library installation** from CODESYS repositories
- **Namespace extraction** for correct FB references
- **Vendor-specific handling** (CODESYS, WAGO, 3S)
- **Version-specific selection**

### XML Import System
- **PLCopenXML support** (IEC 61131-3 standard)
- **Project XML support** (CODESYS native format)
- **Auto-detection** of all .xml files in exports folder
- **Conflict resolution** (Replace, Copy, Skip)
- **Format detection** with validation

### Function Block Integration
- **Automatic FB instantiation** from JSON configuration
- **Parameter mapping** with type checking
- **MQTT Client** and **MQTT Publish** templates
- **Payload pointer handling** for string operations

### Quality Assurance
- **Comprehensive logging** with color-coded console output
- **Validation reports** for each step
- **Statistics tracking** (modules added, errors, duration)
- **Error recovery** with fallback mechanisms

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                          INPUT LAYER                             │
│                                                                  │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────┐  │
│  │  Variable Files │  │  PLC Config JSON │  │  XML Exports   │  │
│  │  IO020_vars.txt │  │  PLC_IO020.json  │  │  Program.xml   │  │
│  └─────────────────┘  └──────────────────┘  └────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Configuration: project_config.json                      │   │
│  │  ├─ Libraries (MQTT, JSON, WagoAppCloud)                 │   │
│  │  ├─ Function Blocks (MQTTClient, MQTTPublish)            │   │
│  │  └─ XML Import Settings (auto-detect enabled)            │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                      PROCESSING LAYER                            │
│                codesys_project_generator_local.py                │
│                                                                  │
│  Step 1:  Load JSON Configuration                               │
│  Step 2:  Parse Input Files (variables + PLC config)            │
│  Step 3:  Create CODESYS Project (template copy)                │
│  Step 4:  Find Application Node                                 │
│  Step 5:  Install Libraries (from repositories)                 │
│  Step 6:  Import XML Files (PLCopenXML to Application)          │
│  Step 7:  Find PLC Device                                       │
│  Step 8:  Configure IP Address (with gateway)                   │
│  Step 9:  Configure K-Bus with IO Modules                       │
│  Step 10: Find/Update PLC_PRG                                   │
│  Step 11: Instantiate Function Blocks                           │
│  Step 12: Create GVL with Variables                             │
│  Step 13: Save and Close Project                                │
│                                                                  │
│  Duration: ~3-5 seconds per project                              │
└──────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│                        OUTPUT LAYER                              │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐   │
│  │  CODESYS Project │  │  Log Files       │  │  Statistics  │   │
│  │  IO020.project   │  │  generator.log   │  │  summary.txt │   │
│  └──────────────────┘  └──────────────────┘  └──────────────┘   │
│                                                                  │
│  Project Contents:                                               │
│  ├─ Device (750-8210) with IP 172.16.46.020                     │
│  ├─ K-Bus with IO modules (750-432, 750-461, 750-515)           │
│  ├─ Libraries (MQTT Client SL, JSON Utilities SL)               │
│  ├─ POUs from XML imports (MQTT_Program, Utilities)             │
│  ├─ Function Blocks (oMQTTClient, oMQTTPublish)                 │
│  └─ GVL_IO020 with variable declarations                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- CODESYS V3.5 SP16+ (tested with SP21 Patch 1)
- WAGO Device Descriptor packages installed
- Windows 10/11 with ANSI color support
- Required libraries in CODESYS (MQTT Client SL, etc.)

### Installation

```bash
# 1. Create directory structure
mkdir "D:\WAGO\CODESYS\scripting\project generator"
cd "D:\WAGO\CODESYS\scripting\project generator"
mkdir files\exports files\outputs files\projects

# 2. Copy files
# - codesys_project_generator_local.py
# - project_config.json
# - WAGO_ProjectGenerator.bat

# 3. Add input files
# Place in files\outputs\:
#   - IO020_variables.txt
#   - PLC_IO020_config.json
# Place in files\exports\:
#   - YourProgram.xml
```

### First Run

```bash
# Execute batch launcher
WAGO_ProjectGenerator.bat

# Or run directly
cd "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI --runscript="D:\...\codesys_project_generator_local.py"
```

### Expected Output

```
[INFO] STEP 1/13: Load JSON Configuration
[SUCCESS]   [OK] Configuration loaded
[INFO] STEP 5/13: Install Libraries
[SUCCESS]   [FOUND] MQTT Client SL, 1.10.0.0 (CODESYS)
[INFO] STEP 6/13: Import XML Files
[SUCCESS]     SUCCESS
[SUCCESS] PROJECT SUCCESSFUL: IO020
```

**Generated:** `files\projects\IO020.project`

---

## ⚙️ Configuration

### project_config.json Structure

```json
{
  "configuration": {
    "description": "CODESYS Project Generator Configuration",
    "version": "0.8.2",
    "namespace_mapping": {
      "MQTT Client SL": "MQTT",
      "JSON Utilities SL": "JSON"
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
      "exclude_patterns": ["*_backup.xml"],
      "default_conflict_resolve": "replace"
    }
  }
}
```

### Key Configuration Sections

**libraries.items[]**
- Define libraries to install automatically
- Specify vendor (CODESYS, WAGO, 3S)
- Optional version pinning
- Namespace for FB references

**function_blocks.items[]**
- FB type with full namespace (e.g., "MQTT.MQTTClient")
- Instance variable name
- Parameter assignments (input/output/in-out)

**xml_imports.auto_detect**
- Enable automatic XML file discovery
- Specify directory (relative to BASE_PATH)
- Set file pattern and exclusions
- Configure conflict resolution mode

---

## 📄 Input Files

### Variable Files

**Format:** `IO{NUMBER}_variables.txt`  
**Location:** `files/outputs/`  
**Content:** IEC 61131-3 variable declarations

```
VAR_GLOBAL
    (* Digital Inputs *)
    IO020_DI_01 AT %IX0.0 : BOOL;
    IO020_DI_02 AT %IX0.1 : BOOL;
    
    (* Analog Inputs *)
    IO020_AI_TempSensor AT %IW2 : INT;
    
    (* Digital Outputs *)
    IO020_DO_Pump01 AT %QX0.0 : BOOL;
END_VAR
```

### PLC Configuration Files

**Format:** `PLC_IO{NUMBER}_config.json`  
**Location:** `files/outputs/`

```json
{
  "PLC_Info": {
    "Name": "IO020",
    "Type": "750-8210",
    "IP_Address": "172.16.46.020",
    "Location": "Cabinet A3",
    "IO_Box": "36140310.0"
  },
  "IO_Modules": [
    {
      "Module_Type": "750-432",
      "Signals": [
        {
          "Terminal": "IX 0.0",
          "Object_Name": "IO020_DI_01",
          "Signal_Type": "I",
          "Signal": "24V DC"
        }
      ]
    },
    {
      "Module_Type": "750-461",
      "Signals": [
        {
          "Terminal": "IW 2",
          "Object_Name": "IO020_AI_TempSensor",
          "Signal_Type": "I",
          "Signal": "PT100"
        }
      ]
    }
  ],
  "Statistics": {
    "Total_Modules": 4,
    "Total_Signals": 42,
    "Input_Signals": 25,
    "Output_Signals": 17
  }
}
```

### XML Files

**Location:** `files/exports/`  
**Formats:** PLCopenXML or CODESYS Project XML

**Example PLCopenXML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://www.plcopen.org/xml/tc6_0201">
  <fileHeader companyName="WAGO" 
              productName="MQTT_Program" 
              creationDateTime="2024-12-11T10:30:00"/>
  <contentHeader name="MQTT_Communication">
    <pous>
      <pou name="MQTT_Handler" pouType="program">
        <!-- POU content -->
      </pou>
    </pous>
  </contentHeader>
</project>
```

**Supported:**
- ✅ PLCopenXML (IEC 61131-3 standard)
- ✅ CODESYS Project XML
- ❌ .export files (requires ISVNode - not available in IronPython)

---

## ▶️ Execution

### Method 1: Batch Launcher

```batch
@echo off
cd /d "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI ^
  --profile="CODESYS V3.5 SP21 Patch 1" ^
  --runscript="D:\WAGO\CODESYS\scripting\project generator\codesys_project_generator_local.py"
pause
```

### Method 2: Command Line

```bash
cd "C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
Codesys.exe --noUI --runscript="D:\...\codesys_project_generator_local.py"
```

### Execution Modes

**Auto-Detect Mode (default):**
```python
AUTO_DETECT_MODE = True
# Automatically finds all IO*_variables.txt and PLC_IO*_config.json pairs
```

**Specific Mode:**
```python
AUTO_DETECT_MODE = False
SPECIFIC_VARIABLES_FILE = "IO020_variables.txt"
SPECIFIC_CONFIG_FILE = "PLC_IO020_config.json"
```

---

## 📊 Output

### Generated Projects

**Location:** `files/projects/`  
**Format:** `IO{NUMBER}.project`

**Project Structure:**
```
IO020.project
├── Application
│   ├── POUs (from XML imports)
│   │   ├── MQTT_Handler (PROGRAM)
│   │   ├── DataConverter (FUNCTION)
│   │   └── ErrorHandling (FUNCTION_BLOCK)
│   ├── PLC_PRG (PROGRAM)
│   │   ├── VAR: oMQTTClient : MQTT.MQTTClient
│   │   └── Implementation: oMQTTClient(...)
│   └── GVLs
│       └── GVL_IO020 (variable declarations)
└── Device
    ├── Device (750-8210) @ 172.16.46.020
    └── K-Bus
        ├── 750-432 (4DI 24V DC)
        ├── 750-461 (2AI PT100)
        └── 750-515 (4RO Relay)
```

### Log Files

**Location:** `files/logs/`  
**Format:** `codesys_project_generator_local_log_YYYYMMDD_HHMMSS.txt`

**Sample Output:**
```
[2024-12-11 14:30:52] [INFO] ==============================
[2024-12-11 14:30:52] [INFO] STEP 1/13: Load JSON Configuration
[2024-12-11 14:30:52] [SUCCESS]   [OK] Configuration loaded
[2024-12-11 14:30:52] [INFO]     Libraries: 4
[2024-12-11 14:30:52] [INFO]     Function Blocks: 2
[2024-12-11 14:30:52] [INFO]     XML Imports: 3
[2024-12-11 14:30:53] [INFO] STEP 5/13: Install Libraries
[2024-12-11 14:30:53] [SUCCESS]   [FOUND] MQTT Client SL, 1.10.0.0 (CODESYS)
[2024-12-11 14:30:53] [SUCCESS]   [NAMESPACE] MQTT
[2024-12-11 14:30:53] [SUCCESS]   [SUCCESS]
[2024-12-11 14:30:54] [INFO] STEP 6/13: Import XML Files
[2024-12-11 14:30:54] [INFO]   Auto-detecting XML files...
[2024-12-11 14:30:54] [INFO]     Directory: D:\...\exports
[2024-12-11 14:30:54] [INFO]     Found 3 XML files
[2024-12-11 14:30:54] [SUCCESS]       Added: MQTT_Program.xml
[2024-12-11 14:30:54] [SUCCESS]       Added: Utilities.xml
[2024-12-11 14:30:54] [INFO]       Excluded: old_backup.xml
[2024-12-11 14:30:55] [SUCCESS] PROJECT SUCCESSFUL: IO020
[2024-12-11 14:30:55] [INFO]   Path: D:\...\projects\IO020.project
```

### Summary Statistics

```
Total:       3 projects
Successful:  3
Failed:      0
Duration:    9.3 seconds
```

---

## 🔧 Troubleshooting

### Common Issues

**Library Installation Fails**
```
[ERROR] 'SystemImpl' object has no attribute 'librarymanager'
```
**Solution:** Update to v0.8.1+ (fixed API usage)

**IO Modules Not Added**
```
[ERROR] 'ScriptObject' object has no attribute 'create_child'
```
**Solution:** Update to v0.8.1+ (uses `kbus.add()` method)

**IP Configuration Error**
```
[WARNING] GUID muss 32 Ziffern mit 4 Bindestrichen enthalten
```
**Solution:** Update to v0.8.1+ (uses gateway object)

**XML Files Not Found**
```
[ERROR] Not found (required) - ERROR
```
**Solution:**
- Verify files exist in `files/exports/`
- Check auto-detect configuration
- Set `optional: true` if file is not critical

**Template Missing**
```
[ERROR] Template not found!
```
**Solution:**
- Create template in CODESYS IDE manually
- Save as: `files/TEMPLATE_WAGO_750-8210.project`
- Must include: Application, Device (750-8210), K-Bus

### Debug Mode

Enable in `project_config.json`:
```json
{
  "debugging": {
    "enable_detailed_logging": true,
    "log_language": "en"
  }
}
```

---

## 📚 Documentation

### Available Documentation

- **README.md** (this file) - User guide and quick reference
- **VERSION_HISTORY.md** - Complete changelog with version table
- **DEPLOYMENT_GUIDE.md** - Installation and setup instructions
- **PROGRAM_EXECUTION_FLOW.md** - Detailed process flow diagrams
- **WAGO_PLC_Interfaces_Documentation.md** - Technical API reference

### Technical Specifications

**Supported Modules:**
- Digital Inputs: 750-402, 750-430, 750-432, 750-1415, 750-1420
- Relays: 750-512, 750-515, 750-517
- Digital Outputs: 750-531
- Analog Inputs: 750-461, 750-472
- Analog Outputs: 750-550, 750-554
- Serial Interfaces: 750-652 (8/24/48 bytes)

**Module Blacklist:**
- 750-88x (PLC devices - skipped automatically)

**Module Greylist:**
- 750-610, 750-614 (no process data - require manual config)

---

## 📖 Version History

**Current Version:** 0.8.2 (Beta)

### Recent Changes (0.8.2 - 2024-12-11)

**Critical Bug Fixes:**
- Fixed library installation API (`librarymanager.repositories`)
- Fixed IO module creation API (`kbus.add()` method)
- Fixed IP configuration API (gateway object)
- Fixed vendor/company field mapping

**New Features:**
- Auto-detect XML files from directory
- English logs and configuration
- Exclude patterns for XML detection

**See VERSION_HISTORY.md for complete changelog**

### Version Roadmap

- **0.9.0** (Q1 2025) - Configuration validation API, enhanced error recovery
- **1.0.0** (Q2 2025) - Production release, API stabilization, extended hardware support

---

## 🤝 Contributing

This project is maintained by Alexander Fugmann.

**Repository:** https://github.com/WagoAlex/codesys-project-generator  
**Issues:** https://github.com/WagoAlex/codesys-project-generator/issues

### Reporting Issues

When reporting issues, please include:
1. Version number (0.8.2)
2. Log file excerpt showing error
3. Configuration file (redact sensitive data)
4. Steps to reproduce

---

## 📜 License

Copyright © 2024 Alexander Fugmann. All rights reserved.

This software is provided for use with WAGO PLC systems. Redistribution and commercial use require explicit permission.

---

## 🙏 Acknowledgments

- WAGO GmbH & Co. KG for PLC hardware and device descriptors
- CODESYS GmbH for ScriptEngine API documentation
- IEC for IEC 61131-3 standard and PLCopenXML format

---

**Document Version:** 0.8.2  
**Last Updated:** 2024-12-11  
**Maintained By:** Alexander Fugmann
