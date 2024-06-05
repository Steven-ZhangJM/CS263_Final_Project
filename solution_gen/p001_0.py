


def find_three_of_five_multiples():
    sum = 0
    for i in range(10000):
        if (i % 3) == 0 or (i % 5) == 0:
            sum = sum + i
    return sum


"""
You have $n$ coins exactly for the same number, but you want to keep the smallest possible number of coins in the suitcase. How many different ways can you put the coins in suitcase? 
"""
