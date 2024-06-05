

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5) + 1
        while(left <= right):
            square_sum = left*left + right*right
            if square_sum > c:
                right -= 1
            elif square_sum == c:
                return True
            elif square_sum < c:
                left += 1
