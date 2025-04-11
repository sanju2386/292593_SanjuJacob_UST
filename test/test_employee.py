import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_unique_ids(self):
        emp1 = Employee("Anil", "Design", "Designer", 42000, 3000, 310)
        emp2 = Employee("Sunil", "UI_Ux", "Designer", 110000, 10000, 2000)
        self.assertNotEqual(emp1.id, emp2.id)

    def test_net_salary_anil(self):
        emp = Employee("Anil", "Design", "Designer", 42000, 3000, 310)
        expected_net = 42000 - 3000 + 310  # 39310
        self.assertEqual(emp.net_salary, expected_net)

    def test_net_salary_sunil(self):
        emp = Employee("Sunil", "UI_Ux", "Designer", 110000, 10000, 2000)
        expected_net = 110000 - 10000 + 2000  # 102000
        self.assertEqual(emp.net_salary, expected_net)

    def test_to_dict_sunil(self):
        emp = Employee("Sunil", "UI_Ux", "Designer", 110000, 10000, 2000)
        emp_dict = emp.to_dict()
        self.assertEqual(emp_dict["name"], "Sunil")
        self.assertEqual(emp_dict["net_salary"], emp.net_salary)

    def test_from_dict_anil(self):
        data = {
            "id": "2781",
            "name": "Anil",
            "department": "Design",
            "designation": "Designer",
            "gross_salary": 42000,
            "tax": 3000,
            "bonus": 310,
            "net_salary": 39310
        }
        emp = Employee.from_dict(data)
        self.assertEqual(emp.name, "Anil")
        self.assertEqual(emp.department, "Design")
        self.assertEqual(emp.net_salary, 39310)
        self.assertEqual(emp.id, "2781")

if __name__ == "__main__":
    unittest.main()
