# numbers  = ["3", "56", "78"]
# numbers = list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a

# num = [2,3,4,5,6,45,67]
# square = list(map(sq, num))
# print(square)

# num = [2,3,4,5,6,45,67, 99]
# square = list(map(lambda x: x*x, num))
# print(square)


# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)

# ----------------------FILTER-----------------------
# list_1 = [1, 2, 3, 4, 5, 7]
# def is_greater_4(num):
#     return num>4

# gr_than_4 = list(filter(is_greater_4, list_1))
# print(gr_than_4)

# ----------------------REDUCE------------------------
from functools import reduce

list1 = [1,2,34,45]
num = reduce(lambda x,y:x*y, list1)
print(num)
