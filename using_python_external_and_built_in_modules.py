# import random
# random_number = random.randint(0, 1)
# print(random_number)

# rand = random.random()*100
# print(rand)

# import my_module
# my_module.greeting('prince')

# from math import sqrt, factorial
# print(sqrt(16))
# print(factorial(6))

# import math
# print(math.sqrt(25))
# print(math.pi)
# print(math.degrees(2))
# print(math.radians(60))
# print(math.sin(5))
# print(math.tan(0.23))
# print(math.factorial(7))

# UNIX EPOCH, JANUARY 1ST 1970: This is the date when the time started for unix computers and that timestamp is 
# marked as '0'. Any time since that date is calculated based on the number of seconds elapsed.

import datetime
from datetime import date
import time
print(time.time())
print(date.fromtimestamp(time.time()))