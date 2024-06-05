
# Solution from leetcode
def find_uniq_square_number(n):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        #if n > 30:
            #d = n**0.5
            #if n % d == 0:
              #  return False
        if 2 > n//2:
            return True
        for i in range(1, 21):
            if not (n % (i+2)):
                return False
        return True

    ret = 0
    for k in range(3, 100000):
        # k^4+3k^3+7k^2+k+7 should be k^2+1
        tmp = 1
        for j in range(1, 10):
            tmp *= k - j*j
        if tmp < k*k:
            continue
        if k*k == tmp:
            if is_prime(k):
                ret = k
                break
    return str(n) + str(ret) + str(ret*ret