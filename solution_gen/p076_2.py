
def ways(low,high):
    if high == low:
        return 1
    if low == 0:
        return 0
    if low < 0:
        return 0
    else:
        return ways(low-1,high)+ ways(low,high-low)

total_ways = 0
for low in range(0, 101):
    total_ways += ways(low,low)
print(total_ways)
