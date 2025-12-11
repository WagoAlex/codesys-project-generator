# PROGRAM EXECUTION FLOW

**CODESYS Project Generator**  
**Version:** 0.8.2 (Beta)  
**Author:** Alexander Fugmann  
**Last Updated:** 2024-12-11

---

## 📊 HIGH-LEVEL OVERVIEW

```
┌──────────────────────────────────────────────────────────────────┐
│                         MAIN WORKFLOW                            │
└──────────────────────────────────────────────────────────────────┘

1. Initialize logging system
2. Load project configuration (project_config.json)
3. Discover input files (auto-detect or specific mode)
4. FOR EACH PLC pair (variable file + config file):
   ├─► Execute 13-step generation process
   └─► Generate CODESYS project file
5. Output summary statistics
6. Close and cleanup

Duration: ~3-5 seconds per project
Batch Performance: 78 projects in ~6.5 minutes
```

---

## 🔧 MAIN EXECUTION FLOW

```
┌─────────────────────────────────────────────────────────────────┐
│                      main()                                      │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ├─► init_logging(script_name)
                       │   ├─► Create log directory if missing
                       │   ├─► Generate timestamped log file
                       │   │   Format: codesys_project_generator_local_log_YYYYMMDD_HHMMSS.txt
                       │   └─► Initialize color-coded console output
                       │
                       ├─► log_step("Collect Files")
                       │   │
                       │   ├─► IF AUTO_DETECT_MODE:
                       │   │   ├─► find_all_files("IO*_variables.txt")
                       │   │   ├─► find_all_files("PLC_IO*_config.json")
                       │   │   └─► match_files() → pairs
                       │   │       └─► Regex: IO(\d+)_variables.txt ↔ PLC_IO\1_config.json
                       │   │
                       │   └─► ELSE:
                       │       └─► Use SPECIFIC_VARIABLES_FILE + SPECIFIC_CONFIG_FILE
                       │
                       ├─► FOR EACH (var_file, config_file, plc_id) in matched_pairs:
                       │   │
                       │   ├─► log("PROJECT {current}/{total}: {plc_id}")
                       │   │
                       │   ├─► create_single_project(var_file, config_file, plc_id)
                       │   │   └─► [13-step process - see DETAILED FLOW]
                       │   │
                       │   └─► Update success_count or failure_count
                       │
                       └─► Output Summary:
                           ├─► Total projects processed
                           ├─► Successful count
                           ├─► Failed count
                           ├─► Total duration (formatted)
                           └─► Log file path
```

---

## 🎯 13-STEP DETAILED FLOW

### create_single_project(var_file, config_file, plc_name)

