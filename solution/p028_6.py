e python code to solve the problem:

```Python
def calculate_spiral_sum(n):
    total = 0
    num = 1
    direction = "right"
    
    for i in range(4*n - 3):
        if direction == "right":
            for j in range(n-2):
                if i % (2*(n-1)) == 0:
                    direction = "down"
                else:
                    total += num
                    num += 1
            direction = "down"
        elif direction == "down":
            for k in range(n-2):
                total += num
                num += 1
            direction = "left"
        elif direction == "left":
            for l in range(n-2):
                if i % (2*(n-1)) == 0:
                    direction = "up"
                else:
                    total += num
                    num += 1
            direction = "up"
        elif direction == "up":
            for m in range(n-2):
                total += num
                num += 1
            direction = "right"
    
    return total

n = 1001
print(calculate_spiral_sum(n))