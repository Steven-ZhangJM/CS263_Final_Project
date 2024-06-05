```
from math import prod
from itertools import product

# Define a function to generate all possible numbers
def generate_numbers():
    # Generate all possible digits (0-9) for each position
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Generate all possible combinations of these digits
    numbers = list(product(digits, repeat=18))
    
    return numbers

# Define a function to count the number of times each digit appears in a given number
def count_digits(num):
    counts = [0] * 10  # Initialize counts for each digit (0-9)
    for digit in num:
        counts[int(digit)] += 1  # Increment count for each digit
    
    return counts

# Define the main function to solve the problem
def solve_problem():
    numbers = generate_numbers()
    
    count = 0
    for num in numbers:
        if all(count <= 3 for count in count_digits(num)):
            count += 1
    
    print(count)

solve_problem()