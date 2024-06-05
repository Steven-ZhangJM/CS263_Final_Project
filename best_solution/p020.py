import math

def factorial(n):
    return math.factorial(n)

n = 100
fact = factorial(n)
str_fact = str(fact)

sum_of_digits = sum(int(digit) for digit in str_fact)
print(sum_of_digits)