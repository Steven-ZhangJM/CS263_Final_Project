def fibonacci(n):
    fib_sequence = [1, 2]
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

even_sum = 0

for num in fibonacci(4000000):
    if num % 2 == 0:
        even_sum += num
    if num > 4000000:
        break

print(even_sum)