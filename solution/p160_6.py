def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def find_last_five_digits(n):
    fact = str(factorial(n))
    last_five_digits = int(fact[:-3].rstrip('0'))
    return last_five_digits

N = 10**12  # N = 1000000000000
print(find_last_five_digits(N))