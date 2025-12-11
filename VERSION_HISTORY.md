# Version History

## CODESYS Project Generator for WAGO PLCs

**Status:** Beta - Active Development  
**Current Version:** 0.8.2  
**Author:** Alexander Fugmann

---

## Version Table

| Date | Version | Author | Change Summary |
|------|---------|--------|----------------|
| 11.12.2024 | 0.8.2 | Alexander Fugmann | Auto-detect XML files from directory, exclude patterns support |
| 11.12.2024 | 0.8.2 | Alexander Fugmann | English logs and configuration, internationalization prep |
| 11.12.2024 | 0.8.1 | Alexander Fugmann | Fixed library installation API (librarymanager.repositories) |
| 11.12.2024 | 0.8.1 | Alexander Fugmann | Fixed IO module creation (kbus.add method) |
| 11.12.2024 | 0.8.1 | Alexander Fugmann | Fixed IP configuration (gateway object vs string) |
| 11.12.2024 | 0.8.1 | Alexander Fugmann | Fixed vendor/company field mapping in JSON config |
| 10.12.2024 | 0.8.0 | Alexander Fugmann | Added XML import capability (PLCopenXML/ProjectXML) |
| 10.12.2024 | 0.8.0 | Alexander Fugmann | Format detection and conflict resolution modes |
| 10.12.2024 | 0.8.0 | Alexander Fugmann | MQTT Client and MQTT Publish function block templates |
| 10.12.2024 | 0.8.0 | Alexander Fugmann | Renamed configuration: library_fb_config.json → project_config.json |
| 10.12.2024 | 0.8.0 | Alexander Fugmann | Restructured project paths: files/{exports,outputs,projects} |
| 05.12.2024 | 0.7.1 | Alexander Fugmann | Enhanced library installation using repository API |
| 05.12.2024 | 0.7.1 | Alexander Fugmann | Function block instantiation from JSON configuration |
| 05.12.2024 | 0.7.1 | Alexander Fugmann | Fixed device descriptor mapping for 750-series modules |
| 01.12.2024 | 0.7.0 | Alexander Fugmann | Template-based project creation (shutil.copy2 + projects.open) |
| 01.12.2024 | 0.7.0 | Alexander Fugmann | Automatic I/O module configuration from JSON |
| 01.12.2024 | 0.7.0 | Alexander Fugmann | GVL generation with variable declarations |
| 25.11.2024 | 0.6.0 | Alexander Fugmann | JSON-based configuration system |
| 25.11.2024 | 0.6.0 | Alexander Fugmann | Batch processing of multiple PLCs |
| 20.11.2024 | 0.5.0 | Alexander Fugmann | Initial ScriptEngine automation |

---

## Version 0.8.2 (2024-12-11) - Stability & Internationalization

### Critical Bug Fixes
**Library Installation API**
- Fixed: `'SystemImpl' object has no attribute 'librarymanager'`
- Root Cause: Incorrect API usage - `system.librarymanager` does not exist
- Solution: Use `librarymanager.repositories` directly
- Impact: Libraries can now be installed successfully

**IO Module Creation API**
- Fixed: `'ScriptObject' object has no attribute 'create_child'`
- Root Cause: Wrong method - `create_child()` is not available for Kbus objects
- Solution: Use `kbus.add(device_name, device_id, descriptor, version)` method
- Impact: IO modules are now properly added to K-Bus

**IP Configuration API**
- Fixed: `GUID muss 32 Ziffern mit 4 Bindestrichen enthalten`
- Root Cause: Passing IP as string instead of gateway object
- Solution: Use `get_first_gateway()` to retrieve gateway object, then `device.set_gateway_and_ip_address(gateway, ip)`
- Impact: IP addresses can now be configured without GUID errors

**Configuration Field Mapping**
- Fixed: Vendor/Company field confusion in JSON configuration
- Root Cause: Mixed usage of "vendor" and "company" fields
- Solution: Standardized on "vendor" field throughout
- Impact: Library searches now work correctly with CODESYS and WAGO vendors

