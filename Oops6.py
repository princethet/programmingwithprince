class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
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

prince = Employee("Prince", 23456, "khalasi")
harry = Employee("Harry", 2786, "Instructor")
rohan = Employee.from_str("Karan-480-student") 

print(rohan.no_of_leaves)
# harry.change_leaves(34)
# print(harry.no_of_leaves)

Employee.printgood("HARRY")