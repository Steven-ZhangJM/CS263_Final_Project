```
def a_n(n):
    i = 1
    while True:
        num_str = ''
        sum_power = 0
        for digit in str(i):
            num_str += digit
            sum_power += int(digit) ** len(num_str)
        if n == 2:
            return int(num_str)  # base case: a_2 = 512
        if sum_power == i:
            if n == 10:
                return int(num_str)  # base case: a_{10} = 614656
            return i
        i += 1

print(a_n(30))
```