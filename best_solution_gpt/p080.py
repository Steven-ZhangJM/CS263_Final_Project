import math
from decimal import Decimal, getcontext

# Set precision for Decimal operations
getcontext().prec = 102

def digital_sum(n):
    # Find the square root of n with Decimal precision
    root = Decimal(n).sqrt()
    # Convert to string, remove the decimal point, take the first 100 digits
    digits = str(root).replace('.', '')[:100]
    # Calculate the sum of these digits
    return sum(int(digit) for digit in digits)

# Calculate the total digital sum for the first 100 natural numbers
total_sum = sum(digital_sum(i) for i in range(1, 101) if not math.isqrt(i)**2 == i)

print(total_sum)