# -*- coding: utf-8 -*-
# encoding: utf-8
"""
CODESYS XML Import - Standalone
Demonstrates XML import functionality independently
"""

import sys
import os

# =============================================================================
# CONFIGURATION
# =============================================================================
PROJECT_PATH = r"C:\Projects\MyProject.project"

XML_FILES = [
    {
        "path": r"exports/Program.xml",
        "description": "Main program",
        "conflict_resolve": "replace",
        "optional": False
    },
]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def log(message, level="INFO"):
    """Console logging"""
    print("[{0}] {1}".format(level, message))

def detect_xml_format(filepath):
    """
    Detect XML file format
    Returns: 'export', 'plcopenxml', 'projectxml', or 'unknown'
    
    Note: .export files are NOT supported in IronPython
    """
    try:
        with open(filepath, 'r') as f:
            content = f.read(500)
        
        # .export files start with <ExportFile>
        if content.strip().startswith('<ExportFile'):
            return 'export'
        
        # PLCopenXML contains plcopen.org namespace
        elif 'plcopen.org/xml/tc6' in content:
            return 'plcopenxml'
        
        # CODESYS project XML
        elif '<project' in content and '<fileHeader>' in content:
            return 'projectxml'
        
        return 'unknown'
    except:
        return 'unknown'

def get_conflict_mode(mode_str):
    """
    Convert string to ConflictResolve integer
    
    Modes:
      'replace' -> 0 (overwrite existing objects)
      'copy'    -> 1 (rename imported objects)
      'skip'    -> 2 (skip existing objects)
    """
    mode_lower = mode_str.lower() if mode_str else 'replace'
    
    if mode_lower == 'replace':
        return 0
    elif mode_lower == 'copy':
        return 1
    elif mode_lower == 'skip':
        return 2
    else:
        return 0

def get_application(proj):
    """
    Get Application object from project
    
    ScriptEngine Method Used:
      - IScriptProject.find(name, recursive) -> List[IScriptObject]
      - IScriptObject.get_name() -> String
    """
    try:
        results = proj.find("Application", True)
        
        if not results or len(results) == 0:
            log("No Application found in project", "ERROR")
            return None
        
        app = results[0]
        log("Found Application: {0}".format(app.get_name()))
        
        return app
        
    except Exception as e:
        log("Error finding Application: {0}".format(str(e)), "ERROR")
        return None

def import_xml_file(app, filepath, conflict_mode, description=""):
    """
    Import XML file to Application
    
    CRITICAL: Must call app.import_xml() not proj.import_xml()
              to import into Application node (not Root)
    
    ScriptEngine Method Used:
      - IScriptObject5.import_xml(ConflictResolve, path, import_folder_structure)
        - ConflictResolve: 0=Replace, 1=Copy, 2=Skip
        - path: Full path to XML file
        - import_folder_structure: Boolean (True recommended)
    
    Supported Formats:
      ✓ PLCopenXML (IEC 61131-3 standard)
      ✓ CODESYS Project XML
      ✗ .export files (require ISVNode - not available in IronPython)
    """
    try:
        log("  Importing to Application...")
        
        # Call import_xml on Application object
        app.import_xml(conflict_mode, filepath, True)
        
        log("  SUCCESS: Imported to Application", "SUCCESS")
        return True
        
    except Exception as e:
        log("  ERROR: {0}".format(str(e)), "ERROR")
        return False

# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main():
    """
    Main execution flow:
    1. Open project
    2. Get Application object
    3. Import XML files to Application
    4. Save project
    5. Close project
    """
    log("="*70)
    log("CODESYS XML Import - Standalone Example")
    log("="*70)
    log("")
    
    try:
        # Step 1: Open project
        log("Opening project...")
        if not os.path.exists(PROJECT_PATH):
            log("Project not found: {0}".format(PROJECT_PATH), "ERROR")
            sys.exit(1)
        
        proj = projects.open(PROJECT_PATH)
        log("SUCCESS: Project opened", "SUCCESS")
        log("")
        
        # Step 2: Get Application
        log("="*70)
        log("Getting Application Object")
        log("="*70)
        
        app = get_application(proj)
        if not app:
            log("Cannot proceed without Application", "ERROR")
            proj.close()
            sys.exit(1)
        log("")
        
        # Step 3: Import XML files
        log("="*70)
        log("Importing XML Files")
        log("="*70)
        
        success_count = 0
        error_count = 0
        skipped_count = 0
        
        for idx, xml_item in enumerate(XML_FILES, 1):
            filepath = xml_item['path']
            description = xml_item.get('description', '')
            conflict_mode_str = xml_item.get('conflict_resolve', 'replace')
            optional = xml_item.get('optional', False)
            
            filename = os.path.basename(filepath)
            
            log("")
            log("[{0}/{1}] {2}".format(idx, len(XML_FILES), filename))
            if description:
                log("  Description: {0}".format(description))
            
            # Check file exists
            if not os.path.exists(filepath):
                if optional:
                    log("  File not found (optional) - SKIPPED", "WARNING")
                    skipped_count += 1
                else:
                    log("  File not found (required) - ERROR", "ERROR")
                    error_count += 1
                continue
            
            # Detect format
            file_format = detect_xml_format(filepath)
            log("  Format: {0}".format(file_format.upper()))
            
            # Check if .export (not supported)
            if file_format == 'export':
                log("  .export format NOT SUPPORTED", "ERROR")
                log("  Reason: Requires ISVNode (unavailable in IronPython)", "ERROR")
                log("  Solution: Convert to PLCopenXML or import manually", "ERROR")
                error_count += 1
                continue
            
            # Check if unknown format
            if file_format == 'unknown':
                log("  Unknown format - cannot import", "ERROR")
                error_count += 1
                continue
            
            # Import supported formats
            conflict_mode = get_conflict_mode(conflict_mode_str)
            log("  ConflictResolve: {0} ({1})".format(conflict_mode_str, conflict_mode))
            
            if import_xml_file(app, filepath, conflict_mode, description):
                success_count += 1
            else:
                error_count += 1
        
        # Summary
        log("")
        log("="*70)
        log("IMPORT SUMMARY")
        log("="*70)
        log("Total: {0}".format(len(XML_FILES)))
        log("Success: {0}".format(success_count))
        log("Errors: {0}".format(error_count))
        log("Skipped: {0}".format(skipped_count))
        log("="*70)
        
        # Step 4: Save project
        if success_count > 0:
            log("")
            log("Saving project...")
            proj.save()
            log("SUCCESS: Project saved", "SUCCESS")
        
        # Step 5: Close project
        log("")
        log("Closing project...")
        proj.close()
        log("SUCCESS: Project closed", "SUCCESS")
        
        # Exit with appropriate code
        if error_count > 0:
            log("")
            log("COMPLETED WITH ERRORS", "WARNING")
            sys.exit(1)
        else:
            log("")
            log("COMPLETED SUCCESSFULLY", "SUCCESS")
            sys.exit(0)
        
    except Exception as e:
        log("")
        log("CRITICAL ERROR: {0}".format(str(e)), "ERROR")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
