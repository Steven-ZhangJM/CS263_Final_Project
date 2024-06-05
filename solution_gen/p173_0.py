

from functools import reduce
def tiles_sum(tiles):
    return reduce(lambda a, b: tiles[a] + tiles[b], range(len(tiles)-1), 0)

#using a dynamic programming approach, only O(NM)


tiles = map(int, open('day20.txt').read().split('\n'))

s1 = tiles_sum(set(tiles))
tiles.append(0)
s2 = tiles_sum(set(sorted(tiles)))

print(s2 - s1)

#using a dynamic programming approach - O(N^2)