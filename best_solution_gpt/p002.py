# Python code to find the sum of even-valued terms in the Fibonacci sequence not exceeding four million
a, b = 1, 2
total = 0
while b <= 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
print(total)