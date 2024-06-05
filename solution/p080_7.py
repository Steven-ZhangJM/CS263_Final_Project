```Python
import math
total_sum = 0

for i in range(2,101):
    sqrt_i = str(math.sqrt(i)).replace('.','.')
    sqrt_i += '0'*(100-len(sqrt_i)) # Add zeros to make the length of decimal expansion 100 digits
    total_sum += sum(int(digit) for digit in sqrt_i[:100])

print(total_sum)
```