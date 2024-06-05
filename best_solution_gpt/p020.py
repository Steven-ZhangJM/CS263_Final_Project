import math

def sum_of_digits(n):
    return sum(int(digit) for digit in str(math.factorial(n)))

# Find the sum of the digits in the number 100!
print(sum_of_digits(100))