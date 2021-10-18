# in python, polymorphism defines methods in the child class that have the same name as the 
# Methods in the parent class.However, it is possible to modify in a child class that it has
# inherited from the parent class.

# print(5+6)
# print("5" + "6")

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
print(b.classvar1)
print(b.special)
