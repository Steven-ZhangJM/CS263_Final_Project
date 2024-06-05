
#The main method is to run the check_n_sorted() for each one of the lists to calculate the number of permutations and if they matches 15 (for the array) then add 1 to the counter of the sum

def check_n_sorted(ls):

    counter = 0
    for i in range(0,len(ls)-1):
        if ls[i]<ls[i+1]:
            sorted = ls.copy()
            ls[i] = sorted.insert(i, 0)
            for j in range(0,len(ls)-1):
                if sorted[j] < sorted[j+1]:
                    sorted[j+1] = sorted.insert(j+1, 0)
            counter += len(ls)-1-i
            ls = sorted

    return counter


def solution_one(n):
    return check_n_sorted((list(range(1, n+1))))


print(solution_one(7))
print(solution_one(8))
print(solution_one(9))

#The alternative method is to generate