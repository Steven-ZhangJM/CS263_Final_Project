```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(target, current_sum=0, primes_used=[]):
    if current_sum > target:
        return None
    if current_sum == target:
        return len(primes_used)
    for i in range(2, target):
        if is_prime(i):
            new_sum = current_sum + i
            new_primes_used = primes_used + [i]
            result = sum_of_primes(target, new_sum, new_primes_used)
            if result is not None:
                return result
    return None

start_target = 2
while True:
    result = sum_of_primes(start_target)
    if result > 5000:
        print(start_target)
        break
    start_target += 1
```