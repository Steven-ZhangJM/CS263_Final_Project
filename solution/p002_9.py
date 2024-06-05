def fibonacci(n):
    fib_sequence = [1, 2]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

even_sum = sum(term for term in fibonacci(4000000) if term % 2 == 0)

print(even_sum)
#