

import math



def solution2(l):

    for a,b,c in l:
        if a > b and a > c and b > c:
            yield a**2 + b**2 + c**2


import heapq

def solution1(l):

    for (a,b,c) in l:
        for (x,y,z) in l:
            for y in range(x**2, (x**2) + (x**2) + 1, y):
                yield y**2 + x**2 + (z)**2
        # for (s,t,w) in d:
        #     for d in w:
        #         yield s**2 + t**2 + d**2


    #     def solution2(l):



class Solution:
    def numSquares(self, n):
        a= set([n])
        while len(a) > 0:
            for num in a:
                if num <= 1:
                    continue
                for i in range(int(num**0.5) +