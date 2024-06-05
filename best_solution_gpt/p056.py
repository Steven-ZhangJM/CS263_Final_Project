# Python code to find the maximum digital sum of a^b for 0 < a, b < 100

def digital_sum(n):
    return sum(int(digit) for digit in str(n))

max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        max_sum = max(max_sum, digital_sum(a**b))

print(max_sum)