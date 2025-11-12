# WAGO PLC Configuration Toolchain

**Automatisierte Extraktion, Konvertierung und CODESYS-Integration von PLC-Konfigurationen**

Version: 2.0  
Letztes Update: November 2025

---

## 📋 Inhaltsverzeichnis

- [Genereller Überblick](#-genereller-überblick)
  - [Was ist dieses Projekt?](#was-ist-dieses-projekt)
  - [Hauptfunktionen](#hauptfunktionen)
  - [Wer sollte dieses Tool verwenden?](#wer-sollte-dieses-tool-verwenden)
- [Architektonischer Überblick & Nutzungsanleitung](#-architektonischer-überblick--nutzungsanleitung)
  - [System-Architektur](#system-architektur)
  - [Workflow-Diagramm](#workflow-diagramm)
  - [Schnellstart](#schnellstart)
  - [Detaillierte Nutzungsanleitung](#detaillierte-nutzungsanleitung)
- [Entwickler-Dokumentation](#-entwickler-dokumentation)
  - [Projekt-Struktur](#projekt-struktur)
  - [Komponenten-Details](#komponenten-details)
  - [Datenfluss & Schnittstellen](#datenfluss--schnittstellen)
  - [Erweiterung & Anpassung](#erweiterung--anpassung)

---

## 🎯 Genereller Überblick

### Was ist dieses Projekt?

Die **WAGO PLC Configuration Toolchain** ist eine umfassende Automatisierungslösung für die Verwaltung und Integration von WAGO PLC-Konfigurationen. Sie transformiert Excel-basierte Messpunktlisten in strukturierte JSON-Konfigurationen und CODESYS-kompatible Projektdateien.

#### Problemstellung

In industriellen Automatisierungsprojekten werden PLC-Konfigurationen oft in Excel-Dokumenten verwaltet:
- Hunderte bis Tausende von I/O-Signalen pro Projekt
- Manuelle Übertragung in CODESYS ist fehleranfällig und zeitaufwendig
- Keine zentrale Versionskontrolle oder Validierung
- Schwierige Nachvollziehbarkeit von Änderungen

#### Lösung

Diese Toolchain automatisiert den kompletten Workflow:
1. **Extraktion**: Liest strukturierte Daten aus Excel-Dateien
2. **Validierung**: Prüft IP-Adressen, Moduldefinitionen und Signalkonsistenz
3. **Transformation**: Generiert JSON-Konfigurationen und IEC 61131-3 Variablenlisten
4. **Integration**: Erstellt vollständige CODESYS-Projekte via IronPython ScriptEngine

### Hauptfunktionen

#### ✅ Excel-zu-JSON-Konvertierung
- Automatische Erkennung von bis zu 5 PLCs pro Projekt
- Extraktion von I/O-Modulkonfigurationen (750-4xx, 750-5xx, 750-6xx)
- Validierung von IP-Adressen (172.16.46.x, 172.16.60.x)
- Generierung strukturierter JSON-Dateien

#### ✅ CODESYS-Integration
- Automatische Projekterstellung aus Template
- Konfiguration der K-Bus I/O-Module
- Import von Variablenlisten (IEC 61131-3 Standard)
- IP-Adress-Konfiguration der PLC-Devices

#### ✅ Qualitätssicherung
- Umfassende Validierungsberichte
- Warnungen bei ungültigen Einträgen
- Statistiken pro PLC (Module, Signale, I/O-Typen)
- Logging aller Verarbeitungsschritte

### Wer sollte dieses Tool verwenden?

#### 🎯 Zielgruppen

**Automatisierungsingenieure**
- Erstellen von PLC-Projekten aus Anlagendokumentation
- Schnelle Integration neuer I/O-Konfigurationen
- Konsistente Projekt-Strukturen

**Systemintegratoren**
- Batch-Verarbeitung mehrerer PLCs
- Standardisierte Projektvorlagen
- Dokumentation und Nachverfolgbarkeit

**Projektmanager**
- Überblick über Projekt-Umfang (Anzahl Signale, Module)
- Validierung von Planungsdaten
- Qualitätssicherung vor Inbetriebnahme

---

## 🏗️ Architektonischer Überblick & Nutzungsanleitung

### System-Architektur

```
┌─────────────────────────────────────────────────────────────────┐
│                         INPUT LAYER                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Excel-Datei: LIST_OF_MEASURING_POINTS.xls              │   │
│  │  ┌──────────────┬──────────────┬───────────────────┐    │   │
│  │  │  IO-Boxen    │  SIGNALLIST  │  LOCATION/LEGEND │    │   │
│  │  │  (PLC-Info)  │  (Signale)   │  (Metadaten)     │    │   │
│  │  └──────────────┴──────────────┴───────────────────┘    │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  batch_processor.py                                      │   │
│  │  ├─► excel_to_json_converter.py (PLCConfigExtractor)    │   │
│  │  │   ├─► Extract PLCs (IO-Boxen Sheet)                  │   │
│  │  │   ├─► Extract Signals (SIGNALLIST Sheet)             │   │
│  │  │   ├─► Validate IP Addresses                          │   │
│  │  │   ├─► Group by Module Type                           │   │
│  │  │   └─► Calculate Statistics                           │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT LAYER                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  JSON Configurations                                     │   │
│  │  ├─► PLC_IO020_config.json                              │   │
│  │  ├─► PLC_IO043_config.json                              │   │
│  │  └─► PLC_IO251_config.json                              │   │
│  │                                                          │   │
│  │  IEC 61131-3 Variable Lists                             │   │
│  │  ├─► IO020_variables.txt                                │   │
│  │  ├─► IO043_variables.txt                                │   │
│  │  └─► IO251_variables.txt                                │   │
│  │                                                          │   │
│  │  Reports                                                 │   │
│  │  ├─► summary.txt                                        │   │
│  │  └─► validation_report.txt                              │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CODESYS INTEGRATION LAYER                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  create_codesys_project.py (IronPython)                 │   │
│  │  ├─► Load Template Project (TEMPLATE_WAGO_750-8210)     │   │
│  │  ├─► Configure PLC Device (750-8210)                    │   │
│  │  ├─► Add K-Bus I/O Modules                              │   │
│  │  ├─► Import Variables (GVL)                             │   │
│  │  ├─► Set IP Address                                     │   │
│  │  └─► Save CODESYS Project                               │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                         FINAL OUTPUT                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  CODESYS Projects (.project)                            │   │
│  │  ├─► IO020.project                                      │   │
│  │  ├─► IO043.project                                      │   │
│  │  └─► IO251.project                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Workflow-Diagramm

```
START
  │
  ├──► [1] Excel-Datei bereitstellen
  │     ├─ Prüfe Sheets: IO-Boxen, SIGNALLIST
  │     └─ Validiere Struktur (Header-Zeilen)
  │
  ├──► [2] Batch-Verarbeitung starten
  │     └─ python batch_processor.py --input=file.xls --output=./output
  │
  ├──► [3] Extraktion & Validierung
  │     ├─ Parse IO-Boxen (PLCs, IP-Adressen)
  │     ├─ Parse SIGNALLIST (Signale, Module)
  │     ├─ Validiere IP-Adressen
  │     └─ Gruppiere nach PLC & Modultyp
  │
  ├──► [4] JSON-Generierung
  │     ├─ PLC_IO020_config.json
  │     ├─ PLC_IO043_config.json
  │     ├─ summary.txt
  │     └─ validation_report.txt
  │
  ├──► [5] Variablenlisten-Generierung
  │     └─ python codesys_import_example.py --input=./output
  │
  ├──► [6] CODESYS-Projekt-Erstellung (optional)
  │     ├─ Öffne CODESYS mit ScriptEngine
  │     ├─ Führe create_codesys_project.py aus
  │     └─ Generiere .project Dateien
  │
  └──► [7] Qualitätsprüfung
        ├─ Überprüfe validation_report.txt
        ├─ Kontrolliere Statistiken
        └─ Teste CODESYS-Import
  │
END
```

### Schnellstart

#### Voraussetzungen

**Python-Umgebung:**
```bash
Python 3.8+
pandas >= 1.5.0
openpyxl >= 3.0.0  # Für .xlsx Support
xlrd >= 2.0.0      # Für .xls Support
```

**CODESYS (optional für Projekt-Generierung):**
```
CODESYS V3.5 SP19+
WAGO PFC200 Device Description
IronPython ScriptEngine aktiviert
```

#### Installation

```bash
# 1. Repository klonen
git clone <repository-url>
cd wago-plc-config-toolchain

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. Verzeichnisstruktur erstellen
mkdir -p input output projects
```

#### Erste Schritte

**Schritt 1: Excel-Datei vorbereiten**
```bash
# Kopiere deine Excel-Datei ins input-Verzeichnis
cp /path/to/LIST_OF_MEASURING_POINTS.xls ./input/
```

**Schritt 2: Batch-Verarbeitung starten**
```bash
python batch_processor.py \
  --input=./input/LIST_OF_MEASURING_POINTS.xls \
  --output=./output
```

**Schritt 3: Ergebnisse prüfen**
```bash
# Übersicht anzeigen
cat ./output/summary.txt

# Validierungsbericht prüfen
cat ./output/validation_report.txt

# JSON-Dateien ansehen
ls -lh ./output/*.json
```

**Schritt 4: Variablenlisten generieren**
```bash
python codesys_import_example.py \
  --input=./output
```

### Detaillierte Nutzungsanleitung

#### Excel-Dateiformat

##### Sheet: "IO-Boxen"
Header in **Zeile 4**, Daten ab **Zeile 5**:

| Spalte | Bezeichnung | Beschreibung | Beispiel |
|--------|-------------|--------------|----------|
| 1 | IO BOX | Box-Nummer | 36140310.0 |
| 2 | Location | Standort | I A 3 |
| 3 | PLC | PLC-Name | IO043 |
| 6 | IP-Adress | IP-Adresse | 172.16.60.043 |

##### Sheet: "SIGNALLIST"
Header in **Zeile 1**, Daten ab **Zeile 2**:

| Spalte | Bezeichnung | Beschreibung | Beispiel |
|--------|-------------|--------------|----------|
| 5 | PLC | PLC-Zuordnung | IO045 |
| 6 | Type | Signal-Typ | I (Input) / O (Output) |
| 11 | Signal | Signalart | NC / 4-20mA / 24V DC |
| 62 | Mode_Type | IO-Modultyp | 750-432 / 750-554 |
| 69 | PLC_terminal | Terminal-Adresse | IX 65.3 -A3.5 |
| 72 | Objektname | Signalname | I0001_Me_MnCoolCmnAlrm |

#### Kommandozeilen-Optionen

##### batch_processor.py

```bash
python batch_processor.py [OPTIONS]

Optionen:
  --input PATH   (erforderlich)  Pfad zur Excel-Datei
  --output PATH  (erforderlich)  Pfad zum Ausgabeverzeichnis

Beispiele:
  # Einfache Verarbeitung
  python batch_processor.py --input=data.xls --output=./configs
  
  # Mit absoluten Pfaden
  python batch_processor.py \
    --input=/home/user/data/measuring_points.xls \
    --output=/home/user/output/configs
```

##### codesys_import_example.py

```bash
python codesys_import_example.py [OPTIONS]

Optionen:
  --input PATH  (erforderlich)  Verzeichnis mit JSON-Konfigurationen
  --plc NAME    (optional)      Spezifische PLC (z.B. IO251)

Beispiele:
  # Alle PLCs verarbeiten
  python codesys_import_example.py --input=./output
  
  # Nur eine spezifische PLC
  python codesys_import_example.py --input=./output --plc=IO020
```

##### create_codesys_project.py

```bash
# Muss in CODESYS ScriptEngine ausgeführt werden
# Konfiguration in Datei anpassen:

AUTO_DETECT_MODE = True  # Findet automatisch alle IO*_variables.txt
DEFAULT_PROJECT_PATH = r"D:\WAGO\CODESYS\projects"
DEFAULT_VARIABLES_PATH = r"D:\WAGO\CODESYS\outputs"
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210.project"
```

#### Output-Dateien

##### JSON-Konfiguration (PLC_IO043_config.json)

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

##### Variablenliste (IO043_variables.txt)

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

##### Summary-Report (summary.txt)

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

##### Validierungs-Report (validation_report.txt)

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

#### Fehlerbehebung

##### Problem: "No PLC configuration files found"
```bash
# Lösung 1: Prüfe Dateinamenmuster
ls ./output/PLC_*_config.json

# Lösung 2: Prüfe Berechtigungen
chmod -R 755 ./output

# Lösung 3: Führe Batch-Prozessor erneut aus
python batch_processor.py --input=data.xls --output=./output
```

##### Problem: "Invalid IP address format"
```python
# In validation_report.txt nachsehen:
cat ./output/validation_report.txt | grep "IP"

# Gültige IP-Bereiche:
# - 172.16.46.020 - 172.16.46.251
# - 172.16.60.001 - 172.16.60.255
```

##### Problem: "Module 750-XXX not found"
```python
# Verfügbare Module prüfen in create_codesys_project.py:
# WAGO_DEVICE_DESCRIPTORS Dictionary

# Unterstützte Module (Beispiele):
# - 750-402, 750-430, 750-432 (Digital Input)
# - 750-517, 750-530, 750-554 (Analog Output)
# - 750-610, 750-652 (Serielle Kommunikation)
```

---

## 👨‍💻 Entwickler-Dokumentation

### Projekt-Struktur

```
wago-plc-config-toolchain/
│
├── batch_processor.py              # CLI-Wrapper für Excel-Verarbeitung
├── excel_to_json_converter.py      # Kern-Extraktionslogik
├── codesys_import_example.py       # Variablenlisten-Generator
├── create_codesys_project.py       # CODESYS IronPython Integration
│
├── input/                          # Eingabe-Verzeichnis
│   └── LIST_OF_MEASURING_POINTS.xls
│
├── output/                         # Ausgabe-Verzeichnis
│   ├── PLC_IO020_config.json
│   ├── PLC_IO043_config.json
│   ├── PLC_IO251_config.json
│   ├── IO020_variables.txt
│   ├── IO043_variables.txt
│   ├── IO251_variables.txt
│   ├── summary.txt
│   └── validation_report.txt
│
├── projects/                       # CODESYS-Projekte
│   ├── IO020.project
│   ├── IO043.project
│   └── IO251.project
│
├── TEMPLATE_WAGO_750-8210.project  # CODESYS Template
│
├── requirements.txt                # Python-Abhängigkeiten
├── README.md                       # Diese Datei
├── PROGRAMMABLAUFPLAN.md           # Workflow-Dokumentation
├── ENTWICKLER_ZUSAMMENFASSUNG.md   # Entwickler-Notizen
└── WAGO_PLC_Schnittstellen_Dokumentation.md  # API-Referenz
```

### Komponenten-Details

#### 1. batch_processor.py

**Zweck:** CLI-Einstiegspunkt für die Batch-Verarbeitung

**Hauptfunktionen:**

```python
def parse_arguments() -> argparse.Namespace
    """
    Parst Kommandozeilen-Argumente
    
    Returns:
        Namespace mit 'input' und 'output' Attributen
    """

def main() -> None
    """
    Hauptausführungslogik:
    1. Validiere Input-Datei
    2. Erstelle Output-Verzeichnis
    3. Initialisiere PLCConfigExtractor
    4. Verarbeite Excel-Datei
    5. Gebe Zusammenfassung aus
    """
```

**Verwendungsbeispiel:**

```python
# Kommandozeile
python batch_processor.py --input=data.xls --output=./configs

# Programmaufruf
from batch_processor import main
import sys
sys.argv = ['batch_processor.py', '--input=data.xls', '--output=./configs']
main()
```

#### 2. excel_to_json_converter.py

**Zweck:** Kern-Extraktions- und Konvertierungslogik

**Klasse: PLCConfigExtractor**

```python
class PLCConfigExtractor:
    """
    Extrahiert PLC-Konfigurationen aus Excel und generiert JSON
    
    Attributes:
        excel_file (str): Pfad zur Excel-Eingabedatei
        plcs (dict): Dictionary aller extrahierten PLCs
        validation_log (list): Liste aller Log-Einträge
        stats (dict): Statistiken zur Verarbeitung
    """
    
    def __init__(self, excel_file: str):
        """Initialisiert Extractor mit Excel-Datei"""
        
    def extract_plcs_from_io_boxes(self) -> None:
        """
        Extrahiert PLC-Informationen aus Sheet 'IO-Boxen'
        
        Verarbeitung:
        1. Lese Sheet mit pandas (Header in Zeile 3 oder 0)
        2. Iteriere über Zeilen ab Zeile 5
        3. Extrahiere: PLC-Name, IP, Location, IO Box
        4. Validiere IP-Adresse
        5. Speichere in self.plcs
        """
        
    def extract_signals_from_signallist(self) -> None:
        """
        Extrahiert Signale aus Sheet 'SIGNALLIST'
        
        Verarbeitung:
        1. Lese Sheet mit pandas (Header in Zeile 0)
        2. Iteriere über Zeilen ab Zeile 2
        3. Gruppiere Signale nach PLC und Modultyp
        4. Berechne Statistiken (Input/Output-Zähler)
        """
        
    def validate_ip_address(self, ip: str) -> tuple[bool, str]:
        """
        Validiert IP-Adress-Format
        
        Args:
            ip: IP-Adresse als String
            
        Returns:
            (is_valid, result_or_error_message)
            
        Validierungsregeln:
        - Format: xxx.xxx.xxx.xxx
        - Jedes Oktett: 0-255
        - Nicht leer
        """
        
    def generate_json_files(self, output_dir: str) -> list:
        """
        Generiert JSON-Konfigurationsdateien
        
        Args:
            output_dir: Zielverzeichnis
            
        Returns:
            Liste generierter Dateinamen
            
        Format:
        - PLC_Info: Name, Type, IP, Location, IO_Box
        - IO_Modules: Liste von Modulen mit Signalen
        - Statistics: Zähler
        - Metadata: Generierungsinfos
        """
        
    def generate_summary(self, output_dir: str) -> str:
        """Generiert summary.txt mit Übersicht"""
        
    def generate_validation_report(self, output_dir: str) -> str:
        """Generiert validation_report.txt mit Warnungen/Fehlern"""
        
    def process(self, output_dir: str) -> list:
        """
        Hauptverarbeitungs-Pipeline
        
        Args:
            output_dir: Ausgabeverzeichnis
            
        Returns:
            Liste generierter JSON-Dateien
            
        Workflow:
        1. extract_plcs_from_io_boxes()
        2. extract_signals_from_signallist()
        3. generate_json_files()
        4. generate_summary()
        5. generate_validation_report()
        """
```

**Datenstrukturen:**

```python
# self.plcs Dictionary-Struktur
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

# validation_log Einträge
[
    "[INFO] Reading IO-Boxen sheet...",
    "[WARNING] Row 15: Empty PLC field, skipping",
    "[ERROR] PLC IO999: Invalid IP format: 999.999.999.999"
]

# stats Dictionary
{
    'total_plcs': 3,
    'total_signals': 427,
    'total_modules': 15,
    'warnings': 2,
    'errors': 0
}
```

#### 3. codesys_import_example.py

**Zweck:** Generiert IEC 61131-3 Variablenlisten aus JSON

**Hauptfunktionen:**

```python
def load_plc_config(json_file: str) -> dict:
    """
    Lädt JSON-Konfiguration
    
    Args:
        json_file: Pfad zur JSON-Datei
        
    Returns:
        Dictionary mit PLC-Konfiguration oder None bei Fehler
    """

def create_variable_list(config: dict, output_file: str) -> None:
    """
    Erstellt IEC 61131-3 Variablenliste
    
    Args:
        config: PLC-Konfiguration aus JSON
        output_file: Ausgabedatei (z.B. IO043_variables.txt)
        
    Generiert:
        VAR_GLOBAL
            (* Kommentare für Modultypen *)
            variable_name : data_type;
        END_VAR
        
    Datentyp-Mapping:
        - "I" / "O" mit "NC" / "NO" → BOOL
        - "I" / "O" mit "4-20mA" / "0-10V" → INT
        - "RS485" / "RS232" → Keine Variable (Kommentar)
    """

def find_json_configs(directory: str) -> list:
    """
    Findet alle PLC_*_config.json Dateien
    
    Args:
        directory: Suchverzeichnis
        
    Returns:
        Liste von Dictionaries mit:
        - plc_name: PLC-Bezeichnung (z.B. "IO043")
        - filepath: Vollständiger Pfad zur JSON-Datei
    """

def process_plc(config_info: dict, output_dir: str) -> bool:
    """
    Verarbeitet eine einzelne PLC
    
    Args:
        config_info: Dict mit plc_name und filepath
        output_dir: Ausgabeverzeichnis
        
    Returns:
        True bei Erfolg, False bei Fehler
        
    Workflow:
    1. Lade JSON-Konfiguration
    2. Zeige Zusammenfassung (PLC-Info, Module, Signale)
    3. Generiere Variablenliste
    """
```

**IEC 61131-3 Ausgabeformat:**

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
```

#### 4. create_codesys_project.py

**Zweck:** CODESYS-Projekterstellung via IronPython ScriptEngine

**Wichtige Konstanten:**

```python
# Pfad-Konfiguration
DEFAULT_PROJECT_PATH = r"D:\WAGO\CODESYS\projects"
DEFAULT_VARIABLES_PATH = r"D:\WAGO\CODESYS\outputs"
DEFAULT_CONFIG_PATH = r"D:\WAGO\CODESYS\outputs"

# Template-Projekt
USE_TEMPLATE = True
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210.project"

# Auto-Detect Modus
AUTO_DETECT_MODE = True  # Findet automatisch alle IO*_variables.txt

# Manuelle Konfiguration (wenn AUTO_DETECT_MODE = False)
SPECIFIC_VARIABLES_FILE = r"...\IO020_variables.txt"
SPECIFIC_CONFIG_FILE = r"...\PLC_IO020_config.json"
```

**WAGO Device Descriptors:**

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
    # ... weitere Module
}
```

**Hauptfunktionen:**

```python
def create_project_from_template(plc_name: str, project_path: str, 
                                  template_path: str) -> tuple:
    """
    Erstellt CODESYS-Projekt aus Template
    
    Args:
        plc_name: PLC-Bezeichnung (z.B. "IO043")
        project_path: Zielverzeichnis
        template_path: Pfad zum Template-Projekt
        
    Returns:
        (project_object, full_path)
        
    Workflow:
    1. Kopiere Template zu {plc_name}.project
    2. Öffne Projekt mit ScriptEngine
    3. Returniere Projekt-Objekt
    """

def find_plc_device(proj) -> object:
    """
    Findet PLC-Device (Type 4096)
    
    Args:
        proj: CODESYS Project Object
        
    Returns:
        Device Object oder None
        
    Suche-Strategie:
    1. Durchsuche alle Devices rekursiv
    2. Prüfe device_identification.type == 4096
    3. Returniere erstes Match
    """

def find_kbus(device) -> object:
    """
    Findet K-Bus unter PLC-Device
    
    Args:
        device: PLC Device Object
        
    Returns:
        K-Bus Object oder None
    """

def add_io_modules_to_kbus(kbus, config: dict) -> None:
    """
    Fügt I/O-Module zum K-Bus hinzu
    
    Args:
        kbus: K-Bus Device Object
        config: JSON-Konfiguration
        
    Workflow:
    1. Iteriere über config['IO_Modules']
    2. Für jedes Modul:
       a. Hole Device Descriptor aus WAGO_DEVICE_DESCRIPTORS
       b. Erstelle Device mit create_device()
       c. Setze Name und Position
    """

def configure_device_ip(proj, device, ip_address: str) -> None:
    """
    Konfiguriert IP-Adresse des PLC-Devices
    
    Args:
        proj: Project Object
        device: PLC Device Object
        ip_address: IP als String (z.B. "172.16.60.043")
        
    Workflow:
    1. Suche Ethernet-Adapter unter Device
    2. Setze IP, Subnet, Gateway
    """

def create_gvl_with_variables(app, gvl_name: str, var_block: str):
    """
    Erstellt Global Variable List (GVL)
    
    Args:
        app: Application Object
        gvl_name: Name der GVL (z.B. "GVL_IO043")
        var_block: IEC 61131-3 VAR_GLOBAL Block
        
    Workflow:
    1. Erstelle GVL mit app.create_gvl()
    2. Setze textual_declaration auf var_block
    """

def create_single_project(var_file: str, config_file: str, 
                         plc_name: str) -> bool:
    """
    Erstellt ein vollständiges CODESYS-Projekt
    
    Args:
        var_file: Pfad zu IO043_variables.txt
        config_file: Pfad zu PLC_IO043_config.json
        plc_name: PLC-Bezeichnung
        
    Returns:
        True bei Erfolg, False bei Fehler
        
    Workflow:
    1. Parse Variablenliste und JSON-Config
    2. Erstelle Projekt aus Template
    3. Suche Application und PLC Device
    4. Konfiguriere IP-Adresse
    5. Füge I/O-Module zum K-Bus hinzu
    6. Erstelle GVL mit Variablen
    7. Speichere und schließe Projekt
    """

def main() -> None:
    """
    Haupt-Ausführungslogik
    
    Workflow:
    1. Zeige verfügbare Device Descriptors
    2. Sammle Dateien (Auto-Detect oder manuell)
    3. Für jedes PLC-Paar (variables.txt + config.json):
       - Erstelle CODESYS-Projekt
       - Logge Erfolg/Fehler
    4. Zeige Zusammenfassung
    """
```

**ScriptEngine API-Verwendung:**

```python
# CODESYS ScriptEngine Namespace
from ScriptEngine import projects
from ScriptEngine.HostAccess import ScriptTypes

# Projekt öffnen
proj = projects.open(filepath, None, True)

# Application suchen
app = proj.find("Application", True)[0]

# Device erstellen
device = kbus.create_device(device_descriptor)

# GVL erstellen
gvl = app.create_gvl("GVL_IO043")
gvl.textual_declaration.replace(var_block)

# Projekt speichern
proj.save()
proj.close()
```

### Datenfluss & Schnittstellen

#### Datenfluss-Diagramm (detailliert)

```
┌─────────────────────────────────────────────────────────────────────┐
│ EXCEL: LIST_OF_MEASURING_POINTS.xls                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Sheet: IO-Boxen (Header Zeile 4)                                   │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ IO BOX | Location | PLC   | ... | IP-Adress      | Type      │ │
│  ├────────────────────────────────────────────────────────────────┤ │
│  │ 361403 | I A 3    | IO043 | ... | 172.16.60.043  | 750-8210  │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  Sheet: SIGNALLIST (Header Zeile 1)                                 │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ PLC | Type | Signal | Mode_Type | PLC_terminal | Objektname  │ │
│  ├────────────────────────────────────────────────────────────────┤ │
│  │IO043│  I   │  NC    │  750-432  │ IX 65.3-A3.5 │ I0001_Me..  │ │
│  └────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ pandas.read_excel()
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.extract_plcs_from_io_boxes()                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  DataFrame → Iteration über Zeilen → Validierung                    │
│                                                                      │
│  self.plcs["IO043"] = {                                             │
│      "PLC_Info": {                                                  │
│          "Name": "IO043",                                           │
│          "Type": "750-8210",                                        │
│          "IP_Address": "172.16.60.043",                             │
│          "Location": "I A 3",                                       │
│          "IO_Box": "36140310.0"                                     │
│      },                                                             │
│      "IO_Modules": {},  # Noch leer                                 │
│      "Statistics": {...}                                            │
│  }                                                                  │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.extract_signals_from_signallist()                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  DataFrame → Gruppierung nach (PLC, Module_Type)                    │
│                                                                      │
│  self.plcs["IO043"]["IO_Modules"]["750-432"] = {                   │
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
│                                                                      │
│  Statistics aktualisieren:                                          │
│  - Total_Modules++                                                  │
│  - Total_Signals++                                                  │
│  - Input_Signals++ / Output_Signals++                              │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PLCConfigExtractor.generate_json_files()                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Für jeden PLC in self.plcs:                                        │
│      1. Konvertiere IO_Modules dict → list                          │
│      2. Füge Metadata hinzu                                         │
│      3. json.dump() → PLC_IO043_config.json                         │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: JSON-Dateien                                                 │
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
│ create_variable_list()                                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Für jeden PLC:                                                     │
│      Für jedes Module in IO_Modules:                                │
│          Für jedes Signal:                                          │
│              Map Signal_Type → IEC Datentyp                         │
│              Generiere Deklaration                                  │
│                                                                      │
│  VAR_GLOBAL                                                         │
│      (* Module: 750-432 *)                                          │
│      I0001_Me_MnCoolCmnAlrm : BOOL;                                 │
│  END_VAR                                                            │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: Variablenlisten                                              │
├─────────────────────────────────────────────────────────────────────┤
│  IO043_variables.txt                                                │
│  IO020_variables.txt                                                │
│  IO251_variables.txt                                                │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ create_codesys_project.py (IronPython)
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ create_single_project()                                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1. Lade IO043_variables.txt → var_block (String)                  │
│  2. Lade PLC_IO043_config.json → config (Dict)                      │
│  3. Template kopieren → IO043.project                               │
│  4. Projekt öffnen mit ScriptEngine                                 │
│  5. PLC Device suchen (Type 4096)                                   │
│  6. IP-Adresse konfigurieren                                        │
│  7. K-Bus suchen                                                    │
│  8. I/O-Module hinzufügen:                                          │
│      Für jedes Modul in config['IO_Modules']:                       │
│          descriptor = WAGO_DEVICE_DESCRIPTORS[Module_Type]          │
│          device = kbus.create_device(descriptor['descriptor'])      │
│  9. GVL erstellen:                                                  │
│      gvl = app.create_gvl("GVL_IO043")                              │
│      gvl.textual_declaration.replace(var_block)                     │
│  10. Projekt speichern & schließen                                  │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ OUTPUT: CODESYS-Projekte                                             │
├─────────────────────────────────────────────────────────────────────┤
│  projects/IO043.project                                             │
│  projects/IO020.project                                             │
│  projects/IO251.project                                             │
└─────────────────────────────────────────────────────────────────────┘
```

#### Schnittstellen-Definition

##### Python → JSON (excel_to_json_converter.py)

**Input:** Excel-Datei mit definierten Sheets

**Output:** JSON nach folgendem Schema:

```json
{
  "PLC_Info": {
    "Name": "string",           // PLC-Bezeichnung (z.B. "IO043")
    "Type": "string",           // PLC-Typ (z.B. "750-8210")
    "IP_Address": "string",     // IP im Format xxx.xxx.xxx.xxx
    "Location": "string",       // Standort
    "IO_Box": "string"          // Box-Nummer
  },
  "IO_Modules": [               // Liste aller I/O-Module
    {
      "Module_Type": "string",  // WAGO Modultyp (z.B. "750-432")
      "Signals": [              // Liste aller Signale dieses Moduls
        {
          "Terminal": "string", // Terminal-Adresse (z.B. "IX 65.3 -A3.5")
          "Object_Name": "string", // Signalname
          "Signal_Type": "string", // "I", "O", "SI", "SO", "RS485", etc.
          "Signal": "string"    // Signalart (z.B. "NC", "4-20mA")
        }
      ]
    }
  ],
  "Statistics": {
    "Total_Modules": "integer",    // Anzahl Module
    "Total_Signals": "integer",    // Anzahl Signale
    "Input_Signals": "integer",    // Anzahl Eingänge
    "Output_Signals": "integer"    // Anzahl Ausgänge
  },
  "Metadata": {
    "Generated": "ISO 8601 datetime",
    "Source_File": "string",
    "Generator": "string"
  }
}
```

##### JSON → IEC 61131-3 (codesys_import_example.py)

**Input:** JSON wie oben definiert

**Output:** Textdatei im IEC 61131-3 Format

**Mapping-Regeln:**

| Signal_Type | Signal | IEC Datentyp | Beispiel |
|-------------|--------|--------------|----------|
| I | NC / NO | BOOL | `I0001_Signal : BOOL;` |
| O | NC / NO | BOOL | `O0001_Signal : BOOL;` |
| I | 4-20mA / 0-10V | INT | `I0001_Signal : INT;` |
| O | 4-20mA / 0-10V | INT | `O0001_Signal : INT;` |
| SI | INT | INT | `I0001_Signal : INT;` |
| SO | INT | INT | `O0001_Signal : INT;` |
| RS485 / RS232 | - | (Kommentar) | `(* Serial Module *)` |

##### IEC 61131-3 + JSON → CODESYS (create_codesys_project.py)

**Input:**
- IO043_variables.txt (IEC 61131-3 Text)
- PLC_IO043_config.json (JSON)
- TEMPLATE_WAGO_750-8210.project (CODESYS Template)

**Output:**
- IO043.project (CODESYS-Projekt)

**API-Aufrufe:**

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

### Erweiterung & Anpassung

#### Neue I/O-Module hinzufügen

**1. Device Descriptor ermitteln:**

```python
# In CODESYS:
# 1. Öffne Device Repository
# 2. Suche WAGO Modul (z.B. 750-456)
# 3. Rechtsklick → Properties → Device Identification
# 4. Notiere: Device ID, Descriptor String, Version
```

**2. Zu WAGO_DEVICE_DESCRIPTORS hinzufügen:**

```python
# In create_codesys_project.py
WAGO_DEVICE_DESCRIPTORS = {
    # ... bestehende Module
    
    "750-456": {
        "device_id": 32776,                 # Aus CODESYS
        "descriptor": "8401_0750045600000000",  # Aus CODESYS
        "version": "2.0.0.10",              # Aus CODESYS
        "name": "750-456",
        "description": "4DO 24VDC 0.5A"    # Beschreibung
    },
}
```

**3. Testen:**

```python
# Excel mit 750-456 Modul verarbeiten
python batch_processor.py --input=test.xls --output=./output

# Prüfen ob Modul erkannt wird
cat ./output/validation_report.txt | grep "750-456"
```

#### Neue Signal-Typen hinzufügen

**In codesys_import_example.py:**

```python
def map_signal_to_datatype(signal_info):
    """Map signal information to IEC 61131-3 data type"""
    signal_type = signal_info.get('Signal_Type', '')
    signal = signal_info.get('Signal', '')
    
    # Bestehende Mappings...
    
    # NEUE MAPPINGS HINZUFÜGEN:
    if signal_type in ['AI'] and 'PT100' in signal:
        return 'REAL'  # Temperatur als Fließkommazahl
    
    if signal_type in ['AO'] and 'PWM' in signal:
        return 'WORD'  # PWM als 16-bit Wort
    
    # Default
    return 'INT'
```

#### Eigene Validierungsregeln

**In excel_to_json_converter.py:**

```python
class PLCConfigExtractor:
    
    def custom_validation(self, plc_data):
        """Eigene Validierungen hinzufügen"""
        
        # Beispiel 1: Maximale Anzahl Module pro PLC
        if plc_data['Statistics']['Total_Modules'] > 64:
            self.log_warning(
                f"PLC {plc_data['PLC_Info']['Name']}: "
                f"Mehr als 64 Module ({plc_data['Statistics']['Total_Modules']})"
            )
        
        # Beispiel 2: Prüfe auf doppelte Terminal-Adressen
        terminals = []
        for module in plc_data['IO_Modules']:
            for signal in module['Signals']:
                terminal = signal['Terminal']
                if terminal in terminals:
                    self.log_error(
                        f"Doppelte Terminal-Adresse: {terminal}"
                    )
                terminals.append(terminal)
        
        # Beispiel 3: Prüfe Namenskonvention
        for module in plc_data['IO_Modules']:
            for signal in module['Signals']:
                name = signal['Object_Name']
                if not name.startswith(('I', 'O')):
                    self.log_warning(
                        f"Signal {name}: Entspricht nicht Namenskonvention"
                    )
    
    def process(self, output_dir):
        """Erweiterte Verarbeitung mit Custom Validation"""
        # ... bestehender Code
        
        # Custom Validations ausführen
        for plc_name, plc_data in self.plcs.items():
            self.custom_validation(plc_data)
        
        # ... weiter wie gehabt
```

#### Template-Projekt anpassen

**1. Neues Template erstellen:**

```
1. Öffne CODESYS
2. Erstelle neues Projekt mit WAGO PFC200 (750-8210)
3. Konfiguriere:
   - Ethernet-Einstellungen (Standard-IP)
   - Task-Konfiguration
   - Bibliotheken (z.B. Standard, Util)
4. Speichere als: TEMPLATE_WAGO_750-8210_v2.project
```

**2. In create_codesys_project.py aktualisieren:**

```python
TEMPLATE_PROJECT = r"D:\WAGO\CODESYS\TEMPLATE_WAGO_750-8210_v2.project"
```

**3. Template-spezifische Anpassungen:**

```python
def customize_template_project(proj, config):
    """Template-spezifische Anpassungen nach Erstellung"""
    
    # Beispiel: Setze Projekt-Informationen
    proj.set_project_information("Author", "Automation Team")
    proj.set_project_information("Company", config['PLC_Info'].get('Location', ''))
    
    # Beispiel: Konfiguriere Task
    app = proj.active_application
    tasks = app.find("Task Configuration", True)
    if tasks:
        task = tasks[0]
        # Setze Zykluszeit auf 10ms
        task.cycle_time = 10000  # Mikrosekunden
```

#### Batch-Verarbeitung mit Filterung

```python
# In batch_processor.py erweitern
def process_with_filter(input_file, output_dir, plc_filter=None):
    """
    Verarbeite nur bestimmte PLCs
    
    Args:
        plc_filter: Liste von PLC-Namen (z.B. ['IO020', 'IO043'])
    """
    
    extractor = PLCConfigExtractor(input_file)
    extractor.extract_plcs_from_io_boxes()
    extractor.extract_signals_from_signallist()
    
    # Filtern
    if plc_filter:
        filtered_plcs = {
            name: data for name, data in extractor.plcs.items()
            if name in plc_filter
        }
        extractor.plcs = filtered_plcs
    
    # Weiterverarbeitung
    json_files = extractor.generate_json_files(output_dir)
    # ...
```

**Verwendung:**

```python
# Nur bestimmte PLCs verarbeiten
process_with_filter(
    'measuring_points.xls',
    './output',
    plc_filter=['IO020', 'IO043']
)
```

#### Logging erweitern

```python
import logging

# In excel_to_json_converter.py
class PLCConfigExtractor:
    
    def __init__(self, excel_file):
        # ... bestehender Code
        
        # Logger konfigurieren
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
        # Nicht auf Console ausgeben
```

---

## 📚 Zusätzliche Ressourcen

### Externe Dokumentation

- **CODESYS ScriptEngine**: Siehe `ScriptEngine.md` im Projektverzeichnis
- **WAGO PLC Dokumentation**: `WAGO_PLC_Schnittstellen_Dokumentation.md`
- **Workflow-Beschreibung**: `PROGRAMMABLAUFPLAN.md`
- **Entwickler-Notizen**: `ENTWICKLER_ZUSAMMENFASSUNG.md`

### Support & Kontakt

Bei Fragen oder Problemen:

1. Prüfe `validation_report.txt` auf Warnungen/Fehler
2. Konsultiere dieses README
3. Prüfe Log-Dateien in Output-Verzeichnis

### Lizenz & Copyright

© 2025 - Alle Rechte vorbehalten

---

**Version:** 2.0  
**Stand:** November 2025  
**Maintainer:** Automation Team
