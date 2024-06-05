total = 0
for n in range(1, 150000001):
    nums = [n*n+1, n*n+3, n*n+7, n*n+9, n*n+13, n*n+27]
    if all(map(is_prime, nums)):
        total += n
        print(total)
        break