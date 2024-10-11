@echo off
REM Checks if the virtual environment folder exists
IF NOT EXIST env (
    echo Creating virtual environment...
    py -m venv env
)

REM Activate the virtual environment
echo Activating virtual environment...
call env\Scripts\activate

REM Install openpyxl in the virtual environment
echo Installing openpyxl...
pip install openpyxl

REM Run the Python script
echo Running secret_santa.py...
py secret_santa.py

REM Deactivate the virtual environment after execution
echo Deactivating virtual environment...
deactivate

pause
