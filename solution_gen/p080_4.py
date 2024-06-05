
from math import sqrt

N = 100

s = 0
for i in range(1, N + 1):
    if sqrt(i).is_integer() == False:
        ds = 0
        while sqrt(i).is_integer() == False:    
            s += sum(int(digit) for digit in str(ds))
            ds += 1

print(s)
