class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}."


prince = Employee("Prince", 23456, "khalasi")
harry = Employee("Harry", 2786, "Instructor")
print(harry.salary)