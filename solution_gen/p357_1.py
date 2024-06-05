


def DIVISORS(NUM):
    DIV_POSSIBLE = 0
    for DIV_ITERATION in range(2, int(NUM ** (1 / 2)) + 1, 2):
        for DIV_NUM in range(1, NUM // DIV_ITERATION, 2):
            if NUM % DIV_NUM == 0:
                DIV_POSSIBLE += DIV_NUM
                NUM = NUM // DIV_NUM
    return DIV_POSSIBLE

if __name__=="__main__":
    x = DIVISORS(NUM)
    print(x)
