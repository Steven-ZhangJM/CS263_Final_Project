# Python code to calculate the difference between the sum of the squares and the square of the sum of the first one hundred natural numbers

# Function to calculate the sum of squares
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# Function to calculate the square of the sum
def square_of_sum(n):
    return sum(range(1, n+1)) ** 2

# Calculate the difference
difference = square_of_sum(100) - sum_of_squares(100)
difference