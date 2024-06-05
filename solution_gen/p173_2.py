

def num_permutations(size, n, r):
    """recursively recieve a laminar pattern of given size, take one tile from list, then create a pattern of same size by recursively calling the algortihm
    it will stop when all the tiles are used up. Then return the total number of possible patterns"""
    remainder = n - 1
    if r == 0: # base case
        return 1
    elif size > r: # recursion
        return 0
    else:
        for i in range(r):
            sum = num_permutations(size, n, r - 1)
            remainder -= 1
            sum += num_permutations(size, remainder, size)
        return sum

# given lamina pattern of a size n of size k has k(k-1) permutations
# sum of all permutation of each size k pattern is (k-1 * k) permutations each of size k-1

def n_permutations(n, k, r):
    """recursively compute the number of pattern of given size and pattern of given length
