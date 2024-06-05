

# Solution 1
def find_smallest_number_divisibledivisibleby_20():
    for i in reversed(range(20, 1, -1)):
        if i*i > 20:
            return i

# Solution 2
def find_smallest_number_divisibledivisibleby_20():
    divisible20 = 0
    minimumnumber = 0
    while(1):
        minnumber = divisible20 + 1
        i = 0
        while(True):
            if (divisible20+i+1) % (i+1) == 0:
                i += 1
                        
            else:
                i = 0
                break
                
        if i == 1:
            break
        
        divisible20 = minnumber

if __name__ == "__main__":
    print(f"The smallest positive number that is evenly divisible divisible by all of the numbers from 1 - 20 is: {find_smallest_number_divisibledivisibleby_20()}")
 
