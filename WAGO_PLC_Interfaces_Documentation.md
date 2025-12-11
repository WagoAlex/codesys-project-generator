# WAGO PLC Configuration System - Technical Documentation

**Version:** 0.8.2 (Beta)  
**Author:** Alexander Fugmann  
**Last Updated:** 2024-12-11

---

## 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     WAGO PLC CONFIGURATION SYSTEM                       │
└─────────────────────────────────────────────────────────────────────────┘

Phase 1: EXCEL → JSON CONVERSION
────────────────────────────────────

   ┌────────────────┐
   │  Excel File    │  LIST_OF_MEASURING_POINTS.xls
   │   (.xls/.xlsx) │  ├─ Sheet: IO-Boxen (Header: Row 4)
   └────────┬───────┘  └─ Sheet: SIGNALLIST (Header: Row 1)
            │
            │ [pandas.read_excel()]
            ↓
   ┌────────────────────────┐
   │  PLCConfigExtractor    │  Main class
   │  ──────────────────    │
   │  .extract_plcs_from_   │  → Parse IO-Boxen
   │   io_boxes()           │     - PLC name, IP, Location, IO-Box
   │                        │
   │  .extract_signals_     │  → Parse SIGNALLIST
   │   from_signallist()    │     - Modules, Terminals, Signals
   │                        │
   │  .validate_ip_address()│  → IP validation
   │  .extract_plc_type()   │  → PLC type extraction
   └────────┬───────────────┘
            │
            │ [json.dump()]
            ↓
   ┌────────────────────────┐
   │  JSON Files            │  PLC_IO020_config.json
   │  ─────────────         │  PLC_IO021_config.json
   │  PLC_Info             │  ...
   │  IO_Modules           │
   │  Statistics           │
   └────────┬───────────────┘
            │
            ↓
   ┌────────────────────────┐
   │  Companion Files       │
   │  ──────────────        │
   │  summary.txt          │  → Overview of all PLCs
   │  validation_report.txt│  → Errors/Warnings
   └────────────────────────┘


Phase 2: JSON → CODESYS PROJECT
────────────────────────────────

   ┌────────────────────────┐
   │  Input Files           │
   │  ──────────────        │
   │  PLC_IO020_config.json │  → PLC configuration
   │  IO020_variables.txt   │  → Variable declarations
   │  project_config.json   │  → System configuration
   └────────┬───────────────┘
            │
            │ [codesys_project_generator_local.py]
            ↓
   ┌────────────────────────────────────┐
   │  13-Step Generation Process        │
   │                                    │
   │  Step 1:  Load JSON configuration  │
   │  Step 2:  Parse input files        │
   │  Step 3:  Create CODESYS project   │
   │  Step 4:  Find Application         │
   │  Step 5:  Install libraries        │
   │  Step 6:  Import XML files         │
   │  Step 7:  Find PLC device          │
   │  Step 8:  Configure IP address     │
   │  Step 9:  Configure K-Bus          │
   │  Step 10: Find/Update PLC_PRG      │
   │  Step 11: Instantiate FBs          │
   │  Step 12: Create GVL               │
   │  Step 13: Save project             │
   └────────┬───────────────────────────┘
            │
            │ [CODESYS ScriptEngine API]
            ↓
   ┌────────────────────────┐
   │  CODESYS Project       │  IO020.project
   │  ────────────────      │
   │  Application          │
   │  ├─ Libraries          │  MQTT_Client_SL, JSON_Utilities_SL
   │  ├─ POUs (from XML)    │  MQTT_Handler, Utilities
   │  ├─ PLC_PRG            │  Main program
   │  │  ├─ VAR section     │  FB instances (oMQTTClient, etc.)
   │  │  └─ Implementation  │  FB calls
   │  └─ GVL_IO020          │  Global variables
   │                        │
   │  Device (750-8210)     │
   │  └─ K-Bus              │
   │     ├─ 750-432 (4DI)   │
   │     ├─ 750-461 (2AI)   │
   │     └─ 750-515 (4RO)   │
   └────────────────────────┘
