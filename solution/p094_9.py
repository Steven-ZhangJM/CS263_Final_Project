```python
import math

def is_almost_equilateral(a, b, c):
    if abs(a-b) <= 1 and abs(b-c) <= 1 and abs(c-a) <= 1:
        return True
    else:
        return False

def calculate_perimeter(a, b, c):
    return a + b + c

def sum_of_perimeters(max_perimeter):
    total = 0
    for a in range(2, max_perimeter // 3):
        for b in range(a-1, a+3):
            c = abs(b-a)
            if (a**2 + b**2 - c**2) == 0 and ((a*b)/2)**.5 % 1 == 0:
                total += calculate_perimeter(a, b, c)
    return total

print(sum_of_perimeters(1000000000))
```