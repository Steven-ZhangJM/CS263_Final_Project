```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

max_consecutive = 0
max_sum = 0
for sum_of_primes in range(6, 1000000):  # start from 6 and go up to one million
    consecutive_count = 0
    current_sum = 0
    for primes in range(2, sum_of_primes + 1):
        if is_prime(primes):
            current_sum += primes
            consecutive_count += 1
            if current_sum == sum_of_primes:
                break
        else:
            current_sum = 0
            consecutive_count = 0
    if current_sum == sum_of_primes and consecutive_count > max_consecutive:
        max_consecutive = consecutive_count
        max_sum = sum_of_primes

print(max_sum)
```