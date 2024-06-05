

import math
def is_triangle(s1,s2,s3):
    return s1==s2+s3 or s1==s3+s2
def max_deviation(s1,s2,s3):
    if abs(s1-s2-s3)<=2 and abs(s1+s2-s3)<=2 and abs(s1-s3-s2)<=2:
        return 0
    max_x=max(s1,s2,s3)+1
    max_y=max(s1,s2,s3)-min(s1,s2,s3)+1
    for m in range(1,max_x,1):
        n=1
        while n<=max_y:
            if s1==m*(m+1)//2+n*(n+1)//2 and s2==m*(m-1)//2+n*(n+1)//2 and s3==m*(m+1)//2+n*(n-1)//2