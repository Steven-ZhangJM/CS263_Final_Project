```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def longest_sum_of_consecutive_primes(limit):
    max_length = 0
    max_prime = 0
    for i in range(2, limit):
        current_sum = 0
        length = 0
        while current_sum <= i and is_prime(i - current_sum + 1):
            if is_prime(current_sum):
                max_length = max(max_length, length)
                max_prime = i
            current_sum += (length + 1)
            length += 1
    return max_prime

print(longest_sum_of_consecutive_primes(1000000))
```