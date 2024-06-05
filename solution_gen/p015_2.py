

from math import factorial,factorial2

t = int(input())
while t > 0:
    n = int(input())
    fact = factorial(n)
    k_2 = factorial2(2*n-1)
    fact = fact*k_2
    print(fact)
    t -= 1
