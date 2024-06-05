def calculate_series(n):
    result = 0
    for i in range(1, n+1):
        result += i ** (i + 1)
    return result % 10000000000  # last 10 digits

n = 1000
print(calculate_series(n))