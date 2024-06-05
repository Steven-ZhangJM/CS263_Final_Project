


## TLE
import math

class Solution:
    def solve(self):
        print(math.floor(math.sqrt(10**7)) / 2)


s = Solution()
s.solve()

## TLE
import math

class Solution:
    def solve(self):
        nums = None
        num_max = 10**7
        result = 0
        for i in range(1, num_max):
            divisors = 1
            divisor = 2
            while divisor * num_max / i < i:
                divisors += 1
                divisor += i

            if all(map(lambda x: i % x == 0, range(2, int(math.sqrt(num_max))) + range(2, int(math.sqrt(i) + 1)))) and all(map(lambda x: num_max / i % x, range(2, int(math.sqrt(num_max))) + range(2, int(math.sqrt(i) + 1)))):
                print(i)
                result += i