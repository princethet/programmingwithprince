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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary


emp1 = Employee("prince", 346, "programmer")
emp2 = Employee("rohan", 65, "cleaner")

print(emp1 / emp2)

# Mapping operators to functions