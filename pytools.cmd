@echo off
REM Set the path to your Python interpreter
set PYTHON_EXECUTABLE=py

REM Retrieve the function name from the command-line arguments
set function=%1

REM Retrieve the function arguments from the command-line arguments
set arguments=%2 %3 %4 %5 %6 %7 %8 %9

REM Get the current directory
set script_dir=%~dp0

REM Execute the Python script with the user-specified function and arguments
%PYTHON_EXECUTABLE% "%script_dir%pytools.py" %function% %arguments%


