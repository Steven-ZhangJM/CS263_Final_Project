

num = 0

for i in range (100,1000):
    num = i
    num2 = num * 2
    num3 = num * 3
    num4 = num * 4
    num5 = num * 5
    num6 = num * 6
    if (set(str(num)) == set(str(num2))) and (set(str(num)) == set(str(num3))) and (set(str(num)) == set(str(num4))) and (set(str(num)) == set(str(num5))) and (set(str(num)) == set(str(num6))):
        print ("First loop")
        break
for i2 in range (100,1000):
    num = i2
    num2 = num * 2
    num3 = num * 3
    num4 = num * 4
    num5 = num * 5
    num6 = num * 6
    if (set(str(num)) == set(str(num2))) and (set(str(num)) == set(str(num3))) and (set(str(num)) == set(str(num4))) and (set(str(num)) == set(str(num5))) and (set(str(num)) == set(str(num6))):
        print ("Second loop")
        
        



