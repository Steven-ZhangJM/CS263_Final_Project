



import math 

def pythag(n):
	l=[]
	a=int(math.sqrt(n))
	for i in range(a+1,n):
		t=(i**2 + 3*a**2) #equation of the triangle
		c=int(math.sqrt(t))
		for j in range(c+1,n):
			if(i+j+a==1000):
				l.append(i*j*a)
	if(len(l)==0):
		print("no Triple")
	else:
		print(l)
	return l


s=pythag(1000)


"""