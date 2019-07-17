class Employee:
    increment = 1.5

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increaseSalary(self):
        self.salary = int(self.salary * Employee.increment)


class Programmer(Employee):

    def __init__(self , name, age, salary, language, exp):
        super().__init__(name, age, salary)
        self.language = language
        self.exp = exp

    def increaseSalary(self):
        self.salary = int(self.salary * (Employee.increment +0.4))

emp =Employee('waq', 25, 88000 )
emp.increaseSalary()
print(emp.salary)

prog  = Programmer('waquar', 26, 88000, 'python', 3)
prog.increaseSalary()
print(prog.salary)


# avoid using code duplicacy, try to use super keyword if code needs repitition
# every function if return type not given it will return none, nomatter what function is doing internally