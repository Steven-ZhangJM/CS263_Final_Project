
#%%
import math

from Practice1 import findPythagoreanTriples
from Practice1 import PerimeterConstantSolutions

def main():

    pythagorean_triples = findPythagoreanTriples(1000)
    list_of_solutions = PerimeterConstantSolutions(pythagorean_triples)
    print('The number of solutions', len(list_of_solutions))
    print(list_of_solutions)
    return(list_of_solutions)


if __name__ == "__main__":
    main()