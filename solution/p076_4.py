def count_ways(n):
    def ways_to_sum(k, parts=1):
        if k == 0:
            return 1
        total = 0
        for i in range(parts, k + 1):
            if i > k // i:
                break
            total += ways_to_sum(k - i, i)
        return total

    return ways_to_sum(n)

print(count_ways(100))