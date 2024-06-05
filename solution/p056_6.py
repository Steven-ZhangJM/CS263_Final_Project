import itertools

def calculate_max_digital_sum():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            digital_sum = sum(int(digit) for digit in str(a**b))
            if digital_sum > max_sum:
                max_sum = digital_sum
    return max_sum

print(calculate_max_digital_sum())