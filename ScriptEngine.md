# Combined CODESYS API Events

## IFileReference.PromptUpdate Event

**Summary:** This event is triggered after the contents of this file reference has been changed, in
            order to prompt client code whether the embedded file data should be updated or not.
            .

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
event FileReferenceCancelEventHandler PromptUpdate
```

---

## IFileReference.PropertyChanged Event

**Summary:** This event is triggered when a property of this file reference has been changed.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
event FileReferenceEventHandler PropertyChanged
```

---

## IProject6.WriteProtectionModeChanged Event

**Summary:** This event is triggered when the current write-protection mode of this project is
            changed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ProjectChangedEventHandler WriteProtectionModeChanged
```

---

## IProject.ActiveApplicationChanged Event

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ProjectChangedEventHandler ActiveApplicationChanged
```

---

## IProject.DirtyChanged Event

**Summary:** This event is triggered after theDirtyflag of this project has changed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ProjectChangedEventHandler DirtyChanged
```

---

## IProject.PathChanged Event

**Summary:** This event is triggered after thePathproperty of this project has
            changed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ProjectChangedEventHandler PathChanged
```

---

## IProject.SelectionChanged Event

**Summary:** This event is triggered after theSelectedSVNodesproperty of this
            project has changed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ProjectChangedEventHandler SelectionChanged
```

---

## IStructuredView.NodeAdded Event

**Summary:** This event is triggered whenever a node has been added to this structued view (even if
            it was caused by adding an object directly into an Object Manager project).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeEventHandler NodeAdded
```

---

## IStructuredView.NodeLoaded Event

**Summary:** This event is triggered whenever an object represented by a node within this structured
            view has been loaded.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeEventHandler NodeLoaded
```

---

## IStructuredView.NodeModified Event

**Summary:** This event is triggered whenever an object represented by a node within this structured
            view has been modified.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeModifiedEventHandler NodeModified
```

---

## IStructuredView.NodeMoved Event

**Summary:** This event is triggered whenever a node within this structured view has been moved.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeMovedEventHandler NodeMoved
```

---

## IStructuredView.NodePropertyModified Event

**Summary:** This event is triggered whenever a property associated with an object represented by a
            node within this structured view has been modified.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodePropertyModifiedEventHandler NodePropertyModified
```

---

## IStructuredView.NodeRemoved Event

**Summary:** This event is triggered whenever a node has been removed from this structured view
            (even if it was caused by removing an object directly from an Object Manager project).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeEventHandler NodeRemoved
```

---

## IStructuredView.NodeRenamed Event

**Summary:** This event is triggered whenever an object represented by a node within this structured
            view has been renamed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
event SVNodeRenamedEventHandler NodeRenamed
```

---

## IOnlineApplication12.FlowControlEnabledChanged Event

**Summary:** This event is triggered whenever theFlowControlEnabledproperty of this online
            application changes.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event EventHandler FlowControlEnabledChanged
```

---

## IOnlineApplication13.AfterApplicationDownload2 Event

**Summary:** Called after download completed successfully.
            In opposite to AfterApplicationDownload, this event is fired at the complete end of the download. At this point
            all error reply tags from the runtime are evaluated an so this event is only fired, if the download completed successfully.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterApplicationDownload2EventHandler AfterApplicationDownload2
```

---

## IOnlineApplication2.AfterApplicationDownload Event

**Summary:** Called after a successfull download to an application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterApplicationDownloadEventHandler AfterApplicationDownload
```

---

## IOnlineApplication2.BeforeApplicationDownload Event

**Summary:** Called before a download to an application occurs. This event may be canceled.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeApplicationDownloadEventHandler BeforeApplicationDownload
```

---

## IOnlineApplication2.DuringApplicationDownload Event

**Summary:** Called during the download of an application. Client code can attach to this event to 
            take part in a download.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event DuringApplicationDownloadEventHandler DuringApplicationDownload
```

---

## IOnlineApplication6.OnForcingVariables Event

**Summary:** This event is triggered when any variable gets forced in any editor.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event OnForcingVariablesEventHandler OnForcingVariables
```

---

## IOnlineApplication6.OnWritingVariables Event

**Summary:** This event is triggered when a value gets written to any variable in any editor.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event OnWritingVariablesEventHandler OnWritingVariables
```

---

## IOnlineApplication8.AfterOfflineBootapplication Event

**Summary:** Called after an offline boot project is created (inStreamDownloadCommand(BinaryWriter))

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterOfflineBootApplicationEventHandler AfterOfflineBootapplication
```

---

## IOnlineApplication8.BeforeOfflineBootapplication Event

**Summary:** Called before an offline boot project is created (inStreamDownloadCommand(BinaryWriter))

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeOfflineBootApplicationEventHandler BeforeOfflineBootapplication
```

---

## IOnlineApplication9.AfterApplicationReset Event

**Summary:** Called after a reset of the online application

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterApplicationResetEventHandler AfterApplicationReset
```

---

## IOnlineApplication.AfterApplicationLogin Event

**Summary:** Raised when a login to the application succeeded.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterApplicationLoginEventHandler AfterApplicationLogin
```

---

## IOnlineApplication.AfterApplicationLogout Event

**Summary:** Raised when the application has been logged out.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterApplicationLogoutEventHandler AfterApplicationLogout
```

---

## IOnlineApplication.ApplicationStateChanged Event

**Summary:** Raised when the application state changed.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event ApplicationStateChangedEventHandler ApplicationStateChanged
```

---

## IOnlineApplication.BeforeApplicationLogin Event

**Summary:** Raised right before a login to the application. It is possible to cancel the operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeApplicationLoginEventHandler BeforeApplicationLogin
```

---

## IOnlineApplication.BeforeApplicationLogout Event

**Summary:** Raised right before a logout from the application. It is possible to cancel the operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeApplicationLogoutEventHandler BeforeApplicationLogout
```

---

## IOnlineApplication.CurrentPositionChanged Event

**Summary:** Raised when the current execution position of an application has changed.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event CurrentPositionChangedEventHandler CurrentPositionChanged
```

---

## IOnlineApplication.OperatingStateChanged Event

**Summary:** Raised when the operation state of the application changed.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event OperatingStateChangedEventHandler OperatingStateChanged
```

---

## IOnlineDevice.AfterDeviceLogin Event

**Summary:** Called after a login to a device succeeded.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterDeviceLoginEventHandler AfterDeviceLogin
```

---

## IOnlineDevice.AfterDeviceLogout Event

**Summary:** Called after a logout from a device

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event AfterDeviceLogoutEventHandler AfterDeviceLogout
```

---

## IOnlineDevice.BeforeDeviceLogin Event

**Summary:** Called before a login to a device is performed. The operation may be cancelled by setting theExceptionmember of the event arguments.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeDeviceLoginEventHandler BeforeDeviceLogin
```

---

## IOnlineDevice.BeforeDeviceLogout Event

**Summary:** Called before a logout from a device is performed. The operation may be cancelled by setting the 
            	member e of theException

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event BeforeDeviceLogoutEventHandler BeforeDeviceLogout
```

---

## IOnlineVarRef.Changed Event

**Summary:** This event is raised if the value or the state of this object changes.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
event OnlineVarRefEventHandler Changed
```

---

## IVersionCompatibilityManager4.BeginUpdateEnvironmentStage Event

**Summary:** This event is raised when one of the stages of of the project environment updated is started.

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
event EventHandler<UpdateEnvironmentEventArgs> BeginUpdateEnvironmentStage
```

---

## IVersionCompatibilityManager4.EndUpdateEnvironmentStage Event

**Summary:** This event is raised after one of the stages of of the project environment updated is completed.

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
event EventHandler<UpdateEnvironmentEventArgs> EndUpdateEnvironmentStage
```

---

## IFileReference Events

**Summary:** This event is triggered when the contents of this file reference has been changed.

---

## IFileReference2 Events

**Summary:** This event is triggered when the contents of this file reference has been changed.

---

## IFileReference3 Events

**Summary:** This event is triggered when the contents of this file reference has been changed.

---

## IFileReference4 Events

**Summary:** This event is triggered when the contents of this file reference has been changed.

---

## IProject Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IProject2 Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IProject3 Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IProject4 Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IProject5 Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IProject6 Events

**Summary:** This event is triggered after theActiveApplicationproperty of this
            project has changed.

---

## IStructuredView Events

**Summary:** This event is triggered whenever a node has been added to this structued view (even if
            it was caused by adding an object directly into an Object Manager project).

---

## IOnlineApplication Events

**Summary:** Raised when a login to the application succeeded.

---

## IOnlineApplication10 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication11 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication12 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication13 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication14 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication2 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication3 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication4 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication5 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication6 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication7 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication8 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineApplication9 Events

**Summary:** Called after a successfull download to an application.

---

## IOnlineDevice Events

**Summary:** Called after a login to a device succeeded.

---

## IOnlineVarRef Events

**Summary:** This event is raised if the value or the state of this object changes.

---

## IOnlineVarRef2 Events

**Summary:** This event is raised if the value or the state of this object changes.

---

## IVersionCompatibilityManager4 Events

**Summary:** This event is raised when one of the stages of of the project environment updated is started.

---

## ObjectManagerException._nProjectHandle Field

**Summary:** The project handle of the affected object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected int _nProjectHandle
```

---

## ObjectManagerException._objectGuid Field

**Summary:** The GUID of the affected object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected Guid _objectGuid
```

---

## ObjectManagerException._stObjectName Field

**Summary:** No summary available.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected string _stObjectName
```

---

## ObjectManagerException._stReason Field

**Summary:** The reason for that exception.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected string _stReason
```

---

## PreparedValues.Unforce Field

**Summary:** Unforce a previously forced variable.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Object Unforce
```

---

## PreparedValues.UnforceAndRestore Field

**Summary:** Unforce a previously forced variable and set it to the value it had
            	before it was forced.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Object UnforceAndRestore
```

---

## ProjectAttributes.CompiledLibrary Field

**Summary:** Indicates that the project is a compiled library. Compiled library projects will be
            closed automatically when the primary project is closed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Guid CompiledLibrary
```

---

## ProjectAttributes.Library Field

**Summary:** Indicates that the project is a library. Library projects will be closed automatically
            when the primary project is closed.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Guid Library
```

---

## ProjectAttributes.Primary Field

**Summary:** Indicates that the project is primary. The primary project is the root of the language
            model.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Guid Primary
```

---

## ProjectAttributes.ProvidesLanguageModel Field

**Summary:** Indicates that the project is providing language model. Objects within that project are
            automatically queried for their language model when the project is opened, and their
            language models will automatically be updated whenever the objects change.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Guid ProvidesLanguageModel
```

---

## ProjectAttributes.ReadOnly Field

**Summary:** Indicates that the project is read-only. Objects within those project cannot be edited,
            neither by the user nor by plug-in components.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static readonly Guid ReadOnly
```

---

## ObjectManagerException Fields

**Summary:** The project handle of the affected object.

---

## ObjectNameInvalidException Fields

**Summary:** The project handle of the affected object.

---

## PreparedValues Fields

**Summary:** Unforce a previously forced variable.

---

## ProjectAttributes Fields

**Summary:** Indicates that the project is a compiled library. Compiled library projects will be
            closed automatically when the primary project is closed.

---

## _3S.CoDeSys.Core Namespaces

**Summary:**

---

## _3S.CoDeSys.Core.Online Namespaces

**Summary:**

---

## ExactVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## ExactVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## ExactVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## ExactVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## ExactVersionConstraint Constructor

**Summary:** Constructs the version constraint, using the specified version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ExactVersionConstraint(
	Version version
)
```

---

## NewestBeforeVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## NewestBeforeVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## NewestBeforeVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## NewestBeforeVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## NewestBeforeVersionConstraint Constructor

**Summary:** Constructs the version constraint, using the specified version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public NewestBeforeVersionConstraint(
	Version version
)
```

---

## NewestBetweenVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## NewestBetweenVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## NewestBetweenVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## NewestBetweenVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## NewestBetweenVersionConstraint Constructor

**Summary:** Constructs the version constraint, using the specified version range.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public NewestBetweenVersionConstraint(
	Version fromVersion,
	Version toVersion
)
```

---

## NewestVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## NewestVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## NewestVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## NewestVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## NewestVersionConstraint Constructor

**Summary:** Initializes a new instance of theNewestVersionConstraintclass

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public NewestVersionConstraint()
```

---

## OldestAfterVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## OldestAfterVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## OldestAfterVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## OldestAfterVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## OldestAfterVersionConstraint Constructor

**Summary:** Constructs the version constraint, using the specified version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OldestAfterVersionConstraint(
	Version version
)
```

---

## OldestBetweenVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## OldestBetweenVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## OldestBetweenVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## OldestBetweenVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## OldestBetweenVersionConstraint Constructor

**Summary:** Constructs the version constraint, using the specified version range.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OldestBetweenVersionConstraint(
	Version fromVersion,
	Version toVersion
)
```

---

## OldestVersionConstraint.Equals Method

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## OldestVersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## OldestVersionConstraint.GetHashCode Method

**Summary:** Serves as a hash function for a particular type.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## OldestVersionConstraint.ToString Method

**Summary:** Returns aStringobject that represents this object.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string ToString()
```

---

## OldestVersionConstraint Constructor

**Summary:** Initializes a new instance of theOldestVersionConstraintclass

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OldestVersionConstraint()
```

---

## Profile.AddControlledExtension Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void AddControlledExtension(
	string stOriginator,
	Guid plugInGuid,
	Version version
)
```

---

## Profile.Equals Method

**Summary:** SeeEquals(Object).

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override bool Equals(
	Object obj
)
```

---

## Profile.FromFile Method

**Summary:** Creates a new instance of theProfileclass by reading a profile file at
            the specified location.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static Profile FromFile(
	string stPath
)
```

---

## Profile.FromStream Method

**Summary:** Creates a new instance of theProfileclass by reading the specified
            stream.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public static Profile FromStream(
	Stream stream
)
```

---

## Profile.GetControlledExtension Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version GetControlledExtension(
	string stOriginator,
	Guid plugInGuid
)
```

---

## Profile.GetEntries Method

**Summary:** Gets an array of all plug-in GUIDs that are part of this profile.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid[] GetEntries()
```

---

## Profile.GetHashCode Method

**Summary:** SeeGetHashCode.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override int GetHashCode()
```

---

## Profile.GetVersionConstraint Method

**Summary:** Returns the version constraint of the specified plug-in as defined in this profile.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public VersionConstraint GetVersionConstraint(
	Guid plugInGuid
)
```

---

## Profile.HasExtensions Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public bool HasExtensions()
```

---

## Profile.IsExtension Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public bool IsExtension(
	Guid plugInGuid
)
```

---

## Profile.RemoveControlledExtension Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void RemoveControlledExtension(
	string stOriginator,
	Guid plugInGuid
)
```

---

## Profile.SetExtension Method

**Summary:** This method is for internal use and should not be called.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void SetExtension(
	Guid plugInGuid,
	bool bExtension
)
```

---

## Profile.SetVersionConstraint Method

**Summary:** Sets the version constraint of the specified plug-in in this profile.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void SetVersionConstraint(
	Guid plugInGuid,
	VersionConstraint constraint
)
```

---

## Profile Constructor

**Summary:** Initializes a new instance of theProfileclass

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Profile()
```

---

## VersionConstraint.FindVersion Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version FindVersion(
	Version[] array
)
```

---

## VersionConstraint.FindVersionFast Method

**Summary:** Finds the version which matches this version constraint.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public abstract Version FindVersionFast(
	IEnumerable<Version> versions
)
```

---

## VersionConstraint Constructor

**Summary:** Initializes a new instance of theVersionConstraintclass

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected VersionConstraint()
```

---

## FileReferenceCancelEventArgs Constructor

**Summary:** Creates an instance ofFileReferenceCancelEventArgs.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
public FileReferenceCancelEventArgs(
	IFileReference fileReference
)
```

---

## FileReferenceEventArgs Constructor

**Summary:** Creates an instance ofFileReferenceEventArgs.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
public FileReferenceEventArgs(
	IFileReference fileReference
)
```

---

## IFileReference2.GetAbsolutePath Method (Boolean, Boolean)

**Summary:** Returns the absolute path of this file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetAbsolutePath(
	bool bCheckExisting,
	bool bResolveEnvironmentVariables
)
```

---

## IFileReference4.ReleaseAll Method

**Summary:** Releases this file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool ReleaseAll(
	Guid owningObjectGuid
)
```

---

## IFileReference.Freeze Method

**Summary:** Freezes a file reference, i.e. the link to a file system object is released. The
            contents of the file will solely exist in the corresponding Object Manager project, and
            it cannot be updated by file system changes any more.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Freeze()
```

---

## IFileReference.GetAbsolutePath Method

**Summary:** Returns the absolute path of this file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetAbsolutePath(
	bool bCheckExisting
)
```

---

## IFileReference.GetChecksum Method

**Summary:** Calculates a 32-bit checksum over the physical file reference data.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
long GetChecksum()
```

---

## IFileReference.GetEditPath Method

**Summary:** Gets the absolute path where this file reference is edited. This is the absolute path
            itself if the file reference is linked to a file system object, or a temporary path if
            it is embedded into a project.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetEditPath()
```

---

## IFileReference.GetLogicalData Method

**Summary:** Gets a logical data object associated with this file reference, identified by the
            specified representation GUID.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object GetLogicalData(
	Guid representationGuid
)
```

---

## IFileReference.GetPhysicalData Method

**Summary:** Gets the physical data of this file reference (i.e. the raw file contents).

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] GetPhysicalData()
```

---

## IFileReference.GetProjectPath Method

**Summary:** If this file reference has been loaded as Object Manager project, returns the absolute
            path of this project. This might differ from the original path if the project had to be
            converted before loading.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetProjectPath()
```

---

## IFileReference.NeedUpdate Method

**Summary:** Checks whether the physical file contents differ from the embedded data.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool NeedUpdate()
```

---

## IFileReference.Release Method

**Summary:** Releases this file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Release(
	Guid owningObjectGuid
)
```

---

## IFileReference.SetLogicalData Method

**Summary:** Associates a logical data object with this file reference, identified by the specified
            representation GUID.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetLogicalData(
	Guid representationGuid,
	Object data
)
```

---

## IFileReference.Update Method

**Summary:** Updates the embedded data to reflect the lastest physical file contents.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Update()
```

---

## IMessageService2.Prompt Method (String, PromptChoice, PromptResult, String, String)

**Summary:** Prompts the user. This method blocks until the user has answered the question. This
            method allows the user to store his/her answer. The next time the same question is
            prompted to the user by this method, the method immediately returns with the stored
            result.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	string stStoreResultText,
	string stStoredResultKey
)
```

---

## IMessageService2.ResetStoredResult Method

**Summary:** Resets any prompt results stored byPrompt(String, PromptChoice, PromptResult, String, String).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ResetStoredResult(
	string stStoredResultKey
)
```

---

## IMessageService3.Error Method (String, String, Object[])

**Summary:** A reimplementation of the method error, that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Error(
	string stMessage,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService3.Information Method (String, String, Object[])

**Summary:** A reimplementation ofInformation(String, String,Object), that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Information(
	string stMessage,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService3.Prompt Method (String, PromptChoice, PromptResult, String, Object[])

**Summary:** A reimplementation ofPrompt(String, PromptChoice, PromptResult), that is interpretable by automated tools (eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService3.Prompt Method (String, PromptChoice, PromptResult, String, String, String, Object[])

**Summary:** A reimplementation ofPrompt(String, PromptChoice, PromptResult, String, String), that is interpretable by automated tools (eg. an
            automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	string stStoreResultText,
	string stStoredResultKey,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService3.Prompt Method (String, Object[], PromptChoice, PromptResult, Boolean[], String, Object[])

**Summary:** A reimplementation ofPrompt(String,Object, PromptChoice, PromptResult,Boolean), that is interpretable by automated tools (eg. an
            automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	Object[] items,
	PromptChoice choice,
	PromptResult defaultResult,
	out bool[] selection,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService3.Warning Method (String, String, Object[])

**Summary:** A reimplementation ofWarning(String, String,Object), that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Warning(
	string stMessage,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService4.MultipleChoicePrompt Method

**Summary:** Displays a multiple choice prompt to the user. This method blocks until the user has
            chosen and result.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
int MultipleChoicePrompt(
	string stMessage,
	string[] options,
	int nInitialSelection,
	bool bCancellable,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.ErrorWithDetails Method (String, EventHandler, EventArgs)

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ErrorWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.ErrorWithDetails Method (String, EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation of the method error, that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ErrorWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.InformationWithDetails Method (String, EventHandler, EventArgs)

**Summary:** Reports an informational message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void InformationWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.InformationWithDetails Method (String, EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation ofInformation(String), that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void InformationWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.MultipleChoicePromptWithDetails Method

**Summary:** Displays a multiple choice prompt to the user. This method blocks until the user has
            chosen and result.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
int MultipleChoicePromptWithDetails(
	string stMessage,
	string[] options,
	int nInitialSelection,
	bool bCancellable,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.PromptWithDetails Method (String, PromptChoice, PromptResult, EventHandler, EventArgs)

**Summary:** Prompts the user. This method blocks until the user has answered the question.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.PromptWithDetails Method (String, PromptChoice, PromptResult, EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation ofPrompt(String, PromptChoice, PromptResult), that is interpretable by automated tools (eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.PromptWithDetails Method (String, PromptChoice, PromptResult, String, String, EventHandler, EventArgs)

**Summary:** Prompts the user. This method blocks until the user has answered the question. This
            method allows the user to store his/her answer. The next time the same question is
            prompted to the user by this method, the method immediately returns with the stored
            result.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	string stStoreResultText,
	string stStoredResultKey,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.PromptWithDetails Method (String, PromptChoice, PromptResult, String, String, EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation ofPrompt(String, PromptChoice, PromptResult, String, String), that is interpretable by automated tools (eg. an
            automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult,
	string stStoreResultText,
	string stStoredResultKey,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.PromptWithDetails Method (String, Object[], PromptChoice, PromptResult, Boolean[], EventHandler, EventArgs)

**Summary:** Prompts the user, allowing the user to select item for which to apply the answer. This
            method blocks until the user has answered the question.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	Object[] items,
	PromptChoice choice,
	PromptResult defaultResult,
	out bool[] selection,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.PromptWithDetails Method (String, Object[], PromptChoice, PromptResult, Boolean[], EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation ofPrompt(String,Object, PromptChoice, PromptResult,Boolean), that is interpretable by automated tools (eg. an
            automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult PromptWithDetails(
	string stMessage,
	Object[] items,
	PromptChoice choice,
	PromptResult defaultResult,
	out bool[] selection,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService5.WarningWithDetails Method (String, EventHandler, EventArgs)

**Summary:** Reports a warning message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void WarningWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs
)
```

---

## IMessageService5.WarningWithDetails Method (String, EventHandler, EventArgs, String, Object[])

**Summary:** A reimplementation ofWarning(String), that is interpretable by automated tools
            	(eg. an automated test tool).

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void WarningWithDetails(
	string stMessage,
	EventHandler detailsClickHandler,
	EventArgs detailsClickArgs,
	string stMessageKey,
	params Object[] messageArguments
)
```

---

## IMessageService.Error Method

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Error(
	string stMessage
)
```

---

## IMessageService.Information Method

**Summary:** Reports an informational message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Information(
	string stMessage
)
```

---

## IMessageService.Prompt Method (String, PromptChoice, PromptResult)

**Summary:** Prompts the user. This method blocks until the user has answered the question.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	PromptChoice choice,
	PromptResult defaultResult
)
```

---

## IMessageService.Prompt Method (String, Object[], PromptChoice, PromptResult, Boolean[])

