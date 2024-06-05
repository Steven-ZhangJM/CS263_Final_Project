def fibonacci(n):
    fib_sequence = [1, 2]
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

even_sum = sum([num for num in fibonacci(4000000) if num % 2 == 0])

print(even_sum)