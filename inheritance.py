class Employee:
    no_of_leaves = 8
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

class Programmer(Employee):
    no_of_holidays = 56
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages
        
    def printprog(self):
        return f"the programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}. the languages they is : {self.languages}."

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "students")

shubham = Programmer("Shubham", 555, "Programmer", ['python', 'ruby', 'javascript'])
karan = Programmer("Karan", 777, "Programmer", ['c++', 'c', 'c#'])
print(karan.no_of_holidays)