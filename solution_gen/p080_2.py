
#Answer: 443533678227586403565984418953840
##

import time
tic = time.perf_counter()

total = 0

for i in range(1,10001):
    a = int(i ** (1/2))
    digit_sum = 0
    for digit in str(a):
        digit_sum += int(digit)
    if digit_sum!= int(digit_sum) and int((digit_sum + 1) ** (1/2))!= a:
        print(i,a,digit_sum)
    digit_sum = 0
    
toc = time.perf_counter()
print(f"Time elapsed during program {toc-tic} seconds")

#print(str(a) + " = " + str(digit_sum))
##
