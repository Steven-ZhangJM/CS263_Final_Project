def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def curious_number(num):
    sum = 0
    for digit in str(num):
        sum += factorial(int(digit))
    return sum

sum = 0
for i in range(3, 254016): # upper limit is arbitrary, but large enough to ensure we don't miss any numbers
    if curious_number(i) == i:
        sum += i

print(sum)