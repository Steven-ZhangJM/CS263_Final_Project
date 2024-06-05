*
```
import math

def find_square():
    for i in range(1, 1000000):
        square = str(i * i)
        if len(square) == 9 and set(square) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            return i

print(find_square())
```
**