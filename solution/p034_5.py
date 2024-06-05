def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def curious_sum(n):
    sum_factorials = 0
    for digit in str(n):
        sum_factorials += factorial(int(digit))
    return sum_factorials

total_sum = 0
for i in range(3, 254016): # 3 is the smallest possible value of a 6-digit number
    if i == curious_sum(i):
        total_sum += i
print(total_sum)