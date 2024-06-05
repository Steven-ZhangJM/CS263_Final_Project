


from itertools import product

def how_many(in_tiles, max_size):
    possibilities = ([], 0)
    for tile_size in range(1, len(in_tiles)-1):
        for i, j, k in product(range(in_tiles[tile_size]), repeat=tile_size):
            j += 1
            k = len(in_tiles)-1-tile_size
            num_tiles = 1
            while i < len(in_tiles[i])-j and k-i == j:
                num_tiles += 1
                i += 1
            possibilities[1] += num_tiles
            if num_tiles == max_size and possibilities[0] == ([], 0):
                possibilities = (in_tiles[::-1], possibilities[1])
                break
    return possibilities[1]

def all_possibilities(in_tiles, max_size):
    possibilities = ([], 0)
    for i, tile_size in product(range(len(in_