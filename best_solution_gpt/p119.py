def find_a_n(n):
    result = []
    for a in range(2, 100):  # Assuming the power is less than 100
        for b in range(2, 10**a):  # Assuming the number is less than 10 raised to the power of a
            if sum(int(digit) for digit in str(b)) == a and b == a**int(str(b)[0]):
                result.append(b)
                if len(result) == n:
                    return result[-1]
    return -1  # In case n is not found within the assumed range

# Find a_30
print(find_a_n(30))