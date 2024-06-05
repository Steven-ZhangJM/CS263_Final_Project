def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for n in range(1, 150000000):
    numbers = [n*n+1, n*n+3, n*n+7, n*n+9, n*n+13, n*n+27]
    if all(is_prime(num) for num in numbers):
        sum += n

print(sum)