```
┌─────────────────────────────────────────────────────────────────┐
│              STEP 1/13: Load JSON Configuration                 │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► load_config_from_json(CONFIG_JSON_PATH)
                           ├─► Parse libraries section
                           │   └─► Extract: name, vendor, version, namespace, required
                           │
                           ├─► Parse function_blocks section
                           │   └─► Extract: fb_type, instance, params
                           │
                           ├─► Parse xml_imports section
                           │   ├─► Check auto_detect.enabled
                           │   ├─► IF enabled:
                           │   │   └─► auto_detect_xml_files()
                           │   │       ├─► Scan directory (e.g., "exports")
                           │   │       ├─► Apply pattern (e.g., "*.xml")
                           │   │       ├─► Exclude patterns (e.g., "*_backup.xml")
                           │   │       └─► Build xml_imports list
                           │   └─► ELSE:
                           │       └─► Use manual_files list
                           │
                           └─► Returns: (libraries, fb_instances, xml_imports, settings)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 2/13: Parse Input Files                       │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ├─► parse_variables_file(var_file)
                       │   ├─► Open file with UTF-8 encoding
                       │   ├─► Read entire content
                       │   │   Expected format: IEC 61131-3 VAR_GLOBAL block
                       │   └─► Returns: var_block (string)
                       │
                       └─► parse_config_json(config_file)
                           ├─► Open JSON with UTF-8 encoding
                           ├─► Validate: "PLC_Info" key present
                           ├─► Extract:
                           │   ├─► PLC_Info.Name
                           │   ├─► PLC_Info.Type
                           │   ├─► PLC_Info.IP_Address
                           │   └─► IO_Modules[] array
                           └─► Returns: config (dict)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 3/13: Create CODESYS Project                  │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► create_project_from_template()
                           ├─► Verify TEMPLATE_PROJECT exists
                           │   └─► Path: files/TEMPLATE_WAGO_750-8210.project
                           │
                           ├─► Build output path
                           │   └─► files/projects/{plc_name}.project
                           │
                           ├─► Create projects directory if missing
                           │
                           ├─► Delete old project file if exists
                           │
                           ├─► Copy template using shutil.copy2()
                           │   └─► Preserves file metadata
                           │
                           └─► Open project
                               ├─► projects.open(full_path, None, True)
                               └─► Returns: (proj, full_path)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 4/13: Find Application                        │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► find_or_create_application(proj)
                           ├─► Method 1: proj.find("Application", True)
                           │   └─► Search recursively for Application node
                           │
                           ├─► Method 2: Traverse all project objects
                           │   └─► proj.get_children(True)
                           │       └─► Check type and name for "Application"
                           │
                           └─► Method 3: Use active application
                               └─► proj.active_application
                               └─► Returns: app (Application object)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 5/13: Install Libraries                       │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► install_libraries_enhanced(proj, app, libraries)
                           │
                           ├─► get_library_manager_object(app)
                           │   ├─► app.get_children(recursive=True)
                           │   └─► Find object with: hasattr(obj, 'is_libman')
                           │
                           └─► FOR EACH library in libraries:
                               │
                               ├─► find_library_in_repositories(name, vendor, version)
                               │   │
                               │   ├─► Access: librarymanager.repositories
                               │   │   NOTE: Direct access, NOT system.librarymanager
                               │   │
                               │   ├─► FOR EACH repo in repositories:
                               │   │   └─► librarymanager.get_all_libraries(repo)
                               │   │       └─► FOR EACH lib:
                               │   │           ├─► Match: lib.title == name
                               │   │           ├─► Match: lib.company == vendor
                               │   │           └─► Match: lib.version == version
                               │   │
                               │   └─► extract_namespace_from_library(lib)
                               │       ├─► Try: lib.name (primary)
                               │       ├─► Try: lib.namespace (secondary)
                               │       ├─► Try: lib.default_namespace (tertiary)
                               │       └─► Fallback: lib.title
                               │
                               └─► add_library_to_application(libman, lib)
                                   ├─► libman.add_library(target_lib)
                                   └─► Track: added/skipped/failed counts

┌─────────────────────────────────────────────────────────────────┐
│              STEP 6/13: Import XML Files                        │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► import_xml_files(proj, xml_imports, conflict_mode)
                           │
                           ├─► Find Application object
                           │   └─► proj.find("Application", True)[0]
                           │
                           └─► FOR EACH xml_item in xml_imports:
                               │
                               ├─► Verify file exists
                               │   ├─► IF not found AND required:
                               │   │   └─► Log error, increment error_count
                               │   └─► IF not found AND optional:
                               │       └─► Log warning, increment skipped_count
                               │
                               ├─► detect_xml_format(filepath)
                               │   ├─► Read first 500 characters
                               │   ├─► Check for: "<ExportFile" → 'export'
                               │   ├─► Check for: "plcopen.org/xml/tc6" → 'plcopenxml'
                               │   ├─► Check for: "<project" → 'projectxml'
                               │   └─► Returns: format type
                               │
                               ├─► Validate format
                               │   └─► IF 'export':
                               │       └─► ERROR: Not supported (ISVNode required)
                               │
                               ├─► get_conflict_resolve_mode(mode_str)
                               │   ├─► "replace" → 0
                               │   ├─► "copy" → 1
                               │   └─► "skip" → 2
                               │
                               └─► app.import_xml(conflict_mode, filepath, True)
                                   └─► Imports POUs to Application node

┌─────────────────────────────────────────────────────────────────┐
│              STEP 7/13: Find PLC Device                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► find_plc_device(proj)
                           ├─► proj.find('Device', True)
                           │   └─► Returns array of Device objects
                           │
                           ├─► Filter by device name
                           │   └─► IF '750' in name OR 'PFC' in name:
                           │       └─► Likely WAGO controller
                           │
                           └─► Fallback: Use first device
                               └─► Returns: device (Device object)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 8/13: Configure IP Address                    │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► configure_device_ip(proj, device, ip_address)
                           │
                           ├─► Normalize IP address
                           │   └─► "172.16.46.020" → "172.16.46.20"
                           │       └─► Remove leading zeros from octets
                           │
                           ├─► Get gateway object
                           │   └─► get_first_gateway()
                           │       ├─► Access: online.gateways
                           │       └─► Returns: gateway object (not string!)
                           │
                           └─► Set IP address
                               ├─► device.set_gateway_and_ip_address(gateway, ip)
                               │   └─► NOTE: Requires gateway OBJECT, not string
                               │
                               └─► IF fails:
                                   └─► Log warning: Manual configuration needed

┌─────────────────────────────────────────────────────────────────┐
│              STEP 9/13: Configure K-Bus with IO Modules         │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ├─► find_kbus(device)
                       │   ├─► device.find('Kbus', True)
                       │   └─► Fallback: Search in device.get_children()
                       │       └─► Look for name containing "Kbus" or "KBus"
                       │
                       └─► add_io_modules_to_kbus(kbus, config)
                           │
                           └─► FOR EACH module in config["IO_Modules"]:
                               │
                               ├─► Extract module_type (e.g., "750-432")
                               │
                               ├─► is_blacklisted(module_type)?
                               │   └─► Blacklist: ["750-88", "750-89"]
                               │       └─► SKIP: PLC devices, not I/O modules
                               │
                               ├─► is_greylisted(module_type)?
                               │   └─► Greylist: ["750-610", "750-614"]
                               │       └─► SKIP: No process data
                               │
                               ├─► get_device_descriptor(module_type)
                               │   │
                               │   ├─► Lookup in WAGO_DEVICE_DESCRIPTORS
                               │   │   └─► 16 module types supported
                               │   │
                               │   ├─► Fallback for 750-652:
                               │   │   └─► IF base == "750-652":
                               │   │       └─► Return "750-652#48" descriptor
                               │   │
                               │   └─► Returns: {device_id, descriptor, version, name}
                               │
                               ├─► Refresh Kbus reference
                               │   └─► parent_device.find('Kbus', True)[0]
                               │       └─► Ensures up-to-date object reference
                               │
                               └─► Add module to K-Bus
                                   ├─► kbus.add(device_name, device_id, descriptor, version)
                                   │   └─► NOTE: Uses .add() method, NOT .create_child()
                                   │
                                   └─► Track: success_count/fail_count/skipped_count

┌─────────────────────────────────────────────────────────────────┐
│              STEP 10/13: Find/Update PLC_PRG                    │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► find_or_update_plc_prg(app)
                           ├─► app.find("PLC_PRG", True)
                           │   └─► Search for existing PLC_PRG
                           │
                           ├─► IF found:
                           │   └─► Update declaration and implementation
                           │       ├─► decl = pou.textual_declaration
                           │       └─► impl = pou.textual_implementation
                           │
                           └─► IF not found:
                               └─► app.create_pou("PLC_PRG", PouType.Program, None)
                                   └─► Create new program POU

┌─────────────────────────────────────────────────────────────────┐
│              STEP 11/13: Instantiate Function Blocks            │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► add_fb_instances_to_plc_prg(app, fb_instances)
                           │
                           ├─► Find PLC_PRG
                           │   └─► app.find("PLC_PRG", True)[0]
                           │
                           └─► FOR EACH fb_config in fb_instances:
                               │
                               ├─► create_fb_instance_code(fb_config)
                               │   │
                               │   ├─► Build VAR declaration
                               │   │   └─► "{instance} : {fb_type};"
                               │   │       Example: "oMQTTClient : MQTT.MQTTClient;"
                               │   │
                               │   └─► Build implementation call
                               │       ├─► Parse params dictionary
                               │       ├─► Build parameter list
                               │       │   ├─► Input: "param := value"
                               │       │   └─► Output: "param => variable"
                               │       └─► "{instance}({params});"
                               │           Example: "oMQTTClient(xEnable := xEnable);"
                               │
                               ├─► Update PLC_PRG declaration
                               │   ├─► Get current: pou.textual_declaration.text
                               │   ├─► Append: VAR block with FB instances
                               │   └─► Replace: pou.textual_declaration.replace(new_decl)
                               │
                               └─► Update PLC_PRG implementation
                                   ├─► Get current: pou.textual_implementation.text
                                   ├─► Append: FB calls
                                   └─► Replace: pou.textual_implementation.replace(new_impl)

┌─────────────────────────────────────────────────────────────────┐
│              STEP 12/13: Create GVL with Variables              │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       └─► create_gvl_with_variables(app, gvl_name, var_block)
                           │
                           ├─► Build GVL name
                           │   └─► "GVL_{plc_name}" (e.g., "GVL_IO020")
                           │
                           ├─► app.create_gvl(gvl_name)
                           │   └─► Creates new Global Variable List
                           │
                           └─► IF var_block provided:
                               └─► gvl.textual_declaration.replace(var_block)
                                   └─► Insert variable declarations
                                       Format: IEC 61131-3 VAR_GLOBAL block

┌─────────────────────────────────────────────────────────────────┐
│              STEP 13/13: Save Project                           │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ├─► proj.save()
                       │   └─► Writes all changes to .project file
                       │
                       ├─► proj.close()
                       │   └─► Releases file handles and resources
                       │
                       └─► Log success message
                           ├─► "PROJECT SUCCESSFUL: {plc_name}"
                           └─► "Path: {full_path}"
```

