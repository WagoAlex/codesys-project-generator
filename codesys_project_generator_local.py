# -*- coding: utf-8 -*-
# encoding: utf-8
"""
CODESYS Project Generator - Enhanced Local Edition with XML Import
Based on create_codesys_project_enhanced.py with XML import capability
"""

import sys
import time
import os
import json
import re
import glob

# =============================================================================
# CONFIGURATION
# =============================================================================
BASE_PATH = r"D:\WAGO\CODESYS\scripting\project generator\files"
DEFAULT_PROJECT_PATH = os.path.join(BASE_PATH, "projects")
DEFAULT_VARIABLES_PATH = os.path.join(BASE_PATH, "outputs")
DEFAULT_CONFIG_PATH = os.path.join(BASE_PATH, "outputs")
CONFIG_JSON_PATH = os.path.join(BASE_PATH, "project_config.json")

USE_TEMPLATE = True
TEMPLATE_PROJECT = os.path.join(BASE_PATH, "TEMPLATE_WAGO_750-8210.project")

AUTO_DETECT_MODE = True

SPECIFIC_VARIABLES_FILE = os.path.join(DEFAULT_VARIABLES_PATH, "IO020_variables.txt")
SPECIFIC_CONFIG_FILE = os.path.join(DEFAULT_VARIABLES_PATH, "PLC_IO020_config.json")

TOTAL_STEPS_PER_PROJECT = 13
CURRENT_STEP = 0
LOG_FILE = None

REQUIRED_LIBRARIES = []
FB_INSTANCES = []
XML_IMPORTS = []

EXAMPLE_LIBRARIES = [
    {"name": "MQTT_Client_SL", "vendor": "CODESYS", "version": "1.10.0.0", "required": False},
    {"name": "WagoAppCloud", "vendor": "WAGO", "version": "1.3.5.7", "required": False},
    {"name": "JSON_Utilities_SL", "vendor": "CODESYS", "version": "1.9.0.0", "required": False},
    {"name": "WagoAppJSON", "vendor": "WAGO", "version": "1.1.0.32", "required": False}
]

# =============================================================================
# DEVICE DESCRIPTORS
# =============================================================================
WAGO_DEVICE_DESCRIPTORS = {
    "750-402": {"device_id": 32776, "descriptor": "8401_0750040200000000", "version": "2.0.0.15", "name": "750-402", "description": "4DI 24 VDC 3ms"},
    "750-430": {"device_id": 32776, "descriptor": "8801_0750043000000000", "version": "2.0.0.14", "name": "750-430", "description": "8DI 24 VDC 3ms"},
    "750-432": {"device_id": 32776, "descriptor": "8401_0750043200000000", "version": "2.0.0.11", "name": "750-432", "description": "4DI 24 VDC 3ms 2-wire"},
    "750-1415": {"device_id": 32776, "descriptor": "8801_0750141500000000", "version": "2.0.0.11", "name": "750-1415", "description": "8DI 24 VDC 3ms 2-wire"},
    "750-1420": {"device_id": 32776, "descriptor": "8401_0750142000000000", "version": "2.0.0.11", "name": "750-1420", "description": "4DI 24 VDC 3ms 3-wire"},
    "750-512": {"device_id": 32776, "descriptor": "8202_0750051200000000", "version": "2.0.0.11", "name": "750-512", "description": "2RO AC 250 V 2A Relay2NO"},
    "750-515": {"device_id": 32776, "descriptor": "8402_0750051500000000", "version": "2.0.0.11", "name": "750-515", "description": "4RO AC 250 V 2A Pot-free Relay4NO"},
    "750-517": {"device_id": 32776, "descriptor": "8202_0750051700000000", "version": "2.0.0.11", "name": "750-517", "description": "2RO AC 250 V 1A Pot-free Relay2CO"},
    "750-531": {"device_id": 32776, "descriptor": "8402_0750053100000000", "version": "2.0.0.11", "name": "750-531", "description": "4DO 24 VDC 0.5A 2-wire"},
    "750-461": {"device_id": 32776, "descriptor": "07500461000000000400", "version": "2.0.0.9", "name": "750-461#04", "description": "2AI Pt100/RTD (4 Bytes)"},
    "750-472": {"device_id": 32776, "descriptor": "07500472000000000400", "version": "2.0.0.9", "name": "750-472#04", "description": "2AI 0-20mA SE 16bits (4 Bytes)"},
    "750-550": {"device_id": 32776, "descriptor": "07500550000000000004", "version": "2.0.0.9", "name": "750-550#04", "description": "2AO 0-10 VDC (4 Bytes)"},
    "750-554": {"device_id": 32776, "descriptor": "07500554000000000004", "version": "2.0.0.9", "name": "750-554#04", "description": "2AO 4-20mA (4 Bytes)"},
    "750-652#08": {"device_id": 32776, "descriptor": "07500652000000000808", "version": "2.0.0.25", "name": "750-652#08", "description": "RS232/485 Interface (8 Bytes)"},
    "750-652#24": {"device_id": 32776, "descriptor": "07500652000000002424", "version": "2.0.0.25", "name": "750-652#24", "description": "RS232/485 Interface (24 Bytes)"},
    "750-652#48": {"device_id": 32776, "descriptor": "07500652000000004848", "version": "2.0.0.25", "name": "750-652#48", "description": "RS232/485 Interface (48 Bytes)"},
}

