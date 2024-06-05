def sum_diagonals(n):
    sum = 0
    for k in range(1, n+1):
        i = max(k-2*(k-1), 0)
        j = min(k, n-k+1)
        for _ in range(j-i+1):
            sum += (i+_)*((n+1)-j-_)+1
    return sum

print(sum_diagonals(1001))