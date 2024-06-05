```
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_curious(num):
    sum_factorials = 0
    for digit in str(num):
        sum_factorials += factorial(int(digit))
    return sum_factorials == num

sum_curious_numbers = 0
for i in range(3, 2540160):  # upper limit: 9! = 362880
    if is_curious(i):
        sum_curious_numbers += i

print(sum_curious_numbers)
```