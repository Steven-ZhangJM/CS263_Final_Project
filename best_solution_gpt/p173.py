def count_laminae(tiles):
    count = 0
    for outer_side in range(3, tiles // 4 + 1):
        for inner_side in range(outer_side - 2, 0, -2):
            if outer_side * outer_side - inner_side * inner_side <= tiles:
                count += 1
            else:
                break
    return count

# Using up to one million tiles
print(count_laminae(1000000))