

def check(s, e):
	if e<0:
		if e==0:
			return True
		return False
	prime_list = sieve_of_Eratosthenes(e)
	prime_summation_list=[]
	for idx in range(e):
		if idx in prime_list:
			prime_summation_list.append(idx+s)
		else:
			prime_summation_list.append(0)
	print(prime_summation_list)
	print(s, e)
	for idx in range(s, len(prime_summation_list)):
		for num in prime_list:
			if prime_summation_list[idx]==num:
				if isprime(idx+prime_summation_list[idx]):
					return True
	return False


def isprime(n):
	for i in range(2, int(n**.5)+1):
		if n%i==0:
			return False
	return True

if __name__ == "__main__":
	import time
start = time.process_time()
s_list=srange(10, 5000)
for _ in srange(10000):
	prime_list=[]
	length=0
	for s in s_list:
		e = random.randint(s, 5000)
		if isprime(e):
			if check(s, e):
				length+=1
				prime_list.append(e)
	if length==5:
		print(prime_list[0])
		break
end = time.process_time()
print("Took", end-start, "seconds to finish")

