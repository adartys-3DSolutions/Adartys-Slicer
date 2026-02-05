# This is just a notebook for changes done to make this special version

# Compile

## Update nach abgleich

Adjust translations:
python3 tools/AdartysLocale.py

Adjust svg colors
python3 tools/AdjustSVGColors.py
## MacOS

# Wenn sdk sich geändert hat
rm -rf /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/deps/build/arm64 /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/build/arm64
./build_release_macos.sh -s
open /Users/littwin/Documents/Projekte/Customers/Smolsys/Adartys-Slicer/build/arm64/AdartysSlicer/AdartysSlicer.app

# Changed files
