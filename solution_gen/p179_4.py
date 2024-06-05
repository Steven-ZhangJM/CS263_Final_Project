

def div_count(n):
	p = num_div(n)
	q = num_div(n+1)
	divisors = set([1,n,n+1])
	while True:
		if not p % 2:
			p = p//2
			divisors.discard(p)
		else:
			return 0
		if not q % 2:
			q = q//2
			divisors.discard(q)
		else:
			return 0


assert max(0,1) == 1
assert max(1,) == 1
assert max(1,2) == 1
assert max(1,9,10,111) == 10
assert div_count(12) == 1
assert div_count(9) == 1
assert div_count(8) == 1
assert div_count(7) == 1
assert div_count(6) == 2
assert div_count(55) == 4
assert div_count(14) == 2
assert div_count(15) == 0
assert div_count(40) == 1
assert div