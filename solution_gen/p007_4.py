

import argparse
import math
from itertools import count
from utils import prime, n_th_prime, gen_primes


def main(args):
    assert n_th_prime(num=args.count, start_from=1, primes=gen_primes(max=args.num-1)) == args.num


# def main(args):
#     assert n_th_prime(num=args.count,
#                       start_from=args.start_from,
#                       primes=list(filter(prime, range(args.start_from, args.num)))) == args.count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List of prime numbers up to the specified count')
    parser.add_argument('--num', type=int, default=100, help='the number to find the nth prime')
    parser.add_argument('--count', type=int, default=10001, help='the number to find the nth prime')
    parser.add_argument('--start_from', type=int, default=1, help='first prime to check')
    args = parser.parse_args()
    main(args)
