class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@codewithprince.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. please set it using setter."
        return f"{self.fname}.{self.lname}@codewithprince.com"

    @email.setter
    def email(self, string):
        print("setting now ...........")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill", "F")
# print(id(Employee))
# print(id("my name"))
# print(id("my name"))
# o = "this is a string."
# print(dir(skillf))
# print(dir(o))

import inspect
print(inspect.getmembers(skillf))