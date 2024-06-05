

#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *   # import library

# Complete the pandigital_step function below.
def check(numb):
    if(numb == ''):
        return False

    for i in range(len(numb)):
        if(numb[i] == '0' or numb[i] == '2' or numb[i] == '4' or numb[i] == '7' or numb[i] == '8' or numb[i] == '9'):
            return False
    
    return True

def valid_num(num):
    new_num = Decimal(num)
    if(new_num<0 or new_num>4999999 or not new_num**1000):
        return False
    
    return True

def pandigital_step(num,n):
    print(new_num)
    s1_num = new_num[::2]
    s2_num = new_num[1::2]
    s