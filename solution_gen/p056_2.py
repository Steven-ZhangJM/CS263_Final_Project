

# from problem.a import sieve
# sieve(100, len(str(10**100)))


def sum_digits_of_solution(xxx_todo_changeme1):
    A, B = xxx_todo_changeme1
    return A*B+10*(A%10) + 20*(B%10)


def maximum_sum_of_digits(limit):
    xxx_todo_changeme = range(1, limit)
    return max(map(sum_digits_of_solution, enumerate(xxx_todo_changeme)))


max_s = maximum_sum_of_digits(limit=100)
print(max_s)

"""
Output

319766833

"""