
def main():
	for i in range(37,10000):
		n = str(i)

		# check that all numbers appear exactly once
		nCounter = {}
		for j in range(0,10):
			nCounter[int(n[j])] = nCounter.get(int(n[j]), 0) + 1
			if (nCounter[int(n[j])] > 1):
				break
			if (j == 9):
				continue
			else:
				break

		# check that the numbers don't start with 0
		for j in range(0,10):
			if (nCounter[int(n[j])] == 1):
				if (int(n[j]) in nCounter):
					break
				else:
					# there's one, keep going
					pass

			else: break

		# check that there are 9 numbers after counting start with 0
		if (j ==9):
			# we found it
			nums = list(map(int, n))
			nums.sort()
			if (nums[:8] == list(range(1,10))):
				print(i)
				break
		if (j+1 == 9):
			pass






#-----------------------------------------------------------------------

# import time module
import time
def run_k_first_primes(x):
	k_first_primes = []
	x_prime = x
	while True:
		x += 1
		is_prime = True
		for prime in k_first_primes:
			if not(x % prime == 0):
				is_prime = False
				break
			if (x == prime or x % prime == 0):
				x = prime
				break
		if (is_prime):
			k_first_primes.append(x)		
		if (len(k_first_primes) == x):
			break

	return k_first_primes

def main():
	start = time.time()
	k_first_primes = run_k_first_primes(2)
	n = 1
	for i in range(1,10000):
		if (i >= 10**7):
			break
		elif (i in k_first_primes):
			print(i)
			break
		else:
			n += 1
	print("Execution Time (in second): " + str(time.time() - start))
		
if __name__ == '__main__':
	main()
