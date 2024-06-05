max_sum = 0
for x in range(1, 10001):  # Start from 1 and go up to 10,000
    for y in range(x - 10000, x):  # Make sure y < x
        for z in range(y - 10000, y):
            if is_perfect_square(x + y) and \
               is_perfect_square(x - y) and \
               is_perfect_square(x + z) and \
               is_perfect_square(x - z) and \
               is_perfect_square(y + z) and \
               is_perfect_square(y - z):
                max_sum = x + y + z
                print(max_sum)
                break  # Stop looking for more solutions since we found the smallest one
        if max_sum > 0:
            break  # Stop looking for more solutions since we found the smallest one
    if max_sum > 0:
        break  # Stop looking for more solutions since we found the smallest one

print(max_sum)