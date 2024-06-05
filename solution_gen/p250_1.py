

import itertools
from utilities import utils
from utilities import calc_nonempty_subset


def main2():
    """
    Prints a number of non-empty subsets and their sum divisible by 250
    """

    nonempty_subset = nonempty_subsets[:20]
    nonempty_subset.sort(key=lambda tup:  (tup[0], tup[1] * (tup[0] ** 3)))
    output = f'\n{nonempty_subset}\n* {calc_nonempty_subset(nonempty_subset, 250)}'
    utils.print_with_title(output)


if __name__ == '__main__':
    nonempty_subsets = tuple(itertools.chain(
        *[utils.calc_nonempty_subset(calc.nonempty_subset, 1000)
          for calc in calculation_array]))

    main2()
