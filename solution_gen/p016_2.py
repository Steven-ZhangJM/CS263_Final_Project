

# Solution

def solution(num: int):
    """Return sum of digits of a number."""
    counter = 0
    binary_num = str(num)
    for character in binary_num:
        counter += int(character)
    return counter

# Tests

import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils import Utils
solution = Utils.solution


def test():
    assert(solution(1) == 1)
    assert(solution(2) == 2)
    assert(solution(3) == 3)
    assert(solution(1234567812345678) == 18)
    assert(solution(123456781324567813) == 21)
    assert(solution(1234567812345678) == 18)
    
if __name__ == '__main__':
    pytest.main()
