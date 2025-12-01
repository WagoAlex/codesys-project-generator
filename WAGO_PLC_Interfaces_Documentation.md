# WAGO PLC Configuration System - Interfaces & Methods

## ASCII Overview of Processing Flow

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
   │  JSON Files            │  PLC_IO043_config.json
   │  ─────────────         │  PLC_IO045_config.json
   │  PLC_Info             │  ...
   │  IO_Modules           │
   │  Statistics           │
   │  Metadata             │
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
   │  JSON Configuration    │  PLC_IO020_config.json
   │  + Variables File      │  IO020_variables.txt
   │  + Library Config      │  library_fb_config.json  ◄─── NEW!
   └────────┬───────────────┘
            │
            │ [parse_config_json(), parse_variables_file(), load_config_from_json()]
            ↓
   ┌────────────────────────────────┐
   │  create_codesys_project_       │
   │   enhanced.py V7.0             │
   │  ─────────────────────────────  │
   │  Step 1: Load JSON config      │  load_config_from_json()      ◄─── NEW!
   │  Step 2: Parse input files     │  parse_variables_file()
   │  Step 3: Load template         │  create_project_from_template()
   │  Step 4: Find application      │  find_or_create_application()
   │  Step 5: Install libraries     │  install_libraries_enhanced()  ◄─── NEW!
   │  Step 6: Find PLC device       │  find_plc_device()
   │  Step 7: Configure IP          │  configure_device_ip()
   │  Step 8: Configure Kbus        │  find_kbus()
   │  Step 9: Add IO modules        │  add_io_modules_to_kbus()
   │  Step 10: Update PLC_PRG       │  find_or_update_plc_prg()
   │  Step 11: Add FB instances     │  add_fb_instances_to_plc_prg() ◄─── NEW!
   │  Step 12: Create GVL           │  create_gvl_with_variables()
   │  Step 13: Save                 │  proj.save()
   └────────┬───────────────────────┘
            │
            │ [CODESYS ScriptEngine API]
            ↓
   ┌────────────────────────┐
   │  CODESYS Project       │  IO020.project
   │  ────────────────      │
   │  Application          │  → Logic container
   │  ├─ Libraries          │  → MQTT_Client_SL, JSON_Utilities_SL ◄─── NEW!
   │  └─ Device (PLC)       │  → 750-8210
   │     ├─ Kbus            │  → IO bus
   │     │  ├─ Module 1     │     750-432 (4DI)
   │     │  ├─ Module 2     │     750-554 (2AO)
   │     │  └─ ...          │
   │     └─ IP: 172.16.x.x  │
   │  PLC_PRG               │  → Main program
   │  ├─ VAR ... END_VAR    │  → FB instances              ◄─── NEW!
   │  └─ Implementation     │  → FB calls                  ◄─── NEW!
   │  GVL_IO020             │  → Global variables
   └────────────────────────┘
```

---

## Processing Sequence with Source References

### **Phase 1: Excel → JSON** (excel_to_json_converter.py)

| Step | Method | Purpose | Source |
|------|--------|---------|--------|
| 1 | `PLCConfigExtractor.__init__()` | Initialization, data structures | Line 16-26 |
| 2 | `extract_plcs_from_io_boxes()` | PLC data from sheet "IO-Boxen" | Line 92-224 |
| 3 | `extract_signals_from_signallist()` | Signals from sheet "SIGNALLIST" | Line 210-295 |
| 4 | `generate_json_files()` | Create JSON files | Line 297-328 |
| 5 | `generate_summary()` | Summary report | Line 330-362 |
| 6 | `generate_validation_report()` | Validation report | Line 364-388 |

### **Phase 2: JSON → CODESYS** (create_codesys_project_enhanced.py V7.0)

| Step | Method | Purpose | Source |
|------|--------|---------|--------|
| 1 | `load_config_from_json()` | Load library configuration | Line 180-230 |
| 2 | `parse_variables_file()` | Read variables file | Line ~256-283 |
| 3 | `parse_config_json()` | Parse JSON configuration | Line ~285-304 |
| 4 | `create_project_from_template()` | Project from template | Line ~384-428 |
| 5 | `find_or_create_application()` | Find/create application | Line ~430-475 |
| 6 | `install_libraries_enhanced()` | Install via Repository API | Line 232-413 |
| 7 | `find_plc_device()` | Locate PLC device | Line ~477-530 |
| 8 | `configure_device_ip()` | Configure IP address | Line ~557-606 |
| 9 | `find_kbus()` | Find Kbus object | Line ~608-643 |
| 10 | `add_io_modules_to_kbus()` | Add IO modules | Line ~645-731 |
| 11 | `find_or_update_plc_prg()` | Create/update PLC_PRG | Line ~736-776 |
| 12 | `add_fb_instances_to_plc_prg()` | Instantiate function blocks | Line 800-913 |
| 13 | `create_gvl_with_variables()` | GVL with variables | Line ~778-798 |

---

## Important Interfaces and Methods

### 1. Excel Processing (pandas)

#### **pandas.read_excel()**
**Purpose:** Read Excel sheets into DataFrame objects

**Why used:**
- Standard library for tabular data in Python
- Supports both old (.xls) and new (.xlsx) Excel formats
- Efficient processing of large datasets
- Flexible header detection

**Source:** `excel_to_json_converter.py`, Line 98-103

**Example:**
```python
# Header in row 4 (index 3)
df = pd.read_excel(self.excel_file, sheet_name='IO-Boxen', header=3)

