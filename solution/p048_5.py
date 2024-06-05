def power(n, k):
    return pow(n, k) % 10**10

sum = sum([power(i, i) for i in range(1, 1001)])
print(sum)