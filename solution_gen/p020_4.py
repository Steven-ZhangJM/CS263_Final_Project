





def problem1():

    start = 100
    end = 1000000

    total = 0
    for i in range(start, end):
        total += (i // 10) + (i % 10)

    print(total)



if __name__ == '__main__':

    problem1()
