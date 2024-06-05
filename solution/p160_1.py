```Python
import math

def last_five_digits(n):
    result = 0
    for i in range(5, int(math.log10(n))+1):
        if n // (10**i) > 0:
            result += i * (n // (10**i))
            break
    else:
        result = n % 100000
    return result

print(last_five_digits(1000000000000))
```