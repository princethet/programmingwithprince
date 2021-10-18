# Classes - Template
# Object - Instance of the class 
#DRY - Do not Repeat Yourself

class Student:
    pass
prince = Student()
harry = Student()

prince.name = "Prince"
prince.std = 11
prince.section = 2
harry.subjects = ["hindi", "physics"]
print(prince.name, harry.subjects)