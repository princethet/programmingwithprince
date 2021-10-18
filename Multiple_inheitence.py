class Employee:
    var = 8
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

class Player:
    var = 10
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}.Game is {self.game}"

class CoolProgrammer(Employee, Player):
    languages = 'c++'  
    def printlanguage(self):
        print(self.languages)
        
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "students")

shubham = Player("Shubham", ['Cricket'])
karan = CoolProgrammer("Karan", 8759, 'coolprogrammer')

# det = karan.printdetails()
# karan.printlanguage()
# print(det)

print(karan.var)
