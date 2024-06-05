

def differencesquares(size):
	squaredSum = 0
	sumOfSquares = 0
	for i in range(1,size+1):
		squaredSum += (i ** 2)
		sumOfSquares += i
	return squaredSum - sumOfSquares ** 2

if __name__ == "__main__":
	print(differencesquares(101))