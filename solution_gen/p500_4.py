

import math

def solution():
    num, divisors = [int(k) for k in open("input.txt")]
    divisor_sets = set()

    for p1 in range(math.ceil(math.sqrt(num))):
        for p2 in range(p1+1, math.ceil(math.sqrt(num)) + 1):
            c1 = num // pow(p1+1, 2)
            c2 = num // pow(p2+1, 2)
            if c1 < num and c1 + c2 == num:
                divisor_sets.add(p1+1)
        if p1 == math.ceil(math.sqrt(num)) and p2!= math.ceil(math.sqrt(num)):
            c = num // math.ceil(math.sqrt(num))
            divisor_sets.add(math.ceil(math.sqrt(num)))
    
    s = 0
    for d in range(len(divisor_sets)):
        if len