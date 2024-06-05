from sympy import primerange, isprime

# Generate the set of prime numbers less than 5000
primes = list(primerange(2, 5000))

# Function to calculate the power set of a list
def power_set(lst):
    result = [[]]
    for i in lst:
        new_subset = [subset + [i] for subset in result]
        result.extend(new_subset)
    return result

# Function to check if the sum of elements in a subset is prime
def is_prime_sum(subset):
    return isprime(sum(subset))

# Calculate the power set of primes
pset = power_set(primes)

# Count the number of subsets whose sum of elements is a prime number
prime_sum_subsets_count = sum(1 for subset in pset if is_prime_sum(subset))

# Output the rightmost 16 digits of the count
print(str(prime_sum_subsets_count)[-16:])