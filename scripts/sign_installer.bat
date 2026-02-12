@echo off
REM Sign the CPack-generated installer
REM This script is called by CPack after the installer is created

set INSTALLER_PATH=%~1
set SIGN_TOOL=C:\Users\lb\Dropbox\Crypted\sign\sign.bat

if not exist "%INSTALLER_PATH%" (
    echo ERROR: Installer not found: %INSTALLER_PATH%
    exit /b 1
)

if not exist "%SIGN_TOOL%" (
    echo ERROR: Sign tool not found: %SIGN_TOOL%
    exit /b 1
)

echo.
echo ========================================
echo Signing installer: %INSTALLER_PATH%
echo ========================================
echo.

call "%SIGN_TOOL%" "%INSTALLER_PATH%"

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to sign installer
    exit /b 1
)

echo.
echo ========================================
echo Installer signed successfully!
echo ========================================
echo.

exit /b 0
