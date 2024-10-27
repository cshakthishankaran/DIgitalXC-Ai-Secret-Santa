import unittest
import pandas as pd
from ..employee import Employee
from file_handler import FileHandler
from unittest.mock import patch, MagicMock

class TestFileHandler(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_read_employee_list(self, mock_read_excel):
        # Mock employee data
        mock_data = pd.DataFrame({
            "Employee_Name": ["Alice", "Bob"],
            "Employee_EmailID": ["alice@example.com", "bob@example.com"]
        })
        mock_read_excel.return_value = mock_data

        # Read employee list
        employees = FileHandler.read_employee_list("mock_file.xlsx")
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].name, "Alice")
        self.assertEqual(employees[0].email, "alice@example.com")

    @patch("pandas.read_excel")
    def test_read_previous_assignments(self, mock_read_excel):
        # Mock previous assignment data
        mock_data = pd.DataFrame({
            "Employee_Name": ["Alice"],
            "Employee_EmailID": ["alice@example.com"],
            "Secret_Child_Name": ["Bob"],
            "Secret_Child_EmailID": ["bob@example.com"]
        })
        mock_read_excel.return_value = mock_data

        # Read previous assignments
        previous_assignments = FileHandler.read_previous_assignments("mock_file.xlsx")
        self.assertEqual(previous_assignments["alice@example.com"], "bob@example.com")

    @patch("pandas.DataFrame.to_excel")
    def test_save_assignments(self, mock_to_excel):
        # Mock assignments data
        assignments = [
            {
                "Employee_Name": "Alice",
                "Employee_EmailID": "alice@example.com",
                "Secret_Child_Name": "Bob",
                "Secret_Child_EmailID": "bob@example.com"
            }
        ]
        FileHandler.save_assignments("mock_output.xlsx", assignments)

        # Check if the to_excel function was called
        mock_to_excel.assert_called_once()

if __name__ == "__main__":
    unittest.main()