```

---

## 🔌 Core Interfaces

### Phase 1: Excel to JSON

#### PLCConfigExtractor Class

```python
class PLCConfigExtractor:
    """Extract PLC configuration from Excel files"""
    
    def __init__(self, excel_file_path: str):
        """
        Initialize extractor with Excel file path
        
        Args:
            excel_file_path: Path to Excel file with measuring points
        """
        self.excel_file = excel_file_path
        self.plcs = []
        self.df_io_boxes = None
        self.df_signallist = None
    
    def load_sheets(self) -> bool:
        """
        Load required sheets from Excel file
        
        Returns:
            True if successful, False otherwise
        """
        self.df_io_boxes = pd.read_excel(
            self.excel_file, 
            sheet_name='IO-Boxen', 
            header=3  # Row 4 is header (0-indexed)
        )
        
        self.df_signallist = pd.read_excel(
            self.excel_file,
            sheet_name='SIGNALLIST',
            header=0  # Row 1 is header
        )
    
    def extract_plcs_from_io_boxes(self) -> List[Dict]:
        """
        Extract PLC information from IO-Boxen sheet
        
        Returns:
            List of PLC dictionaries with keys:
            - name: PLC identifier (e.g., "IO020")
            - ip: IP address (e.g., "172.16.46.020")
            - location: Physical location
            - io_box: Box number
        """
        plcs = []
        for index, row in self.df_io_boxes.iterrows():
            if pd.notna(row.get('PLC')) and pd.notna(row.get('IP-Adress')):
                plc = {
                    'name': str(row['PLC']).strip(),
                    'ip': str(row['IP-Adress']).strip(),
                    'location': str(row.get('Location', '')).strip(),
                    'io_box': str(row.get('IO BOX', '')).strip()
                }
                plcs.append(plc)
        return plcs
    
    def extract_signals_from_signallist(self, plc_name: str) -> List[Dict]:
        """
        Extract signals for specific PLC from SIGNALLIST sheet
        
        Args:
            plc_name: PLC identifier to filter signals
        
        Returns:
            List of signal dictionaries grouped by module type
        """
        # Filter signals for specific PLC
        plc_signals = self.df_signallist[
            self.df_signallist['PLC'] == plc_name
        ]
        
        # Group by module type
        modules = {}
        for index, row in plc_signals.iterrows():
            module_type = str(row['Mode_Type']).strip()
            
            if module_type not in modules:
                modules[module_type] = {
                    'Module_Type': module_type,
                    'Signals': []
                }
            
            signal = {
                'Terminal': str(row['PLC_terminal']).strip(),
                'Object_Name': str(row['Objektname']).strip(),
                'Signal_Type': str(row['Type']).strip(),
                'Signal': str(row['Signal']).strip()
            }
            modules[module_type]['Signals'].append(signal)
        
        return list(modules.values())
    
    def validate_ip_address(self, ip: str) -> bool:
        """
        Validate IP address format and range
        
        Args:
            ip: IP address string
        
        Returns:
            True if valid, False otherwise
        """
        # Remove leading zeros and validate
        parts = ip.split('.')
        normalized = '.'.join([str(int(p)) for p in parts])
        
        # Check valid ranges
        valid_ranges = [
            '172.16.46.',  # Primary range
            '172.16.60.'   # Secondary range
        ]
        
        return any(normalized.startswith(r) for r in valid_ranges)
```

#### JSON Output Format

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

---

### Phase 2: JSON to CODESYS Project

#### Main Generator Script

**File:** `codesys_project_generator_local.py`

```python
# Configuration constants
BASE_PATH = r"D:\WAGO\CODESYS\scripting\project generator\files"
DEFAULT_PROJECT_PATH = os.path.join(BASE_PATH, "projects")
DEFAULT_VARIABLES_PATH = os.path.join(BASE_PATH, "outputs")
CONFIG_JSON_PATH = os.path.join(BASE_PATH, "project_config.json")
TEMPLATE_PROJECT = os.path.join(BASE_PATH, "TEMPLATE_WAGO_750-8210.project")

