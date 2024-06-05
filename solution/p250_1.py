nums = [i**i for i in range(1, 251)]
ans = sum_of_subsets(nums)
print(f"The rightmost 16 digits are: {''.join(str(int(x)) for x in ans)}")