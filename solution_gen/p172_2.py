

"""

***
I think the below is a bit of an easy, brute force solution because there are
just so many possible answers.

A few people will probably not answer the problem.

Also, these can be counted without any consideration and there are some
potential approaches that will not be as easy to generalise.

(See the above for example solutions.)

***

"""
# Solution 1
"""
The easiest to understand is to understand the idea.

Each number is either a digit or not a digit, so we can use any possible
permutation of the digits 1 up to 9.

To keep our equation simple, let's first define a product function we can
use for our approach:
"""

def product(digits):
    s = 1
    for i in range(len(digits)):
        s *= digits[i]
    return s

# To create our base case (or terminating condition), we can create an empty
# list and increment it each time.

def base_case(digits):
    nums_seen = []
    nums_seen.append(digits)