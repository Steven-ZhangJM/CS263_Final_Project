def find_max_solutions():
    max_count = 0
    max_p = 0
    for p in range(1, 1001):
        count = 0
        for a in range(1, int(p/2) + 1):
            b_squared = p**2 - 4*a*(p-a)
            if b_squared >= 0:
                b = int((b_squared)**0.5)
                c = p - a - b
                if a <= b <= c and a*b*c % 8 == 0: 
                    count += 1
        if count > max_count:
            max_count = count
            max_p = p
    return max_p

print(find_max_solutions())
#