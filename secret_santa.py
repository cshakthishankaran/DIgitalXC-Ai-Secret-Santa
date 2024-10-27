from file_handler import FileHandler
from secret_santa_assignment import SecretSantaAssignment

def main(employee_file: str, previous_assignments_file: str, output_file: str):
    # Get employee data
    employees = FileHandler.read_employee_list(employee_file)
    
    # Get previous assignments
    previous_assignments = FileHandler.read_previous_assignments(previous_assignments_file)

    # Assign new secret santas
    assignment_manager = SecretSantaAssignment(employees)
    assignment_manager.load_previous_assignments(previous_assignments)
    assignment_manager.assign_secret_children()

    # Generate new santas file for 2024
    assignments = assignment_manager.get_assignments()
    FileHandler.save_assignments(output_file, assignments)
    print(f"Secret Santa assignments saved to {output_file}")

if __name__ == "__main__":
    main("Employee-List.xlsx", "Secret-Santa-Game-Result-2023.xlsx", "Secret-Santa-Assignments-2024.xlsx")
