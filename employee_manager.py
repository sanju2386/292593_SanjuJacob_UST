import os
import pickle
from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.filename = r"C:\Users\292593\Desktop\master\python training\Hackatons\Friday_4th\292593_SanjuJacob_UST\Hackaton_11_April\Hackaton3_v2\employee_data.pkl"
        self.employees = self.load_data()

    def add_employee(self, name, dept, desig, gross, tax, bonus):
        emp = Employee(name, dept, desig, gross, tax, bonus)
        self.employees.append(emp.to_dict())
        self.save_data()
        return emp

    def save_data(self):
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):  # Check if directory is not empty
            os.makedirs(directory, exist_ok=True)

        with open(self.filename, "wb") as f:
            pickle.dump(self.employees, f)

    def load_data(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []
        except pickle.UnpicklingError:
            print("Error unpickling file. Data might be corrupted.")
            return []

    def view_employees(self):
        return [Employee.from_dict(emp_dict) for emp_dict in self.employees]

    def search_employee_by_id(self, emp_id):
        for emp_dict in self.employees:
            if emp_dict["id"] == emp_id:
                return Employee.from_dict(emp_dict)
        return None

    def delete_employee(self, emp_id):
        original_len = len(self.employees)
        self.employees = [emp for emp in self.employees if emp["id"] != emp_id]
        self.save_data()
        return len(self.employees) < original_len
