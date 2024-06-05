*
```python
def count_divisible_subsets():
    total_sum = sum(i**(i+1) for i in range(1, 250251))
    divisible_counts = [0] * (total_sum // 250 + 1)
    
    for num in range(1, 250251):
        remainder = (num % 250)
        if remainder:
            divisible_counts[remainder - 1] += 1
        else:
            for i in range((total_sum // 250) + 1):
                divisible_counts[i] += count_subsets(num, i * 250)

    return sum(count for count in divisible_counts if count > 0)

def count_subsets(n, target):
    counts = [0] * (target // n + 1)
    
    for i in range(2, int((target // n) ** 0.5) + 1):
        power_i = i**(i+1)
        if power_i > n:
            break
        remainder = target % power_i
        counts[remainder - 1] += (i+1) * ((power_i - 1) // i)
        
    return sum(count for count in counts if count > 0)

print(count_divisible_subsets())
```

**