# This is just a notebook for changes done to make this special version

# Downloads

https://smolsys-download.com/downloads/adartys-slicer/mac/AdartysSlicer.dmg
https://smolsys-download.com/downloads/adartys-slicer/windows/AdartysSlicer_Windows_Installer_V2.3.2.exe

# Compile

## Update nach abgleich

Adjust translations:
python3 tools/AdartysLocale.py

Adjust svg colors
python3 tools/AdjustSVGColors.py
## MacOS

### Wenn sdk has changed

rm -rf /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/deps/build/arm64 /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/build/arm64
./build_release_macos.sh -s
open /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/build/arm64/AdartysSlicer/AdartysSlicer.app

Notarize app on MacOS:
./notarize_adartys.sh

# Changed files
