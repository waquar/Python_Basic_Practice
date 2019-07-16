class Employee:

    increment = 1.5


    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname= lname
        self.salary  = salary


harry = Employee('harry', 'roy', 48000)
rohan = Employee('waquar', 'alam', 59000)

print(harry.fname, rohan.fname)