**Summary:** Prompts the user, allowing the user to select item for which to apply the answer. This
            method blocks until the user has answered the question.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptResult Prompt(
	string stMessage,
	Object[] items,
	PromptChoice choice,
	PromptResult defaultResult,
	out bool[] selection
)
```

---

## IMessageService.Warning Method

**Summary:** Reports a warning message to the user. This method blocks until the user has
            acknowledged this message.

**Assembly:** `MessageService (in MessageService.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Warning(
	string stMessage
)
```

---

## IProgressCallback.Finish Method

**Summary:** Call this method after the long-running operation is finished. Do not call any method
            of this instance after that.

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Finish()
```

---

## IProgressCallback.NextTask Method

**Summary:** Call this method if a new task within the long-running operation is starting.

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
void NextTask(
	string stTask,
	int nItemsTotal,
	string stItemsUnit
)
```

---

## IProgressCallback.TaskProgress Method (String)

**Summary:** Call this method when processing of a single task item is starting. The item counter
            will be incremented by one.
            .

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
void TaskProgress(
	string stItem
)
```

---

## IProgressCallback.TaskProgress Method (String, Int32)

**Summary:** Call this method when processing of a single task item is starting. The item counter
            will be incremented as specified.

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
void TaskProgress(
	string stItem,
	int nItemsCompletedIncrement
)
```

---

## IProject2.GetProjectOptionsRootKey Method

**Summary:** Returns the root option key for project options of this project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IOptionKey GetProjectOptionsRootKey()
```

---

## IProject3.SetDirty Method (Boolean)

**Summary:** This method is for internal use only and should not be called.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetDirty(
	bool bDirty
)
```

---

## IProject4.Save Method (Profile, String)

**Summary:** Saves this project at its physical location (seePath), using
            the specified version profile. The resulting project file will be compatible to the
            version specified by the profile.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Save(
	Profile profile,
	string stProfileName
)
```

---

## IProject6.GetWriteProtectionMode Method

**Summary:** Returns information whether and how this project is write-protected.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ProjectWriteProtectionMode GetWriteProtectionMode()
```

---

## IProject6.IsConcurrentlyUsed Method

**Summary:** Determines whether this project is concurrently used by another user.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsConcurrentlyUsed(
	out string userName,
	out string machineName,
	out int pid
)
```

---

## IProject6.MakeWriteable Method

**Summary:** Tries to make the project writeable, if it currently write-protected.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void MakeWriteable(
	ProjectWriteProtectionMode mode
)
```

---

## IProject6.SetReadOnlyAttribute Method

**Summary:** Sets the ReadOnly project attribute for an already created project instance.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetReadOnlyAttribute()
```

---

## IProject.Close Method

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Close()
```

---

## IProject.DeselectSVNode Method

**Summary:** Deselects the specified structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void DeselectSVNode(
	ISVNode svNode
)
```

---

## IProject.DeselectSVNodes Method

**Summary:** Deselects the specified structured view nodes.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void DeselectSVNodes(
	ISVNode[] svNodes
)
```

---

## IProject.GetInstancePathInfo Method

**Summary:** This method is for internal use only and should not called.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void GetInstancePathInfo(
	string stInstancePath,
	out Guid appObjectGuid,
	out bool bExisting,
	out bool bOnline
)
```

---

## IProject.GetProfile Method

**Summary:** Returns information about the version profile which was active when the project was
            stored last.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool GetProfile(
	out Profile profile,
	out string stProfileName
)
```

---

## IProject.HasAttribute Method

**Summary:** Returns whether the specified attribute is set for this project. See theProjectAttributesclass for available project attributes.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool HasAttribute(
	Guid projectAttr
)
```

---

## IProject.Save Method

**Summary:** Saves this project at its physical location (seePath).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Save()
```

---

## IProject.SelectSVNode Method

**Summary:** Selects the specified structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SelectSVNode(
	ISVNode svNode,
	bool bAddToSelection
)
```

---

## IProject.SelectSVNodes Method

**Summary:** Selects the specified structured view nodes.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SelectSVNodes(
	ISVNode[] svNodes,
	bool bAddToSelection
)
```

---

## IProject.SetDirty Method

**Summary:** Forces this project to be marked as changed since the last call toSave.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetDirty()
```

---

## IArchivable2.GetSerializableValue Method (String, IArchiveVersionInfo, IArchiveReporter)

**Summary:** Returns the value with the specified symbolic name to be used for serialization, with
            respect to the version profile specified in theinfoparameter.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object GetSerializableValue(
	string stValueName,
	IArchiveVersionInfo info,
	IArchiveReporter reporter
)
```

---

## IArchivable2.GetSerializableValueNames Method

**Summary:** Gets the symbolic names of the values which should be serialized, with respect to the
            version profile specified in theinfoparameter.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string[] GetSerializableValueNames(
	IArchiveVersionInfo info,
	IArchiveReporter reporter
)
```

---

## IArchivable.AfterDeserialize Method

**Summary:** This method is called after the object is deserialized.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AfterDeserialize()
```

---

## IArchivable.BeforeSerialize Method

**Summary:** This method is called before the object is serialized.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void BeforeSerialize()
```

---

## IArchivable.GetSerializableValue Method

**Summary:** Returns the value with the specified symbolic name to be used for serialization.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object GetSerializableValue(
	string stValueName
)
```

---

## IArchivable.SetSerializableValue Method

**Summary:** Sets the value with the specified symbolic name as created during deserialization.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetSerializableValue(
	string stValueName,
	Object value
)
```

---

## IArchiveReader2.CreateSharedDataStorage Method

**Summary:** Creates a shared data storage for this archive reader. A shared data storage contains
            common information shared between multiple archivable objects.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISharedDataStorage CreateSharedDataStorage()
```

---

## IArchiveReader2.Fill Method (IArchivable, ISharedDataStorage)

**Summary:** Fills an existingIArchivableinstance with deserialized values from the
            underlying stream, using the specified shared data storage.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Fill(
	IArchivable obj,
	ISharedDataStorage sds
)
```

---

## IArchiveReader2.Load Method (ISharedDataStorage)

**Summary:** Deserializes the underlying stream and creates anIArchivablegraph,
            using the specified shared data storage.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IArchivable Load(
	ISharedDataStorage sds
)
```

---

## IArchiveReader.Fill Method

**Summary:** Fills an existingIArchivableinstance with deserialized values from the
            underlying stream.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Fill(
	IArchivable obj
)
```

---

## IArchiveReader.Initialize Method (Stream)

**Summary:** Initializes thisIArchiveReaderinstance to load from the specified
            stream.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	Stream stream
)
```

---

## IArchiveReader.Initialize Method (String)

**Summary:** Initializes thisIArchiveReaderinstance to load from the specified file
            path.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	string stFileName
)
```

---

## IArchiveReader.Load Method

**Summary:** Deserializes the underlying stream and creates anIArchivablegraph.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IArchivable Load()
```

---

## IArchiveReporter.Cancel Method

**Summary:** This method is called when an error occurs during serialization or deserialization. The
            code that triggered the serialization should discard the resulting stream because it
            will not be correctly formatted in this case. The code that triggered the
            deserialization should discard the resulting object because it might be inconsistent.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Cancel(
	string stMessage
)
```

---

## IArchiveReporter.Warn Method

**Summary:** This method is called when a warning occurs during serialization or deserialization.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Warn(
	string stMessage
)
```

---

## IArchiveVersionInfo.GetCurrentVersion Method

**Summary:** Gets the version number of the specified object's type in the current version profile.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Version GetCurrentVersion(
	Object obj
)
```

---

## IArchiveVersionInfo.GetTargetVersion Method

**Summary:** Gets the version number of the specified object's type in the version profile specified
            inProfile.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Version GetTargetVersion(
	Object obj
)
```

---

## IArchiveWriter2.CreateSharedDataStorage Method

**Summary:** Creates a shared data storage for this archive writer. A shared data storage contains
            common information shared between multiple archivable objects.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISharedDataStorage CreateSharedDataStorage()
```

---

## IArchiveWriter2.Initialize Method (Stream, Encoding, Boolean)

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified stream.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	Stream stream,
	Encoding encoding,
	bool bOmitXMLDeclaration
)
```

---

## IArchiveWriter2.Initialize Method (String, Encoding, Boolean)

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified file
            path.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	string stFileName,
	Encoding encoding,
	bool bOmitXMLDeclaration
)
```

---

## IArchiveWriter2.Save Method (IArchivable, ISharedDataStorage)

**Summary:** Serializes the specifiedIArchivablegraph to the underlying stream,
            using the specified shared data storage.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Save(
	IArchivable obj,
	ISharedDataStorage sds
)
```

---

## IArchiveWriter2.Save Method (IArchivable2, Profile, IArchiveReporter)

**Summary:** Serializes the specifiedIArchivable2graph to the underlying stream. The
            resulting stream will be compatible to the version specified by theprofileparameter.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Save(
	IArchivable2 obj,
	Profile profile,
	IArchiveReporter reporter
)
```

---

## IArchiveWriter2.Save Method (IArchivable2, ISharedDataStorage, Profile, IArchiveReporter)

**Summary:** Serializes the specifiedIArchivable2graph to the underlying stream,
            using the specified shared data storage. The resulting stream will be compatible to the
            version specified by theprofileparameter.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Save(
	IArchivable2 obj,
	ISharedDataStorage sds,
	Profile profile,
	IArchiveReporter reporter
)
```

---

## IArchiveWriter.Initialize Method (Stream, Encoding)

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified stream.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	Stream stream,
	Encoding encoding
)
```

---

## IArchiveWriter.Initialize Method (String, Encoding)

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified file
            path.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Initialize(
	string stFileName,
	Encoding encoding
)
```

---

## IArchiveWriter.Save Method

**Summary:** Serializes the specifiedIArchivablegraph to the underlying stream.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Save(
	IArchivable obj
)
```

---

## IEmbeddedObject.GetContentString Method

**Summary:** Gets the string content in the specified range.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetContentString(
	ref long nPosition,
	ref int nLength,
	bool bWord
)
```

---

## IEmbeddedObject.GetPositionText Method

**Summary:** Gets a user-friendly display text for the specified position within this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetPositionText(
	long nPosition
)
```

---

## IMetaObject2.ReplaceObject Method

**Summary:** Replaces the contained object by another object. This operation is only permitted if
            this is a writable metaobject.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ReplaceObject(
	IObject obj
)
```

---

## IMetaObjectStub.GetProperty Method

**Summary:** Gets the object property with the specified GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObjectProperty GetProperty(
	Guid propertyGuid
)
```

---

## IMetaObject.AddProperty Method

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddProperty(
	IObjectProperty property
)
```

---

## IMetaObject.GetProperty Method

**Summary:** Gets the object property with the specified GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObjectProperty GetProperty(
	Guid propertyGuid
)
```

---

## IMetaObject.RemoveProperty Method

**Summary:** Removes the object property with the specified GUID from this object. If the property
            does not exist, does nothing.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RemoveProperty(
	Guid propertyGuid
)
```

---

## IObject2.AcceptsTopLevel Method

**Summary:** Checks whether this object is currently able to be inserted top level in the given
            project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool AcceptsTopLevel(
	int nProjectHandle
)
```

---

## IObject.AcceptsChildObject Method

**Summary:** Checks whether this object is currently able to have a child of the specified type.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool AcceptsChildObject(
	Type childObjectType
)
```

---

## IObject.AcceptsParentObject Method

**Summary:** Checks whether this object is currently able to be a child of the specified parent
            object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool AcceptsParentObject(
	IObject parentObject
)
```

---

## IObject.CheckName Method

**Summary:** Checks whether the specified name is valid for this object. For example, a POU object
            might want to restrict its name to be a valid IEC 61131-3 identifier, whereas a folder
            object does not want to restrict its name at all.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool CheckName(
	string stName
)
```

---

## IObject.CheckRelationships Method

**Summary:** Check the parent/child relationships of this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int CheckRelationships(
	IObject parentObject,
	IObject[] childObjects
)
```

---

## IObject.GetContentString Method

**Summary:** Gets the string content in the specified range.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetContentString(
	ref long nPosition,
	ref int nLength,
	bool bWord
)
```

---

## IObject.GetPositionText Method

**Summary:** Gets a user-friendly display text for the specified position within this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetPositionText(
	long nPosition
)
```

---

## IObject.HandleRenamed Method

**Summary:** This method is called when the name of this object has been changed. Implementations
            might adapt their internal data in this method appropriately.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void HandleRenamed()
```

---

## IOrderedSubObjects.AcceptsChildObject Method

**Summary:** Checks whether this object is currently able to have a child of the specified type at
            the specified index.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool AcceptsChildObject(
	Type childObjectType,
	int nIndex
)
```

---

## IOrderedSubObjects.AddChild Method

**Summary:** Called after a child object has been added to the Object Manager.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddChild(
	Guid subObjectGuid,
	int nIndex
)
```

---

## IOrderedSubObjects.GetChildIndex Method

**Summary:** Gets the zero-based index of the specified child object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int GetChildIndex(
	Guid subObjectGuid
)
```

---

## IOrderedSubObjects.RemoveChild Method

**Summary:** Called after a child object has been removed from the Object Manager.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RemoveChild(
	IMetaObject moRemoved
)
```

---

## ISVFoldersProperty.GetParentObject Method

**Summary:** Gets the object GUID of the folder object which is the parent of the corresponding
            object in the specified structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid GetParentObject(
	Guid structuredView
)
```

---

## ISVFoldersProperty.SetParentObject Method

**Summary:** Sets the object GUID of the folder object which is the parent of the corresponding
            object in the specified structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool SetParentObject(
	Guid structuredView,
	Guid parentObject
)
```

---

## ISVNode.AddObject Method

**Summary:** Adds a child object. This object is added to this structured view as well as to the
            corresponding Object Manager project (i.e. this object will also be visible for other
            structured views). See[!:IObjectManager.AddObject]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddObject(
	Guid objectGuid,
	IObject obj,
	string stName,
	int nIndex
)
```

---

## ISVNode.CanPasteFromStream Method

**Summary:** Do not use this method. UseCanPasteFromStream(ISVNode, Stream)instead.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool CanPasteFromStream(
	Stream stream
)
```

---

## ISVNode.CopyToStream Method

**Summary:** Do not use this method. UseCopyToStream(ISVNode, Stream, Boolean)instead.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CopyToStream(
	Stream stream
)
```

---

## ISVNode.ExportObject Method

**Summary:** Exports this object into two byte arrays.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ExportObject(
	out byte[] metaObjectData,
	out byte[] objectData
)
```

---

## ISVNode.GetChild Method

**Summary:** Returns thenIndex-th child node of this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode GetChild(
	int nIndex
)
```

---

## ISVNode.GetFullName Method

**Summary:** Gets the full name of the object represented by this structured view node. See[!:IObjectManager.GetFullName]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetFullName()
```

---

## ISVNode.GetMetaObjectStub Method

**Summary:** Returns a meta-object stub of the object represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IMetaObjectStub GetMetaObjectStub()
```

---

## ISVNode.GetObjectToModify Method

**Summary:** Returns a modifiable copy of the object represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IMetaObject GetObjectToModify()
```

---

## ISVNode.GetObjectToRead Method

**Summary:** Returns a readable copy of the object represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IMetaObject GetObjectToRead()
```

---

## ISVNode.MoveObject Method

**Summary:** Moves this structured view node to another parent node. This change is also reflected
            in the corresponding Object Manager project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void MoveObject(
	ISVNode newParentNode,
	int nNewIndex
)
```

---

## ISVNode.PasteFromStream Method

**Summary:** Do not use this method. UsePasteFromStream(ISVNode, Stream, StructuredViewPasteNodeEventHandler, StructuredViewPasteConflictEventHandler)instead.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void PasteFromStream(
	Stream stream
)
```

---

## ISVNode.Remove Method

**Summary:** Removes this structured view node recursively. The corresponding objects will also be
            removed from the Object Manager project. See[!:IObjectManager.RemoveObject]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Remove()
```

---

## ISVNode.Rename Method

**Summary:** Renames the object which is represented by this structured view node. See[!:IObjectManager.RenameObject]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Rename(
	string stNewName
)
```

---

## ISVNode.RenameObject Method

**Summary:** Equalivalent toRename(String).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RenameObject(
	string stNewName
)
```

---

## ISharedDataStorage.Load Method

**Summary:** Loads the shared data storage information.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Load(
	Stream stringTableStream,
	Stream schemaTableStream
)
```

---

## ISharedDataStorage.Save Method

**Summary:** Saves the shared data storage information.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Save(
	Stream stringTableStream,
	Stream schemaTableStream
)
```

---

## IStructuredView.AddObject Method

**Summary:** Adds a top-level object. This object is added to this structured view as well as to the
            corresponding Object Manager project (i.e. this object will also be visible for other
            structured views). See[!:IObjectManager.AddObject]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddObject(
	Guid objectGuid,
	IObject obj,
	string stName
)
```

---

## IStructuredView.CanPasteFromStream Method

**Summary:** Returns a value indicating whether the contents of the specified stream (which was
            previously filled byCopyToStream(ISVNode, Stream, Boolean)) can be pasted below a destination
            node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool CanPasteFromStream(
	ISVNode destNode,
	Stream stream
)
```

---

## IStructuredView.CopyToStream Method

**Summary:** Copies the specified structured view nodes into a data stream. This data stream will
            then contain the hierarchical information as well as the object data itself. This
            method can be used to implement clipboard functionality.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CopyToStream(
	ISVNode[] nodes,
	Stream stream,
	bool bRecursive
)
```

---

## IStructuredView.GetChild Method

**Summary:** Returns thenIndex-th top-level node of this structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode GetChild(
	int nIndex
)
```

---

## IStructuredView.GetNode Method

**Summary:** Returns the structured view node which corresponds to the specified object. The search
            is performed recursively.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode GetNode(
	Guid objectGuid
)
```

---

## IStructuredView.MergeFromStream Method

**Summary:** Do not use this method as its exact semantics is not clearly defined yet. UsePasteFromStream(ISVNode, Stream, StructuredViewPasteNodeEventHandler, StructuredViewPasteConflictEventHandler)instead.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void MergeFromStream(
	Stream stream,
	StructuredViewPasteNodeEventHandler progressHandler,
	StructuredViewPasteConflictEventHandler conflictHandler
)
```

---

## IStructuredView.PasteFromStream Method

**Summary:** Pastes the contents of the specified stream (which was previously filled byCopyToStream(ISVNode, Stream, Boolean)) below a destination node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void PasteFromStream(
	ISVNode destNode,
	Stream stream,
	StructuredViewPasteNodeEventHandler progressHandler,
	StructuredViewPasteConflictEventHandler conflictHandler
)
```

---

## IStructuredView.Remove Method

**Summary:** Removes the specified structured view nodes. The corresponding objects will also be
            removed from the Object Manager project. See[!:IObjectManager.RemoveObject]for further details.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Remove(
	ISVNode[] nodes
)
```

---

## IUniqueIdGenerator.GetNext Method

**Summary:** Returns the next ID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
long GetNext(
	bool bMarkAsUsed
)
```

---

## IUniqueIdGenerator.IsUsed Method

**Summary:** Checks whether the specified ID is already in use.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsUsed(
	long nId
)
```

---

## IUniqueIdGenerator.Reset Method

**Summary:** Resets the ID generator.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Reset()
```

---

## IUniqueIdGenerator.RestoreFromString Method

**Summary:** Restores the state of this ID generator from the specified string which has previously
            been generated byStoreToString.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RestoreFromString(
	string st
)
```

---

## IUniqueIdGenerator.StoreToString Method

**Summary:** Stores the state of this ID generator into a string. This string can later be used to
            callRestoreFromString(String).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string StoreToString()
```

---

## IUniqueIdGenerator.Use Method

**Summary:** Marks a specified ID as used. This ID will not be returned byGetNext(Boolean)any
            more unlessResetis called.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Use(
	long nId
)
```

---

## ObjectManagerException.FormatMessage Method

**Summary:** Gets a formatted message string for this exception. It is required that a string
            resource with the same name as the exception class is defined.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected string FormatMessage(
	params Object[] args
)
```

---

## ObjectManagerException Constructor (Int32, Guid, String)

**Summary:** Creates a new instance of theObjectManagerExceptionclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
[ObsoleteAttribute("Use the other constructor.", true)]
protected ObjectManagerException(
	int nProjectHandle,
	Guid objectGuid,
	string stReason
)
```

---

## ObjectManagerException Constructor (Int32, Guid, String, String)

**Summary:** Initializes a new instance of theObjectManagerExceptionclass

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected ObjectManagerException(
	int nProjectHandle,
	Guid objectGuid,
	string stReason,
	string stObjectName
)
```

---

## ObjectNameInvalidException Constructor (Int32, Guid, String)

**Summary:** Initializes a new instance of theObjectNameInvalidExceptionclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ObjectNameInvalidException(
	int nProjectHandle,
	Guid objectGuid,
	string stName
)
```

---

## ObjectNameInvalidException Constructor (Int32, Guid, String, String)

**Summary:** Initializes a new instance of theObjectNameInvalidExceptionclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ObjectNameInvalidException(
	int nProjectHandle,
	Guid objectGuid,
	string stName,
	string stMessage
)
```

---

## SVNodeEventArgs Constructor

**Summary:** Creates a new instance of theSVNodeEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public SVNodeEventArgs(
	ISVNode svNode,
	int nIndex
)
```

---

## SVNodeModifiedEventArgs Constructor

**Summary:** Creates a new instance of theSVNodeModifiedEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public SVNodeModifiedEventArgs(
	ISVNode svNode,
	Object editor
)
```

---

## SVNodeMovedEventArgs Constructor

**Summary:** Creates a new instance of theSVNodeMovedEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public SVNodeMovedEventArgs(
	ISVNode svNode,
	ISVNode svOldParent,
	ISVNode svNewParent,
	int nOldIndex,
	int nNewIndex
)
```

---

## SVNodePropertyModifiedEventArgs Constructor

**Summary:** Creates a new instance of theSVNodePropertyModifiedEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public SVNodePropertyModifiedEventArgs(
	ISVNode svNode,
	IObjectProperty oldProperty,
	IObjectProperty newProperty
)
```

---

## SVNodeRenamedEventArgs Constructor

**Summary:** Creates a new instance of theSVNodeRenamedEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public SVNodeRenamedEventArgs(
	ISVNode svNode,
	string stOldName,
	string stNewName
)
```

---

## StructuredViewPasteConflictEventArgs.GetOverwriteFlag Method

**Summary:** Gets a flag indicating whether the specified paste conflict should be resolved by
            overwriting the conflicting object or not.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public bool GetOverwriteFlag(
	int nConflictIndex
)
```

---

## StructuredViewPasteConflictEventArgs.SetOverwriteFlag Method

**Summary:** Sets a flag indicating whether the specified paste conflict should be resolved by
            overwriting the conflicting object or not.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void SetOverwriteFlag(
	int nConflictIndex,
	bool bOverwrite
)
```

---

## StructuredViewPasteConflictEventArgs Constructor

**Summary:** Creates a new instance of theStructuredViewPasteConflictEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public StructuredViewPasteConflictEventArgs(
	PasteConflict[] conflicts
)
```

---

## StructuredViewPasteNodeEventArgs Constructor

**Summary:** Creates a new instance of theStructuredViewPasteNodeEventArgsclass.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public StructuredViewPasteNodeEventArgs(
	string stName,
	Guid parentSVNodeGuid,
	Guid objectGuid,
	IObject obj,
	IObjectProperty[] properties,
	Exception exception
)
```

---

## Credentials Constructor

**Summary:** Initializes a new instance of theCredentialsclass

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected Credentials()
```

---

## IDeviceAddress.Equals Method

**Summary:** Determine wether this DeviceAddress object andaddressdenote the same address.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Equals(
	IDeviceAddress address
)
```

---

## IDeviceAddress.IsAncestorOf Method

**Summary:** Determine whether this device address is an ancestor node ofaddress.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsAncestorOf(
	IDeviceAddress address
)
```

---

## IDeviceAddress.IsValidAddress Method

**Summary:** Check wether the address provided is in a valid format.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsValidAddress(
	string stAddress
)
```

---

## IDeviceAddress.SetAddress Method

**Summary:** Set the address coded in a string

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetAddress(
	string stAddress
)
```

---

## IDeviceAddress.ToString Method

**Summary:** Create a string representation of this address, eg. 0.123.5

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string ToString()
```

---

## IDeviceGroupList.Add Method

**Summary:** Adds a new group with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceGroup Add(
	string stName
)
```

---

## IDeviceGroupList.Clear Method

**Summary:** Removes all groups.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Clear()
```

---

## IDeviceGroupList.Remove Method

**Summary:** Removes the group with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Remove(
	string stName
)
```

---

## IDeviceGroup.CheckCyclicMembership Method

**Summary:** Checks whether adding the specified group member would cause a cyclic membership
            dependency.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool CheckCyclicMembership(
	string stNewGroupMember
)
```

---

## IDeviceUser2.SetFlags Method

**Summary:** Method to set the flags.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetFlags(
	DeviceUserManagementFlags flags
)
```

---

## IDeviceUserList.Add Method

**Summary:** Adds a new user with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceUser Add(
	string stName
)
```

---

## IDeviceUserList.Clear Method

**Summary:** Removes all users.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Clear()
```

---

## IDeviceUserList.Remove Method

**Summary:** Removes the user with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Remove(
	string stName
)
```

---

## IDeviceUser.SetPassword Method

**Summary:** Sets the password for this user.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetPassword(
	string stPassword
)
```

---

## IGatewayDriver.CreateDeviceAddress Method

**Summary:** Create an empty device address.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceAddress CreateDeviceAddress()
```

---

## IGatewayDriver.CreateDeviceAddress Method (String)

**Summary:** Create a new device address for this gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceAddress CreateDeviceAddress(
	string stAddress
)
```

---

## IGatewayDriver.CreateParams Method

**Summary:** Create an instance of an IGatewayParams object suitable for this
            gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IGatewayParams CreateParams()
```

---

## IGatewayDriver.GetParameterDescriptions Method

**Summary:** Get a list with the descriptions of all parameters which this driver
            expects in a call to Connect().

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IGatewayParamDescription[] GetParameterDescriptions()
```

---

## IGatewayParamDescription.Validate Method

**Summary:** Check whether the provided object is a valid value for this
            parameter.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Validate(
	Object value
)
```

---

## IGatewayParams.Equals Method

**Summary:** Check this object for equality to another IGatewayParams object.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Equals(
	IGatewayParams gwparams
)
```

---

## IGateway.AddDeviceToCache Method

**Summary:** Add a device to the gateways cache.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddDeviceToCache(
	ITargetDescription device
)
```

---

## IGateway.BeginConnect Method

**Summary:** Asynchronous version ofConnect.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginConnect(
	AsyncCallback callback,
	Object state
)
```

---

## IGateway.BeginEnumDevices Method

**Summary:** Starts a network scan on the gateway. For each answering deviceCopy1deviceCallbackwill be called once.
            This function also rebuilds the device cache of this gateway. Only devices marked asLockToCacheare not deleted from the cache, 
            but they may be updated.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
1deviceCallback
```

---

## IGateway.ClearDeviceCache Method

**Summary:** Remove all cached devices, except those marked asLockToCache

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ClearDeviceCache()
```

---

## IGateway.Connect Method

**Summary:** Open a connection to the gateway.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Connect()
```

---

## IGateway.Disconnect Method

**Summary:** Disconnects from the Gateway.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Disconnect()
```

---

## IGateway.EndConnect Method

