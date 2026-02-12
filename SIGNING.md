# Code Signing für AdartysSlicer

## Übersicht

AdartysSlicer unterstützt automatisches Code-Signing für:
1. **adartys-slicer.exe** - Das Hauptprogramm
2. **AdartysSlicer_Windows_Installer_*.exe** - Der NSIS-Installer

## Voraussetzungen

- Windows SDK mit `signtool.exe` installiert
- Code-Signing-Zertifikat (installiert oder als Token)
- Signierung-Skript unter: `C:\Users\lb\Dropbox\Crypted\sign\sign.bat`

## Automatisches Signieren

### Executable-Signierung (beim Build)

Das Executable wird **automatisch** nach jedem erfolgreichen Build signiert:

```batch
# Normaler Release-Build (Executable wird automatisch signiert)
build_release_vs2022.bat

# Debug-Build (Executable wird automatisch signiert)
build_release_vs2022.bat debug
```

Die Signierung ist in `src/CMakeLists.txt` konfiguriert und wird als POST_BUILD-Schritt ausgeführt.

### Installer-Signierung (Build + Package)

Um einen **signierten Installer** zu erstellen, verwenden Sie:

```batch
# Build und erstelle signierten Installer
build_and_package.bat

# Mit Debug-Symbolen
build_and_package.bat debuginfo

# Debug-Build mit Installer
build_and_package.bat debug
```

Dieses Skript führt aus:
1. Vollständiger Build (ruft `build_release_vs2022.bat` auf)
2. Executable wird signiert (automatisch im Build-Prozess)
3. Erstellt Installer mit CPack
4. Signiert den Installer mit `scripts/sign_installer.bat`

Der signierte Installer wird erstellt in:
- `build/AdartysSlicer_Windows_Installer_V*.exe` (Release)
- `build-dbg/AdartysSlicer_Windows_Installer_V*.exe` (Debug)
- `build-dbginfo/AdartysSlicer_Windows_Installer_V*.exe` (RelWithDebInfo)

## Manuelles Signieren

### Nur Installer erstellen (ohne Build)

Wenn Sie bereits gebaut haben und nur den Installer signieren möchten:

```batch
cd build
cpack -G NSIS -C Release
call ..\scripts\sign_installer.bat "AdartysSlicer_Windows_Installer_V*.exe"
```

### Einzelne Datei signieren

```batch
C:\Users\lb\Dropbox\Crypted\sign\sign.bat "path\to\file.exe"
```

## Konfiguration anpassen

### Signierung-Tool-Pfad ändern

In `CMakeLists.txt` oder `src/CMakeLists.txt`:

```cmake
set(SIGN_TOOL_PATH "C:/Ihr/Pfad/zum/sign.bat" CACHE FILEPATH "Path to code signing script")
```

Oder beim CMake-Aufruf:

```batch
cmake .. -DSIGN_TOOL_PATH="C:/custom/path/sign.bat"
```

### Signierung deaktivieren

Verschieben oder entfernen Sie `C:\Users\lb\Dropbox\Crypted\sign\sign.bat`.
CMake wird eine Warnung ausgeben, aber der Build funktioniert weiterhin ohne Signierung.

## Troubleshooting

### "Code signing tool not found"

Das Signierung-Skript wurde nicht gefunden. Prüfen Sie:
- Existiert `C:\Users\lb\Dropbox\Crypted\sign\sign.bat`?
- Ist der Pfad in CMakeLists.txt korrekt?

### "Failed to sign"

Das Signierung-Skript wurde ausgeführt, aber ist fehlgeschlagen:
- Führen Sie das sign.bat-Skript manuell aus, um die Fehlermeldung zu sehen
- Prüfen Sie, ob das Zertifikat noch gültig ist
- Prüfen Sie, ob der Timestamp-Server erreichbar ist

### Installer wird nicht signiert

- Verwenden Sie `build_and_package.bat` statt nur `build_release_vs2022.bat`
- Oder führen Sie nach dem Build manuell CPack und Signierung aus

## Signierung-Details

Das verwendete Signierung-Skript (`sign.bat`) verwendet:
- **Zertifikat**: "Hot-World GmbH & Co. KG" (installiertes Zertifikat)
- **Hash-Algorithmen**: SHA1 + SHA256 (dual signature)
- **Timestamp-Server**: http://timestamp.comodoca.com

Dual Signierung gewährleistet Kompatibilität mit:
- SHA1: Ältere Windows-Versionen (Windows 7, 8)
- SHA256: Moderne Windows-Versionen (Windows 10, 11)
