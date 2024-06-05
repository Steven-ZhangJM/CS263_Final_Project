

import math

def is_prime(n):

	max_divider = math.ceil(math.sqrt(n))
	for i in range(2, max_divider + 1):
		if n % i == 0:
			return False

	return True

def is_permutation(n, s):

	digit_list = list(s)

	digit_list.sort()

	l = len(digit_list)
	for i in range(0, l):
		if n % 10!= digit_list[i]:
			return False

	return True

perms = set()

def make_permutation(s):

	s = str(s)

	l = len(s)

	p = [0] * l

	for i in range(0, l):
		if s[i] in p:
			continue

		found = False
		j = i + 1

		while j > i and not found:
			if s[j] in p:
				if j - i < j - p[s[i]]:
					p[i] = j

				found = True
				p[j] = i
			j += 1

	p = map(str, p)
	return ''.join(p)

for i in range(2, int(10e6)):
	if is_prime(i) and is_permutation(i, str(i)):
		perms.add(make_permutation(i))

for i in perms:
	i = int(i)
	if is_prime(i) and is_permutation(i, str(i)):
		print(i)
		break
