from employee import Employee,HourlyEmployee, SalaryEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self,new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print("current employees: ")
        for i in self.employees:
            print(i.fname,i.lname)
        print("-----------------")
    def pay_employees(self):
        print("paying employees: ")
        for i in self.employees:
            print("paycheck for ",i.fname ,'is: ',i.calculate_paycheck())

def main():
    myCompany = Company()
    employee1 = SalaryEmployee('Sarah','Hess',50000)
    myCompany.add_employee(employee1)
    employee2 = HourlyEmployee('blazej','wilinski',25,20)
    myCompany.add_employee(employee2)
    employee3 = ComissionEmployee('Michal','Antoszczyszyn',100000,7,250)
    myCompany.add_employee(employee3)

    myCompany.display_employees()
    myCompany.pay_employees()
main()