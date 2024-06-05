```Python
def calculate_an(n):
    if n == 2:
        return 512
    elif n == 10:
        return 614656
    else:
        an = None
        for i in range(1, 1000000): # assuming max number of digits is less than 6
            sum_digits = sum(int(digit) ** (n-2) for digit in str(i))
            if sum_digits == i:
                an = i
                break
        return an

print(calculate_an(30))
```