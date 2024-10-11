#!/bin/bash

# Check if the virtual environment folder exists
if [ ! -d "env" ]; then
  echo "Creating virtual environment..."
  python3 -m venv env
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Install openpyxl in the virtual environment
echo "Installing openpyxl..."
pip install openpyxl

# Run the Python script
echo "Running secret_santa.py..."
python3 secret_santa.py


# Run the Test script
echo "Running secret_santa_tests.py..."
python3 secret_santa_tests.py



# Deactivate the virtual environment after execution
echo "Deactivating virtual environment..."
deactivate
