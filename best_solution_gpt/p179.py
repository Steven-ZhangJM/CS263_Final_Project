def count_same_divisors(limit):
    def num_divisors(n):
        divisors = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors += 2 if i * i != n else 1
        return divisors

    count = 0
    prev_divisors = num_divisors(2)
    for n in range(3, limit):
        current_divisors = num_divisors(n)
        if current_divisors == prev_divisors:
            count += 1
        prev_divisors = num_divisors(n + 1)
    return count

# Set the limit as 10^7
limit = 10**7
print(count_same_divisors(limit))