```
import math

def sum_of_divisor_squares(n):
    return sum(i**2 for i in range(1, int(math.sqrt(n))+1) if n % i == 0)

total_sum = sum(n for n in range(1, 64000000+1) if math.isqrt(sum_of_divisor_squares(n))**2 == sum_of_divisor_squares(n))
print(total_sum)
```