---

## 🔑 CRITICAL API CALLS

### Library Management

```python
# CORRECT (v0.8.1+)
repos = librarymanager.repositories              # Direct access
libman = get_library_manager_object(app)         # Find through app.get_children()
libman.add_library(target_lib)                   # Add to project

# INCORRECT (v0.8.0)
repos = system.librarymanager.repositories       # Does not exist
```

### K-Bus Module Addition

```python
# CORRECT (v0.8.1+)
kbus.add(device_name, device_id, descriptor, version)

# INCORRECT (v0.8.0)
kbus.create_child(device_id, 0, descriptor, version)  # Method does not exist
```

### IP Configuration

```python
# CORRECT (v0.8.1+)
gateway = get_first_gateway()                    # Get gateway object
device.set_gateway_and_ip_address(gateway, ip)  # Pass object

# INCORRECT (v0.8.0)
device.set_gateway_and_ip_address(gateway_str, ip)  # Causes GUID error
```

### XML Import

```python
# CORRECT - Import to Application
app = proj.find("Application", True)[0]
app.import_xml(conflict_mode, filepath, True)   # POUs appear under Application

# INCORRECT - Import to Project
proj.import_xml(conflict_mode, filepath, True)  # POUs appear in separate tab
```

---

## 📊 DATA STRUCTURES

