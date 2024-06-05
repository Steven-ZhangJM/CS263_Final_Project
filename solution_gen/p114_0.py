

from decimal import Decimal, Clamped, Overflow

def divisor_generator(number):
    all_candidates = xrange(number + 1)
    for x in all_candidates:
        if x > 1:
            for y in xrange(2,Decimal(x).quotient(Decimal(x - 1)),1):
                if x%y == 0:
                    break
            else:
                yield x

def divisor_gen_upper_trick(number):
    all_candidates = xrange(number + 1)
    for x in all_candidates:
        if x > 1:
            yield x
            for y in all_candidates[all_candidates.index(x)+1:-1]:
                if x%y == 0:
                    break
            else:
                yield x
    
def block_length_generator(number):
    all_candidates = divisor_generator(number)
    for candidate in all_candidates:
        if Decimal(number)/Decimal(candidate) == Dec