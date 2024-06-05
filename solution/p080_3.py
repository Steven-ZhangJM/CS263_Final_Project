```Python
import math

def get_decimal_sum(n):
    sqrt_n = str(math.sqrt(n)).replace('.', '')
    return sum(int(digit) for digit in sqrt_n[:100])

total_sum = sum(get_decimal_sum(i) for i in range(2, 102))
print(total_sum)
```