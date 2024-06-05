max_sum_val = 0
for a in range(2, 100):
    for b in range(1, 100):
        digit_sum = max_sum(a, b)
        if digit_sum > max_sum_val:
            max_sum_val = digit_sum
print(max_sum_val)