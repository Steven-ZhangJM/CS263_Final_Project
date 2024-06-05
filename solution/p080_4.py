```
import math

def sum_digits(n):
    return sum(int(digit) for digit in str(n).replace('.', ''))

total_sum = 0
for i in range(2, 102):  # Start from 2 and end at 101
    if not math.isqrt(i).is_integer:  # Check if the square root is irrational
        total_sum += sum_digits(str(math.sqrt(i)).replace('0.', ''))  # Calculate the digital sum

print(total_sum)
```