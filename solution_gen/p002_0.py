

n = int(4000000)

seq = '1, 2'

for i in range(2, n):
    x, y = i - 1, seq.split(',')[-1]
    print(x)
    print(y)
    z = x + y
    num = x + z
    print(num)
    if z % 2 == 0:
        seq = num + ','+ seq
        print(seq)
    else:
        seq = y
        print(num + ','+ seq)