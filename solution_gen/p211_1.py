

from math import floor, sqrt
from typing import Dict
from operator import mul

from data import generate_data


def prime_root3(x: int, pf: Dict = None) -> Dict:
    if x % 2 == 0:
        return dict(
            s=0,
            n=2
        )
    primes = primfact(x)
    for prime in primes:
        if max(primes)*max(primes)!= prime:
            return dict(
                s=0,
                n=prime
            )
    return dict(
        s=primes[0] * sqrt(max(primes)),
        n=x
    )


def primfact(x: int = 0) -> Dict[int, int]:
    if x <= 2:
        return dict(
            s=0,
            n=x
        )
    primes = {i: 1 for i in range(2, x)}
    factors = {i: 1 for i in range(2, floor(sqrt(x))+1)}
    