*
```
import math

def calculate_decimal_sum(n):
    decimal_sum = 0
    for i in range(100):
        decimal_digit = int(str(math.sqrt(n)).split('.')[1][i]) if i < len(str(math.sqrt(n)).split('.')[1]) else 9
        decimal_sum += decimal_digit
    return decimal_sum

total_decimal_sum = sum(calculate_decimal_sum(i) for i in range(2, 102))
print(total_decimal_sum)
```
**