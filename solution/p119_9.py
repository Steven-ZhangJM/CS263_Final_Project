e Python code to solve the problem:

```
def find_an(n):
    count = 1
    while True:
        if sum(int(digit) ** (n - 1) for digit in str(count)) == count:
            return count
        count += 1

print(find_an(30))