def sum_spiral(n):
    result = 0
    val = 1
    
    for k in range(4 * n - 3):
        if k % 2 == 0:
            for i in range(k, k + n):
                result += val
                val += 1
        else:
            for i in range(k, k + n):
                result -= val
                val += 1
    
    return result

n = 1001
print(sum_spiral(n))