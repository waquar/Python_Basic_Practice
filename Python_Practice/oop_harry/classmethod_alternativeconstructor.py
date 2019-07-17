class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary  =salary

    @classmethod
    def from_str(cls, empdata_string):
        fname,lname,salary = empdata_string.split("-")
        return  cls(fname, lname, salary)


harry = Employee.from_str("waquar-alam-53000")
print(harry.fname)

#use classmethod decorator
#take data and split according to separator
#return the cls and pass to instance variable
