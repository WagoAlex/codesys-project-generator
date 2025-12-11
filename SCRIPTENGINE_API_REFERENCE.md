# CODESYS ScriptEngine API Reference
## Methods Used in Project Generator

This document describes all CODESYS ScriptEngine API methods used in the project generator, with examples and limitations.

---

## Project Management

### projects.open(path)
Opens an existing CODESYS project.

**Parameters:**
- `path` (String): Full path to .project file

**Returns:**
- `IScriptProject`: Project object

**Example:**
```python
proj = projects.open(r"C:\CODESYS\Projects\MyProject.project")
```

---

### projects.create(path)
Creates a new CODESYS project.

**Parameters:**
- `path` (String): Full path for new .project file

**Returns:**
- `IScriptProject`: Project object

**Example:**
```python
proj = projects.create(r"C:\CODESYS\Projects\NewProject.project")
```

---

### projects.create_copy(template_path, output_path)
Creates a new project from a template.

**Parameters:**
- `template_path` (String): Path to template .project file
- `output_path` (String): Path for new project

**Returns:**
- `IScriptProject`: Project object

**Example:**
```python
proj = projects.create_copy(
    r"C:\CODESYS\Templates\Template.project",
    r"C:\CODESYS\Projects\NewProject.project"
)
```

---

### IScriptProject.save()
Saves the project.

**Parameters:** None

**Returns:** None

**Example:**
```python
proj.save()
```

---

### IScriptProject.close()
Closes the project.

**Parameters:** None

**Returns:** None

**Example:**
```python
proj.close()
```

---

## Object Search and Navigation

### IScriptProject.find(name, recursive)
Searches for objects in the project.

**Parameters:**
- `name` (String): Object name to search for
- `recursive` (Boolean): Search recursively in tree

**Returns:**
- `List[IExtendedObject[IScriptObject]]`: List of found objects

**Example:**
```python
# Find Application
results = proj.find("Application", True)
if results:
    app = results[0]

# Find all POUs
pous = proj.find("POU", True)
```

**Note:** Returns `IScriptObject` wrappers, not `ISVNode` objects.

---

### IScriptObject.get_name()
Gets the name of an object.

**Parameters:** None

**Returns:**
- `String`: Object name

**Example:**
```python
app = proj.find("Application", True)[0]
name = app.get_name()  # Returns: "Application"
```

---

### IScriptObject.get_parent()
Gets the parent object.

**Parameters:** None

**Returns:**
- `IScriptObject`: Parent object or None

**Example:**
```python
pou = proj.find("PLC_PRG", True)[0]
parent = pou.get_parent()  # Returns Application
```

---

### IScriptObject.get_children(recursive)
Gets child objects.

**Parameters:**
- `recursive` (Boolean): Include all descendants

**Returns:**
- `List[IScriptObject]`: Child objects

**Example:**
```python
app = proj.find("Application", True)[0]
children = app.get_children(False)
```

---

## XML Import

### IScriptObject5.import_xml(ConflictResolve, path, import_folder_structure)
Imports XML file into object (Application, POU, etc.).

**CRITICAL:** Must be called on the **target object** (e.g., Application), not on project!

**Parameters:**
- `ConflictResolve` (Integer): Conflict resolution mode
  - `0` = Replace (overwrite existing objects)
  - `1` = Copy (rename imported objects)
  - `2` = Skip (skip existing objects)
- `path` (String): Full path to XML file
- `import_folder_structure` (Boolean): Import folder hierarchy

**Returns:** None (raises exception on error)

**Supported Formats:**
- ✅ PLCopenXML (IEC 61131-3 standard)
- ✅ CODESYS Project XML
- ❌ .export files (require ISVNode - not available in IronPython)

**Examples:**
```python
# Get Application object
app = proj.find("Application", True)[0]

# Import with replace mode
app.import_xml(0, r"C:\Exports\Program.xml", True)

# Import with skip mode (don't overwrite existing)
app.import_xml(2, r"C:\Exports\Functions.xml", True)
```

**Common Errors:**
```
"Das Element <fileHeader> fehlt..."
→ File is .export format (not supported)

"Object already exists"
→ Use conflict_resolve=0 (replace) or 2 (skip)
```

**Why Not proj.import_xml():**
```python
# WRONG - imports to Root (separate POUs tab)
proj.import_xml(0, path, True)

# CORRECT - imports to Application
app = proj.find("Application", True)[0]
app.import_xml(0, path, True)
```

---

## Library Management

### IScriptObject.get_library_manager()
Gets the library manager for an Application.

**Parameters:** None

**Returns:**
- `ILibraryManager`: Library manager object

**Example:**
```python
app = proj.find("Application", True)[0]
lib_manager = app.get_library_manager()
```

---

### system.librarymanager.repositories
Accesses library repositories.

**Returns:**
- `List[ILibraryRepository]`: Available repositories

**Example:**
```python
repos = system.librarymanager.repositories
for repo in repos:
    libs = repo.get_all_libraries()
    for lib in libs:
        print("{0} v{1}".format(lib.name, lib.version))
```

---