MODULE_BLACKLIST = ["750-88", "750-89"]
MODULE_GREYLIST = ["750-610", "750-614"]

def is_blacklisted(module_type):
    """Check blacklist"""
    for blacklisted in MODULE_BLACKLIST:
        if module_type.startswith(blacklisted):
            return True
    return False

def is_greylisted(module_type):
    """Check greylist"""
    return module_type in MODULE_GREYLIST

def get_device_descriptor(module_type):
    """Get device descriptor with fallback for 750-652"""
    if module_type in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[module_type]
    base_module = module_type.split('#')[0]
    if base_module in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[base_module]
    if base_module == "750-652":
        return WAGO_DEVICE_DESCRIPTORS.get("750-652#48")
    return None

# =============================================================================
# LOGGING
# =============================================================================
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'

def init_logging(script_name):
    global LOG_FILE
    try:
        log_dir = os.path.join(BASE_PATH, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_filename = "{0}_log_{1}.txt".format(script_name, time.strftime('%Y%m%d_%H%M%S'))
        LOG_FILE = os.path.join(log_dir, log_filename)
        with open(LOG_FILE, 'w') as f:
            f.write("=== CODESYS Project Generator Log ===\n")
    except Exception as e:
        print("[ERROR] Failed to initialize logging: {0}".format(str(e)))
        LOG_FILE = None
        return None
    log("="*70)
    log("CODESYS Project Generator API - Enhanced with XML Import")
    log("Script: {0}".format(script_name))
    log("Start: {0}".format(time.strftime('%Y-%m-%d %H:%M:%S')))
    log("="*70)
    log("")
    return LOG_FILE

def log(message, level="INFO"):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = "[{0}] [{1}] {2}".format(timestamp, level, message)
    color = Colors.RESET
    if level == "ERROR":
        color = Colors.RED + Colors.BOLD
    elif level == "SUCCESS":
        color = Colors.GREEN + Colors.BOLD
    elif level == "WARNING":
        color = Colors.YELLOW
    elif level == "INFO":
        color = Colors.CYAN
    elif level == "DEBUG":
        color = Colors.MAGENTA
    print("{0}{1}{2}".format(color, log_entry, Colors.RESET))
    if LOG_FILE:
        try:
            import codecs
            with codecs.open(LOG_FILE, 'a', 'utf-8') as f:
                f.write(log_entry + '\n')
        except:
            pass

def log_step(description, total_steps=None):
    global CURRENT_STEP
    CURRENT_STEP += 1
    log("")
    log("="*70)
    if total_steps:
        log("STEP {0}/{1}: {2}".format(CURRENT_STEP, total_steps, description))
    else:
        log("STEP {0}: {1}".format(CURRENT_STEP, description))
    log("="*70)

def format_duration(seconds):
    if seconds < 60:
        return "{0:.1f} seconds".format(seconds)
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = seconds % 60
        return "{0} min {1:.0f} sec".format(minutes, secs)
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return "{0} h {1} min".format(hours, minutes)

# =============================================================================
# XML IMPORT - New functionality
# =============================================================================
def detect_xml_format(filepath):
    """Detect XML format"""
    try:
        with open(filepath, 'r') as f:
            content = f.read(500)
        if content.strip().startswith('<ExportFile'):
            return 'export'
        elif 'plcopen.org/xml/tc6' in content:
            return 'plcopenxml'
        elif '<project' in content and '<fileHeader>' in content:
            return 'projectxml'
        return 'unknown'
    except:
        return 'unknown'

def get_conflict_resolve_mode(mode_str):
    """Convert string to ConflictResolve: replace=0, copy=1, skip=2"""
    mode_lower = mode_str.lower() if mode_str else 'replace'
    return 0 if mode_lower == 'replace' else (1 if mode_lower == 'copy' else 2)

def import_xml_files(proj, xml_imports, default_conflict_mode='replace'):
    """Import XML files to Application"""
    if not xml_imports:
        log("No XML imports configured")
        return True
    
    log("Importing XML files...")
    
    try:
        results = proj.find("Application", True)
        if not results or len(results) == 0:
            log("  [ERROR] Application not found", "ERROR")
            return False
        app = results[0]
    except Exception as e:
        log("  [ERROR] Application: {0}".format(str(e)), "ERROR")
        return False
    
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    for idx, xml_item in enumerate(xml_imports, 1):
        filepath = xml_item.get('path', '')
        description = xml_item.get('description', '')
        conflict_mode_str = xml_item.get('conflict_resolve', default_conflict_mode)
        optional = xml_item.get('optional', False)
        
        filename = os.path.basename(filepath)
        log("")
        log("  [{0}/{1}] {2}".format(idx, len(xml_imports), filename))
        if description:
            log("    {0}".format(description))
        
        if not os.path.exists(filepath):
            if optional:
                log("    Not found (optional) - SKIP", "WARNING")
                skipped_count += 1
                continue
            else:
                log("    Not found (required) - ERROR", "ERROR")
                error_count += 1
                continue
        
        file_format = detect_xml_format(filepath)
        log("    Format: {0}".format(file_format.upper()))
        
        if file_format == 'export':
            log("    .export NOT SUPPORTED (ISVNode required)", "ERROR")
            error_count += 1
            continue
        
        if file_format == 'unknown':
            log("    Unknown format", "ERROR")
            error_count += 1
            continue
        
        try:
            conflict_mode = get_conflict_resolve_mode(conflict_mode_str)
            log("    ConflictResolve: {0} ({1})".format(conflict_mode_str, conflict_mode))
            app.import_xml(conflict_mode, filepath, True)
            log("    SUCCESS", "SUCCESS")
            success_count += 1
        except Exception as e:
            log("    ERROR: {0}".format(str(e)), "ERROR")
            error_count += 1
    
    log("")
    log("XML Import Summary:")
    log("  Successful: {0}".format(success_count))
    log("  Errors: {0}".format(error_count))
    log("  Skipped: {0}".format(skipped_count))
    
    return error_count == 0

# =============================================================================
# LIBRARY MANAGEMENT - Using working approach from enhanced version
# =============================================================================
def extract_namespace_from_library(lib):
    """Extract namespace from library object"""
    try:
        if hasattr(lib, 'name'):
            namespace = str(lib.name)
            if namespace and namespace != "":
                return namespace
        if hasattr(lib, 'namespace'):
            namespace = str(lib.namespace)
            if namespace and namespace != "":
                return namespace
        if hasattr(lib, 'default_namespace'):
            namespace = str(lib.default_namespace)
            if namespace and namespace != "":
                return namespace
        namespace = str(lib.title)
        log("      [FALLBACK] Using title as namespace: {0}".format(namespace), "WARNING")
        return namespace
    except Exception as e:
        log("      [ERROR] Namespace extraction failed: {0}".format(str(e)), "ERROR")
        return str(lib.title)

def find_library_in_repositories(lib_name, lib_vendor, lib_version=None):
    """Search for library in all repositories"""
    try:
        for repo in librarymanager.repositories:
            libs = librarymanager.get_all_libraries(repo)
            for lib in libs:
                if lib.title == lib_name and lib.company == lib_vendor:
                    if lib_version:
                        if str(lib.version) == str(lib_version):
                            namespace = extract_namespace_from_library(lib)
                            log("    [FOUND] {0}, {1} ({2})".format(lib.title, lib.version, lib.company), "SUCCESS")
                            log("    [NAMESPACE] {0}".format(namespace), "SUCCESS")
                            return lib, namespace
                    else:
                        namespace = extract_namespace_from_library(lib)
                        log("    [FOUND] {0}, {1} ({2})".format(lib.title, lib.version, lib.company), "SUCCESS")
                        log("    [NAMESPACE] {0}".format(namespace), "SUCCESS")
                        return lib, namespace
        log("    [NOT FOUND] Library not found", "WARNING")
        return None, None
    except Exception as e:
        log("    [ERROR] Search error: {0}".format(str(e)), "ERROR")
        return None, None

def get_library_manager_object(app):
    """Find Library Manager in application"""
    try:
        objects = app.get_children(recursive=True)
        for obj in objects:
            if hasattr(obj, 'is_libman') and obj.is_libman:
                log("  [OK] Library Manager gefunden", "SUCCESS")
                return obj
        log("  [WARNING] Library Manager nicht gefunden", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

def add_library_to_application(libman, proj, lib_title, lib_vendor, lib_version=None):
    """Add library to application"""
    target_lib, namespace = find_library_in_repositories(lib_title, lib_vendor, lib_version)
    
    if not target_lib:
        log("  [ERROR] Library nicht gefunden", "ERROR")
        return False
    
    log("  [FOUND] Library: {0}".format(target_lib.title))
    log("  [NAMESPACE] {0}".format(namespace))
    
    try:
        libman.add_library(target_lib)
        log("  [SUCCESS]", "SUCCESS")
        return True
    except Exception as e:
        log("  [FAILED] {0}".format(str(e)), "ERROR")
        return False

def install_libraries_enhanced(proj, app, required_libs):
    """Install libraries with automatic namespace extraction"""
    log("Library Installation...")
    
    try:
        libman = get_library_manager_object(app)
        if not libman:
            log("  [ERROR] Library Manager not available", "ERROR")
            return {"added": 0, "skipped": 0, "failed": 0}
        
        stats = {"added": 0, "skipped": 0, "failed": 0}
        
        for lib_config in required_libs:
            lib_name = lib_config.get("name", "Unknown")
            lib_vendor = lib_config.get("vendor", "3S")
            lib_version = lib_config.get("version")
            lib_required = lib_config.get("required", False)
            
            log("")
            log("  Library: {0}".format(lib_name))
            log("  " + "-"*66)
            
            success = add_library_to_application(libman, proj, lib_name, lib_vendor, lib_version)
            
            if success:
                stats["added"] += 1
            else:
                stats["failed"] += 1
                if lib_required:
                    log("    [CRITICAL] Required library failed!", "ERROR")
        
        log("")
        log("  " + "="*66)
        log("  Installation completed:")
        log("    Added:     {0}".format(stats["added"]), "SUCCESS")
        log("    Skipped:   {0}".format(stats["skipped"]), "INFO")
        log("    Failed:    {0}".format(stats["failed"]), "ERROR" if stats["failed"] > 0 else "INFO")
        log("  " + "="*66)
        
        return stats
        
    except Exception as e:
        log("  [ERROR] Installation failed: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return {"added": 0, "skipped": 0, "failed": 0}

# =============================================================================
# JSON CONFIGURATION
# =============================================================================
def load_config_from_json(json_path):
    """Load configuration from JSON with auto-detect XML support"""
    log("Loading JSON configuration: {0}".format(os.path.basename(json_path)))
    
    try:
        import codecs
        with codecs.open(json_path, 'r', 'utf-8') as f:
            config = json.load(f)
        
        libraries = []
        fb_instances = []
        xml_imports = []
        settings = {}
        
        # Load libraries
        if 'libraries' in config:
            lib_section = config['libraries']
            if isinstance(lib_section, dict) and 'items' in lib_section:
                libraries = lib_section['items']
            elif isinstance(lib_section, list):
                libraries = lib_section
        
        # Load function blocks
        if 'function_blocks' in config:
            fb_section = config['function_blocks']
            if isinstance(fb_section, dict) and 'items' in fb_section:
                fb_instances = fb_section['items']
            elif isinstance(fb_section, list):
                fb_instances = fb_section
        
        # Load XML imports with auto-detection support
        if 'xml_imports' in config:
            xml_section = config['xml_imports']
            
            # Check for auto-detect configuration
            if isinstance(xml_section, dict) and 'auto_detect' in xml_section:
                auto_config = xml_section['auto_detect']
                if auto_config.get('enabled', False):
                    log("  Auto-detecting XML files...")
                    xml_imports = auto_detect_xml_files(auto_config)
                
                # Add manual files if specified
                if 'manual_files' in xml_section and xml_section['manual_files']:
                    xml_imports.extend(xml_section['manual_files'])
            
            # Legacy format: direct list
            elif isinstance(xml_section, list):
                xml_imports = xml_section
        
        # Load import settings
        if 'import_settings' in config:
            settings = config['import_settings']
        
        log("  [OK] Configuration loaded", "SUCCESS")
        log("    Libraries: {0}".format(len(libraries)))
        log("    Function Blocks: {0}".format(len(fb_instances)))
        log("    XML Imports: {0}".format(len(xml_imports)))
        
        return libraries, fb_instances, xml_imports, settings
        
    except Exception as e:
        log("  [ERROR] JSON error: {0}".format(str(e)), "ERROR")
        return [], [], [], {}

def auto_detect_xml_files(auto_config):
    """Auto-detect XML files in specified directory"""
    xml_imports = []
    
    try:
        directory = auto_config.get('directory', 'exports')
        pattern = auto_config.get('pattern', '*.xml')
        recursive = auto_config.get('recursive', False)
        exclude_patterns = auto_config.get('exclude_patterns', [])
        default_conflict = auto_config.get('default_conflict_resolve', 'replace')
        treat_as_optional = auto_config.get('treat_all_as_optional', False)
        
        # Build full path
        if not os.path.isabs(directory):
            directory = os.path.join(BASE_PATH, directory)
        
        log("    Directory: {0}".format(directory))
        log("    Pattern: {0}".format(pattern))
        
        if not os.path.exists(directory):
            log("    [WARNING] Directory not found: {0}".format(directory), "WARNING")
            return []
        
        # Find all XML files
        search_pattern = os.path.join(directory, pattern)
        if recursive:
            search_pattern = os.path.join(directory, '**', pattern)
            xml_files = glob.glob(search_pattern, recursive=True)
        else:
            xml_files = glob.glob(search_pattern)
        
        log("    Found {0} XML files".format(len(xml_files)))
        
        # Filter out excluded patterns
        for xml_file in xml_files:
            filename = os.path.basename(xml_file)
            
            # Check exclude patterns
            excluded = False
            for exclude_pattern in exclude_patterns:
                if re.match(exclude_pattern.replace('*', '.*'), filename):
                    log("      Excluded: {0}".format(filename), "INFO")
                    excluded = True
                    break
            
            if not excluded:
                xml_imports.append({
                    'path': xml_file,
                    'description': 'Auto-detected: {0}'.format(filename),
                    'conflict_resolve': default_conflict,
                    'optional': treat_as_optional
                })
                log("      Added: {0}".format(filename), "SUCCESS")
        
        return xml_imports
        
    except Exception as e:
        log("    [ERROR] Auto-detection failed: {0}".format(str(e)), "ERROR")
        return []

# =============================================================================
# FILE HANDLING
# =============================================================================
def find_all_files(search_path, pattern):
    """Find files matching pattern"""
    if not os.path.exists(search_path):
        return []
    full_pattern = os.path.join(search_path, pattern)
    try:
        matches = glob.glob(full_pattern)
        return sorted(matches)
    except:
        return []

def match_files(var_files, config_files):
    """Match variable and config file pairs"""
    matched_pairs = []
    for var_file in var_files:
        var_basename = os.path.basename(var_file)
        match = re.match(r'(IO\d+)_variables\.txt', var_basename)
        if not match:
            continue
        plc_id = match.group(1)
        config_pattern = "PLC_{0}_config.json".format(plc_id)
        for config_file in config_files:
            if config_pattern in os.path.basename(config_file):
                matched_pairs.append((var_file, config_file, plc_id))
                log("  [OK] Paar: {0}".format(plc_id))
                break
    return matched_pairs

def parse_variables_file(filepath):
    """Parse variables file"""
    log("Parse Variablen-Datei: {0}".format(os.path.basename(filepath)))
    try:
        import codecs
        with codecs.open(filepath, 'r', 'utf-8') as f:
            content = f.read()
        log("  [OK] {0} Zeichen gelesen".format(len(content)))
        return content
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

def parse_config_json(filepath):
    """Parse JSON configuration"""
    log("Parse JSON-Config: {0}".format(os.path.basename(filepath)))
    try:
        import codecs
        with codecs.open(filepath, 'r', 'utf-8') as f:
            config = json.load(f)
        if 'PLC_Info' not in config:
            log("  [ERROR] 'PLC_Info' fehlt", "ERROR")
            return None
        plc_info = config['PLC_Info']
        log("  [OK] PLC: {0}".format(plc_info.get('Name', 'N/A')))
        log("  [OK] Typ: {0}".format(plc_info.get('Type', 'N/A')))
        log("  [OK] IP: {0}".format(plc_info.get('IP_Address', 'N/A')))
        return config
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

# =============================================================================
# PROJECT CREATION
# =============================================================================
def create_project_from_template(plc_name, project_path, template_path):
    """Create project from template using shutil.copy2 + projects.open"""
    log("Erstelle Projekt aus Template...")
    try:
        import shutil
        full_path = os.path.join(project_path, "{0}.project".format(plc_name))
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        if os.path.exists(full_path):
            os.remove(full_path)
            log("  [OK] Altes Projekt geloescht")
        shutil.copy2(template_path, full_path)
        log("  [OK] Template kopiert: {0}".format(full_path))
        proj = projects.open(full_path, None, True)
        log("  [OK] Projekt geoeffnet!")
        return proj, full_path
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return None, None

def find_or_create_application(proj):
    """Find Application object"""
    log("Suche Application...")
    try:
        applications = proj.find("Application", True)
        if applications and len(applications) > 0:
            app = applications[0]
            log("  [OK] Application gefunden: {0}".format(app.get_name(False)))
            return app
        all_objs = proj.get_children(True)
        log("  Durchsuche {0} Objekte...".format(len(all_objs)))
        for obj in all_objs:
            obj_name = obj.get_name(False)
            obj_type = str(type(obj))
            if "Application" in obj_name or "Application" in obj_type:
                log("  [OK] Application gefunden: {0}".format(obj_name))
                return obj
        try:
            app = proj.active_application
            if app:
                log("  [OK] Active Application gefunden!")
                return app
        except:
            pass
        log("  [ERROR] Keine Application!", "ERROR")
        return None
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

# =============================================================================
# DEVICE CONFIGURATION - Using working approach
# =============================================================================
def find_plc_device(proj):
    """Find PLC device"""
    log("Suche PLC Device...")
    try:
        devices = proj.find('Device', True)
        for device in devices:
            device_name = device.get_name(False)
            if '750' in device_name or 'PFC' in device_name:
                log("  [OK] Device gefunden: {0}".format(device_name))
                return device
        if devices and len(devices) > 0:
            device = devices[0]
            log("  [OK] Erstes Device: {0}".format(device.get_name(False)))
            return device
        log("  [WARNING] Kein PLC Device", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

def find_kbus(device):
    """Find Kbus"""
    log("Suche Kbus...")
    try:
        if not device:
            log("  [ERROR] Kein Device", "ERROR")
            return None
        kbus_results = device.find('Kbus', True)
        if kbus_results and len(kbus_results) > 0:
            kbus = kbus_results[0]
            log("  [OK] Kbus gefunden: {0}".format(kbus.get_name(False)))
            return kbus
        children = device.get_children(False)
        log("  Device hat {0} Kinder".format(len(children)))
        for child in children:
            child_name = child.get_name(False)
            if "Kbus" in child_name or "KBus" in child_name:
                log("  [OK] Kbus gefunden: {0}".format(child_name))
                return child
        log("  [WARNING] Kbus nicht gefunden", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return None

def get_first_gateway():
    """Get first gateway"""
    try:
        gateways = online.gateways
        for gw in gateways:
            try:
                gw_name = gw.name
                log("  Gefundenes Gateway: {0}".format(gw_name))
                return gw
            except:
                continue
        log("  [WARNING] Kein Gateway", "WARNING")
        return None
    except Exception as e:
        log("  [WARNING] Gateway-Zugriff fehlgeschlagen: {0}".format(str(e)), "WARNING")
        return None

def configure_device_ip(proj, device, ip_address):
    """Configure IP address using gateway object"""
    log("Konfiguriere Device IP-Adresse...")
    try:
        parts = ip_address.split('.')
        normalized_ip = '.'.join([str(int(p)) for p in parts])
        log("  IP-Adresse (normalisiert): {0}".format(normalized_ip))
        try:
            gateway = get_first_gateway()
            if gateway:
                log("  Gateway gefunden: {0}".format(gateway.name))
                log("  Versuche IP-Konfiguration...")
                device.set_gateway_and_ip_address(gateway, normalized_ip)
                log("  [SUCCESS] IP-Adresse gesetzt: {0}".format(normalized_ip), "SUCCESS")
                return True
        except AttributeError as e:
            log("  [WARNING] Methode nicht verfuegbar: {0}".format(str(e)), "WARNING")
        except Exception as e:
            log("  [WARNING] Gateway-Methode fehlgeschlagen: {0}".format(str(e)), "WARNING")
        log("  [ERROR] IP-Adresse konnte nicht gesetzt werden", "ERROR")
        log("  [INFO] Bitte manuell konfigurieren", "WARNING")
        return False
    except Exception as e:
        log("  [ERROR] IP-Konfiguration fehlgeschlagen: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

def add_io_modules_to_kbus(kbus, config):
    """Add IO modules using kbus.add() method"""
    log("Konfiguriere Kbus Module...")
    try:
        if not config or "IO_Modules" not in config:
            log("  [WARNING] Keine IO-Module", "WARNING")
            return False
        io_modules = config["IO_Modules"]
        if not io_modules or len(io_modules) == 0:
            log("  [INFO] Keine Module", "INFO")
            return True
        log("  {0} Module gefunden".format(len(io_modules)))
        if not kbus:
            log("  [WARNING] Kbus nicht gefunden", "WARNING")
            return False
        success_count = 0
        fail_count = 0
        skipped_blacklist = 0
        skipped_greylist = 0
        skipped_unknown = 0
        for idx, module in enumerate(io_modules, 1):
            module_type = module.get("Module_Type", "UNKNOWN")
            signal_count = len(module.get("Signals", []))
            log("")
            log("  Modul {0}/{1}: {2} ({3} Signale)".format(idx, len(io_modules), module_type, signal_count))
            log("  " + "-"*66)
            if is_blacklisted(module_type):
                log("    [SKIP] PLC Device (Blacklist): {0}".format(module_type), "WARNING")
                skipped_blacklist += 1
                continue
            if is_greylisted(module_type):
                log("    [SKIP] Kein Process Data (Greylist): {0}".format(module_type), "INFO")
                skipped_greylist += 1
                continue
            descriptor_info = get_device_descriptor(module_type)
            if not descriptor_info:
                log("    [ERROR] Kein Device Descriptor!", "ERROR")
                skipped_unknown += 1
                fail_count += 1
                continue
            try:
                device_name = descriptor_info['name']
                device_id = descriptor_info['device_id']
                descriptor = descriptor_info['descriptor']
                version = descriptor_info['version']
                log("    [INFO] Device: {0}".format(device_name))
                log("    [INFO] Descriptor: {0}".format(descriptor))
                log("    [INFO] Version: {0}".format(version))
                try:
                    parent_device = projects.primary.find('Device', True)[0]
                    if parent_device:
                        kbus = parent_device.find('Kbus', True)[0]
                except:
                    pass
                if kbus:
                    kbus.add(device_name, device_id, descriptor, version)
                    log("    [SUCCESS] Modul hinzugefuegt!", "SUCCESS")
                    success_count += 1
                else:
                    log("    [ERROR] Kbus Objekt ist None", "ERROR")
                    fail_count += 1
            except Exception as e:
                log("    [ERROR] Hinzufuegen fehlgeschlagen: {0}".format(str(e)), "ERROR")
                fail_count += 1
        log("")
        log("  " + "="*66)
        log("  Kbus Konfiguration abgeschlossen:")
        log("    Erfolgreich:  {0}".format(success_count), "SUCCESS")
        if fail_count > 0:
            log("    Fehler:       {0}".format(fail_count), "ERROR")
        if skipped_blacklist > 0:
            log("    Skip (Black): {0}".format(skipped_blacklist), "INFO")
        if skipped_greylist > 0:
            log("    Skip (Grey):  {0}".format(skipped_greylist), "INFO")
        if skipped_unknown > 0:
            log("    Skip (Unkn):  {0}".format(skipped_unknown), "WARNING")
        log("  " + "="*66)
        return True
    except Exception as e:
        log("  [ERROR] Kbus-Konfiguration fehlgeschlagen: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# POU CREATION
# =============================================================================
def find_or_update_plc_prg(app):
    """Find or update PLC_PRG"""
    log("Suche PLC_PRG...")
    try:
        results = app.find("PLC_PRG", True)
        if results and len(results) > 0:
            pou = results[0]
            log("  [OK] PLC_PRG gefunden")
            try:
                decl = pou.textual_declaration
                impl = pou.textual_implementation
                if decl and impl:
                    log("  [OK] PLC_PRG aktualisiert")
            except:
                pass
            return pou
        try:
            from System import Enum
            from ScriptEngine.HostAccess import ScriptTypes
            pou_type = ScriptTypes.PouType.Program
        except:
            pou_type = "Program"
        pou = app.create_pou("PLC_PRG", pou_type, None)
        log("  [OK] PLC_PRG erstellt")
        return pou
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

def create_fb_instance_code(fb_config):
    """Create IEC code for FB - separate declaration and implementation"""
    fb_type = fb_config.get("fb_type", "UNKNOWN")
    instance = fb_config.get("instance", "oInstance")
    params = fb_config.get("params", {})
    
    var_declaration = "{0} : {1};".format(instance, fb_type)
    
    param_list = []
    for param_name, param_value in params.items():
        if param_value and param_value.strip():
            if param_name.endswith("=>"):
                param_name_clean = param_name[:-2].strip()
                if param_value:
                    param_list.append("{0}=>{1}".format(param_name_clean, param_value))
            else:
                param_list.append("{0}:={1}".format(param_name, param_value))
    
    if param_list:
        fb_call = "{0}({1});".format(instance, ", ".join(param_list))
    else:
        fb_call = "{0}();".format(instance)
    
    return var_declaration, fb_call

def add_fb_instances_to_plc_prg(app, fb_instances=None):
    """Add Function Block instances to PLC_PRG"""
    log("Fuege Function Block Instanzen hinzu...")
    
    if not fb_instances:
        log("  [OK] Keine FB-Instanzen")
        return True
    
    try:
        plc_prg_results = app.find("PLC_PRG", True)
        if not plc_prg_results or len(plc_prg_results) == 0:
            log("  [ERROR] PLC_PRG nicht gefunden", "ERROR")
            return False
        pou = plc_prg_results[0]
        log("  [OK] PLC_PRG gefunden")
        
        var_block = []
        impl_block = []
        
        for idx, fb_config in enumerate(fb_instances, 1):
            fb_type = fb_config.get("fb_type", "")
            instance_name = fb_config.get("instance", "")
            
            if not fb_type or not instance_name:
                log("    [WARNING] FB #{0}: Fehlende Daten".format(idx), "WARNING")
                continue
            
            var_decl, fb_call = create_fb_instance_code(fb_config)
            var_block.append(var_decl)
            impl_block.append(fb_call)
            
            log("    [OK] FB #{0}: {1} : {2}".format(idx, instance_name, fb_type))
        
        if var_block:
            try:
                current_decl = pou.textual_declaration.text
                new_decl = current_decl + "\n\n(* FB Instances *)\n" + "\n".join(var_block)
                pou.textual_declaration.replace(new_decl)
                log("  [OK] VAR-Deklarationen hinzugefuegt", "SUCCESS")
            except Exception as e:
                log("  [ERROR] VAR-Update fehlgeschlagen: {0}".format(str(e)), "ERROR")
        
        if impl_block:
            try:
                current_impl = pou.textual_implementation.text
                new_impl = current_impl + "\n\n(* FB Calls *)\n" + "\n".join(impl_block)
                pou.textual_implementation.replace(new_impl)
                log("  [OK] Implementation hinzugefuegt", "SUCCESS")
            except Exception as e:
                log("  [ERROR] Implementation-Update fehlgeschlagen: {0}".format(str(e)), "ERROR")
        
        return True
    except Exception as e:
        log("  [ERROR] FB-Instanziierung fehlgeschlagen: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

def create_gvl_with_variables(app, gvl_name, var_block):
    """Create GVL"""
    log("Erstelle GVL '{0}'...".format(gvl_name))
    try:
        gvl = app.create_gvl(gvl_name)
        log("  [OK] GVL erstellt")
        if var_block:
            try:
                gvl.textual_declaration.replace(var_block)
                log("  [OK] Variablen eingefuegt - {0} Zeichen".format(len(var_block)))
                return gvl
            except:
                log("  [WARNING] Variablen konnten nicht eingefuegt werden", "WARNING")
                return gvl
        return gvl
    except Exception as e:
        log("  [ERROR] {0}".format(str(e)), "ERROR")
        return None

# =============================================================================
# MAIN PROCESS - 13 Steps
# =============================================================================
def create_single_project(var_file, config_file, plc_name):
    """Create single project"""
    global CURRENT_STEP, REQUIRED_LIBRARIES, FB_INSTANCES, XML_IMPORTS
    
    try:
        log_step("Load JSON Configuration", TOTAL_STEPS_PER_PROJECT)
        if os.path.exists(CONFIG_JSON_PATH):
            libs, fbs, xmls, settings = load_config_from_json(CONFIG_JSON_PATH)
            if libs:
                REQUIRED_LIBRARIES = libs
            if fbs:
                FB_INSTANCES = fbs
            if xmls:
                XML_IMPORTS = xmls
        else:
            log("  [INFO] No JSON file, using example libraries", "INFO")
            REQUIRED_LIBRARIES = EXAMPLE_LIBRARIES
        
        log_step("Parse Input Files", TOTAL_STEPS_PER_PROJECT)
        var_block = parse_variables_file(var_file)
        config = parse_config_json(config_file)
        if not var_block or not config:
            return False
        
        log_step("Create CODESYS Project", TOTAL_STEPS_PER_PROJECT)
        if USE_TEMPLATE and os.path.exists(TEMPLATE_PROJECT):
            log("Using template method")
            proj, full_path = create_project_from_template(plc_name, DEFAULT_PROJECT_PATH, TEMPLATE_PROJECT)
        else:
            log("  [ERROR] Template not found!", "ERROR")
            return False
        if not proj:
            return False
        
        log_step("Find Application", TOTAL_STEPS_PER_PROJECT)
        app = find_or_create_application(proj)
        if not app:
            log("  [ERROR] No Application!", "ERROR")
            proj.close()
            return False
        
        log_step("Install Libraries", TOTAL_STEPS_PER_PROJECT)
        install_libraries_enhanced(proj, app, REQUIRED_LIBRARIES)
        
        log_step("Import XML Files", TOTAL_STEPS_PER_PROJECT)
        if XML_IMPORTS:
            default_conflict = settings.get('default_conflict_resolve', 'replace') if 'settings' in locals() else 'replace'
            import_xml_files(proj, XML_IMPORTS, default_conflict)
        else:
            log("No XML files configured")
        
        log_step("Find PLC Device", TOTAL_STEPS_PER_PROJECT)
        device = find_plc_device(proj)
        
        if device and 'PLC_Info' in config:
            plc_info = config['PLC_Info']
            if 'IP_Address' in plc_info:
                log_step("Configure IP Address", TOTAL_STEPS_PER_PROJECT)
                configure_device_ip(proj, device, plc_info['IP_Address'])
        else:
            log_step("Skip IP Configuration", TOTAL_STEPS_PER_PROJECT)
        
        log_step("Configure Kbus with IO Modules", TOTAL_STEPS_PER_PROJECT)
        if device:
            kbus = find_kbus(device)
            if kbus:
                add_io_modules_to_kbus(kbus, config)
            else:
                log("  [WARNING] Kbus not found", "WARNING")
        else:
            log("  [WARNING] Device not found", "WARNING")
        
        log_step("Find/Update PLC_PRG", TOTAL_STEPS_PER_PROJECT)
        pou = find_or_update_plc_prg(app)
        
        log_step("Instantiate Function Blocks", TOTAL_STEPS_PER_PROJECT)
        add_fb_instances_to_plc_prg(app, FB_INSTANCES)
        
        log_step("Create GVL with Variables", TOTAL_STEPS_PER_PROJECT)
        gvl_name = "GVL_{0}".format(plc_name)
        gvl = create_gvl_with_variables(app, gvl_name, var_block)
        
        log_step("Save Project", TOTAL_STEPS_PER_PROJECT)
        proj.save()
        log("  [OK] Project saved")
        proj.close()
        log("  [OK] Project closed")
        log("")
        log("-"*70)
        log("PROJECT SUCCESSFUL: {0}".format(plc_name), "SUCCESS")
        log("  Path: {0}".format(full_path))
        log("-"*70)
        return True
    except Exception as e:
        log("ERROR: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# MAIN
# =============================================================================
def main():
    """Main function"""
    global CURRENT_STEP
    start_time = time.time()
    log_file = init_logging("codesys_project_generator_local")
    
    success_count = 0
    failure_count = 0
    
    try:
        log_step("Collect Files")
        if AUTO_DETECT_MODE:
            log("Auto-Detect mode active")
            var_files = find_all_files(DEFAULT_VARIABLES_PATH, "IO*_variables.txt")
            config_files = find_all_files(DEFAULT_CONFIG_PATH, "PLC_IO*_config.json")
            matched_pairs = match_files(var_files, config_files)
        else:
            log("Specific mode")
            matched_pairs = [(SPECIFIC_VARIABLES_FILE, SPECIFIC_CONFIG_FILE, "IO020")]
        
        if not matched_pairs:
            log("ERROR: No files found!", "ERROR")
            sys.exit(1)
        
        log("")
        log("="*70)
        log("START CREATION: {0} projects".format(len(matched_pairs)))
        log("="*70)
        
        for idx, (var_file, config_file, plc_id) in enumerate(matched_pairs, 1):
            log("")
            log("="*70)
            log("PROJECT {0}/{1}: {2}".format(idx, len(matched_pairs), plc_id))
            log("="*70)
            CURRENT_STEP = 0
            if create_single_project(var_file, config_file, plc_id):
                success_count += 1
            else:
                failure_count += 1
        
        elapsed = time.time() - start_time
        log("")
        log("="*70)
        log("FINISHED!", "SUCCESS")
        log("="*70)
        log("Total: {0}".format(len(matched_pairs)))
        log("Successful: {0}".format(success_count))
        log("Failed: {0}".format(failure_count))
        log("Duration: {0}".format(format_duration(elapsed)))
        if log_file:
            log("Log: {0}".format(log_file))
        log("="*70)
    except Exception as e:
        log("CRITICAL ERROR: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()