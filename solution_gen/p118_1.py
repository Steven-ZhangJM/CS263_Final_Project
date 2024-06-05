

from utilities.matrix_utility import get_prime_numbers_in_range, make_prime_numbers_matrix

def generate_combinations(num_comb, prime_number_array):
    prime_number_matrix = make_prime_numbers_matrix(prime_number_array)
    comb_matrix = []
    number_combo = 0

    for i in range(len(prime_number_array)):
        row = []
        for j in range(num_comb):
            row.append(prime_number_array[j]**i)
        comb_matrix.append(row)
    for i in range(len(prime_number_array)):
        for j in range(num_comb):
            number_combo = combination_with_given_prime_number(prime_number_array[i], comb_matrix[i][j]**num_comb, number_combo)

    print(number_combo)
    return

def combine_numbers(number_1, number_2, prime_numbers_matrix