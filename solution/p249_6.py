Python code to solve this problem:

```Python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_subsets(prime_set, target_sum):
    """Count the number of subsets with a given sum."""
    count = [0] * (target_sum + 1)
    for num in prime_set:
        for i in range(target_sum, num - 1, -1):
            if i >= num:
                count[i] += count[i - num]
    return count[target_sum]

# Generate the set of prime numbers less than 5000
prime_set = [num for num in range(2, 5000) if is_prime(num)]

# Find the number of subsets with a prime sum
target_sum = 1
while True:
    if is_prime(sum(subset)) and count_subsets(prime_set, target_sum):
        print(f"The number of subsets is {count_subsets(prime_set, target_sum)}")
        break
    target_sum += 1