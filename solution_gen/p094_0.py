

import math

def main():
    t1 = 0
    t2 = 0
    t3 = 0
    perim = 0
    triangles = []
    for a in range(5,1000):
        for b in range(a,1000):
            c = 1000-a-b
            if math.sqrt(a**2 + b**2 ) == 1:
                if math.sqrt(b**2 + c**2 ) == 1:
                    if math.sqrt(b**2 + a**2 ) == 1:
                        if math.sqrt(c**2 + a**2 ) == 1:
                            if math.sqrt(c**2 + b**2 ) == 1:
                                t1 = a*b
                                t2 = a*a
                                t3 = b*b
                        if t1 + t2 < b*c or t1+t2 > b*c:
                            if t2 + t1 < a*c or t2+t1 > a*c:
                                if t3 + t1 < b*c or t3+t1 > b*