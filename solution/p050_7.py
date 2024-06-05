def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_consecutive_primes(start, end, max_len):
    max_prime_sum = None
    max_len_found = 0
    for len_ in range(2, min(end - start + 1, max_len) + 1):
        for i in range(len_):
            prime_sum = 0
            for j in range(i, i + len_):
                if is_prime(start + j):
                    prime_sum += start + j
            if prime_sum > 1000000:  # stop when sum exceeds 1 million
                break
            if is_prime(prime_sum):
                max_prime_sum = prime_sum
                max_len_found = len_
    return max_prime_sum, max_len_found

start = 2
end = 1000000
max_len = 50
prime_sum, max_len_found = sum_consecutive_primes(start, end, max_len)
print(f"The longest sum of consecutive primes below one-million that adds to a prime is {prime_sum} with {max_len_found} terms.")