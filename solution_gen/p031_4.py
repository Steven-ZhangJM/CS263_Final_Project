

if __name__ == '__main__':
    """
    A way to test this code
    """

    import common_functions as cf
    test_string = '''
    input:
    1 - £2 is made up of 1 pound and 2 pence, so 1+2 = 3. Then we have: 1×1, 1×2, 1×50p, and 1×(50y) + 2×20p + 3×1p
    2 - £2 is made up of 5 pounds and 2 pence, so 1+2 = 4. Then we have: 1×5p, 1×20p, and 1×2p and 2×1p. (which equals 5x1p and 20x2p = 500p)
    3 - £2 is made up of 5 pounds and 2 pence, so there is no way to make 1+100 y = 200p + 2×5p.
    4 - £2 is made up of a pound and 7 pence, so 1+1 = 2. Then we have: 1×50p + 1×1p + 2×7p
    """
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "1", "2"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "1", "50p"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "1", "100"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "2", "100"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "5", "100"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "1", "50p"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "1", "7p"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "10", "100"))
    print(cf.multiply_lists(["1", "2", "5", "20", "50", "100", "5p", "7p"], "100", "100"))

    input_strings = [
        """
        100
        100
        200
        """,
        """
        1
        2
        100
        5p
        20p
        7p
        """
    ]
    for input_string in input_strings:
        test = cf.multiply_lists(input_string[1:-1].split("\n"), input_string[0], input_string[-1])
        print(test)
        if test!= cf.get_correct_answer():
            print("Input:", input_string)
            print(f"Test string: {test}")
            print(f"Correct answer (should be): {cf.get_correct_answer()}")
            break

