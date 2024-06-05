def is_n_power(n):
    for i in range(1, int(n**0.5) + 1):
        root = i ** (n // i)
        if round(root) ** n == n:
            return True
    return False


count = 0
for n in range(2, 11):
    for k in range(1, 10**(n-1)):
        if is_n_power(k * 10**n + k):
            count += 1

print(count)