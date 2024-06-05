*
```
def max_digital_sum(a_max=99, b_max=99):
    max_sum = 0
    for a in range(1, a_max+1):
        for b in range(1, b_max+1):
            n = a ** b
            digit_sum = sum(int(digit) for digit in str(n))
            if digit_sum > max_sum:
                max_sum = digit_sum
    return max_sum

print(max_digital_sum())
```
**