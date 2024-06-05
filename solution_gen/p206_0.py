

class Solution():
    '''
    Simple solution, just check each digit, if equal to each other, it is possible
    otherwise, then it is not possible by itself, loop thru the digits again
    '''
    def check_pattern(self, n):
        if len(n) == 0:
            return False
        for digit in range(1,10):
            if digit == n[0]:
                pos_digit = n.count(digit)
                flag = True
                for i in range(1,pos_digit):
                    if n[i]!= digit:
                        flag = False
                if flag:
                    return n
                else:
                    pass
            
        return False
    

if __name__ == '__main__':
    s = Solution()
    print(s.check_pattern("_0123456789_01_1_23_45_67_89_0"))
    print(s.check_pattern(""))
    print(s.check_pattern("1_1_2_3_4_5_1_2_3_4_8_