def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum_of_n = 0
for n in range(1, 150000000):
    nums = [n**2 + i for i in [1, 3, 7, 9, 13, 27]]
    if all(is_prime(num) for num in nums):
        sum_of_n += n
print(sum_of_n)