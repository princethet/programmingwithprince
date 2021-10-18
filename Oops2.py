class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 4555
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 3456

print(Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 9
print(rohan.__dict__)
print(Employee.no_of_leaves)