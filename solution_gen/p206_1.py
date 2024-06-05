

class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = set([i*i for i in range(1, int(math.sqrt(n)) + 1)])
        
        q = 0
        m = 10
        while(q!= n):
            count = len(squares - {q + m**2})
            q += min(m, n-q)**2
            m += 1
        
        return count