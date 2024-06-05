
import math

a = 1
z = 0
for b in range(100):
    z = 0
    for c in range(100):
        z += int(str(a**b)[0])
    if a**b > a**100:
        break
    a += 1
print(z)
