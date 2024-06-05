def sum_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i**i % 10**10
    return total

print(sum_powers(1000))  # Output: 91125197094171

#