**Summary:** Waits for a pendingBeginConnect(AsyncCallback, Object)operation to complete.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndConnect(
	IAsyncResult asyncResult
)
```

---

## IGateway.EndEnumDevices Method

**Summary:** Waits for a pendingBeginEnumDevices(EnumDevicesCallback, AsyncCallback, Object)operation. When errors occured during
            the call then an appropriateOnlineManagerExceptionis thrown.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndEnumDevices(
	IAsyncResult asyncResult
)
```

---

## IGateway.GetCachedDevices Method

**Summary:** Gets the list of devices reachable via this gateway. This returns the cached list
            of devices retrieved by the last call toBeginEnumDevices(EnumDevicesCallback, AsyncCallback, Object).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ITargetDescription[] GetCachedDevices()
```

---

## IGateway.Matches Method

**Summary:** Check whether the driver GUID and the parameters of the gateway
            are equal to the provided guid and parameters.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Matches(
	Guid guidDriver,
	IGatewayParams parameters
)
```

---

## IGateway.RemoveDeviceFromCache Method

**Summary:** Removedevicefrom the device cache.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RemoveDeviceFromCache(
	ITargetDescription device
)
```

---

## IOnlineApplication10.ReadApplicationInfo Method

**Summary:** Reads information about the online application from the runtime system.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IOnlineApplicationInfo ReadApplicationInfo()
```

---

## IOnlineApplication11.DownloadNoGenerateCode Method

**Summary:** theDownload(Boolean)-Command performsGenerateCode(Guid, Boolean, Boolean)on the application.
            Sometimes its better to call the command on the outside, to be able to react on the result.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void DownloadNoGenerateCode(
	bool bOnlineChange
)
```

---

## IOnlineApplication11.StreamDownloadCommandForHexFile Method

**Summary:** A method to get the binary content of a boot project into a memory stream.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void StreamDownloadCommandForHexFile(
	BinaryWriter writer
)
```

---

## IOnlineApplication13.AddFlowExpression Method

**Summary:** INTERNAL USE

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddFlowExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication13.RemoveFlowExpression Method

**Summary:** AddFlowExpression(IMonitoringExpression)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RemoveFlowExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication13.ResumeFlowExpression Method

**Summary:** Continue monitoring this IFlowVarRef when previously stopped by a call
            to SuspendMonitoring. Multiple successive calls to this method have the 
            same effect as a single call.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ResumeFlowExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication13.SuspendFlowExpression Method

**Summary:** Stop monitoring on this IFlowVarRef until ResumeMonitoring is called.
            Multiple successive calls to this method have the same effect as a single call.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SuspendFlowExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication14.ReadApplicationContent Method

**Summary:** reads the content of the application on the runtime. Will only succeed for runtime versions >= 3.5.0.0

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IApplicationContent ReadApplicationContent()
```

---

## IOnlineApplication3.CreateBootProject Method

**Summary:** Create bootproject on device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CreateBootProject()
```

---

## IOnlineApplication4.GetPersistentInfo Method

**Summary:** Get the length of and crc over the persistent data area of this application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void GetPersistentInfo(
	out uint uiCRC,
	out uint uiLength
)
```

---

## IOnlineApplication4.ReinitAppOnDevice Method

**Summary:** Reinitialize the application on the device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ReinitAppOnDevice(
	string stParentAppName,
	bool bForceCreate
)
```

---

## IOnlineApplication5.GetForcedVarRefs Method

**Summary:** Gets a list of all OnlineVarRefs which are currently forced. This will never returnnull. Instead, an empty array will be returned if no forced variable exists.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IOnlineVarRef[] GetForcedVarRefs()
```

---

## IOnlineApplication7.DownloadSystemApplication Method

**Summary:** function to download special system applications.
            throws exception if generate code failed

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void DownloadSystemApplication(
	string stLibraryId
)
```

---

## IOnlineApplication8.CheckFileConsistency Method

**Summary:** check if downloaded application matches to boot application and project archive

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CheckFileConsistency(
	out bool bBootProjectUpToDate,
	out bool bArchiveUpToDate
)
```

---

## IOnlineApplication.AddMonitoringExpression Method

**Summary:** INTERNAL USE

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void AddMonitoringExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication.BeginDownload Method

**Summary:** Asynchronous version ofDownload(Boolean).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginDownload(
	AsyncCallback callback,
	Object state,
	bool bOnlineChange
)
```

---

## IOnlineApplication.BeginLogin Method

**Summary:** Asynchronous version of theLogin(Boolean)operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginLogin(
	AsyncCallback callback,
	Object state
)
```

---

## IOnlineApplication.BeginLogout Method

**Summary:** Asynchronous version ofLogout

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginLogout(
	AsyncCallback callback,
	Object state
)
```

---

## IOnlineApplication.ClearPermanentBreakpoint Method

**Summary:** Removes the specified permanent breakpoint from the runtime system.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ClearPermanentBreakpoint(
	ICompiledPOU compiledPOU,
	IBreakpoint breakpoint
)
```

---

## IOnlineApplication.CreateAppOnDevice Method

**Summary:** creates a new application on device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CreateAppOnDevice(
	string stParentObjectName
)
```

---

## IOnlineApplication.Download Method

**Summary:** Download the application to the target device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Download(
	bool bOnlineChange
)
```

---

## IOnlineApplication.EndDownload Method

**Summary:** Waits for a pendingBeginDownload(AsyncCallback, Object, Boolean)operation to complete.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndDownload(
	IAsyncResult asyncResult
)
```

---

## IOnlineApplication.EndLogin Method

**Summary:** Waits for a pendingBeginLogin(AsyncCallback, Object)operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndLogin(
	IAsyncResult asyncResult
)
```

---

## IOnlineApplication.EndLogout Method

**Summary:** Waits for a pendingBeginLogout(AsyncCallback, Object)operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndLogout(
	IAsyncResult asyncResult
)
```

---

## IOnlineApplication.ForceVariables Method

**Summary:** Force the prepared values ofvariables.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ForceVariables(
	IOnlineVarRef[] variables
)
```

---

## IOnlineApplication.Login Method

**Summary:** Login to the application on the target device: 
            
            Establish a connection to the applications target device.
            
            Check application version. If code-id or data-id doesn't match, inform user and allow
            for interactive download of the current application.
            Register this application as a debugging client
            This operation may trigger aProvideCredentialsHandlercallback.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Login(
	bool bTest
)
```

---

## IOnlineApplication.Logout Method

**Summary:** Logout from an application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Logout()
```

---

## IOnlineApplication.ReleaseForceValues Method

**Summary:** will reset the list of forced values in the runtime and in the onlineapplication.
            Must not be called while the application is not logged in!

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool ReleaseForceValues()
```

---

## IOnlineApplication.RemoveMonitoringExpression Method

**Summary:** AddMonitoringExpression(IMonitoringExpression)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void RemoveMonitoringExpression(
	IMonitoringExpression monexp
)
```

---

## IOnlineApplication.Reset Method

**Summary:** Reset the application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Reset(
	ResetOption option
)
```

---

## IOnlineApplication.SetNextStatement Method

**Summary:** Resume execution at the specified breakpoint position.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetNextStatement(
	IBreakpoint breakpoint,
	ICompiledPOU compiledPOU
)
```

---

## IOnlineApplication.SetPermanentBreakpoint Method

**Summary:** Sets a permanent breakpoint in the runtime system. Permanent breakpoints remain set
            until logout or an explicit removal viaClearPermanentBreakpoint(ICompiledPOU, IBreakpoint). If a
            breakpoint at the specified position is already set, this breakpoint will be
            overwritten.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetPermanentBreakpoint(
	ICompiledPOU compiledPOU,
	IBreakpoint breakpoint,
	string stInstancePath,
	string[] tasks,
	HitCountCondition hitCountCondition,
	int nHitCount
)
```

---

## IOnlineApplication.SetTemporaryBreakpoint Method

**Summary:** Sets a temporary breakpoint in the runtime system. Temporary breakpoints remain set
            until a breakpoint (no matter whether permanent or temporary) is hit. If a temporary
            breakpoint is set at a position where a permanent breakpoint already is set, the
            temporary breakpoint will be set with a higher priority (overriding conditions of the
            permanent breakpoint).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetTemporaryBreakpoint(
	ICompiledPOU compiledPOU,
	IBreakpoint breakpoint,
	string stInstancePath,
	string[] tasks
)
```

---

## IOnlineApplication.SingleCycle Method

**Summary:** perform one single cycle on application. Requires an active login.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SingleCycle()
```

---

## IOnlineApplication.Start Method

**Summary:** Start the application. Requires an active login.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Start()
```

---

## IOnlineApplication.Stop Method

**Summary:** Stop the application. Requires an active login.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Stop()
```

---

## IOnlineApplication.StreamDownloadCommand Method

**Summary:** For Create offline boot project: streams the download command to the passed binary writer.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void StreamDownloadCommand(
	BinaryWriter writer
)
```

---

## IOnlineApplication.WriteVariables Method

**Summary:** Write the prepared values ofvariables.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void WriteVariables(
	IOnlineVarRef[] variables
)
```

---

## IOnlineDevice.BeginConnect Method

**Summary:** Asynchronous version of theConnectmethod.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginConnect(
	AsyncCallback callback,
	Object state
)
```

---

## IOnlineDevice.BeginDisconnect Method

**Summary:** Disconnect asynchronously.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginDisconnect(
	AsyncCallback callback,
	Object state
)
```

---

## IOnlineDevice.BeginExecuteService Method

**Summary:** Execute a service asynchronously (ExecuteService(IServiceWriter)).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IAsyncResult BeginExecuteService(
	IServiceWriter service,
	AsyncCallback callback,
	Object state
)
```

---

## IOnlineDevice.Connect Method

**Summary:** Establish the connection to the device. If required by the target device, 
            authentication is performed. This may initiate aProvideCredentialsHandler

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Connect()
```

---

## IOnlineDevice.CreateCustomService Method

**Summary:** Create an instance of a custom service writer with a custom protocol id.
            After filling the instance with the service parameters it can be
            passed toExecuteService(IServiceWriter).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ICustomServiceWriter CreateCustomService(
	long lCommandGroup,
	int nCommand,
	int nProtocolId
)
```

---

## IOnlineDevice.CreateService Method (Int64, Int32)

**Summary:** Create an instance of a service writer using the standard 
            service protocol (0xCD55 or 0x55CD respectivly, depending on the
            byteorder). Uses the targets byteorder. 
            After filling the instance with the service parameters it can be
            passed toExecuteService(IServiceWriter).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ITaggedServiceWriter CreateService(
	long lCommandGroup,
	int nCommand
)
```

---

## IOnlineDevice.CreateService Method (Int64, Int32, Int32)

**Summary:** Create an instance of a standard tagged service writer with a custom protocol id.
            After filling the instance with the service parameters it can be
            passed toExecuteService(IServiceWriter).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ITaggedServiceWriter CreateService(
	long lCommandGroup,
	int nCommand,
	int nProtocolId
)
```

---

## IOnlineDevice.DeleteApplication Method

**Summary:** Deletes the specified application from this device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void DeleteApplication(
	string stApplication
)
```

---

## IOnlineDevice.Disconnect Method

**Summary:** Disconnect and free resources on the target device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Disconnect()
```

---

## IOnlineDevice.EndConnect Method

**Summary:** Waits for a pendingBeginConnect(AsyncCallback, Object)operation to complete.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndConnect(
	IAsyncResult asyncResult
)
```

---

## IOnlineDevice.EndDisconnect Method

**Summary:** Used to finish a previous call toBeginDisconnect(AsyncCallback, Object)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void EndDisconnect(
	IAsyncResult asyncResult
)
```

---

## IOnlineDevice.EndExecuteService Method

**Summary:** Used to retrieve the result of a previous call toBeginExecuteService(IServiceWriter, AsyncCallback, Object)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceReader EndExecuteService(
	IAsyncResult asyncResult
)
```

---

## IOnlineDevice.ExecuteService Method

**Summary:** Execute a service synchronously. You can obtain a IServiceWriter instance
            by theCreateService(Int64, Int32),CreateService(Int64, Int32, Int32)orCreateCustomService(Int64, Int32, Int32)calls.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceReader ExecuteService(
	IServiceWriter service
)
```

---

## IOnlineDevice.ReadApplicationList Method

**Summary:** Reads the complete list of applications currently available on this device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string[] ReadApplicationList()
```

---

## IOnlineDevice.ReadApplicationList Method (Int32, Int32)

**Summary:** Reads a part of the list of applications currently available on this device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string[] ReadApplicationList(
	int nStartIndex,
	int nMaxCount
)
```

---

## IOnlineVarRef.GetStateMessage Method

**Summary:** Get a string describing the current VarRefState. The string will also be used 
            in the message of exceptions thrown byRawValueandValue.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string GetStateMessage()
```

---

## IOnlineVarRef.Release Method

**Summary:** Release the OnlineVarRef and all resources held by it, after it isn't used any more.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Release()
```

---

## IOnlineVarRef.ResumeMonitoring Method

**Summary:** Continue monitoring this IOnlineVarRef when previously stopped by a call
            to SuspendMonitoring. Multiple successive calls to this method have the 
            same effect as a single call.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void ResumeMonitoring()
```

---

## IOnlineVarRef.SuspendMonitoring Method

**Summary:** Stop monitoring on this IOnlineVarRef until ResumeMonitoring is called.
            Multiple successive calls to this method have the same effect as a single call.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SuspendMonitoring()
```

---

## IProvideCredentialsArgs.Cancel Method

**Summary:** Called by the event handler to cancel the operation instead of providing credentials.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Cancel(
	Exception ex
)
```

---

## IServiceReader.Close Method

**Summary:** Close the reader and free resources.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
void Close()
```

---

## IServiceReader.GetContent Method

**Summary:** Get the services content as a byte array. This method allows access to the content
            if anything else then the CoDeSys protocol is used for the service 
            (HeaderTag).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] GetContent()
```

---

## IServiceReader.GetEnumerator Method

**Summary:** Allows for iteration through the toplevel tags of the service,
            eg. by means of a foreach loop.
            Do not use if the service protocol is not the CoDeSys protocol.HeaderTag

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceTagEnumerator GetEnumerator()
```

---

## IServiceTagEnumerator.MoveNext Method

**Summary:** Move to the next element. Initially the enumerator is positioned 
            before the first element. Therefore MoveNext must be called beforeCurrentis accessed for the first time.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool MoveNext()
```

---

## IServiceTagReader.GetEnumerator Method

**Summary:** Allows for iteration through the subtags of this tag.
            The subtags must be returned in the same order they appear within
            the tag.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceTagEnumerator GetEnumerator()
```

---

## IServiceTagReader.ReadByte Method

**Summary:** Read the next content byte.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte ReadByte()
```

---

## IServiceTagReader.ReadBytes Method

**Summary:** Return the content from the current position to the end of the
            tag as an array of bytes.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] ReadBytes()
```

---

## IServiceTagReader.ReadBytes Method (Int32)

**Summary:** Return the content from the current position to the end of the
            tag but no more then nMaxBytes as an array of bytes.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] ReadBytes(
	int nMaxBytes
)
```

---

## IServiceTagReader.ReadInt Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ReadInt()
```

---

## IServiceTagReader.ReadLong Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long ReadLong()
```

---

## IServiceTagReader.ReadShort Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
short ReadShort()
```

---

## IServiceTagReader.ReadString Method

**Summary:** Read a string of the specified type. This function reads until 
            a terminating zero character is found or until the end of the content.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string ReadString(
	Encoding encoding
)
```

---

## IServiceTagReader.ReadUInt Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
uint ReadUInt()
```

---

## IServiceTagReader.ReadULong Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ulong ReadULong()
```

---

## IServiceTagReader.ReadUShort Method

**Summary:** Read the next content element.
            The target byteorder is taken into account.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ushort ReadUShort()
```

---

## ITemporaryLoginCredentialsContext.QueryForCredentials Method

**Summary:** Queries for credentials.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool QueryForCredentials(
	Object sender,
	IProvideCredentialsArgs args
)
```

---

## InvalidDeviceAddress Constructor

**Summary:** Creates an InvalidDeviceAddress.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public InvalidDeviceAddress(
	string stMessage
)
```

---

## InvalidVarRefException Constructor

**Summary:** Create an InvalidVarRefException

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public InvalidVarRefException(
	string message
)
```

---

## NoMonitoringValueException Constructor

**Summary:** Create a NoMonitoringValueException

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public NoMonitoringValueException(
	string message
)
```

---

## OnlineCancelDownloadEventArgs Constructor

**Summary:** Constructor.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineCancelDownloadEventArgs(
	Guid guidObject,
	KindOfDownloadCommand kindof
)
```

---

## OnlineCancelEventArgs.Cancel Method

**Summary:** An event handler calls this method to cancel the operation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public void Cancel(
	Exception ex
)
```

---

## OnlineCancelEventArgs Constructor

**Summary:** Create a cancelable event object.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineCancelEventArgs(
	Guid guidObject
)
```

---

## OnlineDownloadEventArgs Constructor

**Summary:** Constructor.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineDownloadEventArgs(
	Guid guidObject,
	KindOfDownloadCommand kindof
)
```

---

## OnlineEventArgs Constructor

**Summary:** Create an instance of the OnlineEventArgs class

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineEventArgs(
	Guid guidObject
)
```

---

## OnlineManagerException Constructor

**Summary:** Creates an OnlineManagerException.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineManagerException(
	string message
)
```

---

## OnlineResetEventArgs Constructor

**Summary:** Create an reset event object.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public OnlineResetEventArgs(
	Guid guidObject,
	ResetOption resetOption
)
```

---

## PreparedValues Constructor

**Summary:** Initializes a new instance of thePreparedValuesclass

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected PreparedValues()
```

---

## TagTypeException Constructor

**Summary:** Creates a TagTypeException

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public TagTypeException(
	string stMessage,
	int nTagId
)
```

---

## UserPasswordCredentials Constructor

**Summary:** Initializes a new instance of theUserPasswordCredentialsclass

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public UserPasswordCredentials()
```

---

## ProjectAttributes Constructor

**Summary:** Initializes a new instance of theProjectAttributesclass

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected ProjectAttributes()
```

---

## IExtractProjectArchiveNotifyHandler.PromptOverwrite Method

**Summary:** This method is called to prompt the user whether an already existing item or file
            should be overwritten or not.

**Assembly:** `ProjectArchive (in ProjectArchive.dll) Version: 3.5.17.0`

### Syntax
```csharp
PromptOverwriteResult PromptOverwrite(
	string stItemOrFile,
	string stAdditionalText
)
```

---

## IExportReporter.error Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void error(
	IExtendedObject<IScriptObject> obj,
	string message
)
```

---

## IExportReporter.nonexportable Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void nonexportable(
	IExtendedObject<IScriptObject> obj
)
```

---

## IExportReporter.warning Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void warning(
	IExtendedObject<IScriptObject> obj,
	string message
)
```

---

## IImportReporter.added Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void added(
	IExtendedObject<IScriptObject> obj
)
```

---

## IImportReporter.error Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void error(
	string message
)
```

---

## IImportReporter.replaced Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replaced(
	IExtendedObject<IScriptObject> obj
)
```

---

## IImportReporter.resolve_conflict Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
ConflictResolve resolve_conflict(
	IExtendedObject<IScriptObject> obj
)
```

---

## IImportReporter.skipped Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void skipped(
	string objectname
)
```

---

## IImportReporter.warning Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void warning(
	string message
)
```

---

## ILibManager.find_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> find_library(
	string display_name
)
```

---

## ILibManager.get_all_libraries Method (ILibRepository)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_all_libraries(
	ILibRepository repository
)
```

---

## ILibManager.get_all_libraries Method (Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_all_libraries(
	bool exclude_shadowed_libs = true
)
```

---

## ILibManager.get_category Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
ILibCategory get_category(
	Guid guid
)
```

---

## ILibManager.get_file_path Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_file_path(
	IManagedLib library
)
```

---

## ILibManager.get_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IManagedLib get_library(
	string name,
	[OptionalAttribute] ILibRepository repository
)
```

---

## ILibManager.insert_repository Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
ILibRepository insert_repository(
	string rootfolder,
	string name,
	int index = -1
)
```

---

## ILibManager.install_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IManagedLib install_library(
	string filepath,
	[OptionalAttribute] ILibRepository repository,
	bool overwrite = false
)
```

---

## ILibManager.move_repository Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void move_repository(
	ILibRepository repository,
	int new_index
)
```

---

## ILibManager.remove_repository Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_repository(
	ILibRepository repository,
	bool delete_on_disk = false
)
```

---

## ILibManager.uninstall_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void uninstall_library(
	ILibRepository repository,
	IManagedLib library
)
```

---

## ILibManager.update_repository Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void update_repository(
	ILibRepository repository,
	[OptionalAttribute] string new_name,
	[OptionalAttribute] string new_location,
	bool copy_libraries = false
)
```

---

## INativeExportReporter.cancel Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void cancel(
	string message
)
```

---

## INativeExportReporter.skipped Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void skipped(
	string type_name,
	string serializable_value_name
)
```

---

## INativeExportReporter.warn Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void warn(
	string message
)
```

---

## INativeImportHandler.conflict Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
NativeImportResolve conflict(
	string name,
	IExtendedObject<IScriptObject> existingObject,
	Guid newguid
)
```

---

## INativeImportHandler.progress Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void progress(
	string name,
	IExtendedObject<IScriptObject> pastedObject,
	Exception exception
)
```

---

## INativeImportHandler.skipped Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void skipped(
	IList<Object> name
)
```

---

## IScriptApplication2.create_boot_application Method (String, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_boot_application(
	string output_filename,
	bool update_compile_info = false,
	bool write_visu_files = false
)
```

---

## IScriptApplication3.create_task_configuration Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_task_configuration()
```

---

## IScriptApplication.build Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void build()
```

---

## IScriptApplication.clean Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clean()
```

---

## IScriptApplication.create_boot_application Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_boot_application(
	string output_filename
)
```

---

## IScriptApplication.generate_code Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void generate_code()
```

---

## IScriptApplication.rebuild Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rebuild()
```

---

## IScriptComparisonResult.get_changed_objects Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptComparedObject> get_changed_objects(
	ObjectDifferences state = ObjectDifferences.ANY_CHANGES
)
```

---

## IScriptComparisonResult.get_diff_state Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptComparedObject get_diff_state(
	IExtendedObject<IScriptObject> script_object
)
```

---

## IScriptCompoundDataElement.contains Method (IScriptDataElement)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	IScriptDataElement sub_element
)
```

---

## IScriptCompoundDataElement.contains Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	string stIdentifier
)
```

---

## IScriptConnector.get_device_object Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_device_object()
```

---

## IScriptDeviceCollection.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptDeviceCollection.get_devices_of_vendor Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCollection get_devices_of_vendor(
	string vendor
)
```

---

## IScriptDeviceConnectorSet.by_id Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceConnector by_id(
	int id
)
```

---

## IScriptDeviceConnectorSet.contains Method (IScriptDeviceConnector)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	IScriptDeviceConnector element
)
```

---

## IScriptDeviceConnectorSet.contains Method (Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	int id
)
```

---

## IScriptDeviceConnectorSet.contains Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	string visible_name
)
```

---

## IScriptDeviceConnectorSet.get_device_object Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_device_object()
```

---

## IScriptDeviceGroupList.add Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceGroup add(
	string name
)
```

---

## IScriptDeviceGroupList.clear Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clear()
```

---

## IScriptDeviceGroupList.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool remove(
	string name
)
```

---

## IScriptDeviceGroup.check_cyclic_membership Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_cyclic_membership(
	string new_group_member
)
```

---

## IScriptDeviceObject2.get_module_identification Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_module_identification()
```

---

## IScriptDeviceObject3.allowed_interfaces_at Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> allowed_interfaces_at(
	int index
)
```

---

## IScriptDeviceObject4.export_io_mappings_as_csv Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void export_io_mappings_as_csv(
	string file_path
)
```

---

## IScriptDeviceObject4.get_device_communication_settings Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptCommunicationSettings get_device_communication_settings()
```

---

## IScriptDeviceObject4.import_io_mappings_from_csv Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_io_mappings_from_csv(
	string file_path
)
```

---

## IScriptDeviceObject4.set_gateway_and_address Method (IScriptGateway, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_address(
	IScriptGateway gateway,
	string address
)
```

---

## IScriptDeviceObject4.set_gateway_and_device_name Method (IScriptGateway, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_device_name(
	IScriptGateway gateway,
	string device_name
)
```

---