AUTO_DETECT_MODE = True  # Automatically find file pairs
TOTAL_STEPS_PER_PROJECT = 13  # 13-step generation process
```

#### Core Functions

**1. Configuration Loading**

```python
def load_config_from_json(json_path):
    """
    Load project configuration from JSON file
    
    Args:
        json_path: Path to project_config.json
    
    Returns:
        Tuple of (libraries, fb_instances, xml_imports, settings)
    """
    with codecs.open(json_path, 'r', 'utf-8') as f:
        config = json.load(f)
    
    libraries = config.get('libraries', {}).get('items', [])
    fb_instances = config.get('function_blocks', {}).get('items', [])
    
    # Handle XML auto-detection
    xml_imports = []
    xml_section = config.get('xml_imports', {})
    
    if isinstance(xml_section, dict) and 'auto_detect' in xml_section:
        auto_config = xml_section['auto_detect']
        if auto_config.get('enabled', False):
            xml_imports = auto_detect_xml_files(auto_config)
    
    settings = config.get('import_settings', {})
    
    return libraries, fb_instances, xml_imports, settings

def auto_detect_xml_files(auto_config):
    """
    Automatically detect XML files in specified directory
    
    Args:
        auto_config: Dictionary with detection settings
    
    Returns:
        List of XML import dictionaries
    """
    directory = auto_config.get('directory', 'exports')
    pattern = auto_config.get('pattern', '*.xml')
    exclude_patterns = auto_config.get('exclude_patterns', [])
    
    # Build full path
    if not os.path.isabs(directory):
        directory = os.path.join(BASE_PATH, directory)
    
    # Find all XML files
    xml_files = glob.glob(os.path.join(directory, pattern))
    
    # Filter excluded patterns
    xml_imports = []
    for xml_file in xml_files:
        filename = os.path.basename(xml_file)
        
        # Check exclusions
        excluded = any(
            re.match(pattern.replace('*', '.*'), filename)
            for pattern in exclude_patterns
        )
        
        if not excluded:
            xml_imports.append({
                'path': xml_file,
                'description': f'Auto-detected: {filename}',
                'conflict_resolve': auto_config.get('default_conflict_resolve', 'replace'),
                'optional': auto_config.get('treat_all_as_optional', False)
            })
    
    return xml_imports
```

**2. Project Creation**

```python
def create_project_from_template(plc_name, project_path, template_path):
    """
    Create CODESYS project from template
    
    Args:
        plc_name: Name for new project
        project_path: Directory for project file
        template_path: Path to template .project file
    
    Returns:
        Tuple of (project_object, full_path) or (None, None) on failure
    """
    import shutil
    
    # Build target path
    full_path = os.path.join(project_path, f"{plc_name}.project")
    
    # Ensure directory exists
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    
    # Delete old project if exists
    if os.path.exists(full_path):
        os.remove(full_path)
    
    # Copy template
    shutil.copy2(template_path, full_path)
    
    # Open project
    proj = projects.open(full_path, None, True)
    
    return proj, full_path
```

**3. Library Management**

```python
def get_library_manager_object(app):
    """
    Find Library Manager object in application tree
    
    Args:
        app: Application object
    
    Returns:
        Library Manager object or None
    """
    objects = app.get_children(recursive=True)
    for obj in objects:
        if hasattr(obj, 'is_libman') and obj.is_libman:
            return obj
    return None

def find_library_in_repositories(lib_name, lib_vendor, lib_version=None):
    """
    Search for library in all repositories
    
    Args:
        lib_name: Library display name (e.g., "MQTT Client SL")
        lib_vendor: Vendor name (e.g., "CODESYS")
        lib_version: Specific version or None for latest
    
    Returns:
        Tuple of (library_object, namespace) or (None, None)
    """
    # Access repositories directly (NOT system.librarymanager)
    for repo in librarymanager.repositories:
        libs = librarymanager.get_all_libraries(repo)
        
        for lib in libs:
            # Match title and vendor
            if lib.title == lib_name and lib.company == lib_vendor:
                # Check version if specified
                if lib_version and str(lib.version) != str(lib_version):
                    continue
                
                # Extract namespace
                namespace = extract_namespace_from_library(lib)
                return lib, namespace
    
    return None, None

def extract_namespace_from_library(lib):
    """
    Extract namespace from library object
    
    Args:
        lib: Library object from repository
    
    Returns:
        Namespace string (e.g., "MQTT")
    """
    # Try multiple attributes
    if hasattr(lib, 'name') and lib.name:
        return str(lib.name)
    if hasattr(lib, 'namespace') and lib.namespace:
        return str(lib.namespace)
    if hasattr(lib, 'default_namespace') and lib.default_namespace:
        return str(lib.default_namespace)
    
    # Fallback to title
    return str(lib.title)

