from math import factorial

# Function to calculate the sum of factorials of the digits of a number
def sum_of_digit_factorials(n):
    return sum(factorial(int(digit)) for digit in str(n))

# Find all numbers which are equal to the sum of the factorial of their digits
def find_curious_numbers(limit):
    curious_numbers = []
    for i in range(10, limit):  # Starting from 10 because 1! and 2! are not sums
        if i == sum_of_digit_factorials(i):
            curious_numbers.append(i)
    return curious_numbers

# Calculate the upper limit for search (9! * 7 is a reasonable limit because 9! * 8 has more digits)
upper_limit = factorial(9) * 7

# Find curious numbers and calculate their sum
curious_numbers = find_curious_numbers(upper_limit)
sum_curious_numbers = sum(curious_numbers)
print(sum_curious_numbers)