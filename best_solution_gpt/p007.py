def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    count = 0
    prime = 2
    while count < n:
        if is_prime(prime):
            count += 1
        if count < n:
            prime += 1
    return prime

# Find the 10001st prime number
nth_prime = find_nth_prime(10001)
print(nth_prime)