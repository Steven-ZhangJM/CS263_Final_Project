

from math import sqrt

def solution(area):
    a = int(sqrt(area))

    return a * (a + 1) / 2


solution(5) # answer should be 15
solution(9) # answer should be 18
solution(1)  # answer should be 1
