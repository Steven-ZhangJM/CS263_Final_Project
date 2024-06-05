def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(n):
    total = 0
    for i in range(2, n):
        is_consecutive_prime = True
        for j in range(i**2+1, i**2+28, 2):  # only check even numbers as the odd ones are already checked
            if not is_prime(j):
                is_consecutive_prime = False
                break
        if is_consecutive_prime:
            total += i
    return total

print(sum_primes(150000000))