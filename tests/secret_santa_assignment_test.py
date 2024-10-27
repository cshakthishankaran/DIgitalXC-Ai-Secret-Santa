import unittest
from employee import Employee
from secret_santa_assignment import SecretSantaAssignment

class TestSecretSantaAssignment(unittest.TestCase):
    def setUp(self):
        # Create a list of employees
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com")
        ]
        self.assignment_manager = SecretSantaAssignment(self.employees)

    def test_load_previous_assignments(self):
        # Mock previous assignments
        previous_assignments = {"alice@example.com": "bob@example.com"}
        self.assignment_manager.load_previous_assignments(previous_assignments)
        self.assertEqual(self.assignment_manager.previous_assignments["alice@example.com"], "bob@example.com")

    def test_assign_secret_children(self):
        # Perform Secret Santa assignment
        self.assignment_manager.assign_secret_children()

        # Check that all employees have a secret child and there are no duplicates
        assigned_children = {emp.secret_child for emp in self.employees}
        self.assertEqual(len(assigned_children), len(self.employees))

        # Ensure no one is assigned to themselves
        for emp in self.employees:
            self.assertNotEqual(emp.secret_child, emp)

    def test_assignment_respects_previous_assignments(self):
        # Set previous assignment constraints
        previous_assignments = {"alice@example.com": "bob@example.com"}
        self.assignment_manager.load_previous_assignments(previous_assignments)

        # Perform assignment with constraint
        self.assignment_manager.assign_secret_children()

        # Verify Alice does not get Bob again as secret child
        alice = next(emp for emp in self.employees if emp.email == "alice@example.com")
        self.assertNotEqual(alice.secret_child.email, "bob@example.com")

if __name__ == "__main__":
    unittest.main()
