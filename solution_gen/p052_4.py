

import sys
import itertools
from itertools import product

numbers = [2,3,34,55,6,7,88]



def is_good(n):
    return len(set(str(n)) & set(str(n*2))) == len(str(n*2))
    # return n == int(str(n)[::-1])
    

for num in numbers:
    if is_good(num) == True:
        print(num)
        break
        

    

    















