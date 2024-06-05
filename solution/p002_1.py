def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        fib = [1, 2]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

fib_sequence = fibonacci(91)
even_sum = sum(i for i in fib_sequence if i % 2 == 0)

print(even_sum)