def add_library_to_application(libman, proj, lib_title, lib_vendor, lib_version):
    """
    Add library to application
    
    Args:
        libman: Library Manager object
        proj: Project object
        lib_title: Library display name
        lib_vendor: Vendor name
        lib_version: Version or None
    
    Returns:
        True if successful, False otherwise
    """
    target_lib, namespace = find_library_in_repositories(
        lib_title, lib_vendor, lib_version
    )
    
    if not target_lib:
        return False
    
    # Add library (NOT add_placeholder)
    libman.add_library(target_lib)
    return True
```

**4. XML Import**

```python
def import_xml_files(proj, xml_imports, default_conflict_mode='replace'):
    """
    Import XML files to Application
    
    Args:
        proj: Project object
        xml_imports: List of XML import dictionaries
        default_conflict_mode: Default conflict resolution
    
    Returns:
        True if successful, False if errors occurred
    """
    # Find Application object
    results = proj.find("Application", True)
    if not results:
        return False
    app = results[0]
    
    success_count = 0
    error_count = 0
    
    for xml_item in xml_imports:
        filepath = xml_item.get('path', '')
        conflict_mode_str = xml_item.get('conflict_resolve', default_conflict_mode)
        optional = xml_item.get('optional', False)
        
        # Check file exists
        if not os.path.exists(filepath):
            if optional:
                continue
            else:
                error_count += 1
                continue
        
        # Detect format
        file_format = detect_xml_format(filepath)
        
        # Skip unsupported formats
        if file_format == 'export':
            error_count += 1
            continue
        
        # Convert conflict mode string to integer
        conflict_mode = get_conflict_resolve_mode(conflict_mode_str)
        
        # Import to Application
        try:
            app.import_xml(conflict_mode, filepath, True)
            success_count += 1
        except Exception as e:
            error_count += 1
    
    return error_count == 0

def detect_xml_format(filepath):
    """
    Detect XML file format
    
    Args:
        filepath: Path to XML file
    
    Returns:
        Format string: 'export', 'plcopenxml', 'projectxml', or 'unknown'
    """
    with open(filepath, 'r') as f:
        content = f.read(500)
    
    if content.strip().startswith('<ExportFile'):
        return 'export'
    elif 'plcopen.org/xml/tc6' in content:
        return 'plcopenxml'
    elif '<project' in content and '<fileHeader>' in content:
        return 'projectxml'
    
    return 'unknown'

def get_conflict_resolve_mode(mode_str):
    """
    Convert conflict resolution string to integer
    
    Args:
        mode_str: "replace", "copy", or "skip"
    
    Returns:
        Integer: 0 (replace), 1 (copy), or 2 (skip)
    """
    mode_lower = mode_str.lower() if mode_str else 'replace'
    if mode_lower == 'replace':
        return 0
    elif mode_lower == 'copy':
        return 1
    else:  # skip
        return 2
```

**5. K-Bus Configuration**

```python
def add_io_modules_to_kbus(kbus, config):
    """
    Add IO modules to K-Bus
    
    Args:
        kbus: K-Bus object
        config: PLC configuration dictionary
    
    Returns:
        True if successful, False otherwise
    """
    io_modules = config.get("IO_Modules", [])
    
    success_count = 0
    fail_count = 0
    skipped_count = 0
    
    for module in io_modules:
        module_type = module.get("Module_Type", "UNKNOWN")
        
        # Check blacklist (PLC devices)
        if is_blacklisted(module_type):
            skipped_count += 1
            continue
        
        # Check greylist (no process data)
        if is_greylisted(module_type):
            skipped_count += 1
            continue
        
        # Get device descriptor
        descriptor_info = get_device_descriptor(module_type)
        if not descriptor_info:
            fail_count += 1
            continue
        
        # Extract descriptor details
        device_name = descriptor_info['name']
        device_id = descriptor_info['device_id']
        descriptor = descriptor_info['descriptor']
        version = descriptor_info['version']
        
        # Refresh kbus reference (important!)
        try:
            parent_device = projects.primary.find('Device', True)[0]
            kbus = parent_device.find('Kbus', True)[0]
        except:
            pass
        
        # Add module to K-Bus
        try:
            kbus.add(device_name, device_id, descriptor, version)
            success_count += 1
        except Exception as e:
            fail_count += 1
    
    return True

