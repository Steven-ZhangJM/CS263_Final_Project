```Python
import math

def count_subsets(n):
    result = 0
    for i in range(n+1):
        if (i % 250) == 0:
            # calculate the sum of all subsets with sum equal to i
            subset_sum = 0
            for j in range(i+1):
                subset_sum += math.factorial(j + n-1) // math.factorial(j)
            result += subset_sum
    return result

print(format(count_subsets(250250),',d')[-16:])
```