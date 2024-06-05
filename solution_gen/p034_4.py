
from functools import reduce

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_fact(n):
    return sum(map(factorial, list(str(n))))

print('Sum with factorials is: {}'.format(sum([sum_fact(i) for i in range(1, 1000000)])))