### New Features
**Auto-Detect XML Files**
```json
{
  "xml_imports": {
    "auto_detect": {
      "enabled": true,
      "directory": "exports",
      "pattern": "*.xml",
      "exclude_patterns": ["*_backup.xml", "*_old.xml"]
    }
  }
}
```
- Automatically scans directory for all .xml files
- No manual file list configuration needed
- Support for exclude patterns (backups, old versions)
- Configurable conflict resolution per file

**Internationalization**
- All logs converted to English
- Configuration descriptions in English
- Error messages standardized
- Duration formatting: "5 min 23 sec" (was: "5 Min 23 Sek")
- Step indicators: "STEP 5/13" (was: "SCHRITT 5/13")

**Enhanced Logging**
- Color-coded console output (ANSI escape sequences)
- Timestamped file logs with UTF-8 encoding
- Structured log levels: INFO, SUCCESS, WARNING, ERROR, DEBUG
- Auto-generated log files: `codesys_project_generator_local_log_YYYYMMDD_HHMMSS.txt`

### API Corrections
```python
# CORRECT Implementation (v0.8.2)
repos = librarymanager.repositories              # Direct access
libman = get_library_manager_object(app)         # Through app children
kbus.add(device_name, device_id, descriptor, version)  # Proper method
gateway = get_first_gateway()                    # Gateway object
device.set_gateway_and_ip_address(gateway, ip)  # With object

# INCORRECT Implementation (v0.8.0)
repos = system.librarymanager.repositories       # Does not exist
kbus.create_child(device_id, 0, descriptor, version)  # Does not exist
device.set_gateway_and_ip_address(gateway_str, ip)   # Causes GUID error
```

### Configuration Changes
**project_config.json Structure**
```json
{
  "configuration": {
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
        "namespace": "MQTT"
      }
    ]
  },
  "xml_imports": {
    "auto_detect": {
      "enabled": true,
      "directory": "exports"
    }
  }
}
```

---

## Version 0.8.1 (2024-12-11) - API Fixes

### Issues Resolved
1. Library installation completely broken
2. IO modules failing to add to K-Bus
3. IP configuration throwing GUID errors
4. 750-652 serial interface module not recognized

### Implementation Details
**Library Manager Discovery**
```python
def get_library_manager_object(app):
    """Find Library Manager in application tree"""
    objects = app.get_children(recursive=True)
    for obj in objects:
        if hasattr(obj, 'is_libman') and obj.is_libman:
            return obj
    return None
```

**K-Bus Module Addition**
```python
def add_io_modules_to_kbus(kbus, config):
    """Add IO modules using kbus.add() method"""
    descriptor_info = get_device_descriptor(module_type)
    kbus.add(
        descriptor_info['name'],
        descriptor_info['device_id'],
        descriptor_info['descriptor'],
        descriptor_info['version']
    )
```

**750-652 Fallback**
```python
def get_device_descriptor(module_type):
    """Get descriptor with 750-652 fallback"""
    if module_type.startswith("750-652"):
        return WAGO_DEVICE_DESCRIPTORS.get("750-652#48")  # Default to 48 bytes
```

---

## Version 0.8.0 (2024-12-10) - XML Import System

### Major Features
**XML Import Capabilities**
- PLCopenXML Support (IEC 61131-3 standard)
- Project XML Support (CODESYS native format)
- Automatic format detection
- Three conflict resolution modes: Replace (0), Copy (1), Skip (2)
- Application-targeted imports (objects appear under Application node)

**Function Block Templates**
- MQTT.MQTTClient with unique client ID generation
- MQTT.MQTTPublish with payload pointer handling
- Automatic code generation for pointer setup
- WagoSysString integration for string length calculation

**Project Structure**
```
project generator/
├── files/
│   ├── exports/           # PLCopenXML files
│   ├── outputs/           # Variable files (IO020_variables.txt)
│   ├── projects/          # Generated CODESYS projects
│   └── project_config.json
```

### Limitations
- **.export Files Not Supported**: Require ISVNode (unavailable in IronPython ScriptEngine)
- **Workaround**: Convert .export to PLCopenXML or import manually in IDE

