

########################## SOLUTION #########################
def solution():
    '''Finds a solution to the problem
    using Binary Search'''

    primes_list = get_primes (10000) #create a list of primes

    while primes_list[0] * primes_list[1] < 50000 or primes_list[0] + primes_list[1] > 50000:
        primes_list = get_primes (1000)

    first = max(primes_list[2], primes_list[4])
    primes_list.remove(first)
    second = max(primes_list[2], primes_list[3],
                 primes_list[0])
    num = primes_list[2]

    #initial upper bound
    for prim in primes_list:
        first_to_second_prims = prim - num
        if first_to_second_prims in primes_list:
            break
        num = prim
    #initial lower bound
    num = primes_list[0]

#binary search function
    low = 0
    high = len (primes_list) - 1
    found = False
    solution_numbers = []
    while not found:

        divisible = False
        for prim in primes_list:
            if (prim - num) % primes_list[2] == 0:
                divisible = True
                break
            else:
                continue

        if divisible == True:
            num = num + primes_list[2]
            low = low + 1
            high = high - 1
        else:
            num = num + primes_list[high]
            found = True

    return (first, second, num)


########################## DIAGNOSTIC #########################

def diagnostic():
    '''Diagnostic for the solution of this problem.'''
    first,second,num= solution()
    print('First Number :', first, 'Second Number :',
          second, 'Number :', num)

########################## TEST/DETECT YOUR WRONG ANSWERS #########################

class Test:
    @staticmethod
    def test():
        import time

        start_time = time.time()

        (first, second, num) = solution()
        iterations = time.time() - start_time

        return ('Correct', 'Pass', iterations) if (first + second + num) % 2 else ('Correct', 'Fail', iterations)


########################## MAIN - RUN TEST/DEMO #########################

if __name__ == '__main__':
    Test.run_tests()
    solution()
