# import time

# initial = time.time()
# print(initial)
# k = 0
# while (k<45):
#     print("This is prince bhai")
#     k += 1
# print(time.time)
# for i in range (45):
#     print("this is prince bhai")

# import time
# initial = time.time()
# print(initial)
# k = 0
# while(k<45):
#     print("This is prince bhai")
#     k += 1
# print("While loop ran in", time.time()-initial, "seconds")
# initial2 = time.time()
# for i in range(45):
#     print("This is prince bhai")
# print("For loop ran in", time.time()-initial2, "seconds")

import time
ti = time.gmtime()
# python time method time.asctime() is used to convert a tuple or a time.struct_time object representing a time
# as returned by time.gmtime() or localtime() method to a string of the following form:
print("Time calculated using asctime() is: ", end = '')
print(time.asctime(ti))

print("Time calculated using ctime() is: ", end='')
print(time.ctime())
print(time.time())
print(time.gmtime())
