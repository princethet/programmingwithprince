# Public - anyone can see or access
# Protected - only subclasses of this file can access.
# Private -  only for the particular(specific) class and can't be printed normally.

class Employee:
    var = 8
    no_of_leaves = 8
    _protec = 9
    __private = 89
    def __init__(self, name, salary, role, languages=''):
        self.name = name
        self.salary = salary
        self.role = role
        

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("Harry", 343, "Programmer")
#print(emp._protec)
#print(emp.__private)
print(emp._Employee__private)