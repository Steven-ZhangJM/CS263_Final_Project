def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum_counts(target):
    count = 0
    for a in range(2, target+1):
        for b in range(a, target+1):
            if is_prime(a) and is_prime(b) and a + b == target:
                count += 1
    return count

target = 2000000
max_count = 0
result = 0
for i in range(2, target):
    count = prime_sum_counts(i)
    if count > max_count:
        max_count = count
        result = i

print(result)

#