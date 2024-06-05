
# --------------
## SOLUTION
def solution(n):
    '''
    input: n = 10,000 - int
    output: 10 -> integer 
    problem: calculate 10th prime number as the number in the sequence with 2,3,5,7,11,13
    '''
    from math import sqrt

    n_sqrt = int(sqrt(n))

    # initialize the list
    prime = [True]*n_sqrt
    i = 1

    # create numbers with bool array
    while i < n_sqrt:
        if prime[i]:
            # update the next multiples with a
            for k in range(i*2, n, i):
                prime[k] = False
        i += 1

    # return the list of numbers with bool array (2 - 9) in descending order
    return len([prime1 for prime1 in prime if prime1 == True])
    

print(solution(10_001))
