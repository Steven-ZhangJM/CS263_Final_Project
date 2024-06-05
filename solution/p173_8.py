*
```python
def count_laminae(n):
    # Initialize a dictionary to store the number of laminae for each size
    laminae_count = {0: 1}  # base case: no tiles, one way to form no lamina

    for i in range(1, n + 1):
        new_laminae = 0
        for j in range(i):
            if (i - j) * (j + 1) <= n:
                new_laminae += laminae_count.get((n - (i - j) * (j + 1)), 0)
        laminae_count[i] = new_laminae

    return laminae_count.get(n, 0)

# Test the function
max_tiles = 1000000
print("Number of different square laminae that can be formed with", max_tiles, "tiles:", count_laminae(max_tiles))
```
**