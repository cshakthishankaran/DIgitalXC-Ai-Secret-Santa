Secret Santa Game
Overview
This project automates the process of assigning Secret Santa pairings for employees in a company. 
It reads employee data and previous year's Secret Santa assignments from Excel files (.xlsx), 
assigns a unique Secret Child to each employee, and outputs the result to a new Excel file.


******************************************************************

TO EXECUTE THE CODE :

    1. Windows OS

        Double Click "win_start.bat" file to execute the program

    2. Windows OS

        run "linux_start.sh" file through terminal

    --> GENERATES AN OUTPUT FILE , secret-santa-2024.xlsx
    

*******************************************************************

Features
--------

    Avoids assigning an employee to themselves.
    Prevents assigning the same Secret Child as the previous year.
    Outputs results in an Excel file (.xlsx).
    Includes error handling for missing data and invalid assignments.
    Automatically sets up a Python virtual environment and installs required dependencies.

    Prerequisites
    --------
    Python 3.x
    openpyxl library (for reading and writing Excel files)

    Project Structure
    -----------------

    secret_santa.py: Main script for running the Secret Santa game.
    Employee-List.xlsx: Excel file containing the current list of employees (name and email).
    Secret-Santa-Game-Result-2023.xlsx: Excel file containing last year’s Secret Santa assignments.
    secret-santa-2024.xlsx: The output file containing this year's Secret Santa assignments.
    requirements.txt: Lists the project dependencies.
