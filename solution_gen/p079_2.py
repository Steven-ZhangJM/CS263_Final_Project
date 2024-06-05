

import re

def countFreq(pat):
   
    num_re = re.compile(r'.{1}' + pat + r'{1}')
    with open('keylog.txt') as f:
         text=f.read()
    result = num_re.findall(text)
    count = len(result)
    return count

def main():

    pat=input("enter pattern(s) that will be searched: ")
    c=countFreq(pat)
    print(c)
if __name__=="__main__":
    main()
