n = 2
while True:
    count = count_ways(n)
    if count > 5000:
        print(n)
        break
    n += 1