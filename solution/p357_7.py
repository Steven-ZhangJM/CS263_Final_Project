n = 100000000
sum_result = 0
for i in range(1, n+1):
    if all(is_prime(i + j) for j in divisors(i)):
        sum_result += i
print(sum_result)