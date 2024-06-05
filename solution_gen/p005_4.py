

def factors(n):
    for i in range(1,n+1):
        if  n%i==0:
            yield i
#print(factors(2520))
#returns generator object for all factors
#returns the factors of a number n


num=20
divisible=set()
#adds each number up to 2520 to a set
while True:
    prime=True
    divisible.update(factors(num))
    if 5 in divisible:
        divisible.remove(5)
        prime=True
    else:
        prime=False
    if num > 1000:
        if prime:
            print(num)
            break
    #makes sure the set is not empty
    if not divisible:
        divisible.update(factors(num+1))
        if 5 in divisible:
            divisible.remove(5)
            prime = True
        else:
            prime = False
    #increments to next number and checks the prime factorization
    num+=1
print("It took",num,"to find the smallest number that can be divisibly by more than 5 without any remainder.")

"""
#this works but I do not like it
def factors(n):
    for i in range(int(n),0,-1):
        if  i%n==0:
            yield i
divisible=set()
num=20
while True:
	prime=True
	for i in divisible:
		if str(i).find('5')!= -1:
			divisible.remove(i)
			prime=True
			print(str(i))
			break
	print(i)
	if i == 1:
		if 5 in divisible:
			divisible.remove(5)
		prime=False
	if num > 1000:
		if prime:
			print(num)
			break
	divisible.update(factors(num+1))
	if(5 in divisible):
		divisible.remove(5)
		prime=True
	else:
		prime=False
	num += 1

"""