@echo off
REM ============================================================================
REM WAGO CODESYS Project Generator - Config-Based Launcher
REM ============================================================================
REM Version: 3.1
REM Author: WAGO Automation
REM Description: Loads configuration from INI file and executes CODESYS script
REM ============================================================================

setlocal EnableDelayedExpansion

REM Enable ANSI escape sequences (Windows 10+)
reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1

REM Set UTF-8 Code Page
chcp 65001 >nul 2>&1

REM ============================================================================
REM CONFIGURATION FILE PATH
REM ============================================================================

set "CONFIG_FILE=%~dp0WAGO_ProjectGenerator_Config.ini"

REM ============================================================================
REM ASCII ART
REM ============================================================================

cls
echo.
echo    ================================================
echo    ==                                            ==
echo    ==    ##      ##    ###     ####    ####     ==
echo    ==    ##  ##  ##   ## ##   ##      ##  ##    ==
echo    ==    ##  ##  ##  ##   ##  ## ###  ##  ##    ==
echo    ==    ##  ##  ##  #######  ##  ##  ##  ##    ==
echo    ==     ###  ###   ##   ##   ####    ####     ==
echo    ==                                            ==
echo    ================================================
echo.
echo              Project Generator v3.1
echo    ================================================
echo.

REM ============================================================================
REM TIMESTAMP
REM ============================================================================

for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set "TIMESTAMP=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%"

echo    [INFO] Start: %TIMESTAMP%
echo.

REM ============================================================================
REM LOAD CONFIGURATION FROM INI FILE
REM ============================================================================

echo    [CONFIG] Loading configuration from INI file...
echo    ================================================
echo.

if not exist "%CONFIG_FILE%" (
    echo    [ERROR] Configuration file not found:
    echo           %CONFIG_FILE%
    echo.
    echo    [HINT] Create WAGO_ProjectGenerator_Config.ini in same directory
    echo.
    goto :ERROR_EXIT
)

echo    [OK] Config file found: %CONFIG_FILE%
echo.

REM Parse INI file - CODESYS Section
for /f "usebackq tokens=1,2 delims==" %%a in ("%CONFIG_FILE%") do (
    set "line=%%a"
    set "value=%%b"
    
    REM Remove leading/trailing spaces
    for /f "tokens=* delims= " %%x in ("!line!") do set "line=%%x"
    for /f "tokens=* delims= " %%x in ("!value!") do set "value=%%x"
    
    REM Check for keys
    if "!line!"=="InstallPath" set "CODESYS_PATH=!value!"
    if "!line!"=="ExecutableName" set "CODESYS_EXE=!value!"
    if "!line!"=="Profile" set "CODESYS_PROFILE=!value!"
    if "!line!"=="ScriptDirectory" set "SCRIPT_DIR=!value!"
    if "!line!"=="LogDirectory" set "LOG_DIR=!value!"
    if "!line!"=="DefaultScript" set "DEFAULT_SCRIPT=!value!"
    if "!line!"=="MaxLogLines" set "MAX_LOG_LINES=!value!"
)

REM Build full script path
set "PYTHON_SCRIPT=%SCRIPT_DIR%\%DEFAULT_SCRIPT%"

REM Set default values if not found in config
if not defined CODESYS_PATH set "CODESYS_PATH=C:\Program Files\CODESYS 3.5.21.10\CODESYS\Common"
if not defined CODESYS_EXE set "CODESYS_EXE=Codesys.exe"
if not defined CODESYS_PROFILE set "CODESYS_PROFILE=CODESYS V3.5 SP21 Patch 1"
if not defined LOG_DIR set "LOG_DIR=D:\WAGO\CODESYS\logs"
if not defined MAX_LOG_LINES set "MAX_LOG_LINES=15"

echo    [CONFIG] Configuration loaded:
echo             CODESYS Path: %CODESYS_PATH%
echo             Profile:      %CODESYS_PROFILE%
echo             Script:       %DEFAULT_SCRIPT%
echo             Log Dir:      %LOG_DIR%
echo.

REM Check for command line argument override
if not "%~1"=="" (
    set "PYTHON_SCRIPT=%~1"
    echo    [OVERRIDE] Using command line script: %PYTHON_SCRIPT%
    echo.
)

REM ============================================================================
REM VALIDATION
REM ============================================================================

echo    [CHECK] Validating environment...
echo    ================================================
echo.

REM Check CODESYS Installation
if not exist "%CODESYS_PATH%\%CODESYS_EXE%" (
    echo    [ERROR] CODESYS not found at:
    echo           %CODESYS_PATH%\%CODESYS_EXE%
    echo.
    echo    [HINT] Check InstallPath in %CONFIG_FILE%
    echo.
    goto :ERROR_EXIT
)
echo    [OK] CODESYS found

REM Check Python Script
if not exist "%PYTHON_SCRIPT%" (
    echo    [ERROR] Python script not found:
    echo           %PYTHON_SCRIPT%
    echo.
    echo    [HINT] Available scripts in %SCRIPT_DIR%:
    echo.
    for %%F in ("%SCRIPT_DIR%\*.py") do (
        echo           - %%~nxF
    )
    echo.
    goto :ERROR_EXIT
)
echo    [OK] Python script found

