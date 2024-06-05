
from __future__ import annotations


# Code
def test_generator():
    divisor_list = list()
    for divisor in range(1, 1000):
        d = divisor
        for _ in range(d, divisor, -1):
            if not _%divisor:
                d += divisor

        if d > divisor:
            break
        
        if d not in divisor_list:
            divisor_list.append(d)

    for divisor in divisor_list:
        n = (1 + divisor) * divisor // 2
        print(divisor, n)


_start = time.perf_counter()
#_test_loop()
test_generator()
print(_end - _start)
