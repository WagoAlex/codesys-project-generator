# -*- coding: utf-8 -*-
# encoding: utf-8
"""
JSON-Konfigurations-Loader für CODESYS Projekt-Generator V6
Lädt Bibliotheken und FB-Instanzen aus library_fb_config.json
"""

import json
import os
import sys

def load_config_from_json(json_path):
    """
    Lädt die Konfiguration aus einer JSON-Datei
    
    Args:
        json_path (str): Pfad zur JSON-Konfigurationsdatei
    
    Returns:
        tuple: (libraries, fb_instances, project_settings)
    """
    try:
        with open(json_path, 'r') as f:
            config = json.load(f)
        
        # Extrahiere Bibliotheken
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
        
        # Extrahiere FB-Instanzen
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
        
        # Extrahiere Projekt-Einstellungen
        project_settings = {}
        if 'configuration' in config and 'project_settings' in config['configuration']:
            project_settings = config['configuration']['project_settings']
        
        return libraries, fb_instances, project_settings
        
    except Exception as e:
        print("FEHLER beim Laden der JSON-Konfiguration: {0}".format(str(e)))
        import traceback
        traceback.print_exc()
        return [], [], {}

def generate_python_config(json_path, output_path=None):
    """
    Generiert Python-Code aus JSON-Konfiguration
    
    Args:
        json_path (str): Pfad zur JSON-Konfigurationsdatei
        output_path (str): Optionaler Ausgabepfad für Python-Datei
    
    Returns:
        str: Python-Code als String
    """
    libraries, fb_instances, project_settings = load_config_from_json(json_path)
    
    # Generiere Python-Code
    code = """# -*- coding: utf-8 -*-
# Automatisch generiert aus library_fb_config.json
# Datum: {0}

# =============================================================================
# BIBLIOTHEKEN-KONFIGURATION
# =============================================================================
REQUIRED_LIBRARIES = [
""".format(__import__('time').strftime('%Y-%m-%d %H:%M:%S'))
    
    # Füge Bibliotheken hinzu
    for lib in libraries:
        code += """    {{
        "name": "{0}",
        "vendor": "{1}",
        "version": {2},
        "url": {3},
        "required": {4}
    }},
""".format(
            lib['name'],
            lib['vendor'],
            'None' if lib['version'] is None else '"{0}"'.format(lib['version']),
            'None' if lib['url'] is None else '"{0}"'.format(lib['url']),
            str(lib['required'])
        )
    
    code += """]

# =============================================================================
# FUNCTION BLOCK INSTANZIIERUNGEN
# =============================================================================
FB_INSTANCES = [
"""
    
    # Füge FB-Instanzen hinzu
    for fb in fb_instances:
        code += """    {{
        "library": "{0}",
        "fb_type": "{1}",
        "instance": "{2}",
        "params": {{
""".format(fb['library'], fb['fb_type'], fb['instance'])
        
        for param_name, param_value in fb['params'].items():
            code += """            "{0}": "{1}",
""".format(param_name, param_value)
        
        code += """        }},
        "description": "{0}"
    }},
""".format(fb.get('description', ''))
    
    code += """]
"""
    
    # Speichere optional in Datei
    if output_path:
        try:
            with open(output_path, 'w') as f:
                f.write(code)
            print("Python-Konfiguration gespeichert: {0}".format(output_path))
        except Exception as e:
            print("FEHLER beim Speichern: {0}".format(str(e)))
    
    return code

def print_config_summary(json_path):
    """
    Gibt eine Zusammenfassung der Konfiguration aus
    
    Args:
        json_path (str): Pfad zur JSON-Konfigurationsdatei
    """
    libraries, fb_instances, project_settings = load_config_from_json(json_path)
    
    print("")
    print("="*70)
    print("KONFIGURATIONSZUSAMMENFASSUNG")
    print("="*70)
    print("")
    
    print("PROJEKT-EINSTELLUNGEN:")
    print("  Template: {0}".format(project_settings.get('template_path', 'N/A')))
    print("  Output: {0}".format(project_settings.get('output_path', 'N/A')))
    print("  Auto-Detect: {0}".format(project_settings.get('auto_detect_mode', 'N/A')))
    print("")
    
    print("BIBLIOTHEKEN ({0}):".format(len(libraries)))
    for lib in libraries:
        required = "[PFLICHT]" if lib['required'] else "[OPTIONAL]"
        version = lib['version'] if lib['version'] else "Latest"
        print("  {0} {1} ({2}) - Version: {3}".format(
            required, lib['name'], lib['vendor'], version
        ))
    print("")
    
    print("FUNCTION BLOCKS ({0}):".format(len(fb_instances)))
    for fb in fb_instances:
        print("  {0} : {1}".format(fb['instance'], fb['fb_type']))
        print("    Library: {0}".format(fb['library']))
        print("    Beschreibung: {0}".format(fb.get('description', 'N/A')))
        print("    Parameter: {0}".format(len(fb['params'])))
    print("")
    
    print("="*70)

