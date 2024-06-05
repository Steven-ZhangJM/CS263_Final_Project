
"""
>>> find_sum_of_all_n_that_sums_to_a_perfect_square(10)
330
"""

def find_sum_of_all_n_that_sums_to_a_perfect_square(max):
    def is_perfect_square(n):
        return int(np.sqrt(n))**2 == n

    if not is_perfect_square(max):
        return 0

    return sum([i**2 for i in range(1, max) if is_perfect_square(i ** 2)])

print(find_sum_of_all_n_that_sums_to_a_perfect_square(64*1000))

"""
Problem 2
Suppose we have a dictionary, $d$, which we will sort. For all of the items, $d$, and each attribute, $i$,
find the number of times $d[i][0]$ occurs.
Write a function that takes in a dictionary $d$, then you will create a list $A$, of tuples. The tuples
should have their final $1$ element being