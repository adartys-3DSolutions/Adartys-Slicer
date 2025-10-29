# This is just a notebook for changes done to make this special version

# Compile

## Update nach abgleich

Adjust translations:
python3 tools/AdartysLocale.py

Adjust svg colors
python3 tools/AdjustSVGColors.py
## MacOS

CMAKE_IGNORE_PATH="/usr/X11R6:/opt/X11" ./build_release_macos.sh -s

# Changed files
