def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_next_power(a, n):
    i = 1
    while True:
        power_sum = sum_of_digits(a ** i)
        if power_sum == a and i > n:
            return a ** (i - 1)
        i += 1

a30 = find_next_power(512, 29)
print(a30)