REM Create Log Directory
if not exist "%LOG_DIR%" (
    mkdir "%LOG_DIR%" 2>nul
    if errorlevel 1 (
        echo    [WARNING] Could not create log directory
    ) else (
        echo    [OK] Log directory created
    )
) else (
    echo    [OK] Log directory ready
)

echo.

REM ============================================================================
REM EXECUTION SUMMARY
REM ============================================================================

echo    [SUMMARY] Execution Parameters
echo    ================================================
echo.
echo    CODESYS:  %CODESYS_PATH%
echo    Profile:  %CODESYS_PROFILE%
echo    Script:   %PYTHON_SCRIPT%
echo    Logs:     %LOG_DIR%
echo.
echo    ================================================
echo.

REM ============================================================================
REM EXECUTION
REM ============================================================================

echo    [START] Executing CODESYS Project Generator...
echo.

cd /d "%CODESYS_PATH%"

set "START_TIME=%TIME%"

"%CODESYS_EXE%" --noUI --profile="%CODESYS_PROFILE%" --runscript="%PYTHON_SCRIPT%"

set "EXIT_CODE=%ERRORLEVEL%"
set "END_TIME=%TIME%"

echo.
echo    ================================================
echo.

REM ============================================================================
REM RESULT ANALYSIS & LOG DISPLAY
REM ============================================================================

REM Find latest log file
set "LATEST_LOG="
for /f "delims=" %%F in ('dir /b /od "%SCRIPT_DIR%\*_log_*.txt" 2^>nul') do set "LATEST_LOG=%%F"

if %EXIT_CODE% EQU 0 (
    echo    [SUCCESS] Project generation completed!
    echo.
) else (
    echo    [ERROR] Execution failed (Exit Code: %EXIT_CODE%)
    echo.
)

REM Display log file content
if defined LATEST_LOG (
    echo    [LOG] Log file: %LATEST_LOG%
    echo    ================================================
    echo.
    
    REM Try PowerShell first (more reliable)
    powershell -NoProfile -Command "Get-Content '%SCRIPT_DIR%\!LATEST_LOG!' -Tail %MAX_LOG_LINES% 2>$null | ForEach-Object { Write-Host '    ' $_ }" 2>nul
    
    if errorlevel 1 (
        REM Fallback: Use simple type command for all content
        echo    [INFO] Showing complete log (PowerShell not available):
        echo.
        type "%SCRIPT_DIR%\!LATEST_LOG!"
    )
    
    echo.
) else (
    echo    [WARNING] No log file found in %SCRIPT_DIR%
    echo.
)

REM ============================================================================
REM EXECUTION SUMMARY
REM ============================================================================

echo    ================================================
echo.

REM Calculate duration
call :CalcDuration "%START_TIME%" "%END_TIME%"

REM Get final timestamp
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set "END_TIMESTAMP=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%"

if %EXIT_CODE% EQU 0 (
    set "EXIT_CODE_TEXT=SUCCESS"
) else (
    set "EXIT_CODE_TEXT=FAILED (Code: %EXIT_CODE%)"
)

echo    [SUMMARY] Execution Summary
echo    ================================================
echo.
echo    Status:      !EXIT_CODE_TEXT!
echo    Start:       %TIMESTAMP%
echo    End:         %END_TIMESTAMP%
echo    Duration:    !DURATION!
echo.

if defined LATEST_LOG (
    echo    Log File:    %SCRIPT_DIR%\!LATEST_LOG!
    echo.
)

if %EXIT_CODE% EQU 0 (
    echo    ================================================
    echo    ==                                            ==
    echo    ==        EXECUTION SUCCESSFUL                ==
    echo    ==                                            ==
    echo    ================================================
) else (
    echo    ================================================
    echo    ==                                            ==
    echo    ==        EXECUTION FAILED                    ==
    echo    ==                                            ==
    echo    ================================================
)

echo.
echo    ================================================
echo.
echo    Press any key to exit...
pause >nul
goto :END

REM ============================================================================
REM ERROR EXIT
REM ============================================================================
:ERROR_EXIT
echo.
echo    ================================================
echo    ==                                            ==
echo    ==        EXECUTION ABORTED                   ==
echo    ==                                            ==
echo    ================================================
echo.
echo    Press any key to exit...
pause >nul
exit /b 1

REM ============================================================================
REM DURATION CALCULATION
REM ============================================================================
:CalcDuration
set "start_time=%~1"
set "end_time=%~2"

REM Convert to seconds
for /f "tokens=1-3 delims=:." %%a in ("%start_time%") do (
    set /a "start_sec=(((%%a*60)+1%%b-100)*60)+1%%c-100"
)
for /f "tokens=1-3 delims=:." %%a in ("%end_time%") do (
    set /a "end_sec=(((%%a*60)+1%%b-100)*60)+1%%c-100"
)

set /a "duration=end_sec-start_sec"
if %duration% LSS 0 set /a "duration+=86400"

set /a "hours=duration/3600"
set /a "minutes=(duration%%3600)/60"
set /a "seconds=duration%%60"

if %hours% GTR 0 (
    set "DURATION=%hours%h %minutes%m %seconds%s"
) else if %minutes% GTR 0 (
    set "DURATION=%minutes%m %seconds%s"
) else (
    set "DURATION=%seconds%s"
)

goto :eof

REM ============================================================================
REM END
REM ============================================================================
:END
endlocal
exit /b %EXIT_CODE%