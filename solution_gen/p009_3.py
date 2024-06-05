


def solve_problem(answer_list):
    result = 0
    for a in answer_list:
        for b in answer_list:
            for c in answer_list:
                if a + b + c == 1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        result = (a * b * c)
    return result


if __name__ == '__main__':
    answer_list = list(range(1, 1000))
    # answer = solve_problem(answer_list)
    # print(answer)
    answer = solve_problem(answer_list[:-1])
    print(answer)
