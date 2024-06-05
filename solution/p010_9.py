sum_of_primes = 0
for num in range(2, 2000000):  
    if is_prime(num):
        sum_of_primes += num

print(sum_of_primes)