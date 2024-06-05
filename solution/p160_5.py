*
```
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def last_five_digits factorial(n):
    f = factorial(n)
    s = str(f)[::-1].find('0')
    return int(str(f)[::-1][:s])

N = 1000000000
print(last_five_digits(N))
```
**