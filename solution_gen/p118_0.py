
import math

import networkx as nx
import pytest

from utils import is_prime, primes


@pytest.mark.skip(reason='will need to test on large graphs')
def test_count(count_primes=30000):
    """
    count_primes = # of primes to count
    Example: 8346792
    """
    import random

    digits = primes(10)  # all primes below 10^9
    graph = nx.Graph()

    n = 2  # for primality testing
    graph.add_node(1)
    digits = list(digits)  # ensure we are working on a copy here
    count = 0
    while count < count_primes:
        n += 1
        if n <= count_primes:
            print(f'adding node {n}')
            number = ''.join([random.choice(digits) for _ in range(7)])
            if is_prime(int(number)) == True:
                graph.add_node(n)
                for digit in number