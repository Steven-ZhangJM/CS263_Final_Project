

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countPrimes function below.
def countPrimes(n):
    #sieveOfAtkin
    #print(isPrime(2))
    #print(isPrime(3))
    #print(isPrime(4))
    #print(isPrime(25))
    count = 0
    if(n<1):
        return 0
    else:
        print(n)
        #print(n * n)
        while(pow(n,2) > n):
            n = n-1
            #print(n)
        for _x in range(n-1,n,2):
            if isPrime(_x):
                count = count+1
                _x += 1
                #print(_x)
        return count

def isPrime(n):
    if(n<1):
        return False
    if(n==1):
        return False
    if(n==2):
        return True
    else:
        for x in