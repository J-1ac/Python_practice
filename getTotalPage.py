#getTotalPage.py

import math

def getTotalPage(m, n):
    return math.ceil(m/n)

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))