class Employee(object):
    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return "This employee firatname is {} and last name is {}".format(self.fname, self.lname)

    @property
    def email(self):
        return "{}.{}@email.com".format(self.fname, self.lname)

    @email.setter
    def email(self, string):
        self.fname = string.split('@')[0].split('.')[0]
        self.lname = string.split('@')[0].split('.')[1]



emp_1 = Employee('William', 'McBeth')
emp_1.fname = 'Freda'
emp_1.email ='djdndk.dkfm@email.com'
print(emp_1.email)
print(emp_1.fname, emp_1.lname)