class Employee:
    """Class representing an employee."""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.secret_child = None  # To be assigned later

    def assign_secret_child(self, child):
        """Assign a secret child to this employee."""
        self.secret_child = child

    def __repr__(self):
        return f"Employee(name={self.name}, email={self.email}, secret_child={self.secret_child})"