def get_device_descriptor(module_type):
    """
    Get device descriptor for WAGO module
    
    Args:
        module_type: Module identifier (e.g., "750-432")
    
    Returns:
        Dictionary with device_id, descriptor, version, name, description
        or None if not found
    """
    # Direct lookup
    if module_type in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[module_type]
    
    # Handle variants (e.g., 750-652#24)
    base_module = module_type.split('#')[0]
    if base_module in WAGO_DEVICE_DESCRIPTORS:
        return WAGO_DEVICE_DESCRIPTORS[base_module]
    
    # Fallback for 750-652 serial interface
    if base_module == "750-652":
        return WAGO_DEVICE_DESCRIPTORS.get("750-652#48")
    
    return None

# Device descriptor database
WAGO_DEVICE_DESCRIPTORS = {
    "750-402": {
        "device_id": 32776,
        "descriptor": "8401_0750040200000000",
        "version": "2.0.0.15",
        "name": "750-402",
        "description": "4DI 24 VDC 3ms"
    },
    "750-432": {
        "device_id": 32776,
        "descriptor": "8401_0750043200000000",
        "version": "2.0.0.11",
        "name": "750-432",
        "description": "4DI 24 VDC 3ms 2-wire"
    },
    # ... 14 more modules
}

MODULE_BLACKLIST = ["750-88", "750-89"]  # PLC devices
MODULE_GREYLIST = ["750-610", "750-614"]  # No process data
```

**6. Function Block Instantiation**

```python
def add_fb_instances_to_plc_prg(app, fb_instances):
    """
    Add function block instances to PLC_PRG
    
    Args:
        app: Application object
        fb_instances: List of FB configuration dictionaries
    
    Returns:
        True if successful, False otherwise
    """
    # Find PLC_PRG
    plc_prg_results = app.find("PLC_PRG", True)
    if not plc_prg_results:
        return False
    pou = plc_prg_results[0]
    
    var_block = []
    impl_block = []
    
    for fb_config in fb_instances:
        # Create FB code
        var_decl, fb_call = create_fb_instance_code(fb_config)
        
        var_block.append(var_decl)
        impl_block.append(fb_call)
    
    # Update PLC_PRG declaration
    if var_block:
        current_decl = pou.textual_declaration.text
        new_decl = current_decl + "\n\n(* FB Instances *)\n" + "\n".join(var_block)
        pou.textual_declaration.replace(new_decl)
    
    # Update PLC_PRG implementation
    if impl_block:
        current_impl = pou.textual_implementation.text
        new_impl = current_impl + "\n\n(* FB Calls *)\n" + "\n".join(impl_block)
        pou.textual_implementation.replace(new_impl)
    
    return True

def create_fb_instance_code(fb_config):
    """
    Create IEC code for function block instance
    
    Args:
        fb_config: Dictionary with fb_type, instance, params
    
    Returns:
        Tuple of (var_declaration, fb_call)
    """
    fb_type = fb_config.get("fb_type", "UNKNOWN")
    instance = fb_config.get("instance", "oInstance")
    params = fb_config.get("params", {})
    
    # VAR declaration
    var_declaration = f"{instance} : {fb_type};"
    
    # Build parameter list
    param_list = []
    for param_name, param_value in params.items():
        if param_value and param_value.strip():
            if param_name.endswith("=>"):
                # Output parameter
                param_name_clean = param_name[:-2].strip()
                param_list.append(f"{param_name_clean}=>{param_value}")
            else:
                # Input parameter
                param_list.append(f"{param_name}:={param_value}")
    
    # FB call
    if param_list:
        fb_call = f"{instance}({', '.join(param_list)});"
    else:
        fb_call = f"{instance}();"
    
    return var_declaration, fb_call
```

---

## 🔧 CODESYS ScriptEngine API Reference

### Project Management

```python
# Open existing project
proj = projects.open(filepath, None, True)

# Create project (unreliable - use template method instead)
# proj = projects.create(device_id, name)

