*
```python
import math

def find_square():
    for i in range(1, 1000):
        square = str(i ** 2)
        if len(square) == 9 and '0' in square:
            return i

result = find_square()
print(result)
```
**