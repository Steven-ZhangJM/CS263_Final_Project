
a = ''
l = []
for x in range(1,10):

    for y in range(1,10):
        for z in range(1,10):
            if(int(x) + int(y) + int(z) == 9):
                l.append(int(x))
                l.append(int(y))
                l.append(int(z))

print(l)

