


import math
import os
import random
import re
import sys

# Complete the largestPalindrome function below.
def largestPalindrome(n):
    nums = []
    i = 1
    while i*i <= n:
        num = i*i
        if str(num*num) == str(num*num)[::-1]:
            i += 1
            nums.append(num)
        # print(i, num)

    return max(nums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = largestPalindrome(1000)

    fptr.write(str(p) + '\n')

    fptr.close()
