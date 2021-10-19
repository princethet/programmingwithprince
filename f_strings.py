# import math
# me = 'harry'
# a = f"This is {me} {math.cos(65)}"
# print(a)

# *args and **kwargs in python

# def funargs(*args):
#     for item in args:
#         print(item)

# har = ['harry', 'Rohan', 'Skillf', 'Hammad']
# funargs(*har)

# def funargs(*args):
#     print(type(args))
#     print(args[0:3])

# har = ['Harry', 'Rohan', 'Skillf', 'Hammad', 'Shivam']
# funargs(*har)

def funargs(normal, *argsrohan, **kwargs):
    print(normal)
    for item in argsrohan:
        print(item)
har = ['Harry', 'rohan', 'skillf', 'hammad', 'shivoham']
normal = "I am a normal argument:"
funargs(normal, *har)