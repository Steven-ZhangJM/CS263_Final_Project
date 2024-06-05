x = y = z = 1
while True:
    if (is_perfect_square(x + y) and 
        is_perfect_square(x - y) and 
        is_perfect_square(x + z) and 
        is_perfect_square(x - z) and 
        is_perfect_square(y + z) and 
        is_perfect_square(y - z)):
        break
    x += 1