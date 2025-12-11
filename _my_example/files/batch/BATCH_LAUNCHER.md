# Batch Launcher Updates

## Files Created

### 1. ProjectGenerator_Local.bat (For Local Development)
**Configuration:** Uses `ProjectGenerator_Config_Local.ini`  
**Default Script:** `codesys_project_generator_local.py`  
**Paths:** D:\WAGO\CODESYS\scripting\project generator\

**Key Changes:**
- ✅ Reads from `ProjectGenerator_Config_Local.ini`
- ✅ Defaults to `codesys_project_generator_local.py`
- ✅ Title shows "(Local)" in ASCII art
- ✅ All D:\ specific paths

**Usage:**
```bash
# Double-click to run with default script
ProjectGenerator_Local.bat

# Or specify different script
ProjectGenerator_Local.bat standalone_xml_import.py
```

---

### 2. ProjectGenerator_Config_Local.ini (Updated)
**Updated Settings:**
```ini
[SCRIPTS]
Script1=codesys_project_generator_local.py
Script1_Name=CODESYS Project Generator (Local)

DefaultScript=codesys_project_generator_local.py
```

**Full Paths:**
```ini
[PATHS]
BasePath=D:\WAGO\CODESYS\scripting\project generator\files
ScriptDirectory=D:\WAGO\CODESYS\scripting\project generator
LogDirectory=D:\WAGO\CODESYS\scripting\project generator\logs
```

---



## Directory Structure

### Local Development
```
D:\WAGO\CODESYS\scripting\project generator\
├── ProjectGenerator_Local.bat              ← Double-click this
├── ProjectGenerator_Config_Local.ini       ← Configuration
├── codesys_project_generator_local.py      ← Main script
├── standalone_xml_import.py
├── config_loader.py
└── files\
    ├── exports\                            ← PLCopenXML files
    ├── outputs\                            ← IO020_variables.txt
    └── projects\                           ← Generated .project files
```



---

## Quick Start

### Local Development
1. Copy all files to `D:\WAGO\CODESYS\scripting\project generator\`
2. Ensure `codesys_project_generator_local.py` is present
3. Double-click `ProjectGenerator_Local.bat`

### GitHub Clone
1. Clone repository
2. Edit `ProjectGenerator_Config.ini` for your CODESYS path
3. Double-click `ProjectGenerator.bat`

---

## Configuration Notes

### Script Override
Both batch files support command-line override:
```bash
ProjectGenerator_Local.bat standalone_xml_import.py
ProjectGenerator.bat test_xml_import.py
```

### Log Display
- Default: Last 15 lines (configurable via `MaxLogLines` in INI)
- Uses PowerShell for colored output (fallback to type if unavailable)
- Creates logs in configured LogDirectory

### Error Handling
- ✅ Validates CODESYS installation
- ✅ Validates script existence
- ✅ Creates log directory if missing
- ✅ Shows available scripts on error
- ✅ Displays execution summary with duration

---

## ASCII Art Changes

### Local Version
```
================================================
==                                            ==
==    ##      ##    ###     ####    ####     ==
==    ##  ##  ##   ## ##   ##      ##  ##    ==
==    ##  ##  ##  ##   ##  ## ###  ##  ##    ==
==    ##  ##  ##  #######  ##  ##  ##  ##    ==
==     ###  ###   ##   ##   ####    ####     ==
==                                            ==
================================================

     CODESYS Project Generator (Local)
================================================
```



---

## Version Information

**Author:** Alexander Fugmann  
**Updated:** 2024-12-10  
**Purpose:** Local development vs GitHub deployment differentiation

---

## Testing

### Test Local Batch
```bash
cd "D:\WAGO\CODESYS\scripting\project generator"
ProjectGenerator_Local.bat
```

Expected:
- ✅ Loads ProjectGenerator_Config_Local.ini
- ✅ Uses codesys_project_generator_local.py
- ✅ Shows "(Local)" in title
- ✅ All D:\ paths work

### Test GitHub Batch
```bash
cd codesys-project-generator
ProjectGenerator.bat
```

Expected:
- ✅ Loads ProjectGenerator_Config.ini
- ✅ Uses codesys_project_generator.py
- ✅ Generic title
- ✅ Relative paths work

---

**All batch files ready for deployment!**
