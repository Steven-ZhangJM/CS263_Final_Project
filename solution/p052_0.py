Python code to solve the problem:

```
def find_x():
    x = 1
    while True:
        s = str(x)
        for i in range(2, 7):
            if sorted(s) != sorted(str(i*x)):
                break
        else:
            return x
        x += 1

print(find_x())