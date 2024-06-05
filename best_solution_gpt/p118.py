from itertools import permutations

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate all permutations of the digits 1 through 9
perms = [''.join(p) for p in permutations('123456789')]

# Function to split the string into all possible sets of prime numbers
def split_into_primes(s):
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                for l in range(k+1, len(s)):
                    num1 = int(s[:i])
                    num2 = int(s[i:j])
                    num3 = int(s[j:k])
                    num4 = int(s[k:l])
                    num5 = int(s[l:])
                    if is_prime(num1) and is_prime(num2) and is_prime(num3) and is_prime(num4) and is_prime(num5):
                        return True
    return False

# Count the number of distinct sets containing each of the digits one through nine exactly once that contain only prime elements
count = 0
for perm in perms:
    if split_into_primes(perm):
        count += 1

print(count)