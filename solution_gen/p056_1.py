

def sumDigits_a_b_1(a, b):
    """
    Time: O(1)
    Space: O(1)
    """
    sum = a**b
    while a > 0:
        sum += a%10
        a = a//10
    return sum

def sumDigits_a_b_2(a, b):
    """
    Time: O(1)
    Space: O(1)
    """
    sum = a**b
    r = 0
    while a>0:
        r = r + a%10
        a = a//10
    return sum + r

""" 
    
    Time: O(1)
    Space: O(1)
"""

def sumDigits_a_b_3(a, b):
    """
        Runtime: 64 ms, faster than 97.74% of Python3 online submissions for Power of Three.
        Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.

        Time: O(logN)
        Space: O(1)
    """
    res = 0
    while a!= 0:
        res += (a % 10)
        a = a // 10
        if a!= 0:
            res *= 3
            
    return res

"""
    Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
    Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""

def sumDigits_a_b_4(a, b):
    """
        Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
        Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.

        Time: O(1)
        Space: O(1)
    """
    sum = 2
    while a!= 0:
        res = (a % 10) * sum
        if res > 9:
            print(res)
            sum = 1
        else:
            sum = res
            
        a = a // 10
    return res

"""
    Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
    Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""

def sumDigits_a_b_5(a, b):
    """
        Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
        Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.

        Time: O(1)
        Space: O(1)
    """
    sum = 0
    while a!= 0:
        sum += a%10
        a = a//10
    return sum + sum%10

"""
    Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
    Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""

def sumDigits_a_b_6(a, b):
    """
    Time: O(Nlog(1 + log N))/O(N)
    Space: O(1)
    """
    res = 0
    while a!= 0:
        res += (a % 10)
        a = a // 10
        
    sum = 10
    while b!= 1:
        sum = sum * 10 + res%10
        b = b//10
    
    return sum

"""
    Runtime: 64 ms, faster than 98.40% of Python3 online submissions for Power of Three.
    Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Power of Three.
"""
