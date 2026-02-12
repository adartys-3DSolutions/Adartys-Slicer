@echo off
REM Build AdartysSlicer and create signed installer
REM Usage: build_and_package.bat [debug|debuginfo]

setlocal

set BUILD_TYPE=%1
if "%BUILD_TYPE%"=="" set BUILD_TYPE=release

echo.
echo ========================================
echo Building AdartysSlicer...
echo ========================================
echo.

REM Build the application
if "%BUILD_TYPE%"=="debug" (
    call build_release_vs2022.bat debug
    set BUILD_DIR=build-dbg
    set CONFIG=Debug
) else if "%BUILD_TYPE%"=="debuginfo" (
    call build_release_vs2022.bat debuginfo
    set BUILD_DIR=build-dbginfo
    set CONFIG=RelWithDebInfo
) else (
    call build_release_vs2022.bat
    set BUILD_DIR=build
    set CONFIG=Release
)

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Build failed!
    exit /b 1
)

echo.
echo ========================================
echo Creating installer package...
echo ========================================
echo.

cd %BUILD_DIR%

REM Create the installer with CPack
cpack -G NSIS -C %CONFIG%

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: CPack failed!
    cd ..
    exit /b 1
)

echo.
echo ========================================
echo Signing installer...
echo ========================================
echo.

REM Find the generated installer
for %%F in (AdartysSlicer_Windows_Installer_*.exe) do (
    set INSTALLER=%%F
)

if not defined INSTALLER (
    echo ERROR: Installer not found!
    cd ..
    exit /b 1
)

echo Found installer: %INSTALLER%

REM Sign the installer
call ..\scripts\sign_installer.bat "%CD%\%INSTALLER%"

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Signing failed!
    cd ..
    exit /b 1
)

cd ..

echo.
echo ========================================
echo SUCCESS!
echo ========================================
echo.
echo Signed installer created: %BUILD_DIR%\%INSTALLER%
echo.

exit /b 0
