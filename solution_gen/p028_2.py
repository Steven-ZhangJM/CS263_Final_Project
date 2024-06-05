

class Solution(object):
    def sum_spiral_diags(self, matrix, offset, diags, start, n):
        # If we have reached the bottom right corner, return
        if start == n:
            return 0    
        # If we have reached the outer right corner, sum both diags
        if start < offset:
            return (matrix[start][start] + diags[start+offset])
        # No more right and it's bottom spot, increment diags
        if start == offset:
            diags += matrix[start][start]
            start += 1 
            return self.sum_spiral_diags(matrix, offset, diags, start, n)
        # If it's inner spot and it's the outer spot, decrement diags, add next spot's square and return
        if start == offset-1+start and start == n-offset:
            return diags + matrix[start][start] + ((matrix[start][start+n-offset] + matrix[start+n-offset][start-1] + matrix[start+n-offset][start]) * (n // 2))
        else:
            return self.sum_spiral_diags(matrix, offset, diags, start+1, n) + ((matrix[start][start+offset] + matrix[start+offset][start+n-1] + matrix[start+n-1][start]) * (offset // 2))

import poc_simpletest
import random

sol = Solution()

test_case_1 = [[1, 2, 3, 4, 5], \
              [6, 7, 8, 9, 10], \
              [11, 12, 13, 14, 15], \
              [16, 17, 18, 19, 20], \
              [21, 22, 23, 24, 25]]

test_case_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# uncomment this when working on the solution
# poc_simpletest.run_test_cases(sol.sum_spiral_diags, 
#                               [test_case_1, test_case_2])

test_solutions = [[101, 103, 107, 113, 113, 121, 123, 141],
                  [100, 101, 1000001, 9990101, 9990999, 0],
                  [1,2,3,4,5,6,7,8,9,10,11,12]]

def verify_results(result, expected):
    if result!= expected:
        print("fail")
        print("result = {}".format(result))
        print("expected = {}".format(expected))
        print("Test case failed.")
    else:
        print("pass")

# uncomment when ready to run solver
verify_results(sol.sum_spiral_diags(test_case_1, 5, test_solutions[0], 0, 3), 10001)
verify_results(sol.sum_spiral_diags(test_case_2, 3, test_solutions[1], 0, 5), 0)

def test_spiral_diag_sum_2(n, m):
    result = sol.sum_spiral_diags([[random.randint(1, m) for i in range(n)] for x in range(n)], m+1,[random.randint(1, m) for x in range(n)], 0, n)
    expected = sum([sum([row*column for row, column in zip(matrix, range(1, n+1))]) for matrix in matrices])
    print("Test Case 2")
    print("n = {}".format(n))
    print("m = {}".format(m))
    verify_results(result, expected)

def test_spiral_diag_sum_3(n, m):
    result = sol.sum_spiral_diags([[random.randint(1, m) for x in range(n)] for y in range(n)], n+1,[random.randint(1, m) for x in range(n)], n+1,m)
    expected = sum([sum([row*column for row, column in zip(matrix, range(1, n+1))]) for matrix in matrices])
    print("Test Case 3")
    print("n = {}".format(n))
    print("m = {}".format(m))
    verify_results(result, expected)

def test_spiral_diag_sum_4(n, m):
    result = sol.sum_spiral_diags([[random.randint(1, m) for x in range(n)] for y in range(n)], 1,[random.randint(1, m) for x in range(n)], n, n)
    expected = 0
    print("Test Case 4")
    print("n = {}".format(m))
    verify_results(result, expected)

# uncomment this when ready to run solver
# test_spiral_diag_sum_1(1, 1)
# test_spiral_diag_sum_2(1, 1)
# test_spiral_diag_sum_2(2, 2)
# test_spiral_diag_sum_3(2, 5)
# test_spiral_diag_sum_4(2, 2)