### ILibraryRepository.get_all_libraries()
Gets all libraries in a repository.

**Parameters:** None

**Returns:**
- `List[ILibraryReference]`: Library references

**Example:**
```python
repos = system.librarymanager.repositories
for repo in repos:
    libs = repo.get_all_libraries()
```

---

### ILibraryManager.add(library_reference)
Adds a library to the project.

**Parameters:**
- `library_reference` (ILibraryReference): Library to add

**Returns:** None

**Example:**
```python
lib_manager = app.get_library_manager()
repos = system.librarymanager.repositories

# Find library
for repo in repos:
    for lib in repo.get_all_libraries():
        if lib.name == "MQTT Client SL":
            lib_manager.add(lib)
            break
```

---

## Limitations in IronPython ScriptEngine

### ❌ .export File Import
**.export files cannot be imported** using `import_xml()`.

**Reason:**
- .export files use `<ExportFile><StructuredView>` format
- Require `IStructuredView.PasteFromStream()` method
- PasteFromStream requires `ISVNode` objects
- ISVNode is not exposed in IronPython wrapper

**Error:**
```
Exception: Das Element <fileHeader> fehlt im Element <project>
```

**Workarounds:**
1. Convert .export to PLCopenXML format
2. Import manually in CODESYS IDE
3. Use C# CODESYS Automation SDK (not IronPython)

---

### ❌ IStructuredView Not Accessible
`IStructuredView` and `ISVNode` are not accessible in IronPython.

**What doesn't work:**
```python
# These don't work in IronPython:
from System import Guid
guid = Guid("d9b2b2cc-ea99-4c3b-aa42-1e5c49e65b84")
sv = proj.find(guid)  # ERROR: expected str, got Guid

sv.paste_from_stream(node, stream, None, None)  # ISVNode not available
```

**What works:**
```python
# Use IScriptObject methods instead:
app = proj.find("Application", True)[0]
app.import_xml(0, path, True)
```

---

### ❌ proj.active_application Behavior
Setting `proj.active_application` does NOT affect import target.

**Documented behavior (C# API):**
```csharp
Guid ActiveApplication { get; set; }
```

**Actual IronPython behavior:**
```python
# Setting active_application doesn't change import_xml target
proj.active_application = app  # May work or fail
proj.import_xml(0, path, True)  # Still imports to Root!

# Solution: Call import_xml on Application object
app.import_xml(0, path, True)  # Imports to Application
```

---

## Complete Import Example

```python
# Open project
proj = projects.open(r"C:\CODESYS\Projects\MyProject.project")

# Find Application
results = proj.find("Application", True)
app = results[0]

# Detect file format
with open(r"C:\Exports\Program.xml", 'r') as f:
    content = f.read(500)

if '<ExportFile' in content:
    print("ERROR: .export format not supported")
elif 'plcopen.org/xml' in content:
    print("PLCopenXML detected")
    # Import with replace mode
    app.import_xml(0, r"C:\Exports\Program.xml", True)
    print("Import successful")

# Save and close
proj.save()
proj.close()
```

---

## Best Practices

### ✅ DO
- Call `app.import_xml()` on Application object
- Use full absolute paths for files
- Check file format before import
- Handle exceptions for error detection
- Use conflict_resolve=0 (replace) for automation

### ❌ DON'T
- Call `proj.import_xml()` expecting Application import
- Try to import .export files
- Use relative paths
- Assume silent success (check for exceptions)
- Mix IronPython and C# API assumptions

---

## Version Compatibility

**Tested with:**
- CODESYS V3.5 SP16+
- IronPython 2.7 (embedded in ScriptEngine)

**Not compatible:**
- CODESYS V2.x
- Older CODESYS V3.x versions without ScriptEngine

---

## Further Reading

- CODESYS Online Help: ScriptEngine API
- IEC 61131-3 PLCopenXML Specification
- WAGO Documentation Portal

---

## Summary Table

| Method | Purpose | Works in IronPython | Notes |
|--------|---------|---------------------|-------|
| `projects.open()` | Open project | ✅ Yes | - |
| `projects.create()` | Create project | ✅ Yes | - |
| `proj.find()` | Search objects | ✅ Yes | Returns IScriptObject |
| `app.import_xml()` | Import XML | ✅ Yes | PLCopenXML/ProjectXML only |
| `proj.import_xml()` | Import to project | ⚠️ Partial | Imports to Root, not Application |
| `sv.paste_from_stream()` | Import .export | ❌ No | ISVNode not available |
| `IStructuredView` access | Tree navigation | ❌ No | Not exposed in IronPython |

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-10  
**Author:** Alexander Fugmann

---

## Version History

| Date | Version | Author | Change |
|------|---------|--------|--------|
| 10.12.2024 | 1.0 | Alexander Fugmann | Initial ScriptEngine API reference documentation |
| 10.12.2024 | 1.0 | Alexander Fugmann | Documented IronPython limitations (ISVNode, .export files) |
| 10.12.2024 | 1.0 | Alexander Fugmann | Added complete method signatures and examples |
| 10.12.2024 | 1.0 | Alexander Fugmann | Documented Application-targeted XML import requirement |
