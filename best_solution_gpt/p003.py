# Python code to find the largest prime factor
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# The largest prime factor of the number 600851475143
print(largest_prime_factor(600851475143))