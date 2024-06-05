```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_curious_number(num):
    sum_factorial = 0
    for digit in str(num):
        sum_factorial += factorial(int(digit))
    return sum_factorial == num

start_num = 3
curious_sum = 0

while start_num < 2540160: # maximum number of 9! + 8! + ... + 1!
    if is_curious_number(start_num):
        curious_sum += start_num
    start_num += 1

print(curious_sum)
```