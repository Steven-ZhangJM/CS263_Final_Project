
def solution():
	s = 10000
	l = []
	prime = 0
	r = []
	for i in range(2, s):
		if i%2 == 0:
			continue;
		cnt = 0
		for j in range(2, ((i/2)+1)):
			if i%j == 0:
				cnt += 1;
		if cnt == 0:
			prime += 1;
	for i in range(2000, s):
		flag = True
		print(i)
		if len(r) == 0:
			for j in range(4999):
				if str(i)[j]!= '2':
					flag = False;
					break;
		else:
			for j in range(len(r)):
				k = prime-j;
				l.append(k*k)
			for j in range(2000):
				if (i-2000) % l[j]!= 0:
					flag = False;
					break;
		if flag:
			r.append(i)
	print(r)
	