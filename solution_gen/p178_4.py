

class Solution(object):
    """
    Solution is for Problem 7.
    It just works with a generator.
    """
    def pandigital_step_num(self):
    
        step_nums = []
        for x in range(9, 39999999):
            
            a = str(x)
            d = self.find_deltas(a)
            if not d:
                continue
            
            r = range(1, len(d))
            
            for x in range(1, len(d)):
                a = a[:r[x-1]] + str(x) + a[r[x-1]+1:]
            
            a = sorted(list(a))
            r = str(x) + ''.join(a)
            r = int(r) 
            a = str(x)
            
            if not d:
                continue
            
            for i in range(len(d)):
                a = str(x)
                for c in d:
                    a1 = a
                    a = a.replace(