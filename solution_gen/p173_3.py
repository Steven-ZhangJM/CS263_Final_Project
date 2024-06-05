

"""
Solution

    A square lamina is a square outline with a square hole so that the shape possesses vertical and horizontal symmetry. As an example: using exactly thirty-two square tiles we can form two different square laminae: The outer square has an internal hole, the inner square is a square and thus has four sides parallel to each other. Therefore, thirty-two square tiles give a total of four square laminae, forty-one.
"""
from math import sqrt, ceil

# Calculates the square lamina count
#
# @param count   Square lamina count (integer)
# @return        The number of possible square laminae for a given number of tiles
def square_lamina_count(count):

    if count == 0:
        return 0

    # A square lamina is composed of four square tiles, so it has the maximum count possible
    counts = sqrt(count)
    max_per_square_lamina = ceil(counts)
    
    # An inner square has four sides parallel to each other, hence two square laminae
    return max_per_square_lamina * max_