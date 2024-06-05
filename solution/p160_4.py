import math

def f(N):
    factorials = []
    for i in range(1, N+1):
        factorial = math.factorial(i)
        factorials.append(factorial)

    last_five_digits = 0
    for factorial in factorials:
        while len(str(factorial)) > 5:
            factorial //= 10
        last_five_digits += factorial

    return last_five_digits

N = 1_000_000_000_000
print(f(N))