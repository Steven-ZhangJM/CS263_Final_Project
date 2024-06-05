e Python code to solve this problem:

```Python
def sum_of_spiral_diagonals(n):
    total_sum = 0
    num = 1
    direction = 'right'
    
    for i in range(4*n - 3):
        if direction == 'right':
            for j in range(i%2+1):
                print(num, end=' ')
                num += 1
            direction = 'down' if i%2==0 else 'up'
        elif direction == 'down':
            for j in range(n-1):
                print(num, end=' ')
                num += 1
            direction = 'left'
        elif direction == 'up':
            for j in range(n-1):
                print(num, end=' ')
                num += 1
            direction = 'right'
        else:
            for j in range(n-1):
                print(num, end=' ')
                num += 1
            direction = 'down'
        
        if i%2==0:
            print()
    
    for k in range(4*n - 3):
        if k%2==0 and k>0:
            total_sum += (n*(2*k+1)+1)**2 + (n*(2*k-1)+1)**2
        elif k%2!=0 and k>0:
            total_sum += (n*(2*k+1)+1)**2

    return total_sum

print(sum_of_spiral_diagonals(500))