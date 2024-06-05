

from math import sqrt

def check(n):
    i = 2
    sq = int(sqrt(n)) + 1
    prime = [True for _ in range(n + 1)]
    prime[1] = False

    while i <= sq:
        if prime[i] == True:
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    
    is_prime = False
    for i in range(2, n):
        if prime[i] == True:
            is_prime = True

    return is_prime

def get_solution():
    limit = 3000000
    solutions = []
    for i in range(limit):
        if check(i + 1) == True:
            solutions.append(i + 1)

    return solutions

def main():
    start_time = time.time()
    sols = get_solution()
    end_time = time.time()
    print("Solution: {} \nRuntime (in seconds): {}".format(sols[0], end_time - start_time))

main()
