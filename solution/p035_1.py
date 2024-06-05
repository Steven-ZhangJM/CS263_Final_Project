def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def circular_primes(n):
    count = 0
    num_str = str(n)
    for _ in range(len(num_str)):
        num_str = num_str[1:] + num_str[0]
        if is_prime(int(num_str)):
            count += 1
    return count

total_count = 0
for i in range(2, 1000000):
    if circular_primes(i) > 0:
        total_count += 1

print(total_count)