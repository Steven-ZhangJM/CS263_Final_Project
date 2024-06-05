

import math
import collections


def main(test="Y"):
    N = 1000000
    AAList = []
    AAList1 = []
    AAList2 = []

    for i in range(0, N):
        for k in range(0, N):
            for l in range(0, N):
                a = 4 * (i ** 2 + k ** 2)
                b = 4 * ((i ** 2 + k ** 2) * l)
                c = a + b
                if (k == l):
                    c = 3 * (i ** 2 + (k + 1) ** 2)
                print(i, k, l, c)
                if (a == b == c):
                    AAList.append(i)
                    AAList1.append(k)
                    AAList2.append(l)

    AAList1 = list(set(AAList1))
    AAList2 = list(set(AAList2))
    AAList1 = sorted(AAList1)
    AAList2 = sorted(A