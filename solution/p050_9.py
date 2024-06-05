def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def consecutive_primes_sum(length):
    primes = []
    num = 2
    while len(primes) < length:
        if is_prime(num):
            primes.append(num)
        num += 1
    sum_of_consecutive_primes = sum(primes[:])
    return sum_of_consecutive_primes

max_length = 0
result = 0
for i in range(2, 1000000):  # iterate up to one million
    if is_prime(i):
        for length in range(1, i + 1):
            if i == consecutive_primes_sum(length):
                max_length = length
                result = i
                break
        if max_length > 0:
            break

print(result)  # print the result
#