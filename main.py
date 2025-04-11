from employee_manager import EmployeeManager

def main():
    manager = EmployeeManager()

    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search by ID")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            dept = input("Enter department: ")
            desig = input("Enter designation: ")
            gross = float(input("Enter gross salary: "))
            tax = float(input("Enter tax: "))
            bonus = float(input("Enter bonus: "))
            emp = manager.add_employee(name, dept, desig, gross, tax, bonus)
            print(f"Employee {emp.name} added successfully with ID {emp.id}.")

        elif choice == 2:
            employees = manager.view_employees()
            if employees:
                for emp in employees:
                    print(f"ID: {emp.id}, Name: {emp.name}, Dept: {emp.department}, "
                          f"Designation: {emp.designation}, Gross Salary: {emp.gross_salary}, "
                          f"Tax: {emp.tax}, Bonus: {emp.bonus}, Net Salary: {emp.net_salary}")
            else:
                print("No employees found.")

        elif choice == 3:
            emp_id = input("Enter employee ID to search: ")
            employee = manager.search_employee_by_id(emp_id)
            if employee:
                print(f"Employee found: {employee}")
            else:
                print("Employee not found.")

        elif choice == 4:
            emp_id = input("Enter employee ID to delete: ")
            if manager.delete_employee(emp_id):
                print(f"Employee with ID {emp_id} deleted.")
            else:
                print("Employee not found.")

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()