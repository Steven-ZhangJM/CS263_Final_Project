

def calc_fact(n) :
    return n*(n+1)*(n*n+1)//6

nsum = 0
for num in range(100,1000):
    fact = calc_fact(num)
    if fact == num:
        nsum += num 

print(fact)
print(nsum)