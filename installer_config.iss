; THIS PART MADE BY GOOGLE AI AS IDK HOW TO DO IT

; ==============================================================================
; INNO SETUP CONFIGURATION BLUEPRINT
; Engine created by Jordan Russell and Martijn Laan
; ==============================================================================

[Setup]
AppName=Asaiyf Launcher
AppVersion=1.0.0
DefaultDirName={autopf}\Asaiyf Launcher
DefaultGroupName=Asaiyf Launcher
OutputDir=Output
OutputBaseFilename=setup_wizard
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Files]
; Tells the compiler to grab the EXE that Job 1 just manufactured in the cloud
Source: "Asaiyf Launcher\dist\asaiyf_launcher.exe"; DestDir: "{app}"; Flags: ignoreversion
; Tells the compiler to package your other asset folder right next to it
Source: "Asaiyf Launcher\Asaiyf Shortcuts\*"; DestDir: "{app}\YourFolderName"; Flags: ignoreversion recursesubdirs createallsubdirs

[Tasks]
; This adds the exact physical checkbox asking the user for a desktop shortcut
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Icons]
; This instructs Windows to build the shortcut linking straight to the Program Files directory
Name: "{autodesktop}\Asaiyf Launcher"; Filename: "{app}\asaiyf_launcher.exe"; Tasks: desktopicon

[Run]
; Allows the user to check a box to instantly run the app after installation closes
Filename: "{app}\asaiyf_launcher.exe"; Description: "{cm:LaunchProgram,Asaiyf Launcher}"; Flags: nowait postinstall skipifsilent
