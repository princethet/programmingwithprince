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



hindustani_supporter = Employee("Hindustani", "Supporter")
nikhil_raj_pandey = Employee("Nikhil", "raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)