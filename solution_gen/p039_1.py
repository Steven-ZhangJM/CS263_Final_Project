

from math import floor

def maxi_sol_v(a,b,c):
    s1 = (a + b) * 0.5
    s2 = (c + b) * 0.5
    s3 = (a + c) * 0.5
    
    return s1 + s2 + s3

def solve(p):
    answer = []
    
    for i in range(1,p):
        tmp = maxi_sol_v(i,i+1,p-i)
        
        if tmp > p:
            return tmp
        else:
            answer.append(tmp)
            
    return max(answer)

maxi = 1
for p in range(1,1000):
    tmp = solve(p)
    
    if tmp > maxi:
        maxi = tmp
        
print(maxi)

