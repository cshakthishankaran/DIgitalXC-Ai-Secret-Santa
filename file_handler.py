# file_handler.py

import pandas as pd
from typing import List  # Add this line to import List type
from employee import Employee

class FileHandler:
    """Handles reading from and writing to files."""
    
    @staticmethod
    def read_employee_list(filepath: str) -> List[Employee]:
        df = pd.read_excel(filepath)
        return [Employee(row['Employee_Name'], row['Employee_EmailID']) for _, row in df.iterrows()]

    @staticmethod
    def read_previous_assignments(filepath: str) -> dict:
        df = pd.read_excel(filepath)
        return {row['Employee_EmailID']: row['Secret_Child_EmailID'] for _, row in df.iterrows()}

    @staticmethod
    def save_assignments(filepath: str, assignments: List[dict]):
        pd.DataFrame(assignments).to_excel(filepath, index=False)