# Alternative: Header in row 1 (index 0)
df = pd.read_excel(self.excel_file, sheet_name='SIGNALLIST', header=0)
```

**Use Case:**
```python
# Read sheet "IO-Boxen"
df = pd.read_excel('measuring_points.xls', sheet_name='IO-Boxen', header=3)
# Result: DataFrame with columns: IO BOX, Location, PLC, IP-Adress

# Read sheet "SIGNALLIST"
df = pd.read_excel('measuring_points.xls', sheet_name='SIGNALLIST', header=0)
# Result: DataFrame with columns: PLC, Mode_Type, PLC_terminal, Objektname
```

---

#### **DataFrame.iterrows()**
**Purpose:** Row-wise iteration over DataFrame

**Why used:**
- Enables sequential processing of each data row
- Access to row index and data
- Ideal for row-by-row validation

**Source:** `excel_to_json_converter.py`, Line 112, 226

**Example:**
```python
for idx, row in df.iterrows():
    plc_name = str(row['PLC']).strip()
    ip_address = str(row['IP-Adress']).strip()
    
    if not pd.isna(row.get('PLC')):
        # Process row
        process_plc(plc_name, ip_address)
```

---

### 2. JSON Processing (json)

#### **json.dump()**
**Purpose:** Serialization of Python objects to JSON files

**Why used:**
- Structured data storage for CODESYS import
- Human-readable format
- Standardized exchange format

**Source:** `excel_to_json_converter.py`, Line 322-323

**Example:**
```python
plc_data = {
    'PLC_Info': {
        'Name': 'IO043',
        'Type': '750-8210',
        'IP_Address': '172.16.60.043'
    },
    'IO_Modules': [...]
}

with open('PLC_IO043_config.json', 'w', encoding='utf-8') as f:
    json.dump(plc_data, f, indent=2, ensure_ascii=False)
