import random
from typing import List
from employee import Employee

class SecretSantaAssignment:
    """Class handling the Secret Santa assignment logic."""
    def __init__(self, employees: List[Employee]):
        self.employees = employees
        self.previous_assignments = {}

    def load_previous_assignments(self, previous_assignments):
        """Load previous assignments from a dictionary."""
        self.previous_assignments = previous_assignments

    def assign_secret_children(self):
        """Assign secret children while respecting all constraints."""
        try:
            available_children = self.employees.copy()
            random.shuffle(available_children)

            for employee in self.employees:
                for child in available_children:
                    if child.email != employee.email and child.email != self.previous_assignments.get(employee.email):
                        employee.assign_secret_child(child)
                        available_children.remove(child)
                        break
                else:
                    raise ValueError("Unable to complete assignments due to constraints.")

            if available_children:
                raise ValueError("Some employees were not assigned Secret Santa children.")

        except Exception as e:
            print(str(e))
            raise Exception(str(e))    
        
    def get_assignments(self):
        try:    
            """Get a list of current assignments in dictionary format."""
            return [{
                "Employee_Name": e.name,
                "Employee_EmailID": e.email,
                "Secret_Child_Name": e.secret_child.name if e.secret_child else None,
                "Secret_Child_EmailID": e.secret_child.email if e.secret_child else None
            } for e in self.employees]

        except Exception as e:
            print(str(e))
            raise Exception(str(e))
