
def sum_number(n):
    # return n * (n - 1) * factorial(n - 2) + factorial(n - 1) * (n - 1)
    # return factorial(n - 1) - factorial(n - 1)
    my = (factorial(n) // factorial(n - 1)) % 100

    print(my)
    return my


sum_number(100)