### Configuration File (project_config.json)

```python
{
  "libraries": {
    "items": [
      {
        "name": str,          # Display name in CODESYS
        "vendor": str,        # "CODESYS", "WAGO", or "3S"
        "version": str|None,  # Specific version or None for latest
        "namespace": str,     # Internal namespace for FB references
        "required": bool      # Fail if not found?
      }
    ]
  },
  "function_blocks": {
    "items": [
      {
        "fb_type": str,       # Fully qualified (e.g., "MQTT.MQTTClient")
        "instance": str,      # Variable name
        "params": dict        # Parameter assignments
      }
    ]
  },
  "xml_imports": {
    "auto_detect": {
      "enabled": bool,              # Enable auto-detection?
      "directory": str,             # Scan directory
      "pattern": str,               # File pattern
      "exclude_patterns": [str],    # Exclusion patterns
      "default_conflict_resolve": str  # "replace", "copy", "skip"
    }
  }
}
```

### PLC Configuration File (PLC_IO020_config.json)

```python
{
  "PLC_Info": {
    "Name": str,          # PLC identifier (e.g., "IO020")
    "Type": str,          # Controller type (e.g., "750-8210")
    "IP_Address": str,    # IP address with optional leading zeros
    "Location": str,      # Physical location
    "IO_Box": str         # Box number
  },
  "IO_Modules": [
    {
      "Module_Type": str,     # WAGO module (e.g., "750-432")
      "Signals": [
        {
          "Terminal": str,      # Terminal address (e.g., "IX 0.0")
          "Object_Name": str,   # Variable name
          "Signal_Type": str,   # "I" or "O"
          "Signal": str         # Signal type (e.g., "24V DC")
        }
      ]
    }
  ]
}
```

