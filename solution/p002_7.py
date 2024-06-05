*
```
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b

even_sum = 0
n = 4000000
a, b = 1, 2
while b <= n:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print(even_sum)
```
**