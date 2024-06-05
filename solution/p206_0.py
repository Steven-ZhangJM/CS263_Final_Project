*
```
def find_square():
    for i in range(1, 100):
        square = str(i ** 2)
        if len(square) == 10 and set('0123456789') == set(square[:5]) and set('0123456789') == set(square[5:]):
            return i

print(find_square())
```
**