# Find objects in project
results = proj.find(name, recursive=True)

# Get project children
children = proj.get_children(recursive=True)

# Save project
proj.save()

# Close project
proj.close()
```

### Application Management

```python
# Find Application
app = proj.find("Application", True)[0]

# Or use active application
app = proj.active_application

# Create POU
pou = app.create_pou(name, pou_type, None)

# Create GVL
gvl = app.create_gvl(name)

# Import XML
app.import_xml(conflict_mode, filepath, True)
```

### Library Management

```python
# Access repositories (DIRECT, not system.librarymanager)
repos = librarymanager.repositories

# Get all libraries in repository
libs = librarymanager.get_all_libraries(repo)

# Find Library Manager in application
for obj in app.get_children(recursive=True):
    if hasattr(obj, 'is_libman') and obj.is_libman:
        libman = obj
        break

# Add library
libman.add_library(library_object)
```

### Device Configuration

```python
# Find device
device = proj.find('Device', True)[0]

# Get gateway
gateway = online.gateways[0]

# Set IP address (requires gateway OBJECT, not string)
device.set_gateway_and_ip_address(gateway, ip_address)

# Find K-Bus
kbus = device.find('Kbus', True)[0]

# Add module to K-Bus
kbus.add(device_name, device_id, descriptor, version)
```

### POU Manipulation

```python
# Find PLC_PRG
pou = app.find("PLC_PRG", True)[0]

# Get/set declaration
current_decl = pou.textual_declaration.text
pou.textual_declaration.replace(new_declaration)

# Get/set implementation
current_impl = pou.textual_implementation.text
pou.textual_implementation.replace(new_implementation)
```

---

## 📊 Data Flow Diagram

```
┌──────────────────┐
│  project_config  │
│     .json        │
└────────┬─────────┘
         │
         ├─► libraries[]
         │   └─► Install via librarymanager
         │
         ├─► function_blocks[]
         │   └─► Add to PLC_PRG
         │
         └─► xml_imports{}
             └─► auto_detect.enabled?
                 ├─ YES: Scan exports folder
                 └─ NO: Use manual_files[]

┌──────────────────┐      ┌──────────────────┐
│  PLC_IO020       │      │  IO020_variables │
│   _config.json   │      │     .txt         │
└────────┬─────────┘      └────────┬─────────┘
         │                         │
         ├─► PLC_Info              ├─► VAR_GLOBAL block
         │   ├─ Name               │   ├─ Variable declarations
         │   ├─ IP_Address         │   └─ AT %IX/%QX addresses
         │   └─ Type               │
         │                         └─► Insert into GVL_IO020
         └─► IO_Modules[]
             └─► Add to K-Bus

