# l =10 # global variable
# def function1(n):
#     l = 5 #local variable
#     m = 8
#     print(l, m)
#     print(n, 'I have printed')

# function1('This is me')

# l = 10
# def function1(n):
#     m = 8
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, 'I have printed')

# function1('And')

# nested function

def prince():
    x = 20
    def rohan():
        global x
        x = 88
        print('before calling rohan()', x)
    rohan()
    print('after calling rohan()', x)

prince()