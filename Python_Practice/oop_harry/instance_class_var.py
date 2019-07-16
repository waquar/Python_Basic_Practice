class Employee:

    increment = 2
    num_of_employees = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.num_of_employees += 1

    def  increase(self):
        self.salary = int(self.salary * Employee.increment)

print(Employee.num_of_employees)
gola = Employee('amit', 30, 18000)
shaktimaan = Employee('dev', 28, 20000)
print(gola.__dict__)
print(shaktimaan.__dict__)
print(Employee.num_of_employees)
gola.increase()
print(gola.salary)