┌──────────────────┐
│  XML Files       │
│  (exports/*.xml) │
└────────┬─────────┘
         │
         ├─► PLCopenXML (supported)
         ├─► Project XML (supported)
         └─► .export (NOT supported)
         │
         └─► Import to Application
             └─► POUs appear under Application node

                    ↓
              
┌─────────────────────────────────────┐
│  CODESYS Project (IO020.project)    │
├─────────────────────────────────────┤
│  Application                        │
│  ├─ Libraries (from repositories)   │
│  ├─ POUs (from XML imports)         │
│  ├─ PLC_PRG (with FB instances)     │
│  └─ GVL_IO020 (with variables)      │
│                                     │
│  Device (750-8210 @ 172.16.46.020)  │
│  └─ K-Bus                            │
│     ├─ 750-432 (4DI 24V DC)         │
│     ├─ 750-461 (2AI PT100)          │
│     └─ 750-515 (4RO Relay)          │
└─────────────────────────────────────┘
```

---

## 🔍 Common Patterns

### Error Handling

```python
try:
    # Attempt operation
    result = some_operation()
    
    if not result:
        log("Operation failed", "ERROR")
        return False
    
    log("Operation successful", "SUCCESS")
    return True

except AttributeError as e:
    # API method doesn't exist
    log(f"API method not available: {e}", "ERROR")
    return False

except Exception as e:
    # General error
    log(f"Unexpected error: {e}", "ERROR")
    import traceback
    traceback.print_exc()
    return False
```

### Logging Pattern

```python
def log(message, level="INFO"):
    """
    Log message to console and file
    
    Args:
        message: Log message
        level: INFO, SUCCESS, WARNING, ERROR, DEBUG
    """
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {message}"
    
    # Color-coded console output
    color = Colors.RESET
    if level == "ERROR":
        color = Colors.RED + Colors.BOLD
    elif level == "SUCCESS":
        color = Colors.GREEN + Colors.BOLD
    elif level == "WARNING":
        color = Colors.YELLOW
    
    print(f"{color}{log_entry}{Colors.RESET}")
    
    # Write to log file
    if LOG_FILE:
        with codecs.open(LOG_FILE, 'a', 'utf-8') as f:
            f.write(log_entry + '\n')
```

### Progress Tracking

```python
TOTAL_STEPS_PER_PROJECT = 13
CURRENT_STEP = 0

def log_step(description, total_steps=None):
    """
    Log step with progress indicator
    
    Args:
        description: Step description
        total_steps: Total steps for progress
    """
    global CURRENT_STEP
    CURRENT_STEP += 1
    
    log("")
    log("=" * 70)
    if total_steps:
        log(f"STEP {CURRENT_STEP}/{total_steps}: {description}")
    else:
        log(f"STEP {CURRENT_STEP}: {description}")
    log("=" * 70)
```

---

## 📝 Configuration File Schema

### project_config.json

```typescript
interface ProjectConfig {
  configuration: {
    description: string;
    version: string;
    namespace_mapping: {
      [libraryTitle: string]: string;  // Namespace
    };
  };
  
  libraries: {
    items: Array<{
      name: string;          // Display name
      vendor: string;        // "CODESYS", "WAGO", "3S"
      version: string|null;  // Specific or null for latest
      namespace: string;     // For FB references
      required: boolean;     // Fail if not found?
    }>;
  };
  
  function_blocks: {
    items: Array<{
      library: string;              // Library name
      library_namespace: string;    // Namespace
      fb_type: string;              // Fully qualified type
      instance: string;             // Variable name
      params: {                     // Parameter assignments
        [paramName: string]: string;
      };
      additional_code?: {           // Optional extra code
        declaration: string;
        implementation: string;
      };
    }>;
  };
  
  xml_imports: {
    auto_detect: {
      enabled: boolean;
      directory: string;
      pattern: string;
      exclude_patterns: string[];
      default_conflict_resolve: "replace"|"copy"|"skip";
      treat_all_as_optional: boolean;
    };
    manual_files: Array<{
      path: string;
      description: string;
      conflict_resolve: "replace"|"copy"|"skip";
      optional: boolean;
    }>;
  };
  
  import_settings: {
    default_conflict_resolve: "replace"|"copy"|"skip";
    save_after_import: boolean;
    continue_on_error: boolean;
  };
}
```

---

## 🔐 Security Considerations

### File System Access

- Script requires read access to input files
- Requires write access to project and log directories
- Template project should be read-only to prevent corruption

### Network Configuration

- IP configuration requires gateway discovery
- May expose network topology in logs
- Consider VPN for remote execution

### Credential Management

- No credentials stored in configuration files
- Library installation uses system repositories
- CODESYS must be properly licensed

---

## 🚀 Performance Optimization

### Template-Based Creation

**Before (projects.create):**
- Success rate: ~40%
- Duration: Variable (often fails)

**After (template copy):**
- Success rate: 100%
- Duration: ~0.5s per project

### Batch Processing

- Sequential processing: One project at a time
- No parallel execution (CODESYS limitation)
- Progress: 78 projects in ~6.5 minutes

### Optimization Tips

1. Pre-install libraries in CODESYS
2. Use SSD for project files
3. Disable antivirus scanning temporarily
4. Close CODESYS IDE during batch runs
5. Pre-configure template with common libraries

---

## 📚 Additional Resources

- **VERSION_HISTORY.md** - Complete changelog
- **DEPLOYMENT_GUIDE.md** - Setup and installation
- **PROGRAM_EXECUTION_FLOW.md** - Detailed process flow
- **README.md** - User guide and quick start

---

**Document Version:** 0.8.2  
**Last Updated:** 2024-12-11  
**Maintained By:** Alexander Fugmann  
**Repository:** https://github.com/WagoAlex/codesys-project-generator
