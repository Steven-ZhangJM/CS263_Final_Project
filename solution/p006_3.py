*
```
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

def square_sum(n):
    return (sum(range(1, n + 1))) ** 2

n = 100
difference = square_sum(n) - sum_of_squares(n)
print(difference)
```
**