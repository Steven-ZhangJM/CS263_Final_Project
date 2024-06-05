import itertools

# Define the pandigital number range (0-9)
pandigitals = [str(i) for i in range(10)]

# Generate all permutations of pandigitals
permutations = list(itertools.permutations(pandigitals))

# Filter out numbers that exceed 10^40
step_numbers = []
for permutation in permutations:
    num_str = ''.join(permutation)
    if int(num_str) < 10**40 and all(abs(int(d1) - int(d2)) == 1 for d1, d2 in zip(num_str[:-1], num_str[1:])):
        step_numbers.append(num_str)

# Count the pandigital step numbers
pandigital_step_count = len(set(step_numbers))

print(pandigital_step_count)