Python code to solve the problem:

```
def find_x():
    x = 1
    while True:
        digits = str(x)
        for i in range(2, 7):
            if sorted(str(i*x)) != sorted(digits):
                break
        else:
            return x
        x += 1

print(find_x())