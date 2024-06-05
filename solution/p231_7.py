```
def binomial_coefficient(n, k):
    result = 1
    for i in range(k):
        result *= (n - i)
    for i in range(2, k + 1):
        result //= i
    return result

n = 20000000
k = 15000000

result = binomial_coefficient(n, k)

print("The sum of the terms in the prime factorisation of", n, "choose", k, "is", sum(int(i) for i in str(result).split('')))
```