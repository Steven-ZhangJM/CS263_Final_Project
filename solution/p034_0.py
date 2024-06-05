e Python code to solve the problem:

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_curious_number(n):
    sum_factorial = 0
    for digit in str(n):
        sum_factorial += factorial(int(digit))
    return sum_factorial == n

sum_curious_numbers = 0
for i in range(3, 25401601): # upper limit calculated as 9! * 9
    if is_curious_number(i):
        sum_curious_numbers += i

print(sum_curious_numbers)