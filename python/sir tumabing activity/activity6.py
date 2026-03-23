# PAYROLL SYSTEM ACTIVITY
# public, private, protected variables

class User:
    def __init__(self, username, password, employee_name):
        self.username = username
        self.__password = password
        self._employee_name = employee_name

    def check_password(self, password):
        return self.__password == password

    def get_employee_name(self):
        return self._employee_name

    def display_user(self):
        print(f"Username: {self.username}")
        print(f"Employee Name: {self._employee_name}")


# ENCAPSULATION AND DATA HIDING
class PayrollRecord:
    def __init__(self, employee_id, name, basic_salary):
        self.employee_id = employee_id
        self._name = name
        self.basic_salary = basic_salary
        self.__deductions = {}
        self.__secret_code = "PAYROLL-2026"

    def add_deduction(self, deduction_name, amount):
        self.__deductions[deduction_name] = amount

    def get_deductions(self):
        return self.__deductions

    def compute_overtime_pay(self):
        return self.basic_salary * 0.10

    def compute_bonus(self):
        return self.basic_salary * 0.15

    def compute_gross_salary(self):
        return self.basic_salary + self.compute_overtime_pay() + self.compute_bonus()

    def compute_total_deductions(self):
        return sum(self.__deductions.values())

    def compute_net_salary(self):
        return self.compute_gross_salary() - self.compute_total_deductions()

    def display_record(self):
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self._name}")
        print(f"Basic Salary: {self.basic_salary:.2f}")
        print(f"Overtime Pay (10%): {self.compute_overtime_pay():.2f}")
        
        print(f"Bonus (15%): {self.compute_bonus():.2f}")
        print("Deductions:")
        for deduction, amount in self.__deductions.items():
            print(f"  {deduction}: {amount:.2f}")
        print(f"Total Deductions: {self.compute_total_deductions():.2f}")
        print(f"Net Salary: {self.compute_net_salary():.2f}")

    def show_secret_code(self):
        print("Secret Code:", self.__secret_code)


# INHERITANCE
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def role(self):
        print(f"{self.company_name} manages the payroll system.")


class DepartmentInfo:
    def __init__(self, department):
        self.department = department

    def show_department(self):
        print(f"Department: {self.department}")


# Hybrid Inheritance
class Employee(Company, DepartmentInfo):
    def __init__(self, company_name, employee_name, department):
        Company.__init__(self, company_name)
        DepartmentInfo.__init__(self, department)
        self.employee_name = employee_name

    def role(self):
        print(f"{self.employee_name} is an employee in {self.department} department.")


# super() function
class Supervisor(Company):
    def __init__(self, company_name, supervisor_name):
        super().__init__(company_name)
        self.supervisor_name = supervisor_name

    def role(self):
        print(f"{self.supervisor_name} is a supervisor of {self.company_name}.")


class Manager(Company):
    def __init__(self, company_name, manager_name):
        super().__init__(company_name)
        self.manager_name = manager_name

    def role(self):
        print(f"{self.manager_name} is a manager of {self.company_name}.")


# POLYMORPHISM
class PayrollReport:
    def generate_report(self):
        print("Generating general payroll report...")


class EmployeePayrollReport(PayrollReport):
    def generate_report(self):
        print("Generating Employee Payroll Report...")


class CompanyPayrollReport(PayrollReport):
    def generate_report(self):
        print("Generating Company Payroll Report...")


# MAIN PROGRAM
def main():
    print("=== PAYROLL SYSTEM ACTIVITY ===")

    # REGISTRATION
    print("\n--- Registration ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    employee_name = input("Enter employee name: ")

    user1 = User(username, password, employee_name)

    print("\n--- Login ---")
    login_user = input("Username: ")
    login_pass = input("Password: ")

    if login_user == user1.username and user1.check_password(login_pass):
        print("Login successful!")
    else:
        print("Invalid username or password.")
        return

    # Class and Object
    print("\n--- Payroll Record Creation ---")
    employee_id = int(input("Enter employee ID: "))
    basic_salary = float(input("Enter basic salary: "))
    payroll1 = PayrollRecord(employee_id, employee_name, basic_salary)
    print("Payroll record object created successfully.")

    # lists, tuples, dictionaries, sets
    deduction_names = ["SSS/GSIS", "PhilHealth", "Pag-IBIG", "Tax"]
    employee_roles = ("Company", "Supervisor", "Manager", "Employee")
    entered_deductions = set()

    print("\n--- Enter Deductions ---")
    for deduction in deduction_names:
        if deduction == "Tax":
            tax_percent = float(input("Enter tax percentage (%): "))
            amount = payroll1.compute_gross_salary() * (tax_percent / 100)
        else:
            amount = float(input(f"Enter amount for {deduction}: "))
        payroll1.add_deduction(deduction, amount)
        entered_deductions.add(deduction)

    # display record
    payroll1.display_record()

    print("\nDeductions entered (set):", entered_deductions)
    print("System Roles (tuple):", employee_roles)

    # Conditionals
    net_salary = payroll1.compute_net_salary()
    print("\n--- Salary Remarks ---")
    if net_salary >= 50000:
        print("High Net Salary")
    elif net_salary >= 20000:
        print("Average Net Salary")
    else:
        print("Low Net Salary")

    # Encapsulation and Data Hiding
    print("\n--- Encapsulation and Data Hiding ---")
    print("Public:", payroll1.employee_id)
    print("Protected:", payroll1._name)
    print("Private deductions accessed through method:", payroll1.get_deductions())

    # Name Mangling
    print("Name Mangling access:", payroll1._PayrollRecord__secret_code)

    # Inheritance
    print("\n--- Inheritance ---")
    emp = Employee("ABC Company", employee_name, "HR")
    emp.role()
    emp.show_department()

    supervisor = Supervisor("ABC Company", "Mr. Santos")
    supervisor.role()

    manager = Manager("ABC Company", "Ms. Reyes")
    manager.role()

    # Polymorphism
    print("\n--- Polymorphism ---")
    reports = [PayrollReport(), EmployeePayrollReport(), CompanyPayrollReport()]
    for report in reports:
        report.generate_report()

    print("\nSystem finished successfully.")


if __name__ == "__main__":
    main()
