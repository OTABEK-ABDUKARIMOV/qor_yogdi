# 14-Amalyot
# 1-Problem

# class BankAccount:
#     def __init__(self, owner_name, initial_balance=0):
#         self.owner_name = owner_name
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += amount
#         return f"{amount} deposited successfully. New balance: {self.balance}"

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return f"{amount} withdrawn successfully. New balance: {self.balance}"
#         else:
#             return "Insufficient funds"

#     def check_balance(self):
#         return f"Current balance for {self.owner_name}: {self.balance}"

# account = BankAccount("John Doe", 1000)
# print(account.check_balance())
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.check_balance())

# 2-Problem

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = max(salary, 0)  # Maosh 0 dan kam bo'lishi mumkin emas

    def get_salary(self):
        return f"Employee Name: {self.name}, ID: {self.employee_id}, Monthly Salary: {self.salary}"

    def set_salary(self, new_salary):
        self.salary = max(new_salary, 0)
        return f"New salary set for {self.name}: {self.salary}"

    def get_annual_salary(self):
        annual_salary = self.salary * 12
        return f"Employee {self.name}'s Annual Salary: {annual_salary}"

employee = Employee("Otabek Abdukarimov", 12345, 3000)
print(employee.get_salary())
print(employee.set_salary(3500))
print(employee.get_annual_salary())


 
 
