# tests/test_employee.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Alice", "alice@example.com")

    def test_employee_initialization(self):
        self.assertEqual(self.employee.name, "Alice")
        self.assertEqual(self.employee.email, "alice@example.com")
        self.assertIsNone(self.employee.secret_child)

    def test_assign_secret_child(self):
        child = Employee("Bob", "bob@example.com")
        self.employee.assign_secret_child(child)
        self.assertEqual(self.employee.secret_child, child)
        self.assertEqual(self.employee.secret_child.name, "Bob")
        self.assertEqual(self.employee.secret_child.email, "bob@example.com")

if __name__ == "__main__":
    unittest.main()
