def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def f(N):
    fac = str(factorial(N))
    trailing_zeroes = len(str(N)) - len(fac) + 5
    return int(fac[:-trailing_zeroes])

N = 1000000000
print(f(N))