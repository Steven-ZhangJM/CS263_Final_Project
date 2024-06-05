

sum_even_fibonacci_numbers = 0
def fibonacci(n):
    a = 1
    b = 1
    for i in range(1, n):
        if i % 2 == 0:
           sum_even_fibonacci_numbers += i
        c = a + b
        a = b
        b = c
    return c
def solution(number):
    n = 1
    while fibonacci(n) < 4000000:
        n += 1
        if fibonacci(n) % 2 == 0:
            sum_even_fibonacci_numbers += fibonacci(1)
print(sum_even_fibonacci_numbers)