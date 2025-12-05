# -*- coding: utf-8 -*-
# encoding: utf-8
"""
CODESYS Projekt-Generator  - Enhanced Edition with Library Repository API
Features:
- Uses CODESYS librarymanager.repositories API
- Loads configuration aus library_fb_config.json
- Instancing  Function Blocks aus Bibliotheken
- FB-Call
- Library version recognintion  
"""

import sys
import time
import os
import json
import re
import glob

# =============================================================================
# KONFIGURATION / Configuration
# =============================================================================

PROJECT_ROOT = r"<YOUR_PROJECT_ROOT>"

# Project Paths
DEFAULT_PROJECT_PATH = os.path.join(PROJECT_ROOT, "projects")
DEFAULT_VARIABLES_PATH = os.path.join(PROJECT_ROOT, "outputs")
DEFAULT_CONFIG_PATH = os.path.join(PROJECT_ROOT, "outputs")
CONFIG_JSON_PATH = os.path.join(PROJECT_ROOT, "library_fb_config.json")

# Template Configuration
USE_TEMPLATE = True
TEMPLATE_PROJECT = os.path.join(PROJECT_ROOT, "TEMPLATE_WAGO_750-8210.project")

# Auto-Detection Mode
AUTO_DETECT_MODE = True
SPECIFIC_VARIABLES_FILE = os.path.join(PROJECT_ROOT, "outputs", "IO020_variables.txt")
SPECIFIC_CONFIG_FILE = os.path.join(PROJECT_ROOT, "outputs", "PLC_IO020_config.json")
# =============================================================================
# Example Paths in Windows  
# =============================================================================
#DEFAULT_PROJECT_PATH = r"D:\WAGO\CODESYS\scripting\besecke\projects"
#DEFAULT_VARIABLES_PATH = r"D:\WAGO\CODESYS\scripting\besecke\outputs"
#DEFAULT_CONFIG_PATH = r"D:\WAGO\CODESYS\scripting\besecke\outputs"
#CONFIG_JSON_PATH = r"D:\WAGO\CODESYS\scripting\besecke\library_fb_config.json"

#USE_TEMPLATE = True
#TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\scripting\besecke\TEMPLATE_WAGO_750-8210.project"

#AUTO_DETECT_MODE = True

#SPECIFIC_VARIABLES_FILE = r"D:\WAGO\CODESYS\scripting\besecke\outputs\IO020_variables.txt"
#SPECIFIC_CONFIG_FILE = r"D:\WAGO\CODESYS\scripting\besecke\outputs\PLC_IO020_config.json"

TOTAL_STEPS_PER_PROJECT = 12
CURRENT_STEP = 0
LOG_FILE = None

# Wird aus JSON geladen / Will be loaded from JSON
REQUIRED_LIBRARIES = []
FB_INSTANCES = []

# =============================================================================
# BEISPIEL-BIBLIOTHEKEN / Example Libraries
# Diese werden überschrieben wenn JSON vorhanden / Will be overwritten if JSON exists
# =============================================================================
EXAMPLE_LIBRARIES = [
    {
        "name": "MQTT_Client_SL",
        "vendor": "CODESYS",
        "version": "1.10.0.0",
        "required": False
    },
    {
        "name": "WagoAppCloud",
        "vendor": "WAGO",
        "version": "1.3.5.7",
        "required": False
    },
    {
        "name": "JSON_Utilities_SL",
        "vendor": "CODESYS",
        "version": "1.9.0.0",
        "required": False
    },
    {
        "name": "WagoAppJSON",
        "vendor": "WAGO",
        "version": "1.1.0.32",
        "required": False
    }
]

# =============================================================================
# DEVICE DESCRIPTOR MAPPING
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

# =============================================================================
# LOGGING
# =============================================================================
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'

def init_logging(script_name):
    global LOG_FILE
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        script_dir = os.getcwd()
    log_filename = "{0}_log_{1}.txt".format(script_name, time.strftime('%Y%m%d_%H%M%S'))
    LOG_FILE = os.path.join(script_dir, log_filename)
    log("="*70)
    log("CODESYS Projekt-Generator API")
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
    colored_entry = "{0}[{1}] [{2}]{3} {4}".format(color, timestamp, level, Colors.RESET, message)
    print(colored_entry)
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
    log("="*70, "INFO")
    if total_steps:
        log("SCHRITT {0}/{1}: {2}".format(CURRENT_STEP, total_steps, description), "INFO")
    else:
        log("SCHRITT {0}: {1}".format(CURRENT_STEP, description), "INFO")
    log("="*70, "INFO")

def format_duration(seconds):
    if seconds < 60:
        return "{0:.1f} Sekunden".format(seconds)
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = seconds % 60
        return "{0} Min {1:.0f} Sek".format(minutes, secs)
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return "{0} Std {1} Min".format(hours, minutes)

