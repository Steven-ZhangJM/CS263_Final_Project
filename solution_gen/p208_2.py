

from timeit import default_timer as timer


class Solution_1_solution_2(object):

    def findSolution(self, A=69, N=69):
        i = 0
        j = 0
        k = 0
        sum = 70

        while sum > 0:
            if sum == N:
                return i, j, k
            sum -= A
            if sum < N:
                j += 1
                sum += 1 + A
            elif sum > N:
                i += 1
                j = 0
                sum -= 1
                sum = sum - A + 1


if __name__ == "__main__":
    s = timer()
    res = Solution_1_solution_2().findSolution()
    e = timer()
    
    print('{:15,.6f} ms'.format((e - s) * 1000))
    print(res)




