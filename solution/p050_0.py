```python
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def consecutive_primes(k):
    primes = [2]
    num = 3
    while len(primes) < k:
        if check_prime(num):
            primes.append(num)
        num += 2
    total = sum(primes[-k:])
    if check_prime(total):
        return total
    return None

def find_longest_sum():
    max_len = 0
    longest_sum = 1
    for k in range(2, 1000000): # up to one million
        total = consecutive_primes(k)
        if total is not None and check_prime(total):
            if k > max_len:
                max_len = k
                longest_sum = total
    return longest_sum

print(find_longest_sum())
```