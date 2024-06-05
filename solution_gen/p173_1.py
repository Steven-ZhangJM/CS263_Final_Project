

from itertools import chain

T = 2
count = 0

while(T < 1000001):
	t = T
	if((t%4)%2 ==0):
		while(t-2 > 0 and t > 4):
			t = t-2
			if((t%4)%2 ==0):
				t = t-2
			if((t%4)%2!=0):
				t = t-2
	else:
		while(t-2 > 0 and t > 4):
			t = t-2
			if((t%4)%2!=0):
				t = t-2
			if((t%4)%2 ==0):
				t = t-2
	t = t+2
	count = count+1
	T = T+1
print(count)

"""

"""