---

## ⚡ PERFORMANCE METRICS

### Single Project

| Step | Duration | Percentage |
|------|----------|------------|
| 1. Load Configuration | 0.1s | 2% |
| 2. Parse Files | 0.1s | 2% |
| 3. Create Project | 0.5s | 14% |
| 4. Find Application | 0.1s | 2% |
| 5. Install Libraries | 1.0s | 28% |
| 6. Import XML | 0.5s | 14% |
| 7. Find Device | 0.1s | 2% |
| 8. Configure IP | 0.3s | 8% |
| 9. Configure K-Bus | 0.5s | 14% |
| 10. Find PLC_PRG | 0.1s | 2% |
| 11. Instantiate FBs | 0.2s | 6% |
| 12. Create GVL | 0.2s | 6% |
| 13. Save Project | 0.1s | 2% |
| **Total** | **~3.6s** | **100%** |

### Batch Processing

- **3 PLCs**: ~9-15 seconds
- **10 PLCs**: ~30-50 seconds
- **78 PLCs**: ~6-7 minutes

**Time Savings:**
- Manual: 6-13 hours per project
- Automated: 3-5 seconds per project
- **Improvement: 99.2%**

---

## 🛠️ ERROR HANDLING HIERARCHY

```
try:
    create_single_project()
    │
    ├─► Step 1-13 execution
    │   │
    │   └─► Each step has try/except:
    │       ├─► Log warning/error
    │       ├─► Increment fail counters
    │       └─► Continue or return False
    │
    └─► IF any critical failure:
        └─► Return False → Update failure_count

except Exception as e:
    ├─► Log critical error
    ├─► Print traceback
    └─► Return False
```

### Fallback Mechanisms

**Library Installation:**
- Primary: Search in all repositories
- Fallback: Skip if optional
- Critical: Fail if required

**IP Configuration:**
- Primary: Gateway discovery + set_gateway_and_ip_address()
- Fallback: Log warning (manual configuration needed)

**K-Bus Modules:**
- Blacklist: Skip automatically
- Greylist: Skip with info message
- Unknown: Log error, continue with next

**XML Import:**
- Format detection first
- Skip .export files (not supported)
- Continue on optional file errors
- Fail on required file errors

---

## 📝 LOGGING LEVELS

```
[INFO]     - Step progression, general information
[SUCCESS]  - Successful operations (green, bold)
[WARNING]  - Non-critical issues (yellow)
[ERROR]    - Failed operations (red, bold)
[DEBUG]    - Detailed diagnostic info (magenta)
```

**Log File Location:**
```
files/logs/codesys_project_generator_local_log_YYYYMMDD_HHMMSS.txt
```

---

**Document Version:** 0.8.2  
**Last Updated:** 2024-12-11  
**Maintained By:** Alexander Fugmann
