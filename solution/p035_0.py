def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def circular_permutations(n):
    str_n = str(n)
    permutations = []
    for i in range(len(str_n)):
        permutations.append(int(str_n[i:] + str_n[:i]))
    return permutations

count = 0
for num in range(2, 1000000):
    if is_prime(num) and all(is_prime(permutation) for permutation in circular_permutations(num)):
        count += 1

print(count)