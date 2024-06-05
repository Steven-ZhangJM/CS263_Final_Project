def find_an(n):
    i = 1
    while True:
        digits_sum = sum(int(digit) ** (i+3) for digit in str(i))
        if i == n:
            return digits_sum
        elif i > n:
            return None

print(find_an(30))