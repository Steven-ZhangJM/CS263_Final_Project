
import math

def createMatrix(tiles): #creates a 2D matrix of given tile number

    tiles = (int(tiles)/2) + 1
    matrix = [["" for _ in range(math.ceil(tiles))] for _ in range(math.ceil(tiles))] #initialises matrix as specified

    r_lim = math.ceil(tiles)-1 #r = lenght of matrix
    c_lim = math.ceil(tiles)-1 #c = width of matrix
    index = 1 #starts index at 1 because list has first value
    while r_lim >= 0: #will try to create the whole of the matrix (for a given width), if this fails, try one more time
        while c_lim >= 0:
            tiles -= 2 #adjusts value for tiles, used for the square holes that will be added
            tiles = int(tiles/2) +1
            if tiles > 1: #if there is leftover tiles to use
                matrix[r_lim][c_lim] = str(index) #adds to the