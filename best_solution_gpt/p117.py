def count_ways(length, tile_sizes):
    ways = [1] * (length + 1)
    for size in tile_sizes:
        for i in range(size, length + 1):
            ways[i] += ways[i - size]
    return ways[length] - len(tile_sizes)

# Tile sizes for red, green, and blue tiles
tile_sizes = [2, 3, 4]
length = 50
print(count_ways(length, tile_sizes))