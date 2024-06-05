def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

total_sum = 0
for i in range(3, 254016): # 9! is the largest factorial that does not exceed 10^6
    digits = [int(d) for d in str(i)]
    digit_factorial_sum = sum([factorial(int(d)) for d in str(i)])
    if i == digit_factorial_sum:
        total_sum += i

print(total_sum)