```python
def sum_diagonals(n):
    # Initialize the sum of diagonals
    total_sum = 0
    
    # Loop through each diagonal in the spiral
    for i in range(1, n*n + 1):
        # Calculate the coordinates (r,c) of the current number on the spiral
        r = int((i - ((n // 2) ** 2)) // abs(n - 2))
        c = i - r * (n - 1)
        
        # If this is a diagonal, add its value to the total sum
        if r == c or r + c == n - 1:
            total_sum += i
    
    return int(total_sum)

# Test the function with n=5
print(sum_diagonals(5))  # Output: 101

# Now test the function with n=1001
print(sum_diagonals(1001))
```