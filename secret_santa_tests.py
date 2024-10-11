import unittest
from secret_santa import SecretSantaGenerator

class TestSecretSanta(unittest.TestCase):
    """
    Unit tests
    """
    
    def test_valid_assignments(self):

        """
        Testing to ensure that the Secret Santa does not assign an employee to themselves
        and avoids repeating last year's partner pair.
        """

        employees = [
            {'Employee_Name': 'Shakthi', 'Employee_EmailID': 'shakthi@example.com'},
            {'Employee_Name': 'Krishna', 'Employee_EmailID': 'krishna@example.com'},
            {'Employee_Name': 'VIshaal', 'Employee_EmailID': 'vishal@example.com'}
        ]
        previous_assignments = [
            {'Employee_Name': 'Shakthi', 'Employee_EmailID': 'shakthi@example.com', 
             'Secret_Child_Name': 'Krishna', 'Secret_Child_EmailID': 'krishna@example.com'}
        ]
        
        secret_santa = SecretSantaGenerator('', '')
        secret_santa.employees = employees
        secret_santa.previous_secret_santas = previous_assignments
        
        
        new_secret_santas = secret_santa.alot_new_secret_santas()
        self.assertEqual(len(new_secret_santas), 3)
        for secret_santa_pair in new_secret_santas:
            self.assertNotEqual(secret_santa_pair['Employee_EmailID'], secret_santa_pair['Secret_Child_EmailID'])
            self.assertNotIn((secret_santa_pair['Employee_EmailID'], secret_santa_pair['Secret_Child_EmailID']), secret_santa.previous_secret_santas)


if __name__ == '__main__':
    unittest.main()