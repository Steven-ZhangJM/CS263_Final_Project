

# Using recursion
class Solution:
    def solveProblem(self):
        subsets = {0: 0}
        def solve(subset, curSum):
            for i in range(len(input)):
                s = input[i]
                if s <= 1:
                    continue
                if curSum % s == 0:
                    subset += 1
                elif (curSum//s) in subset.keys():
                    subset[curSum//s] += 1
                    
        for i in range(len(input)):
            solve(subsets, input[i])
        print(subsets)
        return sorted(subsets.keys() )[-1]
        
"""
Runtime: 28 ms, faster than 65.53% of Python3 online submissions for Count Numbers with Unique Digits.
Memory Usage: 14.2 MB, less than 43.74% of Python3 online submissions for Count Numbers with Unique Digits.
"""

# Using math
class Solution:
    def solveProblem(self):
        nums = collections.defaultdict(int)
        for ch in str(n