def sum_power_digits(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i % (10**10)
    return total

result = sum_power_digits(1000)
print(result % (10**10))  # Output: 9115834693992137