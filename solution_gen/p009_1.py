
#code:
def find(c=1000):
    for a in range(1,c):
        for b in range(a,c):
            while a*a + b*b > c*c:
                break
            if a*a + b*b == c*c:
                return a*b*c

print(find())
