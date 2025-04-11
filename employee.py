import random

class Employee:
    used_ids = set()  # A class-level set to track used IDs

    def __init__(self, name, department, designation, gross_salary, tax, bonus):
        self.id = self.generate_unique_id()
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    @classmethod
    def generate_unique_id(cls):
        """Generate a unique ID for an employee."""
        while True:
            new_id = random.randint(1000, 9999)
            if new_id not in cls.used_ids:
                cls.used_ids.add(new_id)
                return str(new_id)

    def calculate_net_salary(self):
        """Calculate net salary based on gross salary, tax, and bonus."""
        return self.gross_salary - self.tax + self.bonus

    def __str__(self):
        """String representation of an employee."""
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Designation: {self.designation}, Gross Salary: {self.gross_salary}, Tax: {self.tax}, Bonus: {self.bonus}, Net Salary: {self.net_salary}"

    def to_dict(self):
        """Convert the Employee object to a dictionary for Pickle storage."""
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }

    @classmethod
    def from_dict(cls, data):
        """Convert a dictionary back to an Employee object."""
        emp = cls(data['name'], data['department'], data['designation'], data['gross_salary'], data['tax'], data['bonus'])
        emp.id = data['id']
        emp.net_salary = data['net_salary']
        return emp
