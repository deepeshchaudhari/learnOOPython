class Employee:
    increment = 1.5
    no_of_employee = 0

    def __init__(self, fname, lname, salary): #builtin dubder method
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employee += 1
    @property
    def email(self):
        if self.fname == None or self.lname==None:
            return "Not Exist"
        return self.fname +"."+self.lname +"@gmail.com"
    @email.setter
    def email(self,given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]
    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None

    def increase(self):
        self.salary = int(self.salary * Employee.increment)
    # decorater
    @classmethod
    def changeClasvariable(cls, amount):
        cls.increment = amount
    @classmethod
    def from_str(cls,em_string):
        fname,lname,salary = em_string.split("-")
        return cls(fname,lname,salary)
    # not using any class variable or instance
    @staticmethod
    def inopen(day):
        if day== ('sunday' or 'saturday'):
            return False
        else:
            return True
    # overwrite + dunder method
    def __add__(self, other):
        return self.salary+other.salary
    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname,self.lname,self.salary)