## IScriptDeviceObject4.set_gateway_and_device_name Method (Guid, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_device_name(
	Guid gateway_guid,
	string device_name
)
```

---

## IScriptDeviceObject4.set_gateway_and_device_name Method (String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_device_name(
	string gateway,
	string device_name
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (IScriptGateway, IPAddress, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	IScriptGateway gateway,
	IPAddress ip_address,
	ushort port = 11740
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (IScriptGateway, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	IScriptGateway gateway,
	string ip_address
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (IScriptGateway, String, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	IScriptGateway gateway,
	string ip_address,
	ushort port
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (Guid, IPAddress, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	Guid gateway_guid,
	IPAddress ip_address,
	ushort port = 11740
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (Guid, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	Guid gateway_guid,
	string ip_address
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (Guid, String, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	Guid gateway_guid,
	string ip_address,
	ushort port
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (String, IPAddress, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	string gateway,
	IPAddress ip_address,
	ushort port = 11740
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	string gateway,
	string ip_address
)
```

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method (String, String, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_ip_address(
	string gateway,
	string ip_address,
	ushort port
)
```

---

## IScriptDeviceObject.add Method (String, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.add Method (String, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.disable Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void disable()
```

---

## IScriptDeviceObject.enable Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void enable()
```

---

## IScriptDeviceObject.get_address Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_address()
```

---

## IScriptDeviceObject.get_device_identification Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IDeviceId get_device_identification()
```

---

## IScriptDeviceObject.get_gateway Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Guid get_gateway()
```

---

## IScriptDeviceObject.get_simulation_mode Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool get_simulation_mode()
```

---

## IScriptDeviceObject.insert Method (String, Int32, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	string name,
	int index,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.insert Method (String, Int32, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	string name,
	int index,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.is_enabled Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool is_enabled()
```

---

## IScriptDeviceObject.plug Method (String, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void plug(
	string name,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.plug Method (String, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void plug(
	string name,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.set_gateway_and_address Method (Guid, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_address(
	Guid gateway,
	string address
)
```

---

## IScriptDeviceObject.set_gateway_and_address Method (String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_gateway_and_address(
	string stGateway,
	string address
)
```

---

## IScriptDeviceObject.set_simulation_mode Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_simulation_mode(
	bool simulation
)
```

---

## IScriptDeviceObject.unplug Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void unplug()
```

---

## IScriptDeviceObject.update Method (IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void update(
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceObject.update Method (Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void update(
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptDeviceParameterSet.by_id Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceParameter by_id(
	long id
)
```

---

## IScriptDeviceParameterSet.contains Method (IScriptDeviceParameter)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	IScriptDeviceParameter parameter
)
```

---

## IScriptDeviceParameterSet.contains Method (Int64)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	long id
)
```

---

## IScriptDeviceParameterSet.contains Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool contains(
	string name
)
```

---

## IScriptDeviceParameterSet.get_device_object Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_device_object()
```

---

## IScriptDeviceParameter.get_device_object Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_device_object()
```

---

## IScriptDeviceRepository2.import_device Method (String, IScriptRepositorySource, Guid, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IDeviceId import_device(
	string path,
	IScriptRepositorySource source,
	Guid converter_factory_guid,
	bool save_device_cache = true
)
```

---

## IScriptDeviceRepository.create_device_identification Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IDeviceId create_device_identification(
	int type,
	string id,
	string version
)
```

---

## IScriptDeviceRepository.create_module_identification Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IModuleId create_module_identification(
	int type,
	string id,
	string version,
	string module_id
)
```

---

## IScriptDeviceRepository.get_all_devices Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCollection get_all_devices()
```

---

## IScriptDeviceRepository.get_all_devices Method (IDeviceId)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCollection get_all_devices(
	IDeviceId device_id
)
```

---

## IScriptDeviceRepository.get_all_devices Method (IDeviceId, IScriptRepositorySource)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCollection get_all_devices(
	IDeviceId device_id,
	IScriptRepositorySource source
)
```

---

## IScriptDeviceRepository.get_all_devices Method (IScriptRepositorySource)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCollection get_all_devices(
	IScriptRepositorySource source
)
```

---

## IScriptDeviceRepository.get_all_devices Method (String, IScriptRepositorySource)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_all_devices(
	string name,
	IScriptRepositorySource source = null
)
```

---

## IScriptDeviceRepository.get_all_vendor_descriptions Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_all_vendor_descriptions()
```

---

## IScriptDeviceRepository.get_all_vendor_descriptions Method (IScriptRepositorySource)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_all_vendor_descriptions(
	IScriptRepositorySource source
)
```

---

## IScriptDeviceRepository.get_device Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceDescription get_device(
	IDeviceId device_id
)
```

---

## IScriptDeviceRepository.get_device_category Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCategory get_device_category(
	Guid category
)
```

---

## IScriptDeviceRepository.get_device_category Method (Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceCategory get_device_category(
	int category_id
)
```

---

## IScriptDeviceRepository.get_device_family Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceFamily get_device_family(
	string family
)
```

---

## IScriptDeviceRepository.get_vendor_description Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptVendorDescription get_vendor_description(
	int vendor_id
)
```

---

## IScriptDeviceRepository.import_device Method (Stream, IScriptRepositorySource, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IDeviceId import_device(
	Stream stream,
	IScriptRepositorySource source,
	string source_path,
	bool save_device_cache = true
)
```

---

## IScriptDeviceRepository.import_device Method (String, IScriptRepositorySource, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IDeviceId import_device(
	string path,
	IScriptRepositorySource source,
	bool save_device_cache = true
)
```

---

## IScriptDeviceRepository.import_vendor_description Method (Stream, IScriptRepositorySource, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptVendorDescription import_vendor_description(
	Stream stream,
	IScriptRepositorySource source,
	string source_path
)
```

---

## IScriptDeviceRepository.import_vendor_description Method (String, IScriptRepositorySource)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptVendorDescription import_vendor_description(
	string path,
	IScriptRepositorySource source
)
```

---

## IScriptDeviceRepository.rebuild_device_cache Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rebuild_device_cache()
```

---

## IScriptDeviceRepository.remove_device Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_device(
	IDeviceId device_id,
	IScriptRepositorySource source,
	bool save_device_cache = true
)
```

---

## IScriptDeviceRepository.remove_vendor_description Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_vendor_description(
	int vendor_id,
	IScriptRepositorySource source
)
```

---

## IScriptDeviceRepository.save_device_cache Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_device_cache()
```

---

## IScriptDeviceUser2.set_user_flags Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_user_flags(
	DeviceUserManagementFlags flags
)
```

---

## IScriptDeviceUserList.add Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceUser add(
	string name
)
```

---

## IScriptDeviceUserList.clear Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clear()
```

---

## IScriptDeviceUserList.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool remove(
	string name
)
```

---

## IScriptDeviceUserManagement.download Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download()
```

---

## IScriptDeviceUserManagement.load Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void load(
	string xml_or_file_name
)
```

---

## IScriptDeviceUserManagement.load Method (XmlElement)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void load(
	XmlElement element
)
```

---

## IScriptDeviceUserManagement.reload_from_project Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void reload_from_project()
```

---

## IScriptDeviceUserManagement.save Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string save()
```

---

## IScriptDeviceUserManagement.save Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save(
	string file_name
)
```

---

## IScriptDeviceUserManagement.save Method (XmlWriter)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save(
	XmlWriter writer
)
```

---

## IScriptDeviceUserManagement.store_to_project Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void store_to_project()
```

---

## IScriptDeviceUserManagement.upload Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void upload()
```

---

## IScriptDeviceUser.set_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_password(
	string password
)
```

---

## IScriptDriverInfo.set_bus_cycle_task Method (IExtendedObject`1(IScriptObject))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_bus_cycle_task(
	IExtendedObject<IScriptObject> task
)
```

---

## IScriptDriverInfo.set_bus_cycle_task Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_bus_cycle_task(
	Guid object_guid
)
```

---

## IScriptDriverInfo.set_bus_cycle_task Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_bus_cycle_task(
	string name
)
```

---

## IScriptDriverInfo.set_io_application Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_io_application(
	IExtendedObject<IScriptObject> application
)
```

---

## IScriptEnumerationDataElement.read_online_enum_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptEnumerationValue read_online_enum_value(
	int nTimeout = 1000
)
```

---

## IScriptEnumerationDataElement.write_online_value Method (IScriptEnumerationValue)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_online_value(
	IScriptEnumerationValue value
)
```

---

## IScriptExplicitConnectorObject2.export_io_mappings_as_csv Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void export_io_mappings_as_csv(
	string file_path
)
```

---

## IScriptExplicitConnectorObject2.import_io_mappings_from_csv Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_io_mappings_from_csv(
	string file_path
)
```

---

## IScriptExplicitConnectorObject.add Method (String, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptExplicitConnectorObject.add Method (String, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptExplicitConnectorObject.allowed_interfaces_at Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> allowed_interfaces_at(
	int index
)
```

---

## IScriptExplicitConnectorObject.insert Method (String, Int32, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	string name,
	int index,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptExplicitConnectorObject.insert Method (String, Int32, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	string name,
	int index,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptExternalFileObjectContainer.create_external_file_object Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_external_file_object(
	string file_path,
	string name = null,
	ReferenceMode reference_mode = ReferenceMode.Embed,
	AutoUpdateMode auto_update_mode = AutoUpdateMode.Never
)
```

---

## IScriptExternalFileObject.calculate_checksum Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
long calculate_checksum()
```

---

## IScriptExternalFileObject.change_modes Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void change_modes(
	ReferenceMode reference_mode,
	AutoUpdateMode auto_update_mode = AutoUpdateMode.Never
)
```

---

## IScriptExternalFileObject.create_edit_path Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string create_edit_path()
```

---

## IScriptExternalFileObject.get_data Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
byte[] get_data()
```

---

## IScriptExternalFileObject.get_data Method (Stream)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void get_data(
	Stream stream
)
```

---

## IScriptExternalFileObject.get_data Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void get_data(
	string filename
)
```

---

## IScriptExternalFileObject.update Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void update()
```

---

## IScriptGatewayDrivers.find_with_name Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptGatewayDriver> find_with_name(
	string name
)
```

---

## IScriptGatewayParameterDescription.validate Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void validate(
	Object value
)
```

---

## IScriptGateway.find_address_by_ip Method (IPAddress, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string find_address_by_ip(
	IPAddress address,
	ushort port = 11740
)
```

---

## IScriptGateway.find_address_by_ip Method (String, UInt16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string find_address_by_ip(
	string ip_or_name,
	ushort port = 11740
)
```

---

## IScriptGateway.get_cached_network_scan_result Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptScanTargetDescription> get_cached_network_scan_result()
```

---

## IScriptGateway.perform_network_scan Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptScanTargetDescription> perform_network_scan()
```

---

## IScriptGateways.add_new_gateway Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptGateway add_new_gateway(
	string name,
	IDictionary<Object, Object> parameters,
	IScriptGatewayDriver driver = null,
	Nullable<Guid> gateway_guid = null
)
```

---

## IScriptGateways.convert_gateway_parameter Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Object convert_gateway_parameter(
	Object parameter,
	ParamType paramType
)
```

---

## IScriptGateways.find_with_name Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptGateway> find_with_name(
	string name
)
```

---

## IScriptGateways.remove_gateway Method (IScriptGateway)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_gateway(
	IScriptGateway gateway
)
```

---

## IScriptGateways.remove_gateway Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_gateway(
	Guid guid
)
```

---

## IScriptGroupList.create Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptGroup create(
	string name
)
```

---

## IScriptGroup.add_member Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_member(
	IScriptUserOrGroup member
)
```

---

## IScriptGroup.get_group_members Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_group_members()
```

---

## IScriptGroup.get_user_members Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> get_user_members(
	bool recursive
)
```

---

## IScriptGroup.has_member Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool has_member(
	IScriptUserOrGroup member
)
```

---

## IScriptGroup.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove()
```

---

## IScriptGroup.remove_member Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_member(
	IScriptUserOrGroup member
)
```

---

## IScriptGroup.rename Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rename(
	string newname
)
```

---

## IScriptIecLanguageMemberContainer.create_action Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_action(
	string name,
	Nullable<Guid> language = null
)
```

---

## IScriptIecLanguageMemberContainer.create_method Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_method(
	string name,
	string return_type = null,
	Nullable<Guid> language = null
)
```

---

## IScriptIecLanguageMemberContainer.create_property Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_property(
	string name,
	string return_type = "int",
	Nullable<Guid> language = null
)
```

---

## IScriptIecLanguageMemberContainer.create_transition Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_transition(
	string name,
	Nullable<Guid> language = null
)
```

---

## IScriptIecLanguageObjectContainer2.create_pou Method (SpecialPouType)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_pou(
	SpecialPouType type
)
```

---

## IScriptIecLanguageObjectContainer.create_dut Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_dut(
	string name,
	DutType type = DutType.Structure,
	string baseType = null
)
```

---

## IScriptIecLanguageObjectContainer.create_gvl Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_gvl(
	string name
)
```

---

## IScriptIecLanguageObjectContainer.create_interface Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_interface(
	string name,
	string baseInterfaces = "__System.IQueryInterface"
)
```

---

## IScriptIecLanguageObjectContainer.create_pou Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_pou(
	string name,
	PouType type = PouType.FunctionBlock,
	Nullable<Guid> language = null,
	string return_type = null,
	string base_type = null,
	string interfaces = null
)
```

---

## IScriptLibManObject2.add_library Method (IManagedLib)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_library(
	IManagedLib library
)
```

---

## IScriptLibManObject2.add_placeholder Method (String, IManagedLib)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_placeholder(
	string name,
	IManagedLib default_resolution
)
```

---

## IScriptLibManObjectContainer.get_library_manager Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_library_manager()
```

---

## IScriptLibManObject.add_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_library(
	string name
)
```

---

## IScriptLibManObject.add_placeholder Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_placeholder(
	string name,
	string default_resolution
)
```

---

## IScriptLibManObject.get_libraries Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> get_libraries(
	[OptionalAttribute] bool recursive
)
```

---

## IScriptLibManObject.remove_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_library(
	string name
)
```

---

## IScriptLibraryParameters.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptLibraryReference.get_dependencies Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IScriptLibraryReference> get_dependencies()
```

---

## IScriptLibraryReferences.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptLiveDeviceGroupList.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptLiveDeviceGroup.check_cyclic_membership Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_cyclic_membership(
	string new_group_member
)
```

---

## IScriptLiveDeviceUserList.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptLiveDeviceUserManagement.add_group Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_group(
	string name,
	IList<string> group_members,
	IList<string> user_members
)
```

---

## IScriptLiveDeviceUserManagement.add_user Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_user(
	string name,
	string password,
	bool can_change_password = true,
	bool must_change_password = false
)
```

---

## IScriptLiveDeviceUserManagement.backup Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string backup(
	string directory,
	string password
)
```

---

## IScriptLiveDeviceUserManagement.remove_group Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_group(
	string name
)
```

---

## IScriptLiveDeviceUserManagement.remove_user Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_user(
	string name
)
```

---

## IScriptLiveDeviceUserManagement.restore Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void restore(
	string path,
	string password
)
```

---

## IScriptLiveDeviceUserManagement.set_members_of_group Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_members_of_group(
	string name,
	IList<string> group_members,
	IList<string> user_members
)
```

---

## IScriptLiveDeviceUserManagement.set_user_flags Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_user_flags(
	string name,
	DeviceUserManagementFlags flags
)
```

---

## IScriptLiveDeviceUserManagement.set_user_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_user_password(
	string name,
	string password
)
```

---

## IScriptLiveDeviceUserManagement.upload Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void upload()
```

---

## IScriptMessage.call_details_handler Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void call_details_handler()
```

---

## IScriptObject2.export_native Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void export_native(
	string destination,
	bool recursive,
	string profile_name,
	INativeExportReporter reporter
)
```

---

## IScriptObject2.export_xml Method (IExportReporter, String, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	string path,
	bool recursive,
	bool export_folder_structure
)
```

---

## IScriptObject2.import_native Method (IEnumerable(String), NativeImportFilter, INativeImportHandler)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
NativeImportResult import_native(
	IEnumerable<string> filenames,
	NativeImportFilter filter,
	INativeImportHandler handler
)
```

---

## IScriptObject2.import_native Method (String, NativeImportFilter, INativeImportHandler)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
NativeImportResult import_native(
	string filename,
	NativeImportFilter filter,
	INativeImportHandler handler
)
```

---

## IScriptObject2.import_xml Method (IImportReporter, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	IImportReporter reporter,
	string dataOrPath,
	bool import_folder_structure
)
```

---

## IScriptObject3.create_folder Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_folder(
	string foldername
)
```

---

## IScriptObject4.export_xml Method (IExportReporter, String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	string path,
	bool recursive,
	bool export_folder_structure,
	bool declarations_as_plaintext
)
```

---

## IScriptObject5.export_xml Method (IExportReporter, String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	string path = null,
	bool recursive = false,
	bool export_folder_structure = false,
	bool declarations_as_plaintext = false
)
```

---

## IScriptObject5.export_xml Method (String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	string path = null,
	bool recursive = false,
	bool export_folder_structure = false,
	bool declarations_as_plaintext = false
)
```

---

## IScriptObject5.get_signature_crc Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_signature_crc(
	Object application = null,
	string default_value = null
)
```

---

## IScriptObject5.import_xml Method (ConflictResolve, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	ConflictResolve conflictResolve,
	string dataOrPath,
	bool import_folder_structure = false
)
```

---

## IScriptObject5.import_xml Method (String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	string dataOrPath,
	bool import_folder_structure = false
)
```

---

## IScriptObjectFactories.search_factories_for Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IEnumerable<IScriptObjectFactory> search_factories_for(
	Guid typeguid
)
```

---

## IScriptObjectPermission.check_permission_extended Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Exception check_permission_extended()
```

---

## IScriptObject.export_xml Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	[OptionalAttribute] string path,
	[OptionalAttribute] bool recursive
)
```

---

## IScriptObject.get_name Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_name(
	[OptionalAttribute] bool resolve_localized_display_name
)
```

---

## IScriptObject.import_xml Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	IImportReporter reporter,
	string dataOrPath
)
```

---

## IScriptObject.move Method (IExtendedObject`1(IScriptObject), Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void move(
	IExtendedObject<IScriptObject> new_parent,
	int new_index = -1
)
```

---

## IScriptObject.move Method (IExtendedObject`1(IScriptProject), Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void move(
	IExtendedObject<IScriptProject> new_parent,
	int new_index = -1
)
```

---

## IScriptObject.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove()
```

---

## IScriptObject.rename Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rename(
	string stNewName
)
```

---

## IScriptOnline2.create_online_device Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptOnlineDevice create_online_device(
	[OptionalAttribute] IExtendedObject<IScriptObject> device
)
```

---

## IScriptOnline3.clear_all_credentials Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clear_all_credentials()
```

---

## IScriptOnline3.set_default_credentials Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_default_credentials(
	string username,
	[OptionalAttribute] string password
)
```

---

## IScriptOnline3.set_specific_credentials Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_specific_credentials(
	Object target,
	string username,
	[OptionalAttribute] string password
)
```

---

## IScriptOnline5.register_trusts_certificate Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void register_trusts_certificate(
	IExtendedObject<IScriptObject> device_object,
	TrustsCertificateCallback callback,
	string current_node_name = null
)
```

---

## IScriptOnline5.unregister_all_trusts_certificate Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void unregister_all_trusts_certificate()
```

---

## IScriptOnline5.unregister_trusts_certificate Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void unregister_trusts_certificate(
	IExtendedObject<IScriptObject> device_object,
	string current_node_name = null
)
```

---

## IScriptOnlineApplication2.get_online_device Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptOnlineDevice get_online_device()
```

---

## IScriptOnlineApplication2.reset Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void reset(
	ResetOption reset_option = ResetOption.Warm,
	bool force_kill = false
)
```

---

## IScriptOnlineApplication.create_boot_application Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_boot_application()
```

---

## IScriptOnlineApplication.force_prepared_values Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void force_prepared_values()
```

---

## IScriptOnlineApplication.get_forced_expressions Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> get_forced_expressions()
```

---

## IScriptOnlineApplication.get_prepared_expressions Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> get_prepared_expressions()
```

---

## IScriptOnlineApplication.get_prepared_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_prepared_value(
	string expression
)
```

---

## IScriptOnlineApplication.login Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void login(
	OnlineChangeOption change_option,
	bool delete_foreign_apps
)
```

---

## IScriptOnlineApplication.logout Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void logout()
```

---

## IScriptOnlineApplication.read_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string read_value(
	string expression
)
```

---

## IScriptOnlineApplication.read_values Method (IEnumerable(String))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> read_values(
	IEnumerable<string> expressions
)
```

---

## IScriptOnlineApplication.read_values Method (String[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> read_values(
	params string[] expressions
)
```

---

## IScriptOnlineApplication.set_prepared_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_prepared_value(
	string expression,
	string value
)
```

---

## IScriptOnlineApplication.set_unforce_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_unforce_value(
	string expression,
	[OptionalAttribute] bool restore
)
```

---

## IScriptOnlineApplication.source_download Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void source_download()
```

---

## IScriptOnlineApplication.start Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void start()
```

---

## IScriptOnlineApplication.stop Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void stop()
```

---

## IScriptOnlineApplication.unforce_all_values Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void unforce_all_values()
```

---

## IScriptOnlineApplication.write_prepared_values Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_prepared_values()
```

---

## IScriptOnlineDevice2.connect Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void connect()
```

---

## IScriptOnlineDevice2.create_user_management Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceUserManagement create_user_management(
	bool load_from_project = true
)
```

---

## IScriptOnlineDevice2.disconnect Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void disconnect()
```

---

## IScriptOnlineDevice2.forced_disconnect Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void forced_disconnect()
```

---

## IScriptOnlineDevice3.download_source Method (IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download_source(
	params IScriptProjectArchiveCategory[] additional_items
)
```

---

## IScriptOnlineDevice3.download_source Method (Boolean, IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download_source(
	bool bCompact,
	params IScriptProjectArchiveCategory[] additional_items
)
```

---

## IScriptOnlineDevice3.download_source Method (Boolean, IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download_source(
	bool bCompact,
	IEnumerable<IScriptProjectArchiveCategory> additional_items
)
```

---

## IScriptOnlineDevice3.download_source Method (IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download_source(
	IEnumerable<IScriptProjectArchiveCategory> additional_items
)
```

---

## IScriptOnlineDevice3.upload_source Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void upload_source(
	string archive_path
)
```

---

## IScriptOnlineDevice4.create_directory Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_directory(
	string remote_directory
)
```

---

## IScriptOnlineDevice4.delete_directory Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void delete_directory(
	string remote_directory,
	bool recursive = false
)
```

---

## IScriptOnlineDevice4.delete_file Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void delete_file(
	string remote_file
)
```

---

## IScriptOnlineDevice4.download_file Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void download_file(
	string local_file,
	string remote_file,
	bool force_overwrite
)
```

---

## IScriptOnlineDevice4.get_file_list_of_directory Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDirectoryInfo[] get_file_list_of_directory(
	string remote_directory
)
```

---

## IScriptOnlineDevice4.rename_directory Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rename_directory(
	string old_name,
	string new_name
)
```

---

## IScriptOnlineDevice4.rename_file Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rename_file(
	string old_name,
	string new_name
)
```

---

## IScriptOnlineDevice4.upload_file Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void upload_file(
	string remote_file,
	string local_file,
	bool force_overwrite
)
```

---

## IScriptOnlineDevice5.activate_license Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void activate_license(
	string ticket,
	string url = null,
	params string[] license_names
)
```

---

## IScriptOnlineDevice6.change_user_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void change_user_password(
	string user,
	string oldPassword,
	string newPassword
)
```

---

## IScriptOnlineDevice7.create_live_user_management Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptLiveDeviceUserManagement create_live_user_management()
```

---

## IScriptOnlineDevice7.set_credentials_for_initial_user Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_credentials_for_initial_user(
	string username,
	string password,
	bool can_change_password = true,
	bool must_change_password = false
)
```

---

## IScriptOnlineDevice.reset_origin Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void reset_origin()
```

---

## IScriptOnline.create_online_application Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptOnlineApplication create_online_application(
	[OptionalAttribute] IExtendedObject<IScriptObject> application
)
```

---

## IScriptPermission.check_permission Method (IScriptGroup)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_permission(
	IScriptGroup group
)
```

---

## IScriptPermission.check_permission Method (Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_permission(
	bool silent
)
```

---

## IScriptPermission.check_set_permission_state Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_set_permission_state(
	IScriptGroup group,
	PermissionState state,
	bool silent = true
)
```

---

## IScriptPermission.get_permission_state Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
PermissionState get_permission_state(
	IScriptGroup group,
	bool resolve_effective = true,
	bool resolve_inherited = false
)
```

---

## IScriptPermission.set_permission_state Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_permission_state(
	IScriptGroup group,
	PermissionState state
)
```

---

## IScriptPlaceholderReference.get_redirection Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_redirection()
```

---

## IScriptPlaceholderReference.set_redirection Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_redirection(
	string fixed_resolution = ""
)
```

---

## IScriptPouObjectCollection.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptPouObjectCollection.add Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string pou_name,
	string comment = null
)
```

---

## IScriptPouObjectCollection.insert Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	int index,
	string pou_name,
	string comment = null
)
```

---

## IScriptPouObjectCollection.remove Method (Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove(
	int index
)
```

---

## IScriptPouObjectCollection.remove Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove(
	string pou_name
)
```

---

## IScriptPouObjectCollection.replace Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replace(
	int index,
	string pou_name,
	string comment = null
)
```

---

## IScriptProject10.compare_to Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptComparisonResult compare_to(
	IExtendedObject<IScriptProject> right_project,
	ComparisonFlags flags = ComparisonFlags.NONE
)
```

---

## IScriptProject12.disable_encryption Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void disable_encryption()
```

---

## IScriptProject12.enable_integrity_check Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void enable_integrity_check()
```

---

## IScriptProject12.is_integrity_check_enabled Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool is_integrity_check_enabled()
```

---

## IScriptProject2.export_native Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void export_native(
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	string destination,
	bool recursive,
	bool one_file_per_subtree,
	string profile_name,
	INativeExportReporter reporter
)
```

---

## IScriptProject2.export_xml Method (IExportReporter, IEnumerable(IExtendedObject`1(IScriptObject)), String, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	string path,
	bool recursive,
	bool export_folder_structure
)
```

---

## IScriptProject2.import_native Method (IEnumerable(String), NativeImportFilter, INativeImportHandler)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
NativeImportResult import_native(
	IEnumerable<string> filenames,
	NativeImportFilter filter,
	INativeImportHandler handler
)
```

---

## IScriptProject2.import_native Method (String, NativeImportFilter, INativeImportHandler)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
NativeImportResult import_native(
	string filename,
	NativeImportFilter filter,
	INativeImportHandler handler
)
```

---

## IScriptProject2.import_xml Method (IImportReporter, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	IImportReporter reporter,
	string dataOrPath,
	bool import_folder_structure
)
```

---

## IScriptProject3.login Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void login(
	string username,
	string password
)
```

---

## IScriptProject3.logout Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void logout()
```

