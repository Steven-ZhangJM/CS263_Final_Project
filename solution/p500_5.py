import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
            if i * i == n:
                count -= 1
    return count

n = 120
print(count_divisors(n))

def find_smallest_number_with_k_divisors(k):
    count = 0
    num = 1
    while True:
        div_count = count_divisors(num)
        if div_count == k:
            break
        num += 1
    return num % 500500507

print(find_smallest_number_with_k_divisors(2**500500))