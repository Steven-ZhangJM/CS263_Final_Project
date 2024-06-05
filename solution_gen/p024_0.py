
##
from collections import defaultdict
import time, math
###
time_start = time.time()

# # DONE:
import itertools as it
n = 10 ** 6
all_p = it.permutations(range(1, n+1))

def get_permutations(n):
    """Get n-th permutation (starting with 1)."""
    r = defaultdict(int)
    for i in range(n):
        r[i + 1] = r[n - i]  # 1, 2, 4, 5, 2, 3, 4
    for i, x in enumerate(sorted(r)):
        yield x * n + r[x]  # i+1

print(get_permutations(n))


##
# def pr_to_list(a):
#     arr = (str(i)) for i in a
#     return ''.join(arr)

def pr_to_list(a):
    arr = []
    for i in a:
        arr.append(str(i))
    return arr

num = pr_to_list(get_permutations(4))
print(num)

time_end = time.time()
print("time_end - time_start:", time_end - time_start)