---

## IScriptProject5.check_all_pool_objects Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void check_all_pool_objects()
```

---

## IScriptProject5.clean_all Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clean_all()
```

---

## IScriptProject5.generate_runtime_system_files Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void generate_runtime_system_files(
	string destination_directory,
	bool generate_m4 = true,
	bool generate_c = false
)
```

---

## IScriptProject5.get_project_info Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> get_project_info()
```

---

## IScriptProject5.save_as_compiled_library Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_as_compiled_library(
	[OptionalAttribute] string destination_name
)
```

---

## IScriptProject6.create_folder Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_folder(
	string foldername
)
```

---

## IScriptProject6.create_folder Method (String, Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void create_folder(
	string foldername,
	Guid structured_view
)
```

---

## IScriptProject7.export_xml Method (IExportReporter, IEnumerable(IExtendedObject`1(IScriptObject)), String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	string path,
	bool recursive,
	bool export_folder_structure,
	bool declarations_as_plaintext
)
```

---

## IScriptProject8.save_archive Method (String, IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	params IScriptProjectArchiveCategory[] additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	IEnumerable<IScriptProjectArchiveCategory> additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, IEnumerable(String), IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	IEnumerable<string> additional_files,
	params IScriptProjectArchiveCategory[] additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, String, IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	string comment,
	params IScriptProjectArchiveCategory[] additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, String, IEnumerable(String), IScriptProjectArchiveCategory[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	string comment,
	IEnumerable<string> additional_files,
	params IScriptProjectArchiveCategory[] additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, String, String[], IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	string comment,
	string[] additional_files,
	IEnumerable<IScriptProjectArchiveCategory> additional_categories
)
```

---

## IScriptProject8.save_archive Method (String, String[], IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	string[] additional_files,
	IEnumerable<IScriptProjectArchiveCategory> additional_categories
)
```

---

## IScriptProject9.export_doc Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_doc(
	[OptionalAttribute] string path,
	[OptionalAttribute] string ext_path,
	Formatting formatting = Formatting.Indented
)
```

---

## IScriptProject9.export_xml Method (IExportReporter, IEnumerable(IExtendedObject`1(IScriptObject)), String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	string path = null,
	bool recursive = false,
	bool export_folder_structure = false,
	bool declarations_as_plaintext = false
)
```

---

## IScriptProject9.export_xml Method (IEnumerable(IExtendedObject`1(IScriptObject)), String, Boolean, Boolean, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	string path = null,
	bool recursive = false,
	bool export_folder_structure = false,
	bool declarations_as_plaintext = false
)
```

---

## IScriptProject9.import_xml Method (ConflictResolve, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	ConflictResolve conflictResolve,
	string dataOrPath,
	bool import_folder_structure = false
)
```

---

## IScriptProject9.import_xml Method (String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	string dataOrPath,
	bool import_folder_structure
)
```

---

## IScriptProject9.save_archive Method (String, String, IEnumerable(String), IEnumerable(IScriptProjectArchiveCategory))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path,
	string comment,
	IEnumerable<string> additional_files,
	IEnumerable<IScriptProjectArchiveCategory> additional_categories
)
```

---

## IScriptProjectDeviceExtension.add Method (String, IDeviceId, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	IDeviceId device,
	[OptionalAttribute] string module
)
```

---

## IScriptProjectDeviceExtension.add Method (String, Int32, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add(
	string name,
	int type,
	string id,
	string version,
	[OptionalAttribute] string module
)
```

---

## IScriptProjectInfoObject.change_accessor_generation Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void change_accessor_generation(
	bool generate_accessors
)
```

---

## IScriptProjectSettings.set_sourcedownload Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void set_sourcedownload(
	int timing,
	IEnumerable<IScriptProjectArchiveCategory> content,
	bool compact,
	IExtendedObject<IScriptObject> device
)
```

---

## IScriptProject.close Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void close()
```

---

## IScriptProject.document Method (IExtendedObject`1(IScriptObject)[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void document(
	params IExtendedObject<IScriptObject>[] objects
)
```

---

## IScriptProject.document Method (IEnumerable(IExtendedObject`1(IScriptObject)))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void document(
	IEnumerable<IExtendedObject<IScriptObject>> objects
)
```

---

## IScriptProject.export_xml Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string export_xml(
	IExportReporter reporter,
	IEnumerable<IExtendedObject<IScriptObject>> objects,
	[OptionalAttribute] string path,
	[OptionalAttribute] bool recursive
)
```

---

## IScriptProject.import_xml Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void import_xml(
	IImportReporter reporter,
	string dataOrPath
)
```

---

## IScriptProject.save Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save()
```

---

## IScriptProject.save_archive Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_archive(
	string path
)
```

---

## IScriptProject.save_as Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void save_as(
	string path,
	[OptionalAttribute] string password
)
```

---

## IScriptProjects2.convert Method (String, String, Guid, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> convert(
	string path,
	string output_path = null,
	Guid converter,
	bool primary = true
)
```

---

## IScriptProjects2.convert Method (String, String, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> convert(
	string path,
	string output_path = null,
	string converter = null,
	bool primary = true
)
```

---

## IScriptProjects3.open Method (String, String, String, String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open(
	string path,
	string encryption_password = null,
	string session_user = null,
	string session_password = null,
	bool primary = true
)
```

---

## IScriptProjects3.open_archive Method (String, String, Boolean, String, String, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open_archive(
	string archivefile,
	string projectpath,
	bool overwrite = false,
	string encryption_password = null,
	string session_user = null,
	string session_password = null
)
```

---

## IScriptProjects4.open Method (String, String, String, String, Boolean, VersionUpdateFlags, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open(
	string path,
	string encryption_password = null,
	string session_user = null,
	string session_password = null,
	bool primary = true,
	VersionUpdateFlags update_flags = VersionUpdateFlags.NoUpdates,
	bool allow_readonly = false
)
```

---

## IScriptProjects4.open_archive Method (String, String, Boolean, String, String, String, VersionUpdateFlags)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open_archive(
	string archivefile,
	string projectpath,
	bool overwrite = false,
	string encryption_password = null,
	string session_user = null,
	string session_password = null,
	VersionUpdateFlags update_flags = VersionUpdateFlags.NoUpdates
)
```

---

## IScriptProjects5.open_archive Method (String, String, Boolean, String, String, String, VersionUpdateFlags, PromptAbsolutePath)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open_archive(
	string archivefile,
	string projectpath,
	bool overwrite = false,
	string encryption_password = null,
	string session_user = null,
	string session_password = null,
	VersionUpdateFlags update_flags = VersionUpdateFlags.NoUpdates,
	PromptAbsolutePath prompt_absolute_path = null
)
```

---

## IScriptProjects.create Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> create(
	string path,
	bool primary = true
)
```

---

## IScriptProjects.get_by_path Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> get_by_path(
	string path
)
```

---

## IScriptProjects.open Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open(
	string path,
	string password = null,
	bool primary = true
)
```

---

## IScriptProjects.open_archive Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> open_archive(
	string archivefile,
	string projectpath,
	bool overwrite = false,
	[OptionalAttribute] string password
)
```

---

## IScriptRepositorySourceList.__len__ Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int __len__()
```

---

## IScriptRepositorySourceList.add Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptRepositorySource add(
	string name,
	string location_url
)
```

---

## IScriptRepositorySourceList.move Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void move(
	IScriptRepositorySource source,
	int index
)
```

---

## IScriptRepositorySourceList.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove(
	IScriptRepositorySource source
)
```

---

## IScriptTaskConfigObject.create_task Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptObject> create_task(
	string name
)
```

---

## IScriptTextDocument.append Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void append(
	string text
)
```

---

## IScriptTextDocument.get_line Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_line(
	int lineno
)
```

---

## IScriptTextDocument.get_text Method (Int32, Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_text(
	int offset,
	int length
)
```

---

## IScriptTextDocument.get_text Method (Int32, Int32, Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_text(
	int lineno,
	int lineoffset,
	int length
)
```

---

## IScriptTextDocument.insert Method (Int32, Int32, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	int lineno,
	int lineoffset,
	string text
)
```

---

## IScriptTextDocument.insert Method (Int32, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void insert(
	int offset,
	string text
)
```

---

## IScriptTextDocument.remove Method (Int32, Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove(
	int offset,
	int length
)
```

---

## IScriptTextDocument.remove Method (Int32, Int32, Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove(
	int lineno,
	int lineoffset,
	int length
)
```

---

## IScriptTextDocument.replace Method (Int32, Int32, Int32, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replace(
	int lineno,
	int lineoffset,
	int length,
	string newtext
)
```

---

## IScriptTextDocument.replace Method (Int32, Int32, String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replace(
	int offset,
	int length,
	string newtext
)
```

---

## IScriptTextDocument.replace Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replace(
	string new_text
)
```

---

## IScriptTextDocument.replace_line Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void replace_line(
	int lineno,
	string line
)
```

---

## IScriptTreeObject.find Method (String, Boolean)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IExtendedObject<IScriptObject>> find(
	string name,
	bool recursive = false
)
```

---

## IScriptTreeObject.find Method (String[])

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IExtendedObject<IScriptObject>> find(
	params string[] names
)
```

---

## IScriptTreeObject.get_children Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IExtendedObject<IScriptObject>> get_children(
	bool recursive = false
)
```

---

## IScriptUI.browse_directory_dialog Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string browse_directory_dialog(
	string message,
	string path = "",
	EnvironmentSpecialFolder root_folder = EnvironmentSpecialFolder.MyComputer,
	bool new_folder_button = true
)
```

---

## IScriptUI.choose Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> choose(
	string message,
	IList<Object> options,
	int initial_selection = 0,
	bool cancellable = true,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUI.error Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void error(
	string message,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUI.info Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void info(
	string message,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUI.open_file_dialog Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Object open_file_dialog(
	[OptionalAttribute] string title,
	[OptionalAttribute] string filename,
	[OptionalAttribute] string directory,
	[OptionalAttribute] string filter,
	[OptionalAttribute] Nullable<int> filter_index,
	[OptionalAttribute] string default_extension,
	[OptionalAttribute] Nullable<Guid> stateguid,
	[OptionalAttribute] bool multiselect,
	bool check_file_exists = true,
	bool check_path_exists = true
)
```

---

## IScriptUI.prompt Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
PromptResult prompt(
	string message,
	PromptChoice choice,
	PromptResult default_result,
	[OptionalAttribute] string store_description,
	[OptionalAttribute] string store_key,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUI.query_credentials Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> query_credentials(
	string message = "",
	string username = "",
	string password = "",
	[OptionalAttribute] bool cancellable
)
```

---

## IScriptUI.query_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string query_password(
	string message = "",
	string password = "",
	[OptionalAttribute] bool cancellable
)
```

---

## IScriptUI.query_string Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string query_string(
	string message = "",
	string text = "",
	[OptionalAttribute] bool multi_line,
	[OptionalAttribute] bool cancellable
)
```

---

## IScriptUI.reset_stored_result Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void reset_stored_result(
	string store_key
)
```

---

## IScriptUI.save_file_dialog Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string save_file_dialog(
	[OptionalAttribute] string title,
	[OptionalAttribute] string filename,
	[OptionalAttribute] string directory,
	[OptionalAttribute] string filter,
	[OptionalAttribute] Nullable<int> filter_index,
	[OptionalAttribute] string default_extension,
	[OptionalAttribute] Nullable<Guid> stateguid,
	bool check_file_exists = true,
	[OptionalAttribute] bool check_path_exists,
	bool check_overwrite = true,
	[OptionalAttribute] bool check_create
)
```

---

## IScriptUI.select_many Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> select_many(
	string message,
	PromptChoice choice,
	PromptResult result,
	IList<Object> items,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUI.warning Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void warning(
	string message,
	string message_key = "ScriptMessage",
	params Object[] arguments
)
```

---

## IScriptUserList.create Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptUser create(
	string name
)
```

---

## IScriptUserManagement.check_available Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_available(
	Guid type
)
```

---

## IScriptUserManagement.get_command_permission Method (IScriptCommand)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptCommandPermission get_command_permission(
	IScriptCommand command
)
```

---

## IScriptUserManagement.get_command_permission Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptCommandPermission get_command_permission(
	Guid commandguid
)
```

---

## IScriptUserManagement.get_factory_permission Method (IScriptObjectFactory)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptFactoryPermission get_factory_permission(
	IScriptObjectFactory factory
)
```

---

## IScriptUserManagement.get_factory_permission Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptFactoryPermission get_factory_permission(
	Guid factoryguid
)
```

---

## IScriptUserManagement.get_object_permission Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptObjectPermission get_object_permission(
	IExtendedObject<IScriptObject> obj,
	ObjectPermissionKind kind
)
```

---

## IScriptUserManagement.get_user_management_permission Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptPermission get_user_management_permission()
```

---

## IScriptUserManagement.login Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void login(
	string username,
	string password
)
```

---

## IScriptUserManagement.logout Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void logout()
```

---

## IScriptUserOrGroup.add_to Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void add_to(
	IScriptGroup parent
)
```

---

## IScriptUserOrGroup.remove_from Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove_from(
	IScriptGroup parent
)
```

---

## IScriptUser.change_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void change_password(
	string old_password,
	string new_password
)
```

---

## IScriptUser.check_password Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool check_password(
	string password
)
```

---

## IScriptUser.remove Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void remove()
```

---

## IScriptUser.rename Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void rename(
	string newname
)
```

---

## IScriptValueDataElement.read_online_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string read_online_value(
	int nTimeOut = 1000
)
```

---

## IScriptValueDataElement.write_online_value Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_online_value(
	string value
)
```

---

## IScriptVendorDescription.get_family Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceFamily get_family(
	int family_id
)
```

---

## ISystem2.execute_on_primary_thread Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void execute_on_primary_thread(
	PieceOfCode code,
	[OptionalAttribute] bool async
)
```

---

## ISystem3.clear_messages Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void clear_messages(
	Guid category
)
```

---

## ISystem3.get_message_categories Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Guid> get_message_categories(
	bool bActive = true
)
```

---

## ISystem3.get_message_category_description Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string get_message_category_description(
	Guid category
)
```

---

## ISystem3.get_message_objects Method (Guid, Severity)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IScriptMessage> get_message_objects(
	Guid category,
	Severity severities = Severity.FatalError|Severity.Error|Severity.Warning|Severity.Information|Severity.Text
)
```

---

## ISystem3.get_message_objects Method (String, Severity)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IScriptMessage> get_message_objects(
	string category = null,
	Severity severities = Severity.FatalError|Severity.Error|Severity.Warning|Severity.Information|Severity.Text
)
```

---

## ISystem3.write_message Method (Severity, String, IExtendedObject`1(IScriptObject), Int64, Int16)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_message(
	Severity severity,
	string stMessage,
	IExtendedObject<IScriptObject> obj,
	long position = -1,
	[OptionalAttribute] short length
)
```

---

## ISystem3.write_message Method (Severity, String, IExtendedObject`1(IScriptProject))

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_message(
	Severity severity,
	string stMessage,
	IExtendedObject<IScriptProject> obj
)
```

---

## ISystem4.progress_absolute Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void progress_absolute(
	string item,
	int absolute_progress
)
```

---

## ISystem4.progress_start Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void progress_start(
	string description,
	int items = -1,
	string unit = ""
)
```

---

## ISystem4.progress_step Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void progress_step(
	string item,
	int completed = 1
)
```

---

## ISystem.delay Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void delay(
	int milliseconds
)
```

---

## ISystem.exit Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void exit(
	[OptionalAttribute] int exitcode
)
```

---

## ISystem.get_messages Method (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> get_messages(
	Guid category
)
```

---

## ISystem.get_messages Method (String)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<string> get_messages(
	string category = "{194B48A9-AB51-43ae-B9A9-51D3EDAADDF3}"
)
```

---

## ISystem.process_messageloop Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void process_messageloop()
```

---

## ISystem.write_message Method

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
void write_message(
	Severity severity,
	string stMessage,
	[OptionalAttribute] IScriptTreeObject obj,
	long position = -1,
	[OptionalAttribute] short length
)
```

---

## ValuesFailedException Constructor

**Summary:** Initializes a new instance of theValuesFailedExceptionclass

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public ValuesFailedException(
	IList<string> failed_expressions
)
```

---

## WrongDeviceUserManagementException Constructor

**Summary:** Initializes a new instance of theWrongDeviceUserManagementExceptionclass

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public WrongDeviceUserManagementException(
	string msg
)
```

---

## IVersionCompatibilityManager2.SetVersionUpdateFlags Method

**Summary:** Sets the mode as described inVersionUpdateFlags

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetVersionUpdateFlags(
	VersionUpdateFlags flags
)
```

---

## IVersionCompatibilityManager3.CheckVersioning Method

**Summary:** Explicitly triggers the checks of the version compatibility manager,
            which are normally done in background when project loading is finished.

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
void CheckVersioning(
	int nProjectHandle
)
```

---

## IVersionCompatibilityManager.SetVersionSelectionMode Method

