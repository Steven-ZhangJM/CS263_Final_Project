def count_numbers():
    count = 0
    for i in range(10**(20-2), 10**20):
        if all(sum(int(digit)*int(d) for d in str(i)[k:k+3]) <= 9 for k in range(len(str(i)) - 2)):
            count += 1
    return count

print(count_numbers())