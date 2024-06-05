


def find_tiles(n, tiles):    # finds the number of possible ways tiling a row
        lst = []
        for i in range(1, n + 1):
            if (i % 3 == 0):
                if (i % 5 == 0):
                    lst.append(0.25 * i)
                else:
                    lst.append(0.75 * i)
            else:
                if (i % 5 == 0):
                    lst.append(0.1 * i)
                else:
                    lst.append(0)
        return lst[-1]

# This function converts a binary string to base 2    
def bin_to_base(binStr): 
    return int(binStr, 2) 

print(find_tiles(50, '100111100'))
              