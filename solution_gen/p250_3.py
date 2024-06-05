

#solution

from math import factorial
import numpy
import matplotlib.pyplot as plt

digits = range(1,251)
nums = set([i for b in range(1,8) for i in b**digits*factorial(digits-b)])
dividers = [0]
for prime in [2,3,5,7]:
    for i in range(prime,len(nums)):
        is_divisor = False
        for d in dividers:
            if i % prime == 0:
                is_divisor = True
                break
        if not is_divisor:
            dividers.append(i)
            break
print(numpy.sum(nums[dividers[-16]:dividers[-1]+1]))

#plot_num

"""
import matplotlib.pyplot as plt
from math import factorial

dividers = [0]
for prime in [2,3,5,7,11,13]:
    for i in range(prime