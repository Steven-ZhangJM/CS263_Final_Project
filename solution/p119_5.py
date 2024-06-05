def sum_digits_power(n):
    return sum(int(digit) ** len(str(n)) for digit in str(n))

def find_an(n):
    i = 1
    while True:
        if sum_digits_power(i) == n:
            return i
        i += 1

print(find_an(614656))
print(find_an(512))