class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @property
    def email(self):
        if self.fname == None:
            return 'email not set'
        else:
            return self.fname + '.' + self.lname + '@email.com'


    @email.setter
    def email(self, givenemail):
        new_name = givenemail.split('@')[0].split(".")
        print(new_name)
        self.fname = new_name[0]
        self.lname =new_name[1]


    @email.deleter
    def email(self):
        self.fname = None
        self.lname  = None

if __name__ == '__main__':
    waq = Employee('waquar', 'alam', 77000)
    print(waq.email)
    waq.lname = 'ansari'
    print(waq.email)
    waq.email = 'ansari.waquar@email.com'
    print(waq.email)
    del waq.email
    print(waq.email)






#property makes a function look like attribute and call without using ()
#if using setter then give the function name same in setter and function both
#deleter use to delete the function after use
#name should be same as function .
