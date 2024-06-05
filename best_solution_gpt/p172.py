from itertools import product
from collections import Counter

# Function to check if no digit occurs more than three times
def is_valid(number):
    return all(count <= 3 for count in Counter(number).values())

# Generate all 18-digit numbers and filter based on the condition
valid_numbers = [''.join(p) for p in product('123456789', repeat=1) + product('0123456789', repeat=17) if is_valid(p)]

# Output the count of valid numbers
print(len(valid_numbers))