def validate_config(json_path):
    """
    Validiert die JSON-Konfiguration
    
    Args:
        json_path (str): Pfad zur JSON-Konfigurationsdatei
    
    Returns:
        tuple: (is_valid, errors, warnings)
    """
    errors = []
    warnings = []
    
    try:
        with open(json_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        errors.append("JSON-Parsing fehlgeschlagen: {0}".format(str(e)))
        return False, errors, warnings
    
    # Validiere Struktur
    if 'libraries' not in config:
        warnings.append("Keine 'libraries' Sektion gefunden")
    
    if 'function_blocks' not in config:
        warnings.append("Keine 'function_blocks' Sektion gefunden")
    
    # Validiere Bibliotheken
    if 'libraries' in config and 'items' in config['libraries']:
        for idx, lib in enumerate(config['libraries']['items']):
            if 'name' not in lib:
                errors.append("Bibliothek #{0}: 'name' fehlt".format(idx))
            if 'vendor' not in lib:
                warnings.append("Bibliothek #{0}: 'vendor' fehlt (Standard: 3S)".format(idx))
    
    # Validiere FB-Instanzen
    if 'function_blocks' in config and 'items' in config['function_blocks']:
        for idx, fb in enumerate(config['function_blocks']['items']):
            if 'library' not in fb:
                errors.append("FB #{0}: 'library' fehlt".format(idx))
            if 'fb_type' not in fb:
                errors.append("FB #{0}: 'fb_type' fehlt".format(idx))
            if 'instance' not in fb:
                errors.append("FB #{0}: 'instance' fehlt".format(idx))
            
            # Prüfe ob Parameter vorhanden sind
            if 'params' not in fb:
                warnings.append("FB #{0} ({1}): Keine Parameter definiert".format(
                    idx, fb.get('instance', 'unknown')
                ))
    
    is_valid = len(errors) == 0
    return is_valid, errors, warnings

def create_example_config(output_path):
    """
    Erstellt eine Beispiel-Konfigurationsdatei
    
    Args:
        output_path (str): Pfad für die Ausgabedatei
    """
    example_config = {
        "configuration": {
            "description": "Beispiel-Konfiguration",
            "version": "6.0",
            "project_settings": {
                "template_path": "C:\\CODESYS\\Template.project",
                "output_path": "C:\\CODESYS\\Projects",
                "auto_detect_mode": True
            }
        },
        "libraries": {
            "description": "Beispiel-Bibliotheken",
            "items": [
                {
                    "name": "WagoAppAnalytics",
                    "vendor": "WAGO",
                    "version": None,
                    "url": None,
                    "required": False,
                    "description": "WAGO Analytics Bibliothek"
                }
            ]
        },
        "function_blocks": {
            "description": "Beispiel-FB-Instanzen",
            "items": [
                {
                    "library": "WagoAppAnalytics",
                    "fb_type": "FbStatus",
                    "instance": "oFbStatus",
                    "params": {
                        "xEnable": "TRUE",
                        "aStatus=>": ""
                    },
                    "description": "Status-Überwachung"
                }
            ]
        }
    }
    
    try:
        with open(output_path, 'w') as f:
            json.dump(example_config, f, indent=2)
        print("Beispiel-Konfiguration erstellt: {0}".format(output_path))
        return True
    except Exception as e:
        print("FEHLER beim Erstellen: {0}".format(str(e)))
        return False

# =============================================================================
# MAIN - Kommandozeilen-Interface
# =============================================================================
def main():
    """
    Hauptfunktion für Kommandozeilen-Verwendung
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='JSON-Konfigurations-Loader für CODESYS Projekt-Generator V6'
    )
    
    parser.add_argument(
        'command',
        choices=['load', 'generate', 'validate', 'summary', 'create-example'],
        help='Auszuführende Operation'
    )
    
    parser.add_argument(
        '--config',
        default='library_fb_config.json',
        help='Pfad zur JSON-Konfigurationsdatei (Standard: library_fb_config.json)'
    )
    
    parser.add_argument(
        '--output',
        help='Ausgabepfad für generierte Dateien'
    )
    
    args = parser.parse_args()
    
    if args.command == 'load':
        print("Lade Konfiguration: {0}".format(args.config))
        libraries, fb_instances, settings = load_config_from_json(args.config)
        print("Erfolgreich geladen!")
        print("  - {0} Bibliotheken".format(len(libraries)))
        print("  - {0} FB-Instanzen".format(len(fb_instances)))
    
    elif args.command == 'generate':
        print("Generiere Python-Code aus: {0}".format(args.config))
        output = args.output if args.output else 'generated_config.py'
        code = generate_python_config(args.config, output)
        print("Python-Code generiert!")
    
    elif args.command == 'validate':
        print("Validiere Konfiguration: {0}".format(args.config))
        is_valid, errors, warnings = validate_config(args.config)
        
        if errors:
            print("\nFEHLER:")
            for error in errors:
                print("  - {0}".format(error))
        
        if warnings:
            print("\nWARNUNGEN:")
            for warning in warnings:
                print("  - {0}".format(warning))
        
        if is_valid:
            print("\n Konfiguration ist gültig!")
        else:
            print("\n Konfiguration ist ungültig!")
            sys.exit(1)
    
    elif args.command == 'summary':
        print_config_summary(args.config)
    
    elif args.command == 'create-example':
        output = args.output if args.output else 'example_config.json'
        create_example_config(output)

if __name__ == '__main__':
    # Wenn als Skript aufgerufen
    if len(sys.argv) > 1:
        main()
    else:
        # Interaktiver Modus
        print("")
        print("="*70)
        print("JSON-KONFIGURATIONS-LOADER")
        print("="*70)
        print("")
        print("Verwendung:")
        print("  python config_loader.py load --config library_fb_config.json")
        print("  python config_loader.py generate --config library_fb_config.json --output config.py")
        print("  python config_loader.py validate --config library_fb_config.json")
        print("  python config_loader.py summary --config library_fb_config.json")
        print("  python config_loader.py create-example --output example.json")
        print("")
        print("Oder importiere das Modul in Python:")
        print("  from config_loader import load_config_from_json")
        print("  libraries, fb_instances, settings = load_config_from_json('library_fb_config.json')")
        print("")
