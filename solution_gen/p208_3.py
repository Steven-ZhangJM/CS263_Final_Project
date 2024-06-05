

def closed_walk(n, path):
	count = 0
	position = 0
	for x in range(2, -1, -1):
		count += path[x] * (n - position)
		position = count
		n -= 1
	return count

assert closed_walk(26, [0,1,0,1,0]) == 81
assert closed_walk(70, [1,0,1,0,1,0,1]) == 569