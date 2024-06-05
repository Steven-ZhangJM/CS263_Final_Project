def count_divisors(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                divisors += 1
            else:
                divisors += 2
    return divisors

def find_smallest_with_divisors(k):
    i = 1
    while True:
        n = i * (i + 1) // 2
        if count_divisors(n) >= k:
            return n % 500500507

print(find_smallest_with_divisors(2**500500))