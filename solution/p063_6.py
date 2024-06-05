n = 5
print(f"The {n}-digit number, {7**n}={7**n}, is also a {n}th power.")
n = 9
print(f"The {n}-digit number, {8**n}={8**n}, is a {n}th power.")

count = 0
for n in range(1, 11):
    count += nth_power_digits(n)
    
print(f"Total {n}th powers up to {10**9}: {count}")