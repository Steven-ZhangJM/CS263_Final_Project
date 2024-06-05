```
def solve_p():
    count = [0] * (1001)
    for a in range(1, 1001):
        for b in range(a, 1001):
            c_squared = a**2 + b**2
            if c_squared > 4*b*a and c_squared <= (2*b*a)**2:
                p = a + b + int(c_squared**0.5)
                count[p] += 1
    return max(range(1, 1001), key=lambda x:count[x])

p_max = solve_p()
print(p_max)