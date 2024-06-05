

def main():
	f_file = open('data\p049_digits.txt')
	n = 10

	num_sets = num_digits(n) + 1
	set_count = num_sets**n

	print(f'There are {n} digits.\nWe need {num_sets} * {num_sets} = {set_count} sets.\nThese are:')
	ans = range(num_sets**n)
	ans = reduce(intersect, ans)
	print(ans)

def num_digits(n):
	if n == 1:
		return 4
	if n == 2:
		return 6
	n -= 1
	f_file = open('data\p0(9).txt')

	ans = 4
	for i in range(9,n):
		#print(f'{i} + 1 = {i+1}')
		if 4 < (j := sum([1 for line in f_file if line == str(i+1)])):
			ans += 1

	return ans

def intersect(x, y):
	result_set = x & y
	result_list = tuple(set(x) & set(y))
	return result_set

if __name__ == "__main__":
	main()

