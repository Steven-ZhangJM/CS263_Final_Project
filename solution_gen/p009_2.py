

# n^2 + (n+1)^2 = n^2 + 2*n^2 + 4*n^2 + 2*n^1 +4*n^1 + 2*n^1 + 4*n^1 + 2*n^1 + 4*n^1 + 10*n^1 + 6*n^1 + 4*n^1 + 24*n^1 + 40*n^1 + 3*n^1 + 2*n^1 + 3*n^1 + 2*n^1 + 40 = 64432 = n^2 + 2*n^2 + 4*n^2 + 2*n^1 + 4*n^1 + 2*n^1 = n^2. Thus
# x = 1.5 and c = 25.

def n_sqaure(n): # Finds the n^2 value:
	return int( n * (n+1) * (2*n*(n+1)+4*n)*(3*n*(n+1)+2*n*(n+1)+4*n))) 

c = 25
for x in range(1, 999): # x = 1.5
	if n_sqaure(x) == c and x+x+x == 1000:
		print((str(x) + '^2+'+ str(x+1) + '^2 ='+ str(x+x+x)) )
		break


