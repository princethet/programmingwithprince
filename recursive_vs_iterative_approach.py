# the key difference between recursion and iteration is a process to call a function within the same 
# function while iteration is to execute a set of instructions repeatedly until the given condition is true.

# Iterative method
# def factorial_iterative(n):
#     '''
#     : para n : Integer
#     : return : n(n-1)(n-2).....321
#     '''
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac

# number = int(input('Enter then number: '))
# print('factorial Using Iterative Method', factorial_iterative(number))

# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac

# number = int(input('ENTER the number'))
# print(factorial(number))

#   RECURSIVE METHOD
# def factorial_recursive(n):
#     '''
#     : para n: Integer
#     : return : n*(n-1)*(n-2).....321
#     '''
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# number = int(input('Enter the number'))
# print('Factorial Using recursion method', factorial_recursive(number))

# FIBBONACCI SEQUENCE (EX: 0, 1, 1, 2, 3, 5, 8, 13........)
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the no: "))
print(fibonacci(number))
