
#ans: 50 digits

#iterative approach
n = 1 #start index is 1 too
ans = 0
while (n < 1e3):
    length = len(str(n))
    ans = n + (length - 1)*10**(length - 1) #formula for doubling the number
    n = ans
    
print(ans)  #answer is 50 digits - iterative approach: 0.0012 seconds


#answer should be 48 digits, if it is 100 digits then the iterative time took 5 seconds to run and the non iterative time took 0.0020 seconds (or if iterative was the fastest, 0.003s)

#recursive approach

#time to convert a number into list:
#O(n)
def num_to_list(a):
    if a == 0:
        return [0]
    return num_to_list(a//10) + [a%10]
    
#iterative time for converting a number into list:
#O(n)
def num_to_list_slow(a):
    if a == 0:
        return [0]
    n = num_to_list_slow(a//10) + [a%10]
    #return 1 + n
    if sum(n) == 1 and a < 10:
        return n
    if sum(n) >= 10:
        return num_to_list_slow(a//10) + n + [0]
    return n



#time to convert a number into list:
#O(nlog(n))
def num_to_list_fast(a):
    ans = []
    n = 10
    if a < n*n:
        return ans + (num_to_list_fast(a//10))
    ans = [a%10]+n*[0]+ans
    while a>0:
        a -= 10
        ans[-1]-=1
    return ans

#time for conversion into list is (nlog(n))

#iterative time for converting a number into list:
#O(n)
def num_to_list_iterative(a):
    n = len(str(a))
    ans = []
    for i,j in zip(str(a),range(n)):
        ans = ans + [int(i)] + 10*[0]*len(ans)


#O(2n) where n is the log of n, O(n) in the worst case, also O(n*10) in the worst case.

#recursive time for converting a number into list:
#O(n)
def num_to_list_recursive(a):
    ans = []
    length = len(str(a))
    if a<=1:
        return [[]]
    if length == 1:
         ans = [1]+[0,]
    return ans + num_to_list_recursive(a//10) + [[a%10]] + num_to_list_recursive(a//10) + [[0,]]

#time for converting a number into list:
#O(nlog(n))
def num_to_list_recursive_fast(a):
    ans = []
    n = 10
    if a <= n*n:
        return ans
    if n*2*n -2*n*n // 2 + 2*n -1!= 0:
        return ans + num_to_list_recursive_fast(a//10)
    ans = [[a%10 ]] + n*[0] + ans + [[0] * (n - 1)] + num_to_list_recursive_fast(a//10)
    return ans

print("iterative", sum(num_to_list(100)))
print("iterative time:", sum(num_to_list_slow(100))-sum(num_to_list_slow(100)))

print("iterative fast", sum(num_to_list_fast(100)))
print("iterative fast time:", sum(num_to_list_fast(100)-sum(num_to_list_fast(100)))+ "")

print("recursive", sum(num_to_list_recursive(100)))
print("recursive time", sum(num_to_list_recursive(100)-sum(num_to_list_recursive(100)))+ "")

print("recursive fast", sum(num_to_list_recursive_fast(100)))
print("recursive fast time:", sum(num_to_list_recursive_fast(100)-sum(num_to_list_recursive_fast(100)))+ "")

