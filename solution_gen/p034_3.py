


def sum_factorial(num):
    fact = 1
    sum = 0

    for i in range(1, num + 1):
        fact *= i
    return fact


print(sum_factorial(1000))