### Configuration Renamed
```
OLD: library_fb_config.json
NEW: project_config.json (future-proof naming)
```

---

## Version 0.7.x (2024-12-01 to 2024-12-05)

### Template-Based Architecture (0.7.0)
- Project creation via `shutil.copy2()` + `projects.open()`
- Replaced unreliable `projects.create()` method
- Template: `TEMPLATE_WAGO_750-8210.project`
- Success rate: 100% (was 40% with create method)

### Library Management (0.7.1)
- Repository API integration
- Automatic namespace extraction from library objects
- Vendor-specific handling (CODESYS vs WAGO)
- Version-specific library selection

### IO Module Configuration (0.7.0)
- Automatic K-Bus configuration from JSON
- Device descriptor database (16 WAGO modules)
- Blacklist: 750-88x PLC devices
- Greylist: 750-610, 750-614 (no process data)

### Global Variable Lists (0.7.0)
- Automatic GVL generation from variable files
- IEC 61131-3 compliant declarations
- UTF-8 encoding support
- Preserved formatting and comments

---

## Version 0.6.0 (2024-11-25) - JSON Configuration

### Features
- JSON-based configuration system
- Multi-PLC batch processing
- Auto-detect mode for file pairs
- Structured error reporting
- Statistics tracking

---

## Version 0.5.0 (2024-11-20) - Initial Release

### Features
- ScriptEngine automation foundation
- Basic project creation
- Variable file parsing
- Manual configuration

---

## Technical Specifications

### Supported CODESYS Versions
- CODESYS V3.5 SP16+
- CODESYS V3.5 SP21 Patch 1 (tested)
- IronPython 2.7 (embedded in ScriptEngine)

### Supported Hardware
- WAGO PFC200 series (750-8210, 750-8212, etc.)
- WAGO I/O modules (750-4xx, 750-5xx, 750-6xx series)
- K-Bus topology

### Not Compatible
- CODESYS V2.x
- .export file imports (use PLCopenXML conversion)
- CODESYS versions without ScriptEngine

---

## Migration Guide

### From 0.7.x to 0.8.0
1. Rename configuration file: `library_fb_config.json` → `project_config.json`
2. Add `xml_imports` section to JSON
3. Create `files/exports/` directory
4. Update MQTT function block parameters (see config examples)

### From 0.8.0 to 0.8.1
1. No configuration changes required
2. Scripts will automatically use corrected APIs

### From 0.8.1 to 0.8.2
1. Update `project_config.json` with auto-detect section (optional)
2. No breaking changes - existing configs continue to work

---

## Known Issues

### Beta Status Notice
This project is in **active beta development**. While functional for production use, the API may change between minor versions (0.x.y). Breaking changes will be clearly documented in this version history.

### Current Limitations
1. Single Application per project (multiple Applications not tested)
2. No nested POU folder structure support
3. Limited to WAGO 750-series modules (extensible via descriptor dictionary)
4. IP configuration requires gateway discovery (may fail without network connection)

### Planned Features (0.9.0+)
- [ ] Web-based configuration interface
- [ ] Real-time validation before project generation
- [ ] Support for custom device descriptors
- [ ] Multi-project workspace support
- [ ] Undo/rollback functionality

---

## Development Roadmap

### Version 0.9.0 (Q1 2025)
- Configuration validation API
- Enhanced error recovery
- Project comparison tools
- Backup/restore functionality

### Version 1.0.0 (Q2 2025)
- Production-ready release
- Complete API stabilization
- Comprehensive test suite
- Extended hardware support

---

## Contributing

This project is maintained by Alexander Fugmann. For bug reports, feature requests, or contributions:

- **Repository**: https://github.com/WagoAlex/codesys-project-generator
- **Issues**: https://github.com/WagoAlex/codesys-project-generator/issues
- **Documentation**: See README.md and SCRIPTENGINE_API_REFERENCE.md

---

**Document Status:** Current  
**Last Updated:** 2024-12-11  
**Next Review:** 2025-01-11  
**Maintained By:** Alexander Fugmann
