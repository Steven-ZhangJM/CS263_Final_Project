

def readFile(file):
    lines = file.readlines()
    lines = list(map(lambda string: string.strip(), lines))
    return lines

def processResults(list):
    newList = list.copy()
    for i in range(len(list)):
        for j in range(len(list)):
            if i!= j:
                str1 = newList[i]
                str2 = newList[j]
                str1 = str1.replace('-','')
                str2 = str2.replace('-','')
                str1 = str1.replace(' ','').replace('/',' ').split(" ")
                str2 = str2.replace(' ','').replace('/',' ').split(" ")
                temp = list[3] + list[3]
                if list[3] == list[3]:
                        str1 = str1.sort()
                        str2 = str2.sort()
                        cnt = 1
                        while cnt<=len(list[3]):
                            del newList[i]
                            del newList[j]
                            if newList[i]!= newList[j]:
                                break
                                
                            cnt+=1
                elif str1 == list[3] or str2 == list[2]:
                    cnt = 1
                    while cnt<=len(list[3]):
                        del newList[i]
                        del newList[j]
                        if newList[i]!= newList[j]:
                            break
                        cnt+=1
    return newList    
    
file = open('textFile1.txt', 'r')
data = readFile(file)
print(processResults(data))    
file.close
