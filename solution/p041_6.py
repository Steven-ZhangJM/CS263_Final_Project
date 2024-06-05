pandigital_primes = generate_pandigital_primes(9)

max_prime = max(pandigital_primes)

print("The largest {}-digit pandigital prime that exists is {}".format(len(str(max_prime)), max_prime))