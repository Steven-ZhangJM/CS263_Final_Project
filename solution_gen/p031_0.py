


def main():
    """
    This function tests the generator from Problem 2.6 on Piazza.
    DO NOT CHANGE.
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = []
    ways_iterate(ways, coins, 200, 0, 200)
    print(ways)


def ways_iterate(ways, coins, target_sum, current_sum, target_index):
    if current_sum == target_sum:
        if target_index == len(coins):
            ways.append(1)
        else:
            ways.append(0)
    for index in range(0, len(coins)):
        if index == target_index:
            continue
        ways_iterate(ways, coins, target_sum, current_sum + coins[index], index + 1)


if __name__ == "__main__":
    main()
