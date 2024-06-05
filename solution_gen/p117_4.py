

#!/bin/python3
#from math import factorial
import math

n = int(input())

count = 0
while n>50:
    n = n-50
    if n<0:
        n = 0
    count += 1

print(count)
