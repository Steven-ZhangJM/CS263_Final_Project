e python code to solve this problem:

```
import math

def is_perfect_square(n):
    root = math.isqrt(n)
    return root*root == n

def solve():
    max_x = 0
    for x in range(1, 10000): # you can adjust this range as per your requirement
        for y in range(x-1, 0, -1): # start from x-1 and go down to 1
            z = (x-y)//2 # calculate z based on the given conditions
            if y > z and is_perfect_square(x+y) and is_perfect_square(x-y) and \
               is_perfect_square(x+z) and is_perfect_square(x-z) and \
               is_perfect_square(y+z) and is_perfect_square(y-z):
                return x + y + z

    return None

print("Smallest sum: ", solve())