# =============================================================================
# JSON-KONFIGURATION LADEN / Load JSON Configuration
# =============================================================================
def load_config_from_json(json_path):
    """
    Lädt die Konfiguration aus library_fb_config.json
    Loads configuration from library_fb_config.json
    """
    log("Lade JSON-Konfiguration / Loading JSON config: {0}".format(json_path))
    
    try:
        import codecs
        with codecs.open(json_path, 'r', 'utf-8') as f:
            config = json.load(f)
        
        libraries = []
        if 'libraries' in config and 'items' in config['libraries']:
            for lib in config['libraries']['items']:
                libraries.append({
                    'name': lib.get('name'),
                    'vendor': lib.get('vendor', '3S'),
                    'version': lib.get('version'),
                    'url': lib.get('url'),
                    'required': lib.get('required', False)
                })
        
        fb_instances = []
        if 'function_blocks' in config and 'items' in config['function_blocks']:
            for fb in config['function_blocks']['items']:
                fb_instances.append({
                    'library': fb.get('library'),
                    'fb_type': fb.get('fb_type'),
                    'instance': fb.get('instance'),
                    'params': fb.get('params', {}),
                    'description': fb.get('description', '')
                })
        
        project_settings = {}
        if 'configuration' in config and 'project_settings' in config['configuration']:
            project_settings = config['configuration']['project_settings']
        
        log("  [OK] JSON geladen / JSON loaded", "SUCCESS")
        log("  Bibliotheken / Libraries: {0}".format(len(libraries)))
        log("  FB-Instanzen / FB instances: {0}".format(len(fb_instances)))
        
        return libraries, fb_instances, project_settings
        
    except Exception as e:
        log("  [WARNING] JSON konnte nicht geladen werden / Could not load JSON: {0}".format(str(e)), "WARNING")
        log("  [INFO] Verwende Beispiel-Konfiguration / Using example configuration", "INFO")
        return EXAMPLE_LIBRARIES, [], {}

    
# =============================================================================
# NAMESPACE-EXTRAKTION AUS LIBRARY-OBJEKT / Namespace Extraction from Library Object
# =============================================================================   
def extract_namespace_from_library(lib):
    """
    Extrahiert den Namespace DIREKT aus dem Library-Objekt
    Extracts namespace DIRECTLY from library object
    
    WICHTIG / IMPORTANT:
    Der Namespace ist im Library-Objekt gespeichert, nicht im Title!
    The namespace is stored in the library object, not in the title!
    
    Mögliche Attribute / Possible attributes:
    - lib.name          → Namespace (z.B. "MQTT" für MQTT_Client_SL)
    - lib.namespace     → Namespace (alternative Attribut)
    - lib.default_namespace → Fallback
    
    Args:
        lib: Library-Objekt aus librarymanager.get_all_libraries()
    
    Returns:
        str: Namespace (z.B. "MQTT", "WagoAppCloud")
    """
    try:
        # Methode 1: lib.name → Namespace / Method 1: lib.name → namespace
        if hasattr(lib, 'name'):
            namespace = str(lib.name)
            if namespace and namespace != "":
                log("      [EXTRACT] lib.name = {0}".format(namespace), "DEBUG")
                return namespace
        
        # Methode 2: lib.namespace / Method 2: lib.namespace
        if hasattr(lib, 'namespace'):
            namespace = str(lib.namespace)
            if namespace and namespace != "":
                log("      [EXTRACT] lib.namespace = {0}".format(namespace), "DEBUG")
                return namespace
        
        # Methode 3: lib.default_namespace / Method 3: lib.default_namespace
        if hasattr(lib, 'default_namespace'):
            namespace = str(lib.default_namespace)
            if namespace and namespace != "":
                log("      [EXTRACT] lib.default_namespace = {0}".format(namespace), "DEBUG")
                return namespace
        
        # Fallback: Verwende Title / Fallback: Use title
        namespace = str(lib.title)
        log("      [FALLBACK] Verwende Title als Namespace / Using title as namespace: {0}".format(namespace), "WARNING")
        return namespace
        
    except Exception as e:
        log("      [ERROR] Namespace-Extraktion fehlgeschlagen / Namespace extraction failed: {0}".format(str(e)), "ERROR")
        # Letzter Fallback: Title / Last fallback: title
        return str(lib.title)

