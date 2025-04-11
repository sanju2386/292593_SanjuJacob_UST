import unittest
import os
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary EmployeeManager for testing
        self.manager = EmployeeManager()
        self.manager.filename = "test_employee_data.pkl"  # Use a test-specific file to avoid interference
        self.manager.employees = []  # Clear existing data

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.manager.filename):
            os.remove(self.manager.filename)

    def test_add_employee(self):
        # Add "Anil" employee and check details
        emp = self.manager.add_employee("Anil", "Design", "Designer", 40000, 7000, 6300)
        self.assertEqual(emp.name, "Anil")
        self.assertEqual(emp.department, "Design")
        self.assertEqual(emp.designation, "Designer")

    def test_add_another_employee(self):
        # Add "Sunil" employee and check details
        emp = self.manager.add_employee("Sunil", "UI_Ux", "Designer", 100000, 5000, 17000)
        self.assertEqual(emp.name, "Sunil")
        self.assertEqual(emp.department, "UI_Ux")
        self.assertEqual(emp.designation, "Designer")

    def test_view_employees(self):
        # Adding employees for this specific test case
        self.manager.add_employee("Sunil", "UI_Ux", "Designer", 100000, 5000, 17000)
        self.manager.add_employee("Anil", "Design", "Designer", 40000, 7000, 6300)

        # View and check if the correct employees are returned
        employees = self.manager.view_employees()

        # Ensure that the length is 2
        self.assertEqual(len(employees), 2)
        
        # Check if the names match the expected ones
        self.assertEqual(employees[0].name, "Sunil")
        self.assertEqual(employees[1].name, "Anil")

if __name__ == "__main__":
    unittest.main()