```

**Output (PLC_IO043_config.json):**
```json
{
  "PLC_Info": {
    "Name": "IO043",
    "Type": "750-8210",
    "IP_Address": "172.16.60.043"
  },
  "IO_Modules": [
    {
      "Module_Type": "750-432",
      "Signals": [...]
    }
  ]
}
```

---

#### **json.load()**
**Purpose:** Deserialization of JSON files to Python objects

**Why used:**
- Loading generated configuration files
- Preparation for CODESYS import

**Source:** `create_codesys_project_enhanced.py`, Line ~291-293

**Example:**
```python
with open('PLC_IO020_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    
# Access data
plc_name = config['PLC_Info']['Name']  # "IO020"
ip_address = config['PLC_Info']['IP_Address']  # "172.16.60.020"
modules = config['IO_Modules']  # List of all IO modules
```

---

### 3. Data Validation (Regular Expressions)

#### **re.match() / re.search()**
**Purpose:** Pattern-based validation and extraction

**Why used:**
- IP address validation (RFC-compliant)
- PLC type detection (e.g., "750-8210")
- Flexible string processing

**Source:** `excel_to_json_converter.py`, Line 53-54, 84-88

**Examples:**

**IP Validation:**
```python
def validate_ip_address(self, ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, str(ip).strip())
    
    if match:
        octets = [int(x) for x in match.groups()]
        if all(0 <= o <= 255 for o in octets):
            return True, ip
    
    return False, "Invalid IP format"

# Example:
is_valid, result = validate_ip_address("172.16.60.043")
# Returns: (True, "172.16.60.043")
```

**PLC Type Extraction:**
```python
def extract_plc_type(self, module_type):
    pattern = r'(750-\d{3,4})'
    match = re.search(pattern, str(module_type))
    
    if match:
        return match.group(1)
    return None

# Example:
plc_type = extract_plc_type("750-8210/025-000")
# Returns: "750-8210"
```

---

### 4. CODESYS Library Management (NEW IN V7!)

#### **librarymanager.primary_repository**
**Purpose:** Access to CODESYS library repository for programmatic library installation

**Why used:**
- Automatic library installation without manual download
- Version management and dependency resolution
- Consistent library versions across projects

**Source:** `create_codesys_project_enhanced.py`, Line 242-252

**Example:**
```python
from scriptengine import librarymanager

# Access primary repository
repo = librarymanager.primary_repository

# Search for library
results = repo.search("MQTT_Client_SL", "CODESYS")

if results:
    placeholder = results[0]
    # Install library with dependencies
    placeholder.install()
    print("Installed: {0} v{1}".format(placeholder.name, placeholder.version))
```

---

#### **repo.search(library_name, vendor_name)**
**Purpose:** Search for libraries in CODESYS repository

**Why used:**
- Find specific library versions
- Verify library availability
- Automatic version resolution

**Source:** `create_codesys_project_enhanced.py`, Line 246-284

**Example:**
```python
def install_library_from_repository(app, lib_name, vendor_name, required):
    """Install library from CODESYS repository"""
    
    repo = librarymanager.primary_repository
    
    # Search with vendor filter
    results = repo.search(lib_name, vendor_name)
    
    if not results:
        log("Library not found: {0}".format(lib_name), "WARNING")
        return False
    
    # Take first (usually latest) version
    placeholder = results[0]
    
    # Install
    placeholder.install()
    
    log("Installed: {0} v{1}".format(
        placeholder.name, 
        placeholder.version
    ), "SUCCESS")
    
    return True

# Usage:
install_library_from_repository(app, "MQTT_Client_SL", "CODESYS", True)
```

---

#### **lib.name vs lib.title - CRITICAL DIFFERENCE!**
**Purpose:** Understanding CODESYS library namespace resolution

**Why critical:**
- Display title ≠ Internal namespace
- Using wrong name causes compilation errors
- Must use `lib.name` for namespace, not `lib.title`

**Source:** `create_codesys_project_enhanced.py`, Line 286-334

**Example:**
```python
# WRONG approach (causes errors):
library = app.get_library("MQTT_Client_SL")  # Display title
namespace = library.title  # "MQTT_Client_SL"
fb_type = "{0}.MqttClient".format(namespace)  # "MQTT_Client_SL.MqttClient" ❌

# CORRECT approach:
library = app.get_library("MQTT_Client_SL")  # Display title
namespace = library.name  # "MQTT" (actual namespace!)
fb_type = "{0}.MqttClient".format(namespace)  # "MQTT.MqttClient" ✅

# Real examples from WAGO libraries:
# Library Display Title → Internal Namespace
"MQTT_Client_SL"        → "MQTT"
"JSON_Utilities_SL"     → "JSON"
"WagoAppCloud"          → "WagoAppCloud"  (sometimes same)
"Standard"              → "Standard"
```

**Why this happens:**
```
CODESYS libraries have two identifiers:
1. Display Title (lib.title): User-friendly name shown in library manager
2. Internal Namespace (lib.name): Actual namespace used in code

The ScriptEngine API exposes both, but only lib.name is valid for
code generation and namespace resolution.
```

---

### 5. Function Block Instantiation (NEW IN V7!)

#### **add_fb_instances_to_plc_prg()**
**Purpose:** Programmatically instantiate function blocks in PLC_PRG

**Why used:**
- Automate repetitive FB instantiation
- Ensure consistent FB configuration
- Support complex library integrations

**Source:** `create_codesys_project_enhanced.py`, Line 800-913

**Critical Rules:**
1. **Declarations go in declaration section** (VAR...END_VAR)
2. **Calls go in implementation section** (program body)
3. **Use lib.name for namespace**, not lib.title
4. **Omit namespace prefix** - CODESYS resolves automatically

**Example:**
```python
def add_fb_instances_to_plc_prg(app, fb_instances):
    """
    Add function block instances to PLC_PRG
    
    fb_instances = [
        {
            "instance_name": "fbMqtt",
            "fb_type": "MQTT.MqttClient",
            "library": "MQTT_Client_SL"
        },
        {
            "instance_name": "fbJson",
            "fb_type": "JSON.JSONByteArrayParser",
            "library": "JSON_Utilities_SL"
        }
    ]
    """
    
    pou = app.find("PLC_PRG", False)
    if not pou:
        return
    
    # Build declaration section
    declarations = []
    for fb in fb_instances:
        # Format: instance_name : FB_Type;
        declarations.append("{0} : {1};".format(
            fb['instance_name'],
            fb['fb_type']
        ))
    
    # Current declaration
    current_decl = pou.textual_declaration.text
    
    # Add VAR section if not present
    if "VAR" not in current_decl:
        current_decl = "VAR\nEND_VAR\n" + current_decl
    
    # Insert declarations before END_VAR
    new_decl = current_decl.replace(
        "END_VAR",
        "\t{0}\nEND_VAR".format("\n\t".join(declarations))
    )
    
    pou.textual_declaration.replace(new_decl)
    
    # Build implementation (FB calls)
    current_impl = pou.textual_implementation.text
    
    # Add FB calls
    for fb in fb_instances:
        call = "{0}();".format(fb['instance_name'])
        if call not in current_impl:
            current_impl += "\n{0}".format(call)
    
    pou.textual_implementation.replace(current_impl)
```

**Generated Code:**

```iec61131-3
PROGRAM PLC_PRG
VAR
    fbMqtt : MQTT.MqttClient;
    fbJson : JSON.JSONByteArrayParser;
END_VAR

// Implementation
fbMqtt();
fbJson();
```

---

### 6. CODESYS ScriptEngine API

#### **projects.open()**
**Purpose:** Open existing CODESYS project

**Example:**
```python
from scriptengine import projects

# Open project
proj = projects.open(r"C:\Projects\IO020.project")

# Access project objects
app = proj.active_application
device = proj.find("Device", recursive=True)

# Save and close
proj.save()
proj.close()
```

---

#### **kbus.add(device_name, device_id, descriptor, version)**
**Purpose:** Add IO module to Kbus (CORE FUNCTION!)

**Source:** `create_codesys_project_enhanced.py`, Line ~700-720

**Example:**
```python
# Get descriptor info
descriptor_info = WAGO_DEVICE_DESCRIPTORS["750-432"]

# Add module to Kbus
kbus.add(
    descriptor_info['name'],        # "750-432"
    descriptor_info['device_id'],   # 32776
    descriptor_info['descriptor'],  # "8401_0750043200000000"
    descriptor_info['version']      # "2.0.0.11"
)
```

**Why these parameters:**
```
device_name:  Human-readable identifier
device_id:    CODESYS internal device type (usually 32776 for WAGO)
descriptor:   XML device descriptor string (unique per module/PD size)
version:      Must match installed WAGO device description package
```

---

#### **pou.textual_declaration / pou.textual_implementation**
**Purpose:** Access and modify POU declaration and implementation sections

**Source:** `create_codesys_project_enhanced.py`, Line 866-913

**Example:**
```python
pou = app.find("PLC_PRG", False)

# Read current declaration
current_decl = pou.textual_declaration.text

# Modify declaration
new_decl = current_decl.replace(
    "END_VAR",
    "\tfbMqtt : MQTT.MqttClient;\nEND_VAR"
)
pou.textual_declaration.replace(new_decl)

# Read current implementation
current_impl = pou.textual_implementation.text

# Add code
new_impl = current_impl + "\nfbMqtt();"
pou.textual_implementation.replace(new_impl)
```

---

### 7. File System Operations (glob, os)

#### **glob.glob()**
**Purpose:** File pattern matching for batch processing

**Example:**
```python
import glob

# Find all variable files
var_files = glob.glob(r"D:\outputs\IO*_variables.txt")
# Returns: ['IO020_variables.txt', 'IO021_variables.txt', ...]

# Find all config files
config_files = glob.glob(r"D:\outputs\PLC_IO*_config.json")
# Returns: ['PLC_IO020_config.json', 'PLC_IO021_config.json', ...]
```

---

#### **os.path operations**
**Purpose:** Path manipulation and validation

**Example:**
```python
import os

# Check if file exists
if os.path.exists(template_path):
    print("Template found")

# Get directory
script_dir = os.path.dirname(__file__)

# Join paths
output_path = os.path.join(script_dir, "outputs", "project.json")

# Get absolute path
abs_path = os.path.abspath("relative/path/file.txt")
```

---

## Practical Examples

### Example 1: Complete Excel → CODESYS Workflow

**Input: Excel File**
```
Sheet "IO-Boxen":
┌──────────┬──────────┬─────┬────────────────┐
│ IO BOX   │ Location │ PLC │ IP-Adress      │
├──────────┼──────────┼─────┼────────────────┤
│ 36140310 │ I A 3    │ IO043│ 172.16.60.043 │
└──────────┴──────────┴─────┴────────────────┘

Sheet "SIGNALLIST":
┌─────┬──────────┬─────────────┬──────────────────────┬──────┬────────┐
│ PLC │ Mode_Type│ PLC_terminal│ Objektname           │ Type │ Signal │
├─────┼──────────┼─────────────┼──────────────────────┼──────┼────────┤
│IO043│ 750-432  │ IX 65.3-A3.5│ I0001_Me_MnCoolAlrm │ I    │ NC     │
│IO043│ 750-554  │ QW 3-A5.2   │ O0001_So_ETPOIn     │ O    │ 4-20mA │
└─────┴──────────┴─────────────┴──────────────────────┴──────┴────────┘
```

**Step 1: PLCConfigExtractor**
```python
extractor = PLCConfigExtractor('measuring_points.xls')

# 1.1 Extract PLCs
extractor.extract_plcs_from_io_boxes()
# → self.plcs['IO043'] = {
#     'PLC_Info': {'Name': 'IO043', 'IP_Address': '172.16.60.043', ...}
#   }

# 1.2 Extract Signals
extractor.extract_signals_from_signallist()
# → self.plcs['IO043']['IO_Modules']['750-432'] = {
#     'Module_Type': '750-432',
#     'Signals': [{'Terminal': 'IX 65.3-A3.5', ...}]
#   }

# 1.3 Generate JSON
extractor.generate_json_files('./output')
```

**Output: PLC_IO043_config.json**
```json
{
  "PLC_Info": {
    "Name": "IO043",
    "Type": "750-8210",
    "IP_Address": "172.16.60.043",
    "Location": "I A 3"
  },
  "IO_Modules": [
    {
      "Module_Type": "750-432",
      "Signals": [
        {
          "Terminal": "IX 65.3-A3.5",
          "Object_Name": "I0001_Me_MnCoolAlrm",
          "Signal_Type": "I",
          "Signal": "NC"
        }
      ]
    },
    {
      "Module_Type": "750-554",
      "Signals": [
        {
          "Terminal": "QW 3-A5.2",
          "Object_Name": "O0001_So_ETPOIn",
          "Signal_Type": "O",
          "Signal": "4-20mA"
        }
      ]
    }
  ]
}
```

**Step 2: Create CODESYS Project**
```python
# 2.1 Load configurations
config = parse_config_json('PLC_IO043_config.json')
var_block = parse_variables_file('IO043_variables.txt')
libs, fbs, settings = load_config_from_json('library_fb_config.json')  # NEW!

# 2.2 Project from template
proj = create_project_from_template('IO043', './projects', 'TEMPLATE.project')

# 2.3 Install libraries
install_libraries_enhanced(proj, app, libs)  # NEW!

# 2.4 Configure device
device = find_plc_device(proj)
configure_device_ip(proj, device, '172.16.60.043')

# 2.5 Fill Kbus with modules
kbus = find_kbus(device)
for module in config['IO_Modules']:
    module_type = module['Module_Type']
    descriptor = WAGO_DEVICE_DESCRIPTORS[module_type]
    kbus.add(descriptor['name'], descriptor['device_id'], 
             descriptor['descriptor'], descriptor['version'])

# 2.6 Instantiate function blocks
add_fb_instances_to_plc_prg(app, fbs)  # NEW!

# 2.7 Create GVL
app = find_or_create_application(proj)
gvl = create_gvl_with_variables(app, 'GVL_IO043', var_block)

# 2.8 Save
proj.save()
proj.close()
```

**Result: IO043.project**
```
Application
  ├─ Libraries  (NEW!)
  │   ├─ MQTT_Client_SL
  │   └─ JSON_Utilities_SL
  ├─ Device: 750-8210 (172.16.60.043)
  │   └─ Kbus
  │       ├─ 750-432 (4DI 24VDC)
  │       └─ 750-554 (2AO 4-20mA)
  ├─ PLC_PRG  (ENHANCED!)
  │   ├─ VAR
  │   │   ├─ fbMqtt : MQTT.MqttClient;
  │   │   └─ fbJson : JSON.JSONByteArrayParser;
  │   └─ Implementation
  │       ├─ fbMqtt();
  │       └─ fbJson();
  └─ GVL_IO043
      ├─ I0001_Me_MnCoolAlrm AT %IX65.3 : BOOL;
      └─ O0001_So_ETPOIn AT %QW3 : WORD;
```

---

### Example 2: Batch Processing Multiple PLCs

**Command Line Invocation:**
```bash
python batch_processor.py --input=measuring_points.xls --output=./configs
```

**Workflow:**
```python
# 1. Parse arguments
args = parse_arguments()
input_file = args.input   # "measuring_points.xls"
output_dir = args.output  # "./configs"

# 2. Initialize extractor
extractor = PLCConfigExtractor(input_file)

# 3. Processing
extractor.process(output_dir)
# → Output:
#   ./configs/PLC_IO020_config.json
#   ./configs/PLC_IO043_config.json
#   ./configs/PLC_IO045_config.json
#   ./configs/summary.txt
#   ./configs/validation_report.txt

# 4. Create CODESYS projects (Auto-detect mode)
var_files = find_all_files(output_dir, "IO*_variables.txt")
config_files = find_all_files(output_dir, "PLC_IO*_config.json")
matched_pairs = match_files(var_files, config_files)

for var_file, config_file, plc_id in matched_pairs:
    create_single_project(var_file, config_file, plc_id)
```

**Result:**
```
./configs/
  ├─ PLC_IO020_config.json
  ├─ PLC_IO043_config.json
  ├─ PLC_IO045_config.json
  ├─ summary.txt
  └─ validation_report.txt

./projects/
  ├─ IO020.project
  ├─ IO043.project
  └─ IO045.project
```

---

## Special Design Decisions

### 1. Device Descriptor Mapping
**Source:** `create_codesys_project_enhanced.py`, Line 78-95

**Why:**
- CODESYS requires exact device IDs and descriptor strings
- Hardcoding avoids runtime errors from wrong IDs
- Version numbers must match installed XML files

**Structure:**
```python
WAGO_DEVICE_DESCRIPTORS = {
    "750-432": {
        "device_id": 32776,
        "descriptor": "8401_0750043200000000",
        "version": "2.0.0.11",
        "name": "750-432",
        "description": "4DI 24 VDC 3ms 2-wire"
    }
}
```

---

### 2. Template-based Project Creation
**Source:** `create_codesys_project_enhanced.py`, Line ~384-428

**Why:**
- Faster project creation (copy template instead of create from scratch)
- Pre-configuration (standard settings, libraries)
- Consistency across all projects

**Alternative:**
```python
# Without template (slow, complex)
proj = proj_mgr.create_project("IO020.project", "Standard")
proj.add_library("Standard.library")
app = proj.create_application()
device = app.add_device("WAGO 750-8210")
# ... many more configuration steps

# With template (fast, simple)
template = proj_mgr.open_project("TEMPLATE.project")
proj = proj_mgr.save_as(template, "IO020.project")
# Template already contains: Libraries, Device, Kbus, Standard POUs
```

---

### 3. Blacklist/Greylist for Modules
**Source:** `create_codesys_project_enhanced.py`, Line 97-98

**Why:**
- PLCs (750-88x) are not IO modules
- Power supplies (750-610) have no process data

**Implementation:**
```python
MODULE_BLACKLIST = ["750-88", "750-89"]  # Don't add
MODULE_GREYLIST = ["750-610", "750-614"]  # Skip but log

if any(module_type.startswith(bl) for bl in MODULE_BLACKLIST):
    log("PLC device skipped", "WARNING")
    continue

if module_type in MODULE_GREYLIST:
    log("No process data - skipped", "INFO")
    continue
```

---

### 4. Library Repository API (NEW IN V7!)
**Source:** `create_codesys_project_enhanced.py`, Line 232-413

**Why:**
- Eliminates manual library download/installation
- Automatic version management
- Dependency resolution
- Consistent library versions across projects

**Before (V5):**
```python
# Manual approach - NOT RELIABLE
# 1. Download .library file manually
# 2. Import via GUI
# 3. Hope version matches
# 4. No dependency resolution
```

**After (V7):**
```python
# Automated approach - RELIABLE
repo = librarymanager.primary_repository
results = repo.search("MQTT_Client_SL", "CODESYS")
if results:
    results[0].install()  # Automatic dependencies!
```

---

### 5. FB Instantiation in Implementation (NEW IN V7!)
**Source:** `create_codesys_project_enhanced.py`, Line 800-913

**Why:**
- IEC 61131-3 compliance
- Declarations belong in VAR section
- Executable code belongs in implementation
- Prevents compiler errors

**Wrong (V5 and earlier):**
```iec61131-3
VAR
    fbMqtt : MQTT.MqttClient;
    fbMqtt();  // ❌ Executable code in declaration!
END_VAR
```

**Correct (V7):**
```iec61131-3
VAR
    fbMqtt : MQTT.MqttClient;
END_VAR

// Implementation section
fbMqtt();  // ✅ Executable code in implementation!
```

---

## Summary

The WAGO PLC Configuration System uses a **two-phase architecture**:

**Phase 1 (Python):**
- Excel → JSON conversion with pandas
- Data validation with RegEx
- Structured output (JSON, TXT)

**Phase 2 (IronPython/CODESYS):**
- JSON → CODESYS project
- Template-based creation
- CODESYS ScriptEngine API
- Automatic IO configuration
- **NEW:** Library installation via Repository API
- **NEW:** Function block instantiation

**Core Technologies:**
- **pandas**: Excel processing
- **json**: Data serialization
- **re**: Data validation
- **CODESYS ScriptEngine**: Project automation
- **CODESYS librarymanager**: Library management (V7)
- **glob/os**: File management

**Advantages:**
- Automation of repetitive tasks
- Error reduction through validation
- Consistent project structure
- Scalability (5+ PLCs simultaneously)
- Traceability through logging
- **NEW:** Automatic library management
- **NEW:** Professional FB integration

**Key Innovations V7:**
- Repository API for libraries (no manual download)
- Proper FB instantiation (declaration + implementation)
- Namespace resolution via lib.name (not lib.title)
- External JSON configuration for libraries and FBs

---

## Known Issues and Improvements

### ❌ Issues Encountered During Development

#### 1. Device Descriptor Problem
**Issue:** Creating WAGO devices from scratch via ScriptEngine API failed
```python
# This approach NEVER worked:
device = app.create_device(
    "WAGO 750-8210",
    "750-8210",
    "WAGO 750-8210/025-000"
)
# Error: Device creation not supported via API
```

**Solution:** Template-based approach
```python
# Use pre-configured template instead
template = open_project("TEMPLATE_WAGO_750-8210.project")
proj = save_as(template, "IO020.project")
```

**Why this happened:**
- ScriptEngine API has limited device creation capabilities
- Device descriptor format is undocumented
- WAGO device packages must be pre-installed
- Template approach is more reliable

---

#### 2. IP Address Configuration Problem
**Issue:** Setting IP address programmatically often fails
```python
# These attempts frequently failed:
device.ip_address = "172.16.60.043"  # ❌
gateway.set_parameter("IP", "172.16.60.043")  # ❌
ethernet_interface.set_ip("172.16.60.043")  # ❌
```

**Workaround:** Log warning and manual configuration
```python
log("IP configuration via API unreliable", "WARNING")
log("Please configure IP manually: 172.16.60.043")
```

**Why this happened:**
- CODESYS uses complex internal structures for IP configuration
- Gateway/interface objects vary by device type
- ScriptEngine API doesn't expose all necessary methods

---

#### 3. Library Namespace Confusion
**Issue:** Using library display title instead of internal namespace
```python
# WRONG - caused compilation errors in V5:
library = app.get_library("MQTT_Client_SL")
namespace = library.title  # "MQTT_Client_SL"
fb_type = "{0}.MqttClient".format(namespace)  
# Result: "MQTT_Client_SL.MqttClient" ❌

# CORRECT - V7 approach:
namespace = library.name  # "MQTT"
fb_type = "{0}.MqttClient".format(namespace)
# Result: "MQTT.MqttClient" ✅
```

**Solution:** Always use `lib.name`, never `lib.title`

**Why this happened:**
- CODESYS separates display names from internal identifiers
- Documentation doesn't clearly explain this difference
- Trial and error revealed the correct approach

---

### ✅ What Could Be Improved

#### 1. Direct Device Creation
**Current limitation:** Must use template with pre-configured device

**Potential improvement:**
```python
# Ideal (but doesn't work yet):
device = device_manager.create_from_descriptor(
    descriptor="88XX_0750821000250000",
    version="3.5.19.30"
)
```

**Blockers:**
- Device descriptor format is proprietary
- ScriptEngine doesn't expose device creation API
- Would require CODESYS vendor support

---

#### 2. IP Configuration Reliability
**Current limitation:** IP configuration often fails, requires manual setup

**Potential improvement:**
```python
# More reliable method (if API was enhanced):
device.network_config.set_static_ip(
    ip="172.16.60.043",
    subnet="255.255.0.0",
    gateway="172.16.0.1"
)
```

**Blockers:**
- Current API is incomplete
- Different device types have different configuration methods
- Would require CODESYS API enhancement

---

#### 3. Dynamic Device Descriptor Lookup
**Current limitation:** Hardcoded device descriptor dictionary

**Potential improvement:**
```python
# Read descriptors from WAGO XML files dynamically:
descriptor_db = WagoDescriptorDatabase(
    xml_path=r"C:\Program Files\WAGO Software\CODESYS\DeviceDescriptions"
)

descriptor = descriptor_db.get_descriptor(
    module="750-432",
    process_data_bytes=4,
    version="latest"
)
```

**Blockers:**
- XML parsing complexity
- Version compatibility issues
- Current hardcoded approach is reliable and fast

---

#### 4. Validation Pre-Processing
**Current limitation:** Some errors only discovered during CODESYS project creation

**Potential improvement:**
```python
# Validate JSON before processing:
validator = ProjectValidator()
issues = validator.validate_config(config_json)

if issues:
    print("Issues found:")
    for issue in issues:
        print(f"  - {issue.level}: {issue.message}")
    
    if any(i.level == "ERROR" for i in issues):
        print("Cannot proceed with errors")
        sys.exit(1)
```

**Benefits:**
- Faster feedback loop
- Better error messages
- Avoid partial project creation

---

#### 5. Parallel Processing
**Current limitation:** Sequential processing (78 projects = 2.5 minutes)

**Potential improvement:**
```python
# Process multiple projects in parallel:
from multiprocessing import Pool

with Pool(processes=4) as pool:
    results = pool.map(create_single_project, matched_pairs)

# Potential speedup: 2.5 min → 40 seconds
```

**Blockers:**
- CODESYS ScriptEngine may not be thread-safe
- File locking issues
- Needs thorough testing

---

### 📊 Performance Analysis - What Takes Time?

```
Total time per project: ~2 seconds

Breakdown:
├─ Kbus.add(): 1.0s (50%)  ◄─── Bottleneck (CODESYS internal)
├─ Template copy: 0.2s (10%)
├─ GVL creation: 0.2s (10%)
├─ Project save: 0.2s (10%)
├─ Library install: 0.15s (7.5%)
└─ Other operations: 0.25s (12.5%)

Optimization potential:
✅ Reduced descriptor lookup attempts (V4: 20 → V7: 1)
✅ Eliminated failed device creation attempts
⚠️ Kbus.add() is CODESYS-internal (cannot optimize)
🔍 Template copy could be cached in memory
🔍 Library installation could be done once per batch
```

---

### 🎯 Recommendations for Future Development

1. **Contact CODESYS Support** for device creation API documentation
2. **Implement validation framework** before project creation
3. **Cache template** in memory for faster batch processing
4. **Explore parallel processing** if CODESYS allows it
5. **Create descriptor database** from XML files (if feasible)
6. **Add rollback mechanism** for failed project creation
7. **Implement project comparison** to verify correctness
8. **Add unit tests** for critical functions

---

**Document Version:** 2.0  
**Created:** 2025-01-15  
**Updated:** 2025-11-21  
**Based on:** create_codesys_project_enhanced.py V7.0, excel_to_json_converter.py, batch_processor.py
