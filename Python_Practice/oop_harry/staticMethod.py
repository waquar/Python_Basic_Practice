class Employee:

    def __init__(self, name,age):
        self.name = name
        self.age =age


    @staticmethod
    def isopen(day):
        if day  is  'Sunday':
            return True
        else:
            return  False

print(Employee.isopen('Sunday'))

