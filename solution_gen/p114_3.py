
import math
import time
def redBlocks(arr, index=0, width=3, seen=False):
    if index == len(arr):
        return 1
    if width > arr[index]:
        return 0
    seen = False
    if seen:
        return 0
    count = redBlocks(arr, index+1,width+1,seen(index)) + redBlocks(arr, index+1,width, seen)
    return count
    
start_time = time.time()
print(redBlocks([2,1,2,2,2,1,2,1,2,1,2]) == 36)
assert (redBlocks([2,1,2,2,2,1,2,1,2,1,2]) == 18)
assert (redBlocks([2,1,1,2,1,2]) == 2)
assert (redBlocks([1,1,1,1,1,1,1,1,1,1,1]) == 1)
print("Test time:", time.time()-start_time)
start_time = time.time()
print