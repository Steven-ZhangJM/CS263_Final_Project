import math

def power_set_sum_divisible(n):
    power_set = [i for i in range(1, n+1)]
    
    count = 0
    for i in range(2**len(power_set)):
        subset_sum = sum([power_set[j] for j in range(len(power_set)) if (i & (1 << j))])
        
        if subset_sum % n == 0:
            count += 1
    
    return str(count).zfill(16)

n = 250
print(f"Number of non-empty subsets with sum divisible by {n}: {power_set_sum_divisible(n)}")