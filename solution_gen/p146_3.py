
import itertools
from itertools import count, filterfalse

def main():
    """
    >>> solution = Solution()
    >>> count = 0
    >>> for x in itertools.count(2):
   ...     if solution.is_prime(x):
   ...         count += x
    >>> solution.sum_of_primes_upto(1000000) == count
    True
    """

class Solution(object):
    def sum_of_primes_upto(self, limit):
        is_prime = self.is_prime
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        s = 0
        for n in itertools.count(2):
            if not any([is_prime(n + p) for p in primes]):
                s += n
        return s         
    
    def is_prime(self, x):
        """ Checks if 2 numbers given are prime or not.
        @type x: int
        @param x: integer