# =============================================================================
# BIBLIOTHEKS-MANAGEMENT MIT REPOSITORY API / Library Management with Repository API
# =============================================================================
def find_library_in_repositories(lib_name, lib_vendor, lib_version=None):
    """
    Sucht eine Bibliothek in allen Repositories
    Searches for a library in all repositories
    
    Returns: (library_object, namespace) or (None, None)
    """
    log("  Suche Bibliothek / Searching library: {0} ({1})".format(lib_name, lib_vendor), "DEBUG")
    
    try:
        for repo in librarymanager.repositories:
            libs = librarymanager.get_all_libraries(repo)
            
            for lib in libs:
                # Prüfe Title und Vendor / Check title and vendor
                if lib.title == lib_name and lib.company == lib_vendor:
                    # Wenn Version angegeben, prüfe diese / If version specified, check it
                    if lib_version:
                        if str(lib.version) == str(lib_version):
                            # Extrahiere Namespace / Extract namespace
                            namespace = extract_namespace_from_library(lib)
                            log("    [FOUND] {0}, {1} ({2})".format(lib.title, lib.version, lib.company), "SUCCESS")
                            log("    [NAMESPACE] {0}".format(namespace), "SUCCESS")
                            return lib, namespace 
                    else:
                        # Keine Version angegeben / No version specified
                        namespace = extract_namespace_from_library(lib)
                        log("    [FOUND] {0}, {1} ({2})".format(lib.title, lib.version, lib.company), "SUCCESS")
                        log("    [NAMESPACE] {0}".format(namespace), "SUCCESS")
                        return lib, namespace
        
        log("    [NOT FOUND] Bibliothek nicht gefunden / Library not found", "WARNING")
        return None, None
        
    except Exception as e:
        log("    [ERROR] Fehler bei Suche / Search error: {0}".format(str(e)), "ERROR")
        return None, None

def get_library_manager_object(app):
    """Findet den Library Manager der Application"""
    try:
        objects = app.get_children(recursive=True)
        for obj in objects:
            if hasattr(obj, 'is_libman') and obj.is_libman:
                log("  [OK] Library Manager gefunden / Library Manager found", "SUCCESS")
                return obj
        log("  [WARNING] Library Manager nicht gefunden / Library Manager not found", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] Fehler beim Suchen / Search error: {0}".format(str(e)), "ERROR")
        return None

def add_library_to_application(libman, proj, lib_title, lib_vendor, lib_version=None):
    log("="*70)
    log("DEBUG: Library hinzufügen")
    log("  Title:   {0}".format(lib_title))
    log("  Vendor:  {0}".format(lib_vendor))
    log("  Version: {0}".format(lib_version))
    log("="*70)
    
    # Suche Library
    target_lib, namespace = find_library_in_repositories(lib_title, lib_vendor, lib_version)
    
    if not target_lib:
        log("  [ERROR] Library nicht gefunden!", "ERROR")
        log("  Verfügbare Libraries mit 'MQTT' im Namen:")
        # Zeige alle ähnlichen Libraries
        lm = system.librarymanager
        for repo in lm.repositories:
            for lib in lm.get_all_libraries(repo):
                if "MQTT" in str(lib.title).upper():
                    log("    - {0} ({1})".format(lib.title, lib.company))
        return False
    
    log("  [FOUND] Library: {0}".format(target_lib.title))
    log("  [NAMESPACE] {0}".format(namespace))
    
    # Versuche hinzuzufügen

    try:
        #log("  Benutze Methode : add_placeholder('{0}' = namespace, {1} = target_lib )".format(namespace, target_lib))
        #libman.add_placeholder(namespace, target_lib)
        log("  Benutze Methode : add_library('{0}' = target_lib )".format(target_lib))
        #
        libman.add_library(target_lib)
        
        log("  [SUCCESS]", "SUCCESS")
        return True
    except Exception as e:
        log("  [FAILED] {0}".format(str(e)), "ERROR")
        
        # Fallback not working
        try:
            namespace_full = "{0}, {1} ({2})".format(namespace, target_lib.version, lib_vendor)
            log("  Methode 2: add('{0}')".format(namespace_full))
            libman.add_library(namespace_full)
            log("  [SUCCESS]", "SUCCESS")
            return True
        except Exception as e2:
            log("  [FAILED] {0}".format(str(e2)), "ERROR")
            return False

