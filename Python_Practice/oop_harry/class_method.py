class Employee:
    increment = 1.5

    def __init__(self, name, salary):
        self.name = name
        self.salary  = salary

    def increasesalary(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

emp = Employee('waq', 23000)
# emp.increasesalary()
# print(emp.salary)
emp.change_increment(3)
emp.increasesalary()
print(emp.name, emp.salary)

#it overrides class variable using class method decorator
#first we have to call the decorator part and then we have to call function
#when we dont want to use instance variable we can use class method