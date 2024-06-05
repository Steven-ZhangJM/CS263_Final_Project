def sum_of_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i
    return total % (10**10)  # calculate the last 10 digits

print(sum_of_powers(1000))

#