```
def find_smallest_multiple(n):
    k = 1
    while True:
        if all(i % k == 0 for i in range(1, n + 1)):
            return k
        k += 1

print(find_smallest_multiple(20))
```