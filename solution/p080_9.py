```
import math
from decimal import Decimal, getcontext

def calculate_decimal_sum(n):
    getcontext().prec = 101  # Set the precision to 101 decimal places
    decimal_sqrt = Decimal(str(math.sqrt(n))).normalize()
    return sum(int(digit) for digit in str(decimal_sqrt)[2:102])

total_sum = sum(calculate_decimal_sum(i) for i in range(2, 101))
print(total_sum)
```