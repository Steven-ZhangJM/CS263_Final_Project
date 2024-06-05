

"""


from collections import deque

def solve():

    paths = {('N',0,0,0):('S','E','W',0)}

    for N in range(20):
	for E in range(20):
	    for W in range(20):
		if (E,N,W)!= (0,0,0):
		    q = deque()
		    q.append(((N, E, W, 0), 'N'))
		    while q:
			(pos, dirn) = q.popleft()
			(cx,cy,cz) = pos
			if dirn == 'N':
			    if [cx+E,cy+1,cz] in pos_n:
				pos_s = [cx+E,cy-1,cz]+pos_n[pos_n.index(cx+E)+1:]
				if pos_s!= pos:
					q.append((pos_s, 'W'))
				pos_s = [cx-E,cy-1,cz]+pos_n[