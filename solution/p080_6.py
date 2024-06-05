```
import math

def digital_sum(n):
    return sum(int(digit) for digit in str(n).replace('.', ''))

total_sum = 0
for i in range(2, 102):  
    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i:  
        continue
    total_sum += digital_sum(math.modf(root)[0] * 10**100)[0]  

print(total_sum)
```