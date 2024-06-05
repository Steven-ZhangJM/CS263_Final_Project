def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

sum = 0
for i in range(3, 2540160): # Upper limit is arbitrary, but it's a very large number
    digit_sum = sum(int(digit) * factorial(int(digit)) for digit in str(i))
    if i == digit_sum:
        sum += i

print(sum)