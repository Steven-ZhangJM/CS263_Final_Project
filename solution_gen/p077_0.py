

from numpy import array, arange, mean
from numpy.random import randint

from primesieve import factorint

limit = 5000
primes = factorint(limit).keys()

primes.pop(0)

primes = array(sorted(primes))

"""
We will try to try to write ten as the sum of primes in the first five different ways.
If one of those ways succeed we don't need any primes in the following ones.
That way we can write (a+b)∗(a+b)∗(a+c)∗(b+c)∗(b+c)∗(c+d)=1000×1000×1000×1000×1000∗1000≡100,500×475≡625.
As we know that 10 = 5∗5∗5∗5×5∗15≡20, we know that we can write ten by:
(10–2)∗(10–2)∗(10–2)∗(10–2)×2∗(10–2)∗(10–2)∗(10–2)∗(10–2)∗(10–2)∗(10–2)=1000×1000×1000×10000≡100,500×475≡625.
10 = 2∗2∗2∗2∗2∗2∗4×2∗2∗2∗8, that implies that we can not write ten by: (10–2)×(10–2)∗(10–2)×(10–2)∗(10–2)×(10–2),
which is what we want. That's why we stop trying any further primes.
That's why we need only five primes.

This is not the "easy" question to answer.
But we have an interview and we are going to write our answers as an array of primes.
Every prime element in the array corresponds to one attempt to write ten by one of the solutions found.
If we have an array of five primes, then is the result at least a sum of these primes for a few, and also
a single value. If a primes solution doesn't give a sum, the array is not feasible.

We need five primes to put an "easy" question:
What is the first combination of primes that can be summed by 10?

We consider the first five primes as follows:
4 = 2∗2∗2∗2∗2∗2∗2∗2∗2∗8, the next two are 4∗4×4∗4×4∗4 and 4∗4×4∗4×4∗4∗4 = 2⋅2∗2∗2∗2∗4.
3 = 6∗6×3∗6∗3×3∗3∗6, the next four are 2∗2∗2∗2∗2∗2∗3∗2∗2∗2x3∗3∗6
2 = 12∗12∗12∗12∗12∗12∗12∗12∗12∗12∗12∗12x4, the next five are 2∗2∗2⋅2∗2∗2∗2∗2∗2∗2∗2x2∗2x4.
The next five can be seen as two primes summing to 12.

"""
# let's write 10 for the first attempt
# that's possible with the 5 primes in the first five attempts
primes_to_combine = primes[:5]
combined = []

# we don't need to check very large numbers
a = int(primes[5]) + 1

# we don't need to check very large numbers
b = int(primes[5]) + 1

# we don't need to check very large numbers
c = int(primes[5]) + 1

# we don't need to check very large numbers
d = int(primes[5]) + 1

while len(combined) < 2000:
    combined.append(a)
    b += 1
    while b in combined or b % 1000 == 0:
        b += 1
        if b == a + 1:
            for c_prime in primes_to_combine:
                while b < c_prime and b < 99999999999999:
                    combined.append(b)
                    d += 1
                    while d in combined or d % 100000 == 0:
                        d += 1

                break

            break

    a += 1

print(mean(combined))

