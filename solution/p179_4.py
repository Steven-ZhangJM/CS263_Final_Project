def count_divisors(n):
    divisors = [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
    return (len(divisors) * 2 - ((n**0.5).is_integer()))

total_count = sum(count_divisors(i) for i in range(1, 10**7))

print(total_count)