**Summary:** Sets the mode as described inVersionSelectionMode

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
void SetVersionSelectionMode(
	VersionSelectionMode mode
)
```

---

## UpdateEnvironmentEventArgs Constructor

**Summary:** The constructor.

**Assembly:** `VersionCompatibilityManager (in VersionCompatibilityManager.dll) Version: 3.5.17.0`

### Syntax
```csharp
public UpdateEnvironmentEventArgs(
	UpdateEnvironmentStage Stage,
	VersionUpdateFlags flags
)
```

---

## ExactVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## NewestBeforeVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## NewestBetweenVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## NewestVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## OldestAfterVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## OldestBetweenVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## OldestVersionConstraint Methods

**Summary:** Determines whether the specified System.Object is equal to the current System.Object.

---

## Profile Methods

**Summary:** This method is for internal use and should not be called.

---

## VersionConstraint Methods

**Summary:** Finds the version which matches this version constraint.

---

## FileReferenceCancelEventArgs Methods

**Summary:** No summary available.

---

## FileReferenceEventArgs Methods

**Summary:** No summary available.

---

## IFileReference Methods

**Summary:** Freezes a file reference, i.e. the link to a file system object is released. The
            contents of the file will solely exist in the corresponding Object Manager project, and
            it cannot be updated by file system changes any more.

---

## IFileReference2 Methods

**Summary:** Freezes a file reference, i.e. the link to a file system object is released. The
            contents of the file will solely exist in the corresponding Object Manager project, and
            it cannot be updated by file system changes any more.

---

## IFileReference3 Methods

**Summary:** Freezes a file reference, i.e. the link to a file system object is released. The
            contents of the file will solely exist in the corresponding Object Manager project, and
            it cannot be updated by file system changes any more.

---

## IFileReference4 Methods

**Summary:** Freezes a file reference, i.e. the link to a file system object is released. The
            contents of the file will solely exist in the corresponding Object Manager project, and
            it cannot be updated by file system changes any more.

---

## IMessageService Methods

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService2 Methods

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService3 Methods

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService4 Methods

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService5 Methods

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IProgressCallback Methods

**Summary:** Call this method after the long-running operation is finished. Do not call any method
            of this instance after that.

---

## IProject Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IProject2 Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IProject3 Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IProject4 Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IProject5 Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IProject6 Methods

**Summary:** Closes this project. The corresponding Object Manager project will also be closed. If
            this project has got unsaved changes, these changes will be discarded.

---

## IArchivable Methods

**Summary:** This method is called after the object is deserialized.

---

## IArchivable2 Methods

**Summary:** This method is called after the object is deserialized.

---

## IArchiveReader Methods

**Summary:** Fills an existingIArchivableinstance with deserialized values from the
            underlying stream.

---

## IArchiveReader2 Methods

**Summary:** Creates a shared data storage for this archive reader. A shared data storage contains
            common information shared between multiple archivable objects.

---

## IArchiveReporter Methods

**Summary:** This method is called when an error occurs during serialization or deserialization. The
            code that triggered the serialization should discard the resulting stream because it
            will not be correctly formatted in this case. The code that triggered the
            deserialization should discard the resulting object because it might be inconsistent.

---

## IArchiveVersionInfo Methods

**Summary:** Gets the version number of the specified object's type in the current version profile.

---

## IArchiveWriter Methods

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified stream.

---

## IArchiveWriter2 Methods

**Summary:** Creates a shared data storage for this archive writer. A shared data storage contains
            common information shared between multiple archivable objects.

---

## IEmbeddedObject Methods

**Summary:** This method is called after the object is deserialized.

---

## IFolderObject Methods

**Summary:** Checks whether this object is currently able to have a child of the specified type.

---

## IMetaObject Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject2 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject3 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject4 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject5 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject6 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObject7 Methods

**Summary:** Adds the specified property to this object. If this property is already associated with
            the object, the old values are overwritten.

---

## IMetaObjectStub Methods

**Summary:** Gets the object property with the specified GUID.

---

## IMetaObjectStub2 Methods

**Summary:** Gets the object property with the specified GUID.

---

## IMetaObjectStub3 Methods

**Summary:** Gets the object property with the specified GUID.

---

## IMetaObjectStub4 Methods

**Summary:** Gets the object property with the specified GUID.

---

## IMetaObjectStub5 Methods

**Summary:** Gets the object property with the specified GUID.

---

## IMetaObjectStub6 Methods

**Summary:** Gets the object property with the specified GUID.

---

## IObject Methods

**Summary:** Checks whether this object is currently able to have a child of the specified type.

---

## IObject2 Methods

**Summary:** Checks whether this object is currently able to have a child of the specified type.

---

## IObjectProperty Methods

**Summary:** This method is called after the object is deserialized.

---

## IOrderedSubObjects Methods

**Summary:** Checks whether this object is currently able to have a child of the specified type at
            the specified index.

---

## ISVFoldersProperty Methods

**Summary:** This method is called after the object is deserialized.

---

## ISVNode Methods

**Summary:** Adds a child object. This object is added to this structured view as well as to the
            corresponding Object Manager project (i.e. this object will also be visible for other
            structured views). See[!:IObjectManager.AddObject]for further details.

---

## ISharedDataStorage Methods

**Summary:** Loads the shared data storage information.

---

## IStructuredView Methods

**Summary:** Adds a top-level object. This object is added to this structured view as well as to the
            corresponding Object Manager project (i.e. this object will also be visible for other
            structured views). See[!:IObjectManager.AddObject]for further details.

---

## IUniqueIdGenerator Methods

**Summary:** Returns the next ID.

---

## ObjectManagerException Methods

**Summary:** Gets a formatted message string for this exception. It is required that a string
            resource with the same name as the exception class is defined.

---

## ObjectNameInvalidException Methods

**Summary:** Gets a formatted message string for this exception. It is required that a string
            resource with the same name as the exception class is defined.

---

## SVNodeEventArgs Methods

**Summary:** No summary available.

---

## SVNodeModifiedEventArgs Methods

**Summary:** No summary available.

---

## SVNodeMovedEventArgs Methods

**Summary:** No summary available.

---

## SVNodePropertyModifiedEventArgs Methods

**Summary:** No summary available.

---

## SVNodeRenamedEventArgs Methods

**Summary:** No summary available.

---

## StructuredViewPasteConflictEventArgs Methods

**Summary:** Gets a flag indicating whether the specified paste conflict should be resolved by
            overwriting the conflicting object or not.

---

## StructuredViewPasteNodeEventArgs Methods

**Summary:** No summary available.

---

## Credentials Methods

**Summary:** No summary available.

---

## IDeviceAddress Methods

**Summary:** This method is called after the object is deserialized.

---

## IDeviceGroup Methods

**Summary:** Checks whether adding the specified group member would cause a cyclic membership
            dependency.

---

## IDeviceGroupList Methods

**Summary:** Adds a new group with the specified name.

---

## IDeviceUser Methods

**Summary:** Sets the password for this user.

---

## IDeviceUser2 Methods

**Summary:** Method to set the flags.

---

## IDeviceUserList Methods

**Summary:** Adds a new user with the specified name.

---

## IGateway Methods

**Summary:** Add a device to the gateways cache.

### Syntax
```csharp
1deviceCallback
```

---

## IGatewayDriver Methods

**Summary:** Create an empty device address.

---

## IGatewayParamDescription Methods

**Summary:** Check whether the provided object is a valid value for this
            parameter.

---

## IGatewayParams Methods

**Summary:** This method is called after the object is deserialized.

---

## IOnlineApplication Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication10 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication11 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication12 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication13 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication14 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication2 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication3 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication4 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication5 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication6 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication7 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication8 Methods

**Summary:** INTERNAL USE

---

## IOnlineApplication9 Methods

**Summary:** INTERNAL USE

---

## IOnlineDevice Methods

**Summary:** Asynchronous version of theConnectmethod.

---

## IOnlineVarRef Methods

**Summary:** Get a string describing the current VarRefState. The string will also be used 
            in the message of exceptions thrown byRawValueandValue.

---

## IOnlineVarRef2 Methods

**Summary:** Get a string describing the current VarRefState. The string will also be used 
            in the message of exceptions thrown byRawValueandValue.

---

## IProvideCredentialsArgs Methods

**Summary:** Called by the event handler to cancel the operation instead of providing credentials.

---

## IProvideCredentialsArgs2 Methods

**Summary:** Called by the event handler to cancel the operation instead of providing credentials.

---

## IServiceReader Methods

**Summary:** Close the reader and free resources.

---

## IServiceTagEnumerator Methods

**Summary:** Move to the next element. Initially the enumerator is positioned 
            before the first element. Therefore MoveNext must be called beforeCurrentis accessed for the first time.

---

## IServiceTagReader Methods

**Summary:** Allows for iteration through the subtags of this tag.
            The subtags must be returned in the same order they appear within
            the tag.

---

## ITargetDescription Methods

**Summary:** This method is called after the object is deserialized.

---

## ITargetIdent Methods

**Summary:** This method is called after the object is deserialized.

---

## ITemporaryLoginCredentialsContext Methods

**Summary:** Queries for credentials.

---

## ITemporaryLoginCredentialsContext2 Methods

**Summary:** Queries for credentials.

---

## InvalidDeviceAddress Methods

**Summary:** No summary available.

---

## InvalidVarRefException Methods

**Summary:** No summary available.

---

## NoMonitoringValueException Methods

**Summary:** No summary available.

---

## OnlineCancelDownloadEventArgs Methods

**Summary:** An event handler calls this method to cancel the operation.

---

## OnlineCancelEventArgs Methods

**Summary:** An event handler calls this method to cancel the operation.

---

## OnlineDownloadEventArgs Methods

**Summary:** No summary available.

---

## OnlineEventArgs Methods

**Summary:** No summary available.

---

## OnlineManagerException Methods

**Summary:** No summary available.

---

## OnlineResetEventArgs Methods

**Summary:** No summary available.

---

## PreparedValues Methods

**Summary:** No summary available.

---

## TagTypeException Methods

**Summary:** No summary available.

---

## UserPasswordCredentials Methods

**Summary:** No summary available.

---

## ProjectAttributes Methods

**Summary:** No summary available.

---

## IExtractProjectArchiveNotifyHandler Methods

**Summary:** This method is called to prompt the user whether an already existing item or file
            should be overwritten or not.

---

## IExportReporter Methods

**Summary:** No summary available.

---

## IImportReporter Methods

**Summary:** No summary available.

---

## ILibManager Methods

**Summary:** No summary available.

---

## INativeExportReporter Methods

**Summary:** No summary available.

---

## INativeImportHandler Methods

**Summary:** No summary available.

---

## IScriptApplication Methods

**Summary:** No summary available.

---

## IScriptApplication2 Methods

**Summary:** No summary available.

---

## IScriptApplication3 Methods

**Summary:** No summary available.

---

## IScriptApplication4 Methods

**Summary:** No summary available.

---

## IScriptCommandPermission Methods

**Summary:** No summary available.

---

## IScriptCommands Methods

**Summary:** No summary available.

---

## IScriptComparisonResult Methods

**Summary:** No summary available.

---

## IScriptCompoundDataElement Methods

**Summary:** No summary available.

---

## IScriptConnector Methods

**Summary:** No summary available.

---

## IScriptConnector2 Methods

**Summary:** No summary available.

---

## IScriptDeviceCollection Methods

**Summary:** No summary available.

---

## IScriptDeviceConnector Methods

**Summary:** No summary available.

---

## IScriptDeviceConnector2 Methods

**Summary:** No summary available.

---

## IScriptDeviceConnector3 Methods

**Summary:** No summary available.

---

## IScriptDeviceConnectorSet Methods

**Summary:** No summary available.

---

## IScriptDeviceGroup Methods

**Summary:** No summary available.

---

## IScriptDeviceGroupList Methods

**Summary:** No summary available.

---

## IScriptDeviceObject Methods

**Summary:** No summary available.

---

## IScriptDeviceObject2 Methods

**Summary:** No summary available.

---

## IScriptDeviceObject3 Methods

**Summary:** No summary available.

---

## IScriptDeviceObject4 Methods

**Summary:** No summary available.

---

## IScriptDeviceObject5 Methods

**Summary:** No summary available.

---

## IScriptDeviceObject6 Methods

**Summary:** No summary available.

---

## IScriptDeviceParameter Methods

**Summary:** No summary available.

---

## IScriptDeviceParameter2 Methods

**Summary:** No summary available.

---

## IScriptDeviceParameterSet Methods

**Summary:** No summary available.

---

## IScriptDeviceRepository Methods

**Summary:** No summary available.

---

## IScriptDeviceRepository2 Methods

**Summary:** No summary available.

---

## IScriptDeviceUser Methods

**Summary:** No summary available.

---

## IScriptDeviceUser2 Methods

**Summary:** No summary available.

---

## IScriptDeviceUserList Methods

**Summary:** No summary available.

---

## IScriptDeviceUserManagement Methods

**Summary:** No summary available.

---

## IScriptDriverInfo Methods

**Summary:** No summary available.

---

## IScriptEnumerationDataElement Methods

**Summary:** No summary available.

---

## IScriptExplicitConnectorObject Methods

**Summary:** No summary available.

---

## IScriptExplicitConnectorObject2 Methods

**Summary:** No summary available.

---

## IScriptExplicitConnectorObject3 Methods

**Summary:** No summary available.

---

## IScriptExternalFileObject Methods

**Summary:** No summary available.

---

## IScriptExternalFileObjectContainer Methods

**Summary:** No summary available.

---

## IScriptFactoryPermission Methods

**Summary:** No summary available.

---

## IScriptGateway Methods

**Summary:** No summary available.

---

## IScriptGatewayDrivers Methods

**Summary:** No summary available.

---

## IScriptGatewayParameterDescription Methods

**Summary:** No summary available.

---

## IScriptGatewayParameterDescriptions Methods

**Summary:** No summary available.

---

## IScriptGateways Methods

**Summary:** No summary available.

---

## IScriptGroup Methods

**Summary:** No summary available.

---

## IScriptGroupList Methods

**Summary:** No summary available.

---

## IScriptIecLanguageMemberContainer Methods

**Summary:** No summary available.

---

## IScriptIecLanguageObjectContainer Methods

**Summary:** No summary available.

---

## IScriptIecLanguageObjectContainer2 Methods

**Summary:** No summary available.

---

## IScriptLibManObject Methods

**Summary:** No summary available.

---

## IScriptLibManObject2 Methods

**Summary:** No summary available.

---

## IScriptLibManObjectContainer Methods

**Summary:** No summary available.

---

## IScriptLibraryParameters Methods

**Summary:** No summary available.

---

## IScriptLibraryReference Methods

**Summary:** No summary available.

---

## IScriptLibraryReferences Methods

**Summary:** No summary available.

---

## IScriptLiveDeviceGroup Methods

**Summary:** No summary available.

---

## IScriptLiveDeviceGroupList Methods

**Summary:** No summary available.

---

## IScriptLiveDeviceUserList Methods

**Summary:** No summary available.

---

## IScriptLiveDeviceUserManagement Methods

**Summary:** No summary available.

---

## IScriptManagedLibraryReference Methods

**Summary:** No summary available.

---

## IScriptMappableDeviceParameterSet Methods

**Summary:** No summary available.

---

## IScriptMessage Methods

**Summary:** No summary available.

---

## IScriptObject Methods

**Summary:** No summary available.

---

## IScriptObject2 Methods

**Summary:** No summary available.

---

## IScriptObject3 Methods

**Summary:** No summary available.

---

## IScriptObject4 Methods

**Summary:** No summary available.

---

## IScriptObject5 Methods

**Summary:** No summary available.

---

## IScriptObject6 Methods

**Summary:** No summary available.

---

## IScriptObjectFactories Methods

**Summary:** No summary available.

---

## IScriptObjectPermission Methods

**Summary:** No summary available.

---

## IScriptOnline Methods

**Summary:** No summary available.

---

## IScriptOnline2 Methods

**Summary:** No summary available.

---

## IScriptOnline3 Methods

**Summary:** No summary available.

---

## IScriptOnline4 Methods

**Summary:** No summary available.

---

## IScriptOnline5 Methods

**Summary:** No summary available.

---

## IScriptOnlineApplication Methods

**Summary:** No summary available.

---

## IScriptOnlineApplication2 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice2 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice3 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice4 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice5 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice6 Methods

**Summary:** No summary available.

---

## IScriptOnlineDevice7 Methods

**Summary:** No summary available.

---

## IScriptPermission Methods

**Summary:** No summary available.

---

## IScriptPermissionTypes Methods

**Summary:** No summary available.

---

## IScriptPlaceholderReference Methods

**Summary:** No summary available.

---

## IScriptPouObjectCollection Methods

**Summary:** No summary available.

---

## IScriptProject Methods

**Summary:** No summary available.

---

## IScriptProject10 Methods

**Summary:** No summary available.

---

## IScriptProject11 Methods

**Summary:** No summary available.

---

## IScriptProject12 Methods

**Summary:** No summary available.

---

## IScriptProject2 Methods

**Summary:** No summary available.

---

## IScriptProject3 Methods

**Summary:** No summary available.

---

## IScriptProject4 Methods

**Summary:** No summary available.

---

## IScriptProject5 Methods

**Summary:** No summary available.

---

## IScriptProject6 Methods

**Summary:** No summary available.

---

## IScriptProject7 Methods

**Summary:** No summary available.

---

## IScriptProject8 Methods

**Summary:** No summary available.

---

## IScriptProject9 Methods

**Summary:** No summary available.

---

## IScriptProjectArchiveCategories Methods

**Summary:** No summary available.

---

## IScriptProjectDeviceExtension Methods

**Summary:** No summary available.

---

## IScriptProjectInfoObject Methods

**Summary:** No summary available.

---

## IScriptProjectSettings Methods

**Summary:** No summary available.

---

## IScriptProjects Methods

**Summary:** No summary available.

---

## IScriptProjects2 Methods

**Summary:** No summary available.

---

## IScriptProjects3 Methods

**Summary:** No summary available.

---

## IScriptProjects4 Methods

**Summary:** No summary available.

---

## IScriptProjects5 Methods

**Summary:** No summary available.

---

## IScriptRangeDataElement Methods

**Summary:** No summary available.

---

## IScriptRepositorySourceList Methods

**Summary:** No summary available.

---

## IScriptTaskConfigObject Methods

**Summary:** No summary available.

---

## IScriptTextDocument Methods

**Summary:** No summary available.

---

## IScriptTreeObject Methods

**Summary:** No summary available.

---

## IScriptUI Methods

**Summary:** No summary available.

---

## IScriptUser Methods

**Summary:** No summary available.

---

## IScriptUserList Methods

**Summary:** No summary available.

---

## IScriptUserManagement Methods

**Summary:** No summary available.

---

## IScriptUserOrGroup Methods

**Summary:** No summary available.

---

## IScriptValueDataElement Methods

**Summary:** No summary available.

---

## IScriptVendorDescription Methods

**Summary:** No summary available.

---

## ISystem Methods

**Summary:** No summary available.

---

## ISystem2 Methods

**Summary:** No summary available.

---

## ISystem3 Methods

**Summary:** No summary available.

---

## ISystem4 Methods

**Summary:** No summary available.

---

## ISystem5 Methods

**Summary:** No summary available.

---

## ValuesFailedException Methods

**Summary:** No summary available.

---

## WrongDeviceUserManagementException Methods

**Summary:** No summary available.

---

## IVersionCompatibilityManager Methods

**Summary:** Sets the mode as described inVersionSelectionMode

---

## IVersionCompatibilityManager2 Methods

**Summary:** Sets the mode as described inVersionSelectionMode

---

## IVersionCompatibilityManager3 Methods

**Summary:** Explicitly triggers the checks of the version compatibility manager,
            which are normally done in background when project loading is finished.

---

## IVersionCompatibilityManager4 Methods

**Summary:** Explicitly triggers the checks of the version compatibility manager,
            which are normally done in background when project loading is finished.

---

## UpdateEnvironmentEventArgs Methods

**Summary:** No summary available.

---

## _3S.CoDeSys.Core Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Components Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Device Namespace

**Summary:**

---

## _3S.CoDeSys.Core.External Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Messages Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Objects Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Online Namespace

**Summary:**

---

## _3S.CoDeSys.Core.Online.GwClient Namespace

**Summary:**

---

## _3S.CoDeSys.DeviceObject Namespace

**Summary:**

---

## _3S.CoDeSys.DocExport Namespace

**Summary:**

---

## _3S.CoDeSys.ExternalFileObject Namespace

**Summary:**

---

## _3S.CoDeSys.OnlineUI Namespace

**Summary:**

---

## _3S.CoDeSys.PLCopenXML Namespace

**Summary:**

---

## _3S.CoDeSys.ProjectArchive Namespace

**Summary:**

---

## _3S.CoDeSys.ScriptEngine.BasicFunctionality Namespace

**Summary:** Start here: this namespaces provides the main scripting APIs.

---

## _3S.CoDeSys.TaskConfig Namespace

**Summary:**

---

## _3S.CoDeSys.UserManagement Namespace

**Summary:**

---

## _3S.CoDeSys.VersionCompatibilityManager Namespace

**Summary:**

---

## IFileReference2.GetAbsolutePath Method

**Summary:** Returns the absolute path of this file reference.

---

## IMessageService2.Prompt Method

**Summary:** Prompts the user. This method blocks until the user has answered the question.

---

## IMessageService3.Error Method

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService3.Information Method

**Summary:** Reports an informational message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService3.Prompt Method

**Summary:** Prompts the user. This method blocks until the user has answered the question.

---

## IMessageService3.Warning Method

**Summary:** Reports a warning message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService5.ErrorWithDetails Method

**Summary:** Reports an error message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService5.InformationWithDetails Method

**Summary:** Reports an informational message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService5.PromptWithDetails Method

**Summary:** Prompts the user. This method blocks until the user has answered the question.

---

## IMessageService5.WarningWithDetails Method

**Summary:** Reports a warning message to the user. This method blocks until the user has
            acknowledged this message.

---

## IMessageService.Prompt Method

**Summary:** Prompts the user. This method blocks until the user has answered the question.

---

## IProgressCallback.TaskProgress Method

**Summary:** Call this method when processing of a single task item is starting. The item counter
            will be incremented by one.
            .

---

## IProject3.SetDirty Method

**Summary:** Forces this project to be marked as changed since the last call toSave.

---

## IProject4.Save Method

**Summary:** Saves this project at its physical location (seePath).

---

## IArchivable2.GetSerializableValue Method

**Summary:** Returns the value with the specified symbolic name to be used for serialization.

---

## IArchiveReader2.Fill Method

**Summary:** Fills an existingIArchivableinstance with deserialized values from the
            underlying stream.

---

## IArchiveReader2.Load Method

**Summary:** Deserializes the underlying stream and creates anIArchivablegraph.

---

## IArchiveReader.Initialize Method

**Summary:** Initializes thisIArchiveReaderinstance to load from the specified
            stream.

---

## IArchiveWriter2.Initialize Method

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified stream.

---

## IArchiveWriter2.Save Method

**Summary:** Serializes the specifiedIArchivablegraph to the underlying stream.

---

## IArchiveWriter.Initialize Method

**Summary:** Initializes thisIArchiveWriterinstance to save to the specified stream.

---

## ObjectManagerException Constructor

**Summary:** Creates a new instance of theObjectManagerExceptionclass.

---

## ObjectNameInvalidException Constructor

**Summary:** Initializes a new instance of theObjectNameInvalidExceptionclass.

---

## IDeviceGroupList.Item Property

**Summary:** Gets the group at the specified index.

---

## IDeviceUserList.Item Property

**Summary:** Gets the user at the specified index.

---

## IGatewayDriver.CreateDeviceAddress Method

**Summary:** Create an empty device address.

---

## IOnlineDevice.CreateService Method

**Summary:** Create an instance of a service writer using the standard 
            service protocol (0xCD55 or 0x55CD respectivly, depending on the
            byteorder). Uses the targets byteorder. 
            After filling the instance with the service parameters it can be
            passed toExecuteService(IServiceWriter).

---

## IOnlineDevice.ReadApplicationList Method

**Summary:** Reads the complete list of applications currently available on this device.

---

## IServiceTagReader.ReadBytes Method

**Summary:** Return the content from the current position to the end of the
            tag as an array of bytes.

---

## ILibManager.get_all_libraries Method

**Summary:** No summary available.

---

## IScriptApplication2.create_boot_application Method

**Summary:** No summary available.

---

## IScriptCommands.Item Property

**Summary:** No summary available.

---

## IScriptComparisonResult.Item Property

**Summary:** No summary available.

---

## IScriptCompoundDataElement.Item Property

**Summary:** No summary available.

---

## IScriptCompoundDataElement.contains Method

**Summary:** No summary available.

---

## IScriptDeviceConnectorSet.Item Property

**Summary:** No summary available.

---

## IScriptDeviceConnectorSet.contains Method

**Summary:** No summary available.

---

## IScriptDeviceGroupList.Item Property

**Summary:** No summary available.

---

## IScriptDeviceObject4.set_gateway_and_address Method

**Summary:** No summary available.

---

## IScriptDeviceObject4.set_gateway_and_device_name Method

**Summary:** No summary available.

---

## IScriptDeviceObject4.set_gateway_and_ip_address Method

**Summary:** No summary available.

---

## IScriptDeviceObject.add Method

**Summary:** No summary available.

---

## IScriptDeviceObject.insert Method

**Summary:** No summary available.

---

## IScriptDeviceObject.plug Method

**Summary:** No summary available.

---

## IScriptDeviceObject.set_gateway_and_address Method

**Summary:** No summary available.

---

## IScriptDeviceObject.update Method

**Summary:** No summary available.

---

## IScriptDeviceParameterSet.Item Property

**Summary:** No summary available.

---

## IScriptDeviceParameterSet.contains Method

**Summary:** No summary available.

---

## IScriptDeviceRepository2.import_device Method

**Summary:** No summary available.

---

## IScriptDeviceRepository.get_all_devices Method

**Summary:** No summary available.

---

## IScriptDeviceRepository.get_all_vendor_descriptions Method

**Summary:** No summary available.

---

## IScriptDeviceRepository.get_device_category Method

**Summary:** No summary available.

---

## IScriptDeviceRepository.import_device Method

**Summary:** No summary available.

---

## IScriptDeviceRepository.import_vendor_description Method

**Summary:** No summary available.

---

## IScriptDeviceUserList.Item Property

**Summary:** No summary available.

---

## IScriptDeviceUserManagement.load Method

**Summary:** No summary available.

---

## IScriptDeviceUserManagement.save Method

**Summary:** No summary available.

---

## IScriptDriverInfo.set_bus_cycle_task Method

**Summary:** No summary available.

---

## IScriptEnumerationDataElement.write_online_value Method

**Summary:** No summary available.

---

## IScriptExplicitConnectorObject.add Method

**Summary:** No summary available.

---

## IScriptExplicitConnectorObject.insert Method

**Summary:** No summary available.

---

## IScriptExternalFileObject.get_data Method

**Summary:** No summary available.

---

## IScriptGatewayDrivers.Item Property

**Summary:** No summary available.

---

## IScriptGatewayParameterDescriptions.Item Property

**Summary:** No summary available.

---

## IScriptGateway.find_address_by_ip Method

**Summary:** No summary available.

---

## IScriptGateways.Item Property

**Summary:** No summary available.

---

## IScriptGateways.remove_gateway Method

**Summary:** No summary available.

---

## IScriptGroupList.Item Property

**Summary:** No summary available.

---

## IScriptIecLanguageObjectContainer2.create_pou Method

**Summary:** No summary available.

---

## IScriptLibManObject2.add_library Method

**Summary:** No summary available.

---

## IScriptLibManObject2.add_placeholder Method

**Summary:** No summary available.

---

## IScriptLibraryReferences.Item Property

**Summary:** No summary available.

---

## IScriptLiveDeviceGroupList.Item Property

**Summary:** No summary available.

---

## IScriptLiveDeviceUserList.Item Property

**Summary:** No summary available.

---

## IScriptObject2.export_xml Method

**Summary:** No summary available.

---

## IScriptObject2.import_native Method

**Summary:** No summary available.

---

## IScriptObject2.import_xml Method

**Summary:** No summary available.

---

## IScriptObject4.export_xml Method

**Summary:** No summary available.

---

## IScriptObject5.export_xml Method

**Summary:** No summary available.

---

## IScriptObject5.import_xml Method

**Summary:** No summary available.

---

## IScriptObject.move Method

**Summary:** No summary available.

---

## IScriptOnlineApplication.read_values Method

**Summary:** No summary available.

---

## IScriptOnlineDevice3.download_source Method

**Summary:** No summary available.

---

## IScriptPermission.check_permission Method

**Summary:** No summary available.

---

## IScriptPouObjectCollection.remove Method

**Summary:** No summary available.

---

## IScriptProject2.export_xml Method

**Summary:** No summary available.

---

## IScriptProject2.import_native Method

**Summary:** No summary available.

---

## IScriptProject2.import_xml Method

**Summary:** No summary available.

---

## IScriptProject6.create_folder Method

**Summary:** No summary available.

---

## IScriptProject7.export_xml Method

**Summary:** No summary available.

---

## IScriptProject8.save_archive Method

**Summary:** No summary available.

---

## IScriptProject9.export_xml Method

**Summary:** No summary available.

---

## IScriptProject9.import_xml Method

**Summary:** No summary available.

---

## IScriptProject9.save_archive Method

**Summary:** No summary available.

---

## IScriptProjectArchiveCategories.Item Property

**Summary:** No summary available.

---

## IScriptProjectDeviceExtension.add Method

**Summary:** No summary available.

---

## IScriptProject.document Method

**Summary:** No summary available.

---

## IScriptProjects2.convert Method

**Summary:** No summary available.

---

## IScriptProjects3.open Method

**Summary:** No summary available.

---

## IScriptProjects3.open_archive Method

**Summary:** No summary available.

---

## IScriptProjects4.open Method

**Summary:** No summary available.

---

## IScriptProjects4.open_archive Method

**Summary:** No summary available.

---

## IScriptProjects5.open_archive Method

**Summary:** No summary available.

---

## IScriptRepositorySourceList.Item Property

**Summary:** No summary available.

---

## IScriptTextDocument.get_text Method

**Summary:** No summary available.

---

## IScriptTextDocument.insert Method

**Summary:** No summary available.

---

## IScriptTextDocument.remove Method

**Summary:** No summary available.

---

## IScriptTextDocument.replace Method

**Summary:** No summary available.

---

## IScriptTreeObject.find Method

**Summary:** No summary available.

---

## IScriptUserList.Item Property

**Summary:** No summary available.

---

## IScriptUserManagement.get_command_permission Method

**Summary:** No summary available.

---

## IScriptUserManagement.get_factory_permission Method

**Summary:** No summary available.

---

## ISystem3.get_message_objects Method

**Summary:** No summary available.

---

## ISystem3.write_message Method

**Summary:** No summary available.

---

## ISystem.get_messages Method

**Summary:** No summary available.

---

## ExactVersionConstraint.Version Property

**Summary:** Returns the component version which is to be picked exactly.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version Version { get; }
```

---

## NewestBeforeVersionConstraint.Version Property

**Summary:** Returns the "maximum" component version which is to be picked.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version Version { get; }
```

---

## NewestBetweenVersionConstraint.FromVersion Property

**Summary:** Returns the lower bound component version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version FromVersion { get; }
```

---

## NewestBetweenVersionConstraint.ToVersion Property

**Summary:** Returns the upper bound component version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version ToVersion { get; }
```

---

## OldestAfterVersionConstraint.Version Property

**Summary:** Returns the "minimum" component version which is to be picked.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version Version { get; }
```

---

## OldestBetweenVersionConstraint.FromVersion Property

