

# Solution 1:

a = (1, 360/7)
b = (2, 360/5)
c = (3, 360/3)
d = (0, 360)

def robot(a, b, c, d): # a= (from, to)
	#print('(', a[0], a[1], 'to', b[0], b[1], ')','\t', end = "")
	
	if not d: return -1
	else:
		if (a[0] == c[0]):
			if ((a[1]-b[1])%360 == 0 and (c[1]-a[1])%360 == 0):	#same dir
				r = d[0]
				while r<=(d[1]+b[1]):
					#print(1)
					robot((a[0], a[1]-b[1]+r), (b[0], r+(b[1]-a[1])), (c[0], c[1]-r), d) #(from,to)
					r += 1
