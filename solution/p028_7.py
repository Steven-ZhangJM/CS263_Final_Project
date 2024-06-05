```Python
def get_spiral_sum(n):
    # Initialize sum to 0
    total_sum = 0
    
    # Create the spiral matrix
    spiral_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill up the first row
    num = 1
    for i in range(n):
        spiral_matrix[0][i] = num
        num += 1

    # Fill up each subsequent row (moving right and then down)
    num = 2
    for i in range(1, n):
        for j in range(i, n):
            spiral_matrix[i][j] = num
            num += 1
    
    # Fill up the last column (going back up)
    num = n * n - 1
    for i in range(n-2, -1, -1):
        spiral_matrix[i][n-1] = num
        num -= 1

    # Calculate sum of diagonals
    total_sum = 0
    for k in range(-n+1, n):
        if k == 0:
            continue
        for i in range(abs(k), min(n-abs(k), n)):
            total_sum += spiral_matrix[i][i+k]

    return total_sum

# Test the function
print(get_spiral_sum(1001))
```