**Summary:** Returns the lower bound component version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version FromVersion { get; }
```

---

## OldestBetweenVersionConstraint.ToVersion Property

**Summary:** Returns the upper bound component version.

**Assembly:** `ComponentModel (in ComponentModel.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Version ToVersion { get; }
```

---

## IDeviceIdentification.Id Property

**Summary:** Id of the device. The format for this id is specified 
            	for each type. The id is unique within the class of devices
            	of one type.

**Assembly:** `DeviceIdentification (in DeviceIdentification.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Id { get; }
```

---

## IDeviceIdentification.Type Property

**Summary:** Type of the device.

**Assembly:** `DeviceIdentification (in DeviceIdentification.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Type { get; }
```

---

## IDeviceIdentification.Version Property

**Summary:** The version of the device. The format for the version string is
            	specified for each type.

**Assembly:** `DeviceIdentification (in DeviceIdentification.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Version { get; }
```

---

## FileReferenceCancelEventArgs.FileReference Property

**Summary:** Gets the affected file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IFileReference FileReference { get; }
```

---

## FileReferenceEventArgs.FileReference Property

**Summary:** Gets the affected file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IFileReference FileReference { get; }
```

---

## IFileReference3.OwningProjectHandle Property

**Summary:** Gets the project handle the file reference belongs to.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
int OwningProjectHandle { get; }
```

---

## IFileReference.AutoUpdateMode Property

**Summary:** Gets or sets the automatic update mode for this file reference.If set toAlways, changes on the
            physical file are automatically reflected in the embedded data.If set toNever, changes on the
            physical file are not automatically reflected in the embedded data. Updates can be
            performed by an explicit call toUpdate.If set toPrompt, when the
            pyhsical file changes, thePromptUpdateevent will be triggered in order
            to obtain information whether to automatically update the embedded data or not.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
AutoUpdateMode AutoUpdateMode { get; set; }
```

---

## IFileReference.Embedded Property

**Summary:** Gets or sets a boolean value indicating whether the contents of this file reference
            should be embedded into the corresponding Object Manager project.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Embedded { get; set; }
```

---

## IFileReference.FileId Property

**Summary:** Gets the file ID for this file reference. The content of this string is transparent to
            the caller.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string FileId { get; }
```

---

## IFileReference.Frozen Property

**Summary:** Gets a boolean value indicating whether this file reference is still linked to a file
            system object (return valuefalse) or not (return valuetrue).

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Frozen { get; }
```

---

## IFileReference.LastModification Property

**Summary:** Gets the timestamp of the last modification of this file reference.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
DateTime LastModification { get; }
```

---

## IFileReference.ProjectHandle Property

**Summary:** Gets the project handle, if this file reference is loaded as Object Manager project, or-1otherwise.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## IFileReference.RelativePath Property

**Summary:** Gets the relative path of this file reference which will be resolved withSystemFolder, or the absolute path.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
string RelativePath { get; }
```

---

## IFileReference.SystemFolder Property

**Summary:** Gets the GUID of the system folder which is used to resolve the relative path of this
            file reference, orGuid.Emptyif this file reference points to an absolute path.

**Assembly:** `External (in External.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid SystemFolder { get; }
```

---

## IProgressCallback.Abortable Property

**Summary:** Gets or sets a boolean value indicating whether the operation is cancellable by the
            user.

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Abortable { get; set; }
```

---

## IProgressCallback.Aborting Property

**Summary:** IfAbortableistrue, gets a boolean value indicating whether the
            user attempts to cancel this operation or not,falseotherwise.

**Assembly:** `Engine (in Engine.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Aborting { get; }
```

---

## IProject2.ReadOnly Property

**Summary:** Gets a boolean value indicating whether theReadOnlyattribute has been set for this project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool ReadOnly { get; }
```

---

## IProject5.ExplicitlySaved Property

**Summary:** Iffalse, the projects files are deleted after closing the project. Default value istrue.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool ExplicitlySaved { get; set; }
```

---

## IProject.ActiveApplication Property

**Summary:** Gets or sets the GUID of the currently active application object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ActiveApplication { get; set; }
```

---

## IProject.Attributes Property

**Summary:** Gets an array containing all attributes set for this project. See theProjectAttributesclass for available project attributes.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid[] Attributes { get; }
```

---

## IProject.Dirty Property

**Summary:** Gets a boolean value indicating whether this project has been changed since the last
            call toSave.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Dirty { get; }
```

---

## IProject.Handle Property

**Summary:** The handle of the corresponding Object Manager project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Handle { get; }
```

---

## IProject.Id Property

**Summary:** Gets or sets a string which uniquely identifies this project if it is referenced by
            another project. This is typically meaningful for libraries: here the library's fully
            qualified name (not path!) is returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Id { get; set; }
```

---

## IProject.Library Property

**Summary:** Gets a boolean value indicating whether theLibraryattribute has been set for this project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Library { get; }
```

---

## IProject.Path Property

**Summary:** Gets or sets the absolute path where this project is physically stored.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Path { get; set; }
```

---

## IProject.Primary Property

**Summary:** Gets a boolean value indicating whether thePrimaryattribute has been set for this project.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Primary { get; }
```

---

## IProject.SelectedSVNodes Property

**Summary:** Gets or sets an (possibly empty) array of structured view nodes which are currently
            selected.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode[] SelectedSVNodes { get; set; }
```

---

## IMessage2.FontColor Property

**Summary:** Gets the color of the message text.	Return System.Drawing.Color.Empty, if you do not want to change the default.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Color FontColor { get; }
```

---

## IMessage3.DetailsHandler Property

**Summary:** Gets a details handler for this message. If notnull, this is a hint for the UI
            to display something like a ... button for the message, which will invoke this handler
            on click. Ifnull, this message does not offer any details, and behaves like a
            standard message.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
MessageDetailsHandler DetailsHandler { get; }
```

---

## IMessage3.DetailsHandlerData Property

**Summary:** Gets user-defined data to be passed to theDetailsHandler.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object DetailsHandlerData { get; }
```

---

## IMessage4.Icon Property

**Summary:** Specialized Icon. If null, the icon is set according to the severity.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Icon Icon { get; }
```

---

## IMessage4.Number Property

**Summary:** Unambigous number identifying the message according to its category (compile, LINT, IO-Config, etc).
            Together with thePrefix, the number identifies the message.
            null is returned if not used.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Nullable<uint> Number { get; }
```

---

## IMessage4.Prefix Property

**Summary:** A prefix string identifying the message category (compile, LINT, IO-Config, etc). Together with theNumber,
            the message is unambigously identified.
            null is returned if not used.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Prefix { get; }
```

---

## IMessageCategory.Icon Property

**Summary:** Gets the icon of the message category. A message view might use
            this to decorate the corresponding tab page. If desired, this icon
            can be localized.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Icon Icon { get; }
```

---

## IMessageCategory.Text Property

**Summary:** Gets the text of the message category. This string should be
            localized.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Text { get; }
```

---

## IMessage.Length Property

**Summary:** Gets length of Position.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
short Length { get; }
```

---

## IMessage.ObjectGuid Property

**Summary:** The GUID of the database object of the message position. If this
            message does not have a position,Emptyis
            returned.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectGuid { get; }
```

---

## IMessage.Position Property

**Summary:** The position within the database object of the message position.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
long Position { get; }
```

---

## IMessage.PositionOffset Property

**Summary:** Gets an additional character offset to the position returned by thePositionproperty.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
short PositionOffset { get; }
```

---

## IMessage.ProjectHandle Property

**Summary:** The handle of the project of the message position. If this message
            does not have a position, -1 is returned.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## IMessage.Severity Property

**Summary:** Gets the severity of this message.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
Severity Severity { get; }
```

---

## IMessage.Text Property

**Summary:** Gets the message text. This string can be localized, if desired.

**Assembly:** `MessageStorage (in MessageStorage.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Text { get; }
```

---

## IArchivable.SerializableValueNames Property

**Summary:** Gets the symbolic names of the values which should be serialized.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string[] SerializableValueNames { get; }
```

---

## IArchiveReader.ThrowIfTypeIsMissing Property

**Summary:** Determines whether theLoadorFill(IArchivable)methods should throw an
            exception when a stored type cannot be resolved. If this property isfalse, the
            concerning fields/properties are set tonull. Default value istrue.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool ThrowIfTypeIsMissing { get; set; }
```

---

## IArchiveVersionInfo.Profile Property

**Summary:** Gets the version profile for which a compatible serialization stream should be
            generated.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Profile Profile { get; }
```

---

## IEmbeddedObject.OwnerObject Property

**Summary:** Gets the owner object of this embedded object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObject OwnerObject { get; set; }
```

---

## IFolderObject.StructuredViewGuid Property

**Summary:** Gets or sets the GUID of the structured view where this folder object is associated
            with.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid StructuredViewGuid { get; set; }
```

---

## IIncompleteDeserializationInfo.Cancellation Property

**Summary:** Gets a message why deserialization has been cancelled prematurely, ornull.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Cancellation { get; }
```

---

## IIncompleteDeserializationInfo.Type Property

**Summary:** Gets the type of the target that is being deserialized. This property is used in
            conjunction withUnknownSerializableValueName. IfUnknownSerializableValueNameisnull, this property will also returnnull.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Type Type { get; }
```

---

## IIncompleteDeserializationInfo.UnknownObject Property

**Summary:** Gets a boolean value indicating whether the entire object is unknown (not only one of
            its data members).

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool UnknownObject { get; }
```

---

## IIncompleteDeserializationInfo.UnknownSerializableValueName Property

**Summary:** Gets the serializable value name that appeared in the data stream, but is not known by
            the deserializedType, ornull.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string UnknownSerializableValueName { get; }
```

---

## IIncompleteDeserializationInfo.Warning Property

**Summary:** Gets a warning message that has been raised during deserialization, ornull.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Warning { get; }
```

---

## IMetaObject3.TimeStamp Property

**Summary:** Gets the timestamp of the last change of this object as a tick value.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
long TimeStamp { get; }
```

---

## IMetaObject4.ModificationCounter Property

**Summary:** Gets a counter that is incremented each time a modification on that object appears.
            This counter can be used to check whether a triggered modification is still the last
            modification, or if subsequent modifications have been implicitely happened. Note that
            this counter is not persistently stored.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ModificationCounter { get; }
```

---

## IMetaObject5.DeserializedIncompletely Property

**Summary:** Gets a boolean value indicating whether the object could not be loaded completely.
            That means that the project data stream contained information that was not assigned
            to a member.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool DeserializedIncompletely { get; }
```

---

## IMetaObject6.IncompleteDeserializationInfo Property

**Summary:** Gets more detailed diagnostics information to be used for debugging purposes for the
            case thatDeserializedIncompletelyistrue. If the
            object has been deserialized completely,nullwill be returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IIncompleteDeserializationInfo IncompleteDeserializationInfo { get; }
```

---

## IMetaObject7.EmbeddedObjectTypeGuids Property

**Summary:** Gets the embedded type GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IEnumerable<Guid> EmbeddedObjectTypeGuids { get; }
```

---

## IMetaObject7.ObjectTypeGuid Property

**Summary:** Gets the object's type GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectTypeGuid { get; }
```

---

## IMetaObject7.PropertyTypeGuids Property

**Summary:** Get the property type GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IEnumerable<Guid> PropertyTypeGuids { get; }
```

---

## IMetaObjectStub2.TimeStamp Property

**Summary:** Gets the timestamp of the last change of this object as a tick value.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
long TimeStamp { get; }
```

---

## IMetaObjectStub3.ModificationCounter Property

**Summary:** Gets a counter that is incremented each time a modification on that object appears.
            This counter can be used to check whether a triggered modification is still the last
            modification, or if subsequent modifications have been implicitely happened. Note that
            this counter is not persistently stored.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ModificationCounter { get; }
```

---

## IMetaObjectStub4.DeserializedIncompletely Property

**Summary:** Gets a boolean value indicating whether the object could not be loaded completely.
            That means that the project data stream contained information that was not assigned
            to a member.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool DeserializedIncompletely { get; }
```

---

## IMetaObjectStub5.IncompleteDeserializationInfo Property

**Summary:** Gets more detailed diagnostics information to be used for debugging purposes for the
            case thatDeserializedIncompletelyistrue. If
            the object has been deserialized completely,nullwill be returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IIncompleteDeserializationInfo IncompleteDeserializationInfo { get; }
```

---

## IMetaObjectStub6.EmbeddedObjectTypeGuids Property

**Summary:** Gets the embedded type GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IEnumerable<Guid> EmbeddedObjectTypeGuids { get; }
```

---

## IMetaObjectStub6.ObjectTypeGuid Property

**Summary:** Gets the object's type GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectTypeGuid { get; }
```

---

## IMetaObjectStub6.PropertyTypeGuids Property

**Summary:** Get the property type GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IEnumerable<Guid> PropertyTypeGuids { get; }
```

---

## IMetaObjectStub.EmbeddedObjectTypes Property

**Summary:** Gets the types of the embedded objects, if any.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Type[] EmbeddedObjectTypes { get; }
```

---

## IMetaObjectStub.Index Property

**Summary:** IfOrderedSubObjectsistrue, this property gets the index of this
            object within its parent's children. Otherwise,-1is returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Index { get; }
```

---

## IMetaObjectStub.Name Property

**Summary:** Gets the name of the object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## IMetaObjectStub.Namespace Property

**Summary:** Gets the namespace of this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid Namespace { get; }
```

---

## IMetaObjectStub.ObjectGuid Property

**Summary:** Gets the GUID of the object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectGuid { get; }
```

---

## IMetaObjectStub.ObjectType Property

**Summary:** Gets the type of the contained object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Type ObjectType { get; }
```

---

## IMetaObjectStub.OrderedSubObjects Property

**Summary:** Gets a boolean value indicating whether the subobjects of this object have got a
            particular order. The array returned bySubObjectGuidsmust be considered
            as ordered array then.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool OrderedSubObjects { get; }
```

---

## IMetaObjectStub.ParentObjectGuid Property

**Summary:** Gets the parent object GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ParentObjectGuid { get; }
```

---

## IMetaObjectStub.ProjectHandle Property

**Summary:** Gets the handle of the project the object belongs to.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## IMetaObjectStub.Properties Property

**Summary:** Gets an array containing all properties associated with the specified object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObjectProperty[] Properties { get; }
```

---

## IMetaObjectStub.SubObjectGuids Property

**Summary:** Gets a list of all sub-object GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid[] SubObjectGuids { get; }
```

---

## IMetaObject.Index Property

**Summary:** IfOrderedSubObjectsistrue, this property gets the index of this
            object within its parent's children. Otherwise,-1is returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Index { get; }
```

---

## IMetaObject.IsToModify Property

**Summary:** Gets a value indicating whether this meta-object is currently modifiable.
            Calling this property is equivalent to calling[!:IObjectManager.IsObjectToModify].

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsToModify { get; }
```

---

## IMetaObject.Name Property

**Summary:** Gets the name of the object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## IMetaObject.Namespace Property

**Summary:** Gets the namespace of this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid Namespace { get; }
```

---

## IMetaObject.Object Property

**Summary:** Gets the contained object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObject Object { get; }
```

---

## IMetaObject.ObjectGuid Property

**Summary:** Gets the GUID of the object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectGuid { get; }
```

---

## IMetaObject.OrderedSubObjects Property

**Summary:** Gets a boolean value indicating whether the subobjects of this object have got a
            particular order. The array returned bySubObjectGuidsmust be considered
            as ordered array then.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool OrderedSubObjects { get; }
```

---

## IMetaObject.ParentObjectGuid Property

**Summary:** Gets the parent object GUID.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ParentObjectGuid { get; }
```

---

## IMetaObject.ProjectHandle Property

**Summary:** Gets the handle of the project the object belongs to.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## IMetaObject.Properties Property

**Summary:** Gets an array containing all properties associated with the specified object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IObjectProperty[] Properties { get; }
```

---

## IMetaObject.SubObjectGuids Property

**Summary:** Gets a list of all sub-object GUIDs.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid[] SubObjectGuids { get; }
```

---

## IObject.CanRename Property

**Summary:** Gets a value indicating whether this object can be renamed or not.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool CanRename { get; }
```

---

## IObject.EmbeddedObjects Property

**Summary:** Gets the embedded objects of this object, ornullif this is not meaningful for
            a particular implementation.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IEmbeddedObject[] EmbeddedObjects { get; }
```

---

## IObject.MetaObject Property

**Summary:** Gets or sets the containingIMetaObjectinstance.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IMetaObject MetaObject { get; set; }
```

---

## IObject.Namespace Property

**Summary:** Gets a GUID identifying the namespace of this object. Within an object tree, two
            sibling objects cannot have the same name if they belong to the same namespace.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid Namespace { get; }
```

---

## IObject.UniqueIdGenerator Property

**Summary:** Gets the unique ID generator associated for this object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IUniqueIdGenerator UniqueIdGenerator { get; }
```

---

## ISVFoldersProperty.StructuredViews Property

**Summary:** Gets an array containing all structured views where the corresponding object has got a
            folder parent.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid[] StructuredViews { get; }
```

---

## ISVNode.ChildCount Property

**Summary:** Gets the number of child nodes of this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ChildCount { get; }
```

---

## ISVNode.Children Property

**Summary:** Gets a (possibly empty) array containing the child nodes of this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode[] Children { get; }
```

---

## ISVNode.Index Property

**Summary:** Gets the zero-based index of this node within the child list of its parent. This
            property is only meaningful if the parent node'sOrderedSubObjectsproperty yieldstrue, otherwise-1is returned.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Index { get; }
```

---

## ISVNode.IsFolder Property

**Summary:** Gets a boolean value indicating whether this structured view node represents a folder
            object or not.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsFolder { get; }
```

---

## ISVNode.Name Property

**Summary:** Gets the name of the object which is represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## ISVNode.ObjectGuid Property

**Summary:** Gets the GUID of the object which is represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ObjectGuid { get; }
```

---

## ISVNode.ObjectType Property

**Summary:** Gets the type of the object which is represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Type ObjectType { get; }
```

---

## ISVNode.OrderedSubObjects Property

**Summary:** Gets a boolean flag indicating whether the child nodes of this node are ordered. This
            is the case if the corresponding object implements theIOrderedSubObjectsinterface.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool OrderedSubObjects { get; }
```

---

## ISVNode.Parent Property

**Summary:** Gets the parent node of this structured view node, ornullif this is a
            top-level node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode Parent { get; }
```

---

## ISVNode.ProjectHandle Property

**Summary:** Gets the handle of the project which is represented by this structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## ISVNode.StructuredView Property

**Summary:** Gets theIStructuredViewwhich this node belongs to.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
IStructuredView StructuredView { get; }
```

---

## IStructuredView.ChildCount Property

**Summary:** Gets the number of top-level nodes of this structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ChildCount { get; }
```

---

## IStructuredView.Children Property

**Summary:** Gets a (possibly empty) array containing the top-level nodes of this structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
ISVNode[] Children { get; }
```

---

## IStructuredView.ProjectHandle Property

**Summary:** Gets the handle of the project which is represented by this structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ProjectHandle { get; }
```

---

## IStructuredView.StructuredViewGuid Property

**Summary:** Gets the GUID which identifies this structured view.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid StructuredViewGuid { get; }
```

---

## ObjectManagerException.ObjectName Property

**Summary:** Gets the name of the affected object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
protected string ObjectName { get; }
```

---

## ObjectNameInvalidException.Message Property

**Summary:** Gets a message which describes the current exception.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public override string Message { get; }
```

---

## ObjectNameInvalidException.Name Property

**Summary:** Gets the bname which is not allowed for the corresponding object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string Name { get; }
```

---

## ObjectNameInvalidException.ObjectGuid Property

**Summary:** Gets the GUID of the object in question.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid ObjectGuid { get; }
```

---

## ObjectNameInvalidException.ProjectHandle Property

**Summary:** Gets the handle to the project in question.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public int ProjectHandle { get; }
```

---

## SVNodeEventArgs.Index Property

**Summary:** Gets the zero-based order index of the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public int Index { get; }
```

---

## SVNodeEventArgs.Node Property

**Summary:** Gets the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode Node { get; }
```

---

## SVNodeModifiedEventArgs.Editor Property

**Summary:** Gets the editor which modified the object represented by affected structured view node
            ornullif unknown.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Object Editor { get; }
```

---

## SVNodeModifiedEventArgs.Node Property

**Summary:** Gets the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode Node { get; }
```

---

## SVNodeMovedEventArgs.NewIndex Property

**Summary:** Gets the new zero-based order index of the affected object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public int NewIndex { get; }
```

---

## SVNodeMovedEventArgs.NewParent Property

**Summary:** Gets the new parent of the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode NewParent { get; }
```

---

## SVNodeMovedEventArgs.Node Property

**Summary:** Gets the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode Node { get; }
```

---

## SVNodeMovedEventArgs.OldIndex Property

**Summary:** Gets the old zero-based order index of the affected object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public int OldIndex { get; }
```

---

## SVNodeMovedEventArgs.OldParent Property

**Summary:** Gets the old parent of the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode OldParent { get; }
```

---

## SVNodePropertyModifiedEventArgs.NewProperty Property

**Summary:** Gets the new property.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IObjectProperty NewProperty { get; }
```

---

## SVNodePropertyModifiedEventArgs.Node Property

**Summary:** Gets the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode Node { get; }
```

---

## SVNodePropertyModifiedEventArgs.OldProperty Property

**Summary:** Gets the old property.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IObjectProperty OldProperty { get; }
```

---

## SVNodeRenamedEventArgs.NewName Property

**Summary:** Gets the new name of the object represented by the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string NewName { get; }
```

---

## SVNodeRenamedEventArgs.Node Property

**Summary:** Gets the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ISVNode Node { get; }
```

---

## SVNodeRenamedEventArgs.OldName Property

**Summary:** Gets the old name of the object represented by the affected structured view node.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string OldName { get; }
```

---

## StructuredViewPasteConflictEventArgs.Conflicts Property

**Summary:** Gets an array containing thePasteConflictinstances to handle.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public PasteConflict[] Conflicts { get; }
```

---

## StructuredViewPasteNodeEventArgs.Exception Property

**Summary:** Gets the exception object describing the failure during pasting the specified object,
            ornull.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Exception Exception { get; }
```

---

## StructuredViewPasteNodeEventArgs.Name Property

**Summary:** Gets the name of the pasted object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string Name { get; }
```

---

## StructuredViewPasteNodeEventArgs.Object Property

**Summary:** Gets the pasted object itself.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IObject Object { get; }
```

---

## StructuredViewPasteNodeEventArgs.ObjectGuid Property

**Summary:** Gets the GUID of the pasted object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid ObjectGuid { get; }
```

---

## StructuredViewPasteNodeEventArgs.ParentSVNodeGuid Property

**Summary:** Gets the GUID of the parent of the pasted object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid ParentSVNodeGuid { get; }
```

---

## StructuredViewPasteNodeEventArgs.Properties Property

**Summary:** Gets the properties of the pasted object.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public IObjectProperty[] Properties { get; }
```

---

## ICallStackEntry.LocationInstance Property

**Summary:** The location of the instance of the FB or POU (effectivly the "this" pointer).
            	If the POU is a function, then this points to the variables on the stack.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDataLocation LocationInstance { get; }
```

---

## ICallStackEntry.LocationPOU Property

**Summary:** Location of the current code position (effectively the value of the instruction pointer).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDataLocation LocationPOU { get; }
```

---

## IDeviceAddress.Length Property

**Summary:** Get the length of this device address. The length is the number 
            of address components that make up this address.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Length { get; }
```

---

## IDeviceGroupList.Count Property

**Summary:** Gets the number of groups in this list.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Count { get; }
```

---

## IDeviceGroupList.Flags Property

**Summary:** Gets flags concerning the entire group list.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DeviceUserManagementFlags Flags { get; }
```

---

## IDeviceGroupList.Item Property (Int32)

**Summary:** Gets the group at the specified index.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceGroup this[
	int index
] { get; }
```

---

## IDeviceGroupList.Item Property (String)

**Summary:** Gets the group with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceGroup this[
	string stName
] { get; }
```

---

## IDeviceGroup.Flags Property

**Summary:** Gets flags concerning this particular group.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DeviceUserManagementFlags Flags { get; }
```

---

## IDeviceGroup.GroupMembers Property

**Summary:** Gets the list of all group names which are members of this group.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IList<string> GroupMembers { get; }
```

---

## IDeviceGroup.Name Property

**Summary:** Gets or sets the name of the group.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; set; }
```

---

## IDeviceGroup.UserMembers Property

**Summary:** Gets the list of all user names which are members of this group.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IList<string> UserMembers { get; }
```

---

## IDeviceUserList.Count Property

**Summary:** Gets the number of users in this list.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Count { get; }
```

---

## IDeviceUserList.Flags Property

**Summary:** Gets flags concerning the entire user list.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DeviceUserManagementFlags Flags { get; }
```

---

## IDeviceUserList.Item Property (Int32)

**Summary:** Gets the user at the specified index.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceUser this[
	int index
] { get; }
```

---

## IDeviceUserList.Item Property (String)

**Summary:** Gets the user with the specified name.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceUser this[
	string stName
] { get; }
```

---

## IDeviceUser.Flags Property

**Summary:** Gets flags concerning this particular user.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DeviceUserManagementFlags Flags { get; }
```

---

## IDeviceUser.Name Property

**Summary:** Gets or sets the name of the user.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; set; }
```

---

## IDeviceUser.PasswordHash Property

**Summary:** Gets or sets the encrypted password for this user.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string PasswordHash { get; set; }
```

---

## IGatewayDriver.DriverGuid Property

**Summary:** A Guid that uniquely identifies the driver type.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid DriverGuid { get; }
```

---

## IGatewayDriver.MinPingInterval Property

**Summary:** To show the status whether a gateway is reachable, an application might want to 
            ping a gateway in regular intervals to check if it still does respond.
            This property returns the minimum time to wait between to such pings. This is especially usefull
            when connecting to a gateway over a slow or expensive link, like a dial-up connection.If this property returns 0, the gateway shall not be pinged at all!

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int MinPingInterval { get; }
```

---

## IGatewayDriver.Name Property

**Summary:** Get the user-readable name of this gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## IGatewayParamDescription.Default Property

**Summary:** Default value of the parameter. May be null.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object Default { get; }
```

---

## IGatewayParamDescription.Description Property

**Summary:** Human readable string describing the parameter.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Description { get; }
```

---

## IGatewayParamDescription.Id Property

**Summary:** The id of the parameter.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long Id { get; }
```

---

## IGatewayParamDescription.Name Property

**Summary:** Human readable string, givin the name of the parameter.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## IGatewayParamDescription.ParamType Property

**Summary:** The type of the parameter value.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ParamType ParamType { get; }
```

---

## IGatewayParams.Ids Property

**Summary:** returns the ids of all parameters in this object.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long[] Ids { get; }
```

---

## IGatewayParams.Item Property

**Summary:** Access a parameter value by the parameter id (not the index).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object this[
	long lParamId
] { get; set; }
```

---

## IGateway.Driver Property

**Summary:** This property is only provided for convenience and returns the
            GatewayDriver object for this gateway;

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IGatewayDriver Driver { get; }
```

---

## IGateway.DriverGuid Property

**Summary:** The guid of the gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid DriverGuid { get; set; }
```

---

## IGateway.DriverName Property

**Summary:** The name of the gateway driver. This parameter is only informational.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string DriverName { get; }
```

---

## IGateway.DriverParameters Property

**Summary:** Current configuration of the gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IGatewayParams DriverParameters { get; set; }
```

---

## IGateway.Flags Property

**Summary:** Flags field indicating certain properties of the gateway.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
GatewayFlags Flags { get; set; }
```

---

## IGateway.GatewayGuid Property

**Summary:** A gateway is defined by its Guid

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid GatewayGuid { get; }
```

---

## IGateway.IsConnected Property

**Summary:** Return wether an active connection to the gateway exists.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsConnected { get; }
```

---

## IGateway.Name Property

**Summary:** The (userdefined) name of the gateway.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; set; }
```

---

## IMonitoringExpression.Forced Property

**Summary:** Get or set whether this variable is currently forced.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Forced { get; set; }
```

---

## IMonitoringExpression.MonitoringSuspended Property

**Summary:** Get if monitoring for this variable is currently suspended.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool MonitoringSuspended { get; }
```

---

## IMonitoringExpression.PreparedRawValue Property

**Summary:** Get the target specific binary represantation of the
            	raw value.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] PreparedRawValue { get; }
```

---

## IMonitoringExpression.PreparedValue Property

**Summary:** Get the prepared value of this variable. This value
            	must be used on a request to write or force this variable.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object PreparedValue { get; set; }
```

---

## IMonitoringExpression.RawValue Property

**Summary:** Get / set the current value of the variable in the
            	target specific binary represantation.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] RawValue { get; set; }
```

---

## IMonitoringExpression.State Property

**Summary:** Get or set the state of this variable.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
VarRefState State { get; set; }
```

---

## IMonitoringExpression.Timestamp Property

**Summary:** Get the timestamp when this monitoring 
            	variable has been update the last time.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DateTime Timestamp { get; }
```

---

## IMonitoringExpression.VarRef Property

**Summary:** Get the var ref of this variable.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IVarRef VarRef { get; }
```

---

## IOnlineApplication12.FlowControlEnabled Property

**Summary:** Gets or sets a value whether flow control is enabled for this application. Whenever
            this value is changed, both anFlowControlEnabledChangedas well as an[!:IOnlineManager7.FlowControlEnabledChanged]event is triggered.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool FlowControlEnabled { get; set; }
```

---

## IOnlineApplicationInfo.Author Property

**Summary:** The author who programmed the applicaiton

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Author { get; }
```

---

## IOnlineApplicationInfo.Description Property

**Summary:** A description of the application

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Description { get; }
```

---

## IOnlineApplicationInfo.LastModification Property

**Summary:** The time of the last modification

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DateTime LastModification { get; }
```

---

## IOnlineApplicationInfo.Profile Property

**Summary:** The profile of the programming system

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Profile { get; }
```

---

## IOnlineApplicationInfo.ProjectName Property

**Summary:** The project name

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string ProjectName { get; }
```

---

## IOnlineApplicationInfo.Version Property

**Summary:** The version of the application

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Version { get; }
```

---

## IOnlineApplication.ApplicationGuid Property

**Summary:** The guid of the IApplicationObject in the project.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid ApplicationGuid { get; }
```

---

## IOnlineApplication.ApplicationSessionId Property

**Summary:** The session id obtained by the login to the application. This is NOT the same
            	as the session id of the device, which is obtained by authentication to the device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ApplicationSessionId { get; }
```

---

## IOnlineApplication.ApplicationState Property

**Summary:** Gets the current application state of this application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ApplicationState ApplicationState { get; }
```

---

## IOnlineApplication.CallStack Property

**Summary:** returns callstack of last reached breakpoint
            the callstack is updated every time a breakpoint is reached.
            It is not destroyed when status is running.
            The deepest stack element is first in array.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ICallStackEntry[] CallStack { get; }
```

---

## IOnlineApplication.CodeId Property

**Summary:** After successfull login the codeid is the code id stored on the target

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid CodeId { get; }
```

---

## IOnlineApplication.CurrentHitCount Property

**Summary:** If the application is halted on a breakpoint, this property returns the current hit
            count of this property. If the application is not halted on a breakpoint,-1is
            returned.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int CurrentHitCount { get; }
```

---

## IOnlineApplication.CurrentInstancePath Property

**Summary:** the instance path of the last reached breakpoint.
            If the last breakpoint was not within a method or a function block
            the instance path is null.
            the instance path is updated every time a breakpoint is reached.
            It is not destroyed when status is running.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string CurrentInstancePath { get; }
```

---

## IOnlineApplication.CurrentInstanceVarRef Property

**Summary:** the VarReference of the instance of the last reached breakpoint.
            If the last breakpoint was not within a method or a function block
            the instance path is empty.
            the instance path is updated every time a breakpoint is reached.
            It is not destroyed when status is running.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IVarRef CurrentInstanceVarRef { get; }
```

---

## IOnlineApplication.CurrentPosition Property

**Summary:** If the application is halted on a breakpoint, this property returns the current
            position. If the application is not halted on a breakpoint,nullis returned.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDataLocation CurrentPosition { get; }
```

---

## IOnlineApplication.DataId Property

**Summary:** After successfull login the dataid is the data id stored on the target

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Guid DataId { get; }
```

---

## IOnlineApplication.IsLoggedIn Property

**Summary:** Get the login state of this application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsLoggedIn { get; }
```

---

## IOnlineApplication.OnlineDevice Property

**Summary:** Get the device object that handles the current connection for this application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IOnlineDevice OnlineDevice { get; }
```

---

## IOnlineApplication.OperatingState Property

**Summary:** Gets the current operating state of this application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
OperatingState OperatingState { get; }
```

---

## IOnlineApplication.PreparedVarRefs Property

**Summary:** Get a list of all OnlineVarRefs for which the prepared 
            value is set. This will never returnCopy1null. Instead,
            an empty array will be returned if no prepared OnlineVarRefs exist.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
1null
```

---

## IOnlineDevice.IsConnected Property

**Summary:** Get the connection state of this device object.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsConnected { get; }
```

---

## IOnlineDevice.SessionId Property

**Summary:** Get the session id of the current connection.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int SessionId { get; }
```

---

## IOnlineVarRef2.Tag Property

**Summary:** Gets or sets an object that contains data to associate with the item.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object Tag { get; set; }
```

---

## IOnlineVarRef.Expression Property

**Summary:** The expression that makes up the OnlineVarRef.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IExpression Expression { get; }
```

---

## IOnlineVarRef.Forced Property

**Summary:** Get whether the value is forced.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool Forced { get; }
```

---

## IOnlineVarRef.PreparedRawValue Property

**Summary:** Get the binary representation of the prepared value.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] PreparedRawValue { get; }
```

---

## IOnlineVarRef.PreparedValue Property

**Summary:** Set the value to be used for the next write/force operation. If a force is to be
            released, this property must be set to eitherUnforceorUnforceAndRestore.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object PreparedValue { get; set; }
```

---

## IOnlineVarRef.RawValue Property

**Summary:** Returns the binary representation of the value, as it is stored
            on the PLC. May be used for extended debugging.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
byte[] RawValue { get; }
```

---

## IOnlineVarRef.State Property

**Summary:** The current state of this OnlineVarRef

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
VarRefState State { get; }
```

---

## IOnlineVarRef.Timestamp Property

**Summary:** When the value was updated last.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
DateTime Timestamp { get; }
```

---

## IOnlineVarRef.Value Property

**Summary:** Returns the current value of the expression as a .NET datatype
            (e.g. an Int32 if the IEC-type is DINT or String if the type is a STRING).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Object Value { get; }
```

---

## IProvideCredentialsArgs2.PermittedSourceKinds Property

**Summary:** Gets the permitted source kinds. (This is a hint to theProvideCredentialsHandler.)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
CredentialSourceKind PermittedSourceKinds { get; }
```

---

## IProvideCredentialsArgs.Credentials Property

**Summary:** Set or get the credentials for the connection.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Credentials Credentials { get; set; }
```

---

## IProvideCredentialsArgs.SupportedCredentialTypes Property

**Summary:** Returns a combination ofCredentialsTypeflags, which 
            	determine the authentication methods supported by the authentication target.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
CredentialsType SupportedCredentialTypes { get; }
```

---

## IServiceHeader.Command Property

**Summary:** Get the command within CommandGroup. In the range 0 - 0xFFFF

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Command { get; }
```

---

## IServiceHeader.CommandGroup Property

**Summary:** Get the command group. Always in the range 0 - 0xFFFFFFFF

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long CommandGroup { get; }
```

---

## IServiceHeader.ContentLength Property

**Summary:** The length of the services content.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ContentLength { get; }
```

---

## IServiceHeader.DeviceSessionId Property

**Summary:** The session id of the current login session on the device.
            0 if unknown / not logged in.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int DeviceSessionId { get; }
```

---

## IServiceHeader.HeaderTag Property

**Summary:** The header tag describes the protocol used for the service. 
            If the service does not use the CodeSys protocol the content
            cannot be read by means of the service tags.
            The CoDeSys protocol uses the headertags 0xCD55 (intel-byteorder)
            and 0x55CD (motorola byteorder)
            The header tag must be in the range 0x0000 - 0xFFFF

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int HeaderTag { get; }
```

---

## IServiceHeader.Length Property

**Summary:** Get the length of the header without header tag and length field.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int Length { get; }
```

---

## IServiceReader.ByteOrder Property

**Summary:** Get/set the byte order of the target. 
            Usually the byte order is determined automatically by inspecting the headertag field. 
            If that fails (because a non CoDeSys protocol is used) ByteOrder.Unknown is returned. 
            The byteorder should then be set manually.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
TargetByteOrder ByteOrder { get; set; }
```

---

## IServiceReader.Header Property

**Summary:** Get the service header which describes the service group, command etc.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceHeader Header { get; }
```

---

## IServiceTagEnumerator.Current Property

**Summary:** Return the current element. Initially the enumerator is positioned 
            before the first element. ThereforeMoveNextmust be 
            called beforeCurrentis accessed for the first time.
            The same TagReader will be returned until the next call toMoveNext.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IServiceTagReader Current { get; }
```

---

## IServiceTagReader.ContentSize Property

**Summary:** Get the size of the content.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int ContentSize { get; }
```

---

## IServiceTagReader.EndOfContent Property

**Summary:** Returns true if the content reader is at the end of the tag.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool EndOfContent { get; }
```

---

## IServiceTagReader.IsDataTag Property

**Summary:** Returns whether the current tag is a data tag (true) or
            a complex tag (false).
            Content cannot be accessed in complex tag, instead they contain
            subtags. A data tag on the other hand contains (uninterpreted) content
            but no subtags.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool IsDataTag { get; }
```

---

## IServiceTagReader.TagId Property

**Summary:** Read the id of the current tag.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int TagId { get; }
```

---

## IServiceTagReader.UnreadContentSize Property

**Summary:** The number of content bytes which have not been
            read by now.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int UnreadContentSize { get; }
```

---

## IServiceWriter.MaxContentSize Property

**Summary:** The maximum size of this services content.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
int MaxContentSize { get; }
```

---

## ITargetDescription.Address Property

**Summary:** Gets the router address for this device. An hierarchical addressing
            scheme is used. Example: "123.5". Each component of the router
            address corresponds to an array element of the return value.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceAddress Address { get; }
```

---

## ITargetDescription.Ident Property

**Summary:** Gets the ID of the type to be matched with the installed device
            types (target descriptions).

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
ITargetIdent Ident { get; }
```

---

## ITargetDescription.LockToCache Property

**Summary:** If set to true, the devicedescription will stay in the gateways device cache,
            even during rebuild. So this is not a property of the device itself but a property
            of the device description object and may be changed by the application.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool LockToCache { get; set; }
```

---

## ITargetDescription.Name Property

**Summary:** Gets the name of the device. Example: "PLCFeeder". If no name
            has been explicitly assigned to the device, it is derived from the
            corresponding router address, e.g. "@127.5".

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string Name { get; }
```

---

## ITargetDescription.ParentAddress Property

**Summary:** Get the router address of the parent node of this device. Usually this will be the
            device address without the last address component. Is null if the parentAddress is
            unknown.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
IDeviceAddress ParentAddress { get; }
```

---

## ITargetDescription.Properties Property

**Summary:** Gets extended properties of this device.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
Hashtable Properties { get; }
```

---

## ITargetDescription.TypeName Property

**Summary:** Gets a string indicating the device type. Example: "Beckhoff
            CX1000-100" or "BRC Motion Logic Controller".

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
string TypeName { get; }
```

---

## ITargetIdent.Id Property

**Summary:** The device id.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long Id { get; }
```

---

## ITargetIdent.Type Property

**Summary:** The device class

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long Type { get; }
```

---

## ITargetIdent.Version Property

**Summary:** The device version.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
long Version { get; }
```

---

## ITemporaryLoginCredentialsContext2.AllowResetContextQueried Property

**Summary:** Normally such a login context may only be queries once. 
            In special circumstances it may be allowed to query a certain context more often. In that case this has to return true.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool AllowResetContextQueried { get; }
```

---

## ITemporaryLoginCredentialsContext2.PaswordRenewalPerformed Property

**Summary:** Flag to indicate that a new password had to be set during connect

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
bool PaswordRenewalPerformed { get; }
```

---

## ITemporaryLoginCredentialsContext.PermittedSourceKindsForFallback Property

**Summary:** Gets the permitted source kinds. IfQueryForCredentials(Object, IProvideCredentialsArgs)returns false, and
            at least one of the bits here is set, the code will fall back to the defaultProvideCredentialsHandlerset via[!:IOnlineManager4.SetProvideCredentialsHandler], passing him anIProvideCredentialsArgs2instance whosePermittedSourceKindsmember resembles the
            CredentialSourceKind flags set here. (However, for older or OEMProvideCredentialsHandlerimplementations, it is not guaranteed that those
            flags are honored.)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
CredentialSourceKind PermittedSourceKindsForFallback { get; }
```

---

## OnlineCancelDownloadEventArgs.KindOf Property

**Summary:** Get what kind of download is performed.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public KindOfDownloadCommand KindOf { get; }
```

---

## OnlineCancelEventArgs.Exception Property

**Summary:** Get the exception object set byCancel(Exception). If this
            	property is null, the event will not be canceled.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Exception Exception { get; }
```

---

## OnlineCancelEventArgs.ObjectGuid Property

**Summary:** Get the Guid of the object that the event refers to.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid ObjectGuid { get; }
```

---

## OnlineDownloadEventArgs.KindOf Property

**Summary:** Get what kind of download is performed.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public KindOfDownloadCommand KindOf { get; }
```

---

## OnlineEventArgs.GuidObject Property

**Summary:** Get the Guid of the object that the event refers to.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid GuidObject { get; }
```

---

## OnlineResetEventArgs.ObjectGuid Property

**Summary:** Guid of the object that the event refers to

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public Guid ObjectGuid { get; }
```

---

## OnlineResetEventArgs.Option Property

**Summary:** The type of reset (E.g. warm, cold, origin)

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public ResetOption Option { get; }
```

---

## TagTypeException.TagId Property

**Summary:** Get the tag ID

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public int TagId { get; }
```

---

## UserPasswordCredentials.Password Property

**Summary:** The password for the user.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string Password { get; set; }
```

---

## UserPasswordCredentials.Username Property

**Summary:** The login name

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public string Username { get; set; }
```

---

## IDeviceId.id Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string id { get; }
```

---

## IDeviceId.type Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
int type { get; }
```

---

## ILibCategory.name Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string name { get; }
```

---

## IManagedLib.company Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string company { get; }
```

---

## IScriptApplicationMarker.is_application Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool is_application { get; }
```

---

## IScriptCommandPermission.command_guid Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Guid command_guid { get; }
```

---

## IScriptCommunicationSettings.scanned_target_vendor Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string scanned_target_vendor { get; }
```

---

## IScriptConnector.interface_name Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string interface_name { get; }
```

---

## IScriptDataElement2.io_mapping Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptIoMapping io_mapping { get; }
```

---

## IScriptDataElement.can_access_online Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool can_access_online { get; }
```

---

## IScriptDeviceCollection.vendors Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> vendors { get; }
```

---

## IScriptDeviceGroupList.__len__ Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
[ObsoleteAttribute("The signature for this member is wrong, it should have been a method instead of a property. The implementationactually contains a correct method which will be found by the python binder.")]
int __len__ { get; }
```

---

## IScriptDeviceInfo.families Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> families { get; }
```

---

## IScriptDeviceInfo.name Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string name { get; }
```

---

## IScriptDeviceObject5.driver_info Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDriverInfo driver_info { get; }
```

---

## IScriptDeviceParameter2.disable_mapping Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool disable_mapping { get; }
```

---

## IScriptDeviceParameter.online_access_rights Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
AccessRight online_access_rights { get; }
```

---

## IScriptDeviceUserManagement.groups Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptDeviceGroupList groups { get; }
```

---

## IScriptDriverInfo.update_ios_while_in_stop Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool update_ios_while_in_stop { get; set; }
```

---

## IScriptEnumerationValue.description Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string description { get; }
```

---

## IScriptExternalFileObject.length Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
long length { get; }
```

---

## IScriptGatewayParameterDescriptions.Item Property (Int64)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptGatewayParameterDescription this[
	long id
] { get; }
```

---

## IScriptGroupList.Item Property (Guid)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptGroup this[
	Guid id
] { get; }
```

---

## IScriptImplementationLanguages.st Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Guid st { get; }
```

---

## IScriptLibraryReference.optional Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool optional { get; set; }
```

---

## IScriptLibraryReferences.Item Property (Int64)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptLibraryReference this[
	long id
] { get; }
```

---

## IScriptLiveDeviceUser.flags Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
DeviceUserManagementFlags flags { get; }
```

---

## IScriptObjectPermission.access_kind Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
ObjectPermissionKind access_kind { get; }
```

---

## IScriptObject.embedded_object_types Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Guid> embedded_object_types { get; }
```

---

## IScriptPermission.type Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Guid type { get; }
```

---

## IScriptProjectArchiveCategories.default Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<IScriptProjectArchiveCategory> default { get; }
```

---

## IScriptProjectInfoMarker.is_project_info Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool is_project_info { get; }
```

---

## IScriptRepositorySourceList.Item Property (Int32)

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptRepositorySource this[
	int index
] { get; }
```

---

## IScriptTaskObject.watchdog Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IScriptWatchdog watchdog { get; }
```

---

## IScriptTreeObject.project Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IExtendedObject<IScriptProject> project { get; }
```

---

## IScriptUserOrGroup.id Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
Guid id { get; }
```

---

## IScriptVendorInfo.mail_addresses Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
IList<Object> mail_addresses { get; }
```

---

## IScriptWatchdog.time Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
string time { get; set; }
```

---

## ISystem4.aborting Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool aborting { get; }
```

---

## ISystem.trace Property

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
bool trace { get; set; }
```

---

## IOnlineApplication10 Properties

**Summary:** The guid of the IApplicationObject in the project.

### Syntax
```csharp
1null
```

---

## IOnlineApplication11 Properties

**Summary:** The guid of the IApplicationObject in the project.

### Syntax
```csharp
1null
```

---

## IOnlineApplication12 Properties

**Summary:** The guid of the IApplicationObject in the project.

### Syntax
```csharp
1null
```

---

## IOnlineApplication8 Properties

**Summary:** The guid of the IApplicationObject in the project.

### Syntax
```csharp
1null
```

---

## IOnlineApplication9 Properties

**Summary:** The guid of the IApplicationObject in the project.

### Syntax
```csharp
1null
```

---

## OnlineEventArgs Properties

**Summary:** Get the Guid of the object that the event refers to.

---

## IScriptDeviceDescription2 Properties

**Summary:** No summary available.

---

## IScriptDeviceObject Properties

**Summary:** No summary available.

---

## IScriptDeviceUser Properties

**Summary:** No summary available.

---

## IScriptExplicitConnectorObjectMarker Properties

**Summary:** No summary available.

---

## IScriptGateway Properties

**Summary:** No summary available.

---

## IScriptLiveDeviceUser Properties

**Summary:** No summary available.

---

## IScriptOnlineDevice7 Properties

**Summary:** No summary available.

---

## IScriptProject12 Properties

**Summary:** No summary available.

---

## IScriptProjectInfoMarker Properties

**Summary:** No summary available.

---

## IScriptTaskObject Properties

**Summary:** No summary available.

---

## IScriptTreeObject Properties

**Summary:** No summary available.

---

## ISystem4 Properties

**Summary:** No summary available.

---

## IProject2 Interface

**Summary:** Extension interface forIProject.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IProject2 : IProject
```

---

## IArchiveReader2 Interface

**Summary:** Extension interface forIArchiveReader. These implementations will be able to
            read objects that were stored using a shared data storage (seeISharedDataStorage.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IArchiveReader2 : IArchiveReader
```

---

## IMetaObject4 Interface

**Summary:** Extension interface forIMetaObject3.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IMetaObject4 : IMetaObject3, 
	IMetaObject2, IMetaObject, IArchivable, ICloneable, IComparable
```

---

## IOrderedSubObjects Interface

**Summary:** IObjectimplementations whose subobjects have got a particular order must
            additionally implement this interface. Please note that the order of the subobjects must be
            persisted by the particular implementation!

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IOrderedSubObjects
```

---

## SVNodeRenamedEventArgs Class

**Summary:** Event arguments for theSVNodeRenamedEventHandler.

**Assembly:** `Objects (in Objects.dll) Version: 3.5.17.0`

### Syntax
```csharp
public class SVNodeRenamedEventArgs : EventArgs
```

---

## AfterApplicationResetEventHandler Delegate

**Summary:** Called after an application has been reset

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public delegate void AfterApplicationResetEventHandler(
	Object sender,
	OnlineResetEventArgs e
)
```

---

## IDeviceUser2 Interface

**Summary:** Extension interface toIDeviceUser

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IDeviceUser2 : IDeviceUser
```

---

## IGatewayParams Interface

**Summary:** An opaque object describing the properties of a connection to a gateway.
            An implementation of this interface is specific to one gateway driver.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IGatewayParams : IArchivable, 
	ICloneable, IComparable
```

---

## IOnlineApplication10 Interface

**Summary:** Extension interface for IOnlineApplication

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IOnlineApplication10 : IOnlineApplication9, 
	IOnlineApplication8, IOnlineApplication7, IOnlineApplication6, IOnlineApplication5, IOnlineApplication4, 
	IOnlineApplication3, IOnlineApplication2, IOnlineApplication
```

---

## IOnlineApplication6 Interface

**Summary:** Extension interface forIOnlineApplication5

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IOnlineApplication6 : IOnlineApplication5, 
	IOnlineApplication4, IOnlineApplication3, IOnlineApplication2, IOnlineApplication
```

---

## IOnlineApplicationInfo Interface

**Summary:** An interface for accessing a description of an online application

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IOnlineApplicationInfo
```

---

## IServiceHeader Interface

**Summary:** This interface describes the protocol header of service data.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public interface IServiceHeader
```

---

## OnWritingVariablesEventHandler Delegate

**Summary:** Called when variables have been written to new values.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public delegate void OnWritingVariablesEventHandler(
	Object sender,
	OnlineEventArgs e
)
```

---

## OperatingState Enumeration

**Summary:** The global state of an application. Although not defined as such,
            	this enumeration is treated like a flags field, so the effective 
            	value may be a combination of more of these values.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
public enum OperatingState
```

---

## TargetProperties Enumeration

**Summary:** Flags determining certain properties of a target.

**Assembly:** `Online (in Online.dll) Version: 3.5.17.0`

### Syntax
```csharp
[FlagsAttribute]
public enum TargetProperties
```

---

## AccessRight Enumeration

**Summary:** Defines access rights on a parameter

**Assembly:** `DeviceObject (in DeviceObject.dll) Version: 3.5.17.0`

### Syntax
```csharp
[FlagsAttribute]
public enum AccessRight
```

---

## Formatting Enumeration

**Summary:** No summary available.

**Assembly:** `DocExport (in DocExport.dll) Version: 3.5.17.0`

### Syntax
```csharp
public enum Formatting
```

---

## ReferenceMode Enumeration

**Summary:** No summary available.

**Assembly:** `ExternalFileObject (in ExternalFileObject.dll) Version: 3.5.17.0`

### Syntax
```csharp
public enum ReferenceMode
```

---

## IScriptApplicationMarker Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptApplicationMarker
```

---

## IScriptCommunicationSettings2 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptCommunicationSettings2 : IScriptCommunicationSettings
```

---

## IScriptComparedObject Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptComparedObject
```

---

## IScriptConnector Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptConnector
```

---

## IScriptDeviceObject5 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptDeviceObject5 : IScriptDeviceObject4, 
	IScriptDeviceObject3, IScriptDeviceObject2, IScriptDeviceObject, IScriptDeviceObjectMarker
```

---

## IScriptDeviceUserList Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptDeviceUserList : IEnumerable<IScriptDeviceUser>, 
	IEnumerable
```

---

## IScriptLibManObject2 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptLibManObject2 : IScriptLibManObject, 
	IScriptLibManObjectMarker
```

---

## IScriptLiveDeviceUser Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptLiveDeviceUser
```

---

## IScriptObject5 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptObject5 : IScriptObject4, 
	IScriptObject3, IScriptObject2, IScriptObject, IScriptTreeObject, IEquatable<IScriptObject>, 
	IEquatable<IExtendedObject<IScriptObject>>
```

---

## IScriptOnlineDevice7 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptOnlineDevice7 : IScriptOnlineDevice6, 
	IScriptOnlineDevice5, IScriptOnlineDevice4, IScriptOnlineDevice3, IScriptOnlineDevice2, IScriptOnlineDevice, 
	IDisposable
```

---

## IScriptProject10 Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptProject10 : IScriptProject9, 
	IScriptProject8, IScriptProject7, IScriptProject6, IScriptProject5, IScriptProject4, 
	IScriptProject3, IScriptProject2, IScriptProject, IScriptTreeObject, IEquatable<IScriptProject>, 
	IEquatable<IExtendedObject<IScriptProject>>
```

---

## IScriptRangeDataElement Interface

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public interface IScriptRangeDataElement : IScriptValueDataElement, 
	IScriptDataElement
```

---

## PromptChoiceFilter Delegate

**Summary:** No summary available.

**Assembly:** `ScriptEngine3 (in ScriptEngine3.dll) Version: 4.0.0.0`

### Syntax
```csharp
public delegate bool PromptChoiceFilter(
	string choice
)
```

---

## PermissionState Enumeration

**Summary:** The permission state, either "granted", "denied", or "default".

**Assembly:** `UserManagement (in UserManagement.dll) Version: 3.5.17.0`

### Syntax
```csharp
public enum PermissionState
```

---

