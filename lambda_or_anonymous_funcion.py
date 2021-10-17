# IN python, an anonymous function is a function that is defined without a name. While normal function are
# defined using the def keyword in python, anonymous function are defined using the lambda keyword. hence, anonymous
# functions are also called lambda functions.

# minus = lambda x, y: x-y
# print(minus(9, 4))

# using lambda with sort function
# def a_first(a):
#     return a[1]
# a = [[1, 14], [5, 6], [8, 23]]
# a.sort (key = a_first)
# print(a)

a = [[1, 14], [5, 6], [8, 23]]
a.sort(key= lambda x:x[1])
print(a)