def install_libraries_enhanced(proj, app, required_libs):
    """Installiert alle konfigurierten Bibliotheken mit automatischer Namespace-Extraktion"""
    log("Bibliotheks-Installation mit automatischer Namespace-Extraktion")
    log("Library installation with automatic namespace extraction")
    
    try:
        libman = get_library_manager_object(app)
        if not libman:
            log("  [ERROR] Library Manager nicht verfuegbar / Library Manager not available", "ERROR")
            return {"added": 0, "skipped": 0, "failed": 0}
        
        stats = {"added": 0, "skipped": 0, "failed": 0}
        
        for lib_config in required_libs:
            lib_name = lib_config.get("name", "Unknown")
            lib_vendor = lib_config.get("vendor", "3S")
            lib_version = lib_config.get("version")
            lib_required = lib_config.get("required", False)
            
            log("")
            log("  Bibliothek / Library: {0}".format(lib_name))
            log("  " + "-"*66)
            
            success = add_library_to_application(libman, proj, lib_name, lib_vendor, lib_version)
            
            if success:
                stats["added"] += 1
            else:
                stats["failed"] += 1
                if lib_required:
                    log("    [CRITICAL] Pflicht-Bibliothek fehlgeschlagen / Required library failed!", "ERROR")
        
        log("")
        log("  " + "="*66)
        log("  Bibliotheks-Installation abgeschlossen / Library installation completed:")
        log("    Hinzugefuegt / Added:     {0}".format(stats["added"]), "SUCCESS")
        log("    Uebersprungen / Skipped:  {0}".format(stats["skipped"]), "INFO")
        log("    Fehlgeschlagen / Failed:  {0}".format(stats["failed"]), "ERROR" if stats["failed"] > 0 else "INFO")
        log("  " + "="*66)
        
        return stats
        
    except Exception as e:
        log("  [ERROR] Installation fehlgeschlagen / Installation failed: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return {"added": 0, "skipped": 0, "failed": 0}

# =============================================================================
# FUNCTION BLOCK INSTANZIIERUNG / Function Block Instantiation
# =============================================================================
def create_fb_instance_code(fb_config):
    """
    Erstellt IEC-Code für FB-Instanziierung
    Creates IEC code for FB instantiation
    WICHTIG: Trennung Deklaration/Implementierung / IMPORTANT: Separation declaration/implementation
    """
    fb_type = fb_config.get("fb_type", "UNKNOWN")
    instance = fb_config.get("instance", "oInstance")
    params = fb_config.get("params", {})
    
    # VAR-Deklaration (nur Instanz) / VAR declaration (instance only)
    var_declaration = "{0} : {1};".format(instance, fb_type)
    
    # Implementierung: FB-Aufruf / Implementation: FB call
    param_list = []
    for param_name, param_value in params.items():
        if param_value and param_value.strip():
            # Output-Parameter (endet mit =>) / Output parameter (ends with =>)
            if param_name.endswith("=>"):
                param_name_clean = param_name[:-2].strip()
                if param_value:
                    param_list.append("{0}=>{1}".format(param_name_clean, param_value))
            else:
                # Input/InOut-Parameter
                param_list.append("{0}:={1}".format(param_name, param_value))
    
    if param_list:
        fb_call = "{0}({1});".format(instance, ", ".join(param_list))
    else:
        fb_call = "{0}();".format(instance)
    
    return var_declaration, fb_call

def add_fb_instances_to_plc_prg(app, fb_instances=None):
    """
    Fügt Function Block Instanzen zum PLC_PRG hinzu
    Adds Function Block instances to PLC_PRG
    WICHTIG: FB-Aufrufe in Implementation / IMPORTANT: FB calls in implementation
    """
    log("Fuege Function Block Instanzen hinzu / Adding Function Block instances...")
    
    if fb_instances is None or len(fb_instances) == 0:
        log("  [INFO] Keine FB-Instanzen konfiguriert / No FB instances configured", "INFO")
        return True
    
    try:
        pous = app.find("PLC_PRG", False)
        if not pous or len(pous) == 0:
            log("  [ERROR] PLC_PRG nicht gefunden / PLC_PRG not found!", "ERROR")
            return False
        
        pou = pous[0]
        log("  [OK] PLC_PRG gefunden / PLC_PRG found")
        
        # Erstelle Code-Blöcke / Create code blocks
        var_declarations = []
        fb_calls = []
        
        for fb_config in fb_instances:
            lib_name = fb_config.get("library", "Unknown")
            fb_type = fb_config.get("fb_type", "Unknown")
            description = fb_config.get("description", "")
            
            log("  FB: {0} aus / from {1}".format(fb_type, lib_name))
            if description:
                log("      {0}".format(description))
            
            var_decl, fb_call = create_fb_instance_code(fb_config)
            var_declarations.append(var_decl)
            fb_calls.append(fb_call)
        
        # Erstelle vollständigen Code / Create complete code
        # WICHTIG: Trennung VAR-Block und Implementation / IMPORTANT: Separation VAR block and implementation
        declaration_code = """PROGRAM PLC_PRG
VAR
    // 
    // =============================================================================
    // Function Block instances (automatically generated)
    // =============================================================================
    {0}
END_VAR
""".format("\n    ".join(var_declarations))
        implementation_code ="""
// =============================================================================
// IMPLEMENTATION (FB-Aufrufe) / IMPLEMENTATION (automatically generated)
// =============================================================================
{0}
""".format("\n".join(fb_calls))
        
        try:
            pou.textual_declaration.replace(declaration_code)
            pou.textual_implementation.replace(implementation_code)
            log("  [SUCCESS] {0} FB-Instanzen hinzugefuegt / FB instances added!".format(len(fb_instances)), "SUCCESS")
            return True
        except Exception as e:
            log("  [ERROR] Code-Update fehlgeschlagen / Code update failed: {0}".format(str(e)), "ERROR")
            return False
        
    except Exception as e:
        log("  [ERROR] FB-Instanziierung fehlgeschlagen / FB instantiation failed: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# DEVICE DESCRIPTOR HELPERS
# =============================================================================
def is_blacklisted(module_type):
    """Prüft Blacklist / Checks blacklist"""
    for blacklisted in MODULE_BLACKLIST:
        if module_type.startswith(blacklisted):
            return True
    return False

def is_greylisted(module_type):
    """Prüft Greylist / Checks greylist"""
    return module_type in MODULE_GREYLIST

def get_device_descriptor(module_type):
    """Holt Device Descriptor / Gets device descriptor"""
    if module_type in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[module_type]
    base_module = module_type.split('#')[0]
    if base_module in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[base_module]
    if base_module == "750-652":
        return WAGO_DEVICE_DESCRIPTORS.get("750-652#48")
    return None

def show_available_descriptors():
    """Zeigt verfügbare Module / Shows available modules"""
    log("")
    log("="*70)
    log("VERFUEGBARE WAGO MODULE / AVAILABLE WAGO MODULES:")
    log("="*70)
    for module_name, info in sorted(WAGO_DEVICE_DESCRIPTORS.items()):
        log("  {0}".format(module_name))
        log("    Name:       {0}".format(info['name']))
        log("    Descriptor: {0}".format(info['descriptor']))
        log("    Version:    {0}".format(info['version']))
        log("    Typ:        {0}".format(info['description']))
        log("")
    log("="*70)

# =============================================================================
# AUTO-DETECT
# =============================================================================
def find_all_files(search_path, pattern):
    """Findet Dateien / Finds files"""
    if not os.path.exists(search_path):
        return []
    full_pattern = os.path.join(search_path, pattern)
    try:
        matches = glob.glob(full_pattern)
        return sorted(matches)
    except:
        return []

def match_files(var_files, config_files):
    """Matched Dateipaare / Matches file pairs"""
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
                log("  [OK] Paar / Pair: {0}".format(plc_id))
                break
    return matched_pairs

# =============================================================================
# PARSER
# =============================================================================
def parse_variables_file(filepath):
    """Parsed Variablen-Datei / Parses variables file"""
    log("Parse Variablen-Datei / Parsing variables file...")
    try:
        import codecs
        with codecs.open(filepath, 'r', 'utf-8') as f:
            content = f.read()
        match = re.search(r'VAR_GLOBAL.*?END_VAR', content, re.DOTALL)
        if match:
            var_block = match.group(0)
            log("  [OK] VAR_GLOBAL Block gefunden / found ({0} Zeichen / characters)".format(len(var_block)))
            return var_block
        else:
            log("  [WARNING] Kein VAR_GLOBAL Block / No VAR_GLOBAL block", "WARNING")
            return None
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        return None

def parse_config_json(filepath):
    """Parsed JSON-Konfiguration / Parses JSON configuration"""
    log("Parse JSON-Konfiguration / Parsing JSON configuration...")
    try:
        import codecs
        with codecs.open(filepath, 'r', 'utf-8') as f:
            config = json.load(f)
        if 'PLC_Info' not in config:
            log("  [ERROR] 'PLC_Info' fehlt / missing", "ERROR")
            return None
        plc_info = config['PLC_Info']
        log("  [OK] PLC: {0}".format(plc_info.get('Name', 'N/A')))
        log("  [OK] Typ: {0}".format(plc_info.get('Type', 'N/A')))
        log("  [OK] IP: {0}".format(plc_info.get('IP_Address', 'N/A')))
        return config
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        return None

# =============================================================================
# PROJEKT-ERSTELLUNG / Project Creation
# =============================================================================
def create_project_from_template(plc_name, project_path, template_path):
    """Erstellt Projekt aus Template / Creates project from template"""
    log("Erstelle Projekt aus Template / Creating project from template...")
    try:
        import shutil
        full_path = os.path.join(project_path, "{0}.project".format(plc_name))
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        if os.path.exists(full_path):
            os.remove(full_path)
            log("  [OK] Altes Projekt geloescht / Old project deleted")
        shutil.copy2(template_path, full_path)
        log("  [OK] Template kopiert / Template copied: {0}".format(full_path))
        proj = projects.open(full_path, None, True)
        log("  [OK] Projekt geoeffnet / Project opened!")
        return proj, full_path
    except Exception as e:
        log("  [ERROR] Template-Fehler / Template error: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return None, None

def find_or_create_application(proj):
    """Findet Application / Finds application"""
    log("Suche Application / Searching application...")
    try:
        applications = proj.find("Application", True)
        if applications and len(applications) > 0:
            app = applications[0]
            log("  [OK] Application gefunden / found: {0}".format(app.get_name(False)))
            return app
        all_objs = proj.get_children(True)
        log("  Durchsuche / Searching {0} Objekte / objects...".format(len(all_objs)))
        for obj in all_objs:
            obj_name = obj.get_name(False)
            obj_type = str(type(obj))
            if "Application" in obj_name or "Application" in obj_type:
                log("  [OK] Application gefunden / found: {0}".format(obj_name))
                return obj
        try:
            app = proj.active_application
            if app:
                log("  [OK] Active Application gefunden / found!")
                return app
        except:
            pass
        log("  [ERROR] Keine Application / No application!", "ERROR")
        return None
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return None

def find_plc_device(proj):
    """Findet PLC Device / Finds PLC device"""
    log("Suche PLC Device (Type 4096)...")
    try:
        all_objects = proj.get_children(recursive=True)
        for obj in all_objects:
            if hasattr(obj, 'is_device') and obj.is_device:
                try:
                    dev_id = obj.get_device_identification()
                    obj_name = obj.get_name(False)
                    if dev_id.type == 4096:
                        log("  [OK] PLC Device gefunden / found: {0}".format(obj_name))
                        return obj
                except:
                    continue
        devices = proj.find("Device", True)
        if devices and len(devices) > 0:
            device = devices[0]
            log("  [OK] Device gefunden (Fallback) / found (fallback): {0}".format(device.get_name(False)))
            return device
        log("  [WARNING] Kein PLC Device / No PLC device", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        return None

def find_kbus(device):
    """Findet Kbus"""
    log("Suche Kbus...")
    try:
        if not device:
            log("  [ERROR] Kein Device / No device", "ERROR")
            return None
        kbus_results = device.find('Kbus', True)
        if kbus_results and len(kbus_results) > 0:
            kbus = kbus_results[0]
            log("  [OK] Kbus gefunden / found: {0}".format(kbus.get_name(False)))
            return kbus
        children = device.get_children(False)
        log("  Device hat / has {0} Kinder / children".format(len(children)))
        for child in children:
            child_name = child.get_name(False)
            if "Kbus" in child_name or "KBus" in child_name:
                log("  [OK] Kbus gefunden / found: {0}".format(child_name))
                return child
        log("  [WARNING] Kbus nicht gefunden / not found", "WARNING")
        return None
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return None

def get_first_gateway():
    """Holt erstes Gateway / Gets first gateway"""
    try:
        gateways = online.gateways
        for gw in gateways:
            try:
                gw_name = gw.name
                log("  Gefundenes Gateway / Found gateway: {0}".format(gw_name))
                return gw
            except:
                continue
        log("  [WARNING] Kein Gateway / No gateway", "WARNING")
        return None
    except Exception as e:
        log("  [WARNING] Gateway-Zugriff fehlgeschlagen / Gateway access failed: {0}".format(str(e)), "WARNING")
        return None

def configure_device_ip(proj, device, ip_address):
    """Konfiguriert IP-Adresse / Configures IP address"""
    log("Konfiguriere Device IP-Adresse / Configuring device IP address...")
    try:
        parts = ip_address.split('.')
        normalized_ip = '.'.join([str(int(p)) for p in parts])
        log("  IP-Adresse (normalisiert / normalized): {0}".format(normalized_ip))
        try:
            gateway = get_first_gateway()
            if gateway:
                log("  Gateway gefunden / found: {0}".format(gateway.name))
                log("  Versuche IP-Konfiguration / Trying IP configuration...")
                device.set_gateway_and_ip_address(gateway, normalized_ip)
                log("  [SUCCESS] IP-Adresse gesetzt / IP address set: {0}".format(normalized_ip), "SUCCESS")
                return True
        except AttributeError as e:
            log("  [WARNING] Methode nicht verfuegbar / Method not available: {0}".format(str(e)), "WARNING")
        except Exception as e:
            log("  [WARNING] Gateway-Methode fehlgeschlagen / Gateway method failed: {0}".format(str(e)), "WARNING")
        log("  [ERROR] IP-Adresse konnte nicht gesetzt werden / Could not set IP address", "ERROR")
        log("  [INFO] Bitte manuell konfigurieren / Please configure manually", "WARNING")
        return False
    except Exception as e:
        log("  [ERROR] IP-Konfiguration fehlgeschlagen / IP configuration failed: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

def add_io_modules_to_kbus(kbus, config):
    """Fügt IO-Module hinzu / Adds IO modules"""
    log("Konfiguriere Kbus Module / Configuring Kbus modules...")
    try:
        if not config or "IO_Modules" not in config:
            log("  [WARNING] Keine IO-Module / No IO modules", "WARNING")
            return False
        io_modules = config["IO_Modules"]
        if not io_modules or len(io_modules) == 0:
            log("  [INFO] Keine Module / No modules", "INFO")
            return True
        log("  {0} Module gefunden / found".format(len(io_modules)))
        if not kbus:
            log("  [WARNING] Kbus nicht gefunden / not found", "WARNING")
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
            log("  Modul / Module {0}/{1}: {2} ({3} Signale / signals)".format(idx, len(io_modules), module_type, signal_count))
            log("  " + "-"*66)
            if is_blacklisted(module_type):
                log("    [SKIP] PLC Device (Blacklist): {0}".format(module_type), "WARNING")
                skipped_blacklist += 1
                continue
            if is_greylisted(module_type):
                log("    [SKIP] Kein Process Data / No process data (Greylist): {0}".format(module_type), "INFO")
                skipped_greylist += 1
                continue
            descriptor_info = get_device_descriptor(module_type)
            if not descriptor_info:
                log("    [ERROR] Kein Device Descriptor / No device descriptor!", "ERROR")
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
                    log("    [SUCCESS] Modul hinzugefuegt / Module added!", "SUCCESS")
                    success_count += 1
                else:
                    log("    [ERROR] Kbus Objekt ist None / Kbus object is None", "ERROR")
                    fail_count += 1
            except Exception as e:
                log("    [ERROR] Hinzufuegen fehlgeschlagen / Adding failed: {0}".format(str(e)), "ERROR")
                fail_count += 1
        log("")
        log("  " + "="*66)
        log("  Kbus Konfiguration abgeschlossen / Kbus configuration completed:")
        log("    Erfolgreich / Successful:  {0}".format(success_count), "SUCCESS")
        if fail_count > 0:
            log("    Fehlgeschlagen / Failed:   {0}".format(fail_count), "WARNING")
        if skipped_blacklist > 0:
            log("    Uebersprungen (PLCs):      {0}".format(skipped_blacklist), "WARNING")
        if skipped_greylist > 0:
            log("    Uebersprungen (Kein PD):   {0}".format(skipped_greylist), "INFO")
        if skipped_unknown > 0:
            log("    Uebersprungen (Unbekannt): {0}".format(skipped_unknown), "WARNING")
        log("  " + "="*66)
        return success_count > 0
    except Exception as e:
        log("  [ERROR] Kbus Konfiguration fehlgeschlagen / Kbus configuration failed: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

def find_or_update_plc_prg(app):
    """Findet/Aktualisiert PLC_PRG / Finds/Updates PLC_PRG"""
    log("Suche PLC_PRG...")
    try:
        pous = app.find("PLC_PRG", False)
        if pous and len(pous) > 0:
            pou = pous[0]
            log("  [OK] PLC_PRG gefunden / found")
            try:
                default_code = """PROGRAM PLC_PRG
VAR
END_VAR

// Haupt-Programm / Main program
"""
                try:
                    pou.textual_declaration.replace(default_code)
                    log("  [OK] Code aktualisiert / updated")
                except:
                    pass
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
        log("  [OK] PLC_PRG erstellt / created")
        return pou
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        return None

def create_gvl_with_variables(app, gvl_name, var_block):
    """Erstellt GVL / Creates GVL"""
    log("Erstelle GVL / Creating GVL '{0}'...".format(gvl_name))
    try:
        gvl = app.create_gvl(gvl_name)
        log("  [OK] GVL erstellt / created")
        if var_block:
            try:
                gvl.textual_declaration.replace(var_block)
                log("  [OK] Variablen eingefuegt / Variables inserted - {0} Zeichen / characters".format(len(var_block)))
                return gvl
            except:
                log("  [WARNING] Variablen konnten nicht eingefuegt werden / Could not insert variables", "WARNING")
                return gvl
        return gvl
    except Exception as e:
        log("  [ERROR] Fehler / Error: {0}".format(str(e)), "ERROR")
        return None

# =============================================================================
# HAUPT-ABLAUF / Main Process
# =============================================================================
def create_single_project(var_file, config_file, plc_name):
    """Erstellt einzelnes Projekt / Creates single project"""
    global CURRENT_STEP, REQUIRED_LIBRARIES, FB_INSTANCES
    
    try:
        log_step("Lade JSON-Konfiguration / Load JSON configuration", TOTAL_STEPS_PER_PROJECT)
        
        # Lade JSON-Konfiguration / Load JSON configuration
        if os.path.exists(CONFIG_JSON_PATH):
            libs, fbs, settings = load_config_from_json(CONFIG_JSON_PATH)
            if libs:
                REQUIRED_LIBRARIES = libs
            if fbs:
                FB_INSTANCES = fbs
        else:
            log("  [INFO] Keine JSON-Datei, verwende Beispiel / No JSON file, using example", "INFO")
            REQUIRED_LIBRARIES = EXAMPLE_LIBRARIES
        
        log_step("Parse Eingabedateien / Parse input files", TOTAL_STEPS_PER_PROJECT)
        var_block = parse_variables_file(var_file)
        config = parse_config_json(config_file)
        if not var_block or not config:
            return False
        
        log_step("Erstelle CODESYS-Projekt / Create CODESYS project", TOTAL_STEPS_PER_PROJECT)
        if USE_TEMPLATE and os.path.exists(TEMPLATE_PROJECT):
            log("Verwende Template-Methode / Using template method")
            proj, full_path = create_project_from_template(plc_name, DEFAULT_PROJECT_PATH, TEMPLATE_PROJECT)
        else:
            log("  [ERROR] Template nicht gefunden / Template not found!", "ERROR")
            return False
        if not proj:
            return False
        
        log_step("Suche Application", TOTAL_STEPS_PER_PROJECT)
        app = find_or_create_application(proj)
        if not app:
            log("  [ERROR] Keine Application!", "ERROR")
            proj.close()
            return False
        
        log_step("Installiere Bibliotheken mit Repository API / Install libraries with Repository API", TOTAL_STEPS_PER_PROJECT)
        install_libraries_enhanced(proj, app, REQUIRED_LIBRARIES)
        
        log_step("Suche PLC Device", TOTAL_STEPS_PER_PROJECT)
        device = find_plc_device(proj)
        
        if device and 'PLC_Info' in config:
            plc_info = config['PLC_Info']
            if 'IP_Address' in plc_info:
                log_step("Konfiguriere IP-Adresse / Configure IP address", TOTAL_STEPS_PER_PROJECT)
                configure_device_ip(proj, device, plc_info['IP_Address'])
        
        log_step("Konfiguriere Kbus mit IO-Modulen / Configure Kbus with IO modules", TOTAL_STEPS_PER_PROJECT)
        if device:
            kbus = find_kbus(device)
            if kbus:
                add_io_modules_to_kbus(kbus, config)
            else:
                log("  [WARNING] Kbus nicht gefunden / not found", "WARNING")
        else:
            log("  [WARNING] Device nicht gefunden / not found", "WARNING")
        
        log_step("Suche/Aktualisiere PLC_PRG / Find/Update PLC_PRG", TOTAL_STEPS_PER_PROJECT)
        pou = find_or_update_plc_prg(app)
        
        log_step("Instanziiere Function Blocks", TOTAL_STEPS_PER_PROJECT)
        add_fb_instances_to_plc_prg(app, FB_INSTANCES)
        
        log_step("Erstelle GVL mit Variablen / Create GVL with variables", TOTAL_STEPS_PER_PROJECT)
        gvl_name = "GVL_{0}".format(plc_name)
        gvl = create_gvl_with_variables(app, gvl_name, var_block)
        
        log_step("Speichere Projekt / Save project", TOTAL_STEPS_PER_PROJECT)
        proj.save()
        log("  [OK] Projekt gespeichert / Project saved")
        proj.close()
        log("  [OK] Projekt geschlossen / Project closed")
        log("")
        log("-"*70)
        log("PROJEKT ERFOLGREICH / PROJECT SUCCESSFUL: {0}".format(plc_name), "SUCCESS")
        log("  Pfad / Path: {0}".format(full_path))
        log("-"*70)
        return True
    except Exception as e:
        log("FEHLER / ERROR: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        return False

# =============================================================================
# MAIN
# =============================================================================
def main():
    """Hauptfunktion / Main function"""
    global CURRENT_STEP
    start_time = time.time()
    log_file = init_logging("create_codesys_project")
    show_available_descriptors()
    success_count = 0
    failure_count = 0
    try:
        log_step("Sammle Dateien / Collect files")
        if AUTO_DETECT_MODE:
            log("Auto-Detect Modus aktiv / Auto-detect mode active")
            var_files = find_all_files(DEFAULT_VARIABLES_PATH, "IO*_variables.txt")
            config_files = find_all_files(DEFAULT_CONFIG_PATH, "PLC_IO*_config.json")
            matched_pairs = match_files(var_files, config_files)
        else:
            log("Spezifischer Modus / Specific mode")
            matched_pairs = [(SPECIFIC_VARIABLES_FILE, SPECIFIC_CONFIG_FILE, "IO020")]
        if not matched_pairs:
            log("FEHLER: Keine Dateien gefunden / ERROR: No files found!", "ERROR")
            sys.exit(1)
        log("")
        log("="*70)
        log("STARTE ERSTELLUNG / START CREATION: {0} Projekte / projects".format(len(matched_pairs)))
        log("="*70)
        for idx, (var_file, config_file, plc_id) in enumerate(matched_pairs, 1):
            log("")
            log("="*70)
            log("PROJEKT / PROJECT {0}/{1}: {2}".format(idx, len(matched_pairs), plc_id))
            log("="*70)
            CURRENT_STEP = 0
            if create_single_project(var_file, config_file, plc_id):
                success_count += 1
            else:
                failure_count += 1
        elapsed = time.time() - start_time
        log("")
        log("="*70)
        log("FERTIG / FINISHED!", "SUCCESS")
        log("="*70)
        log("Gesamt / Total: {0}".format(len(matched_pairs)))
        log("Erfolgreich / Successful: {0}".format(success_count))
        log("Fehlgeschlagen / Failed: {0}".format(failure_count))
        log("Dauer / Duration: {0}".format(format_duration(elapsed)))
        log("Log: {0}".format(log_file))
        log("="*70)
    except Exception as e:
        log("KRITISCHER FEHLER / CRITICAL ERROR: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
