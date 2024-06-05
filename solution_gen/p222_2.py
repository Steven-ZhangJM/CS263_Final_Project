

import math

import numpy as np

def solve(length, radii):
    p = [3, 1]
    # p[0]=p0=length/np.log(p0=np.log(20)
    # p[1]=p1=2*np.log(r1_max=2)
    r = 3.5 / 2
    pi = np.pi
    d = np.sqrt(2 * r ** 2 - radii[1] ** 2)
    n = int(1 / 3 * r)
    k = int(np.pi / 2 - pi / n)
    s0 = d * math.log(radii[2] / radii[1])
    s1 = radii[1] * d
    s2 = radii[2] * d

    # check if p[0] and s > 2 is a valid choice
    # s = s1 + s2
    # s2 and s1 are radii, so s is always positive
    # s2 cannot be more than twice as long as s1, so s2 <= s