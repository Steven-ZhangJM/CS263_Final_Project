

def solution_part1(side_length, spiral_type):
	# this function finds a diagonals in spiral way

	center = (0, (side_length - 1) // 2)
	diag_a = spiral_type[::]
	diag_b = (0, 0)

	matrix = []
	row_idx = 0
	col_idx = 0

	for x in range(1, side_length * side_length + 1):
		if row_idx == center[0] and col_idx!= side_length - 1:
			matrix.append(diag_a)
			col_idx += 1
		elif col_idx == center[1] and row_idx < side_length - 1:
			matrix.append(diag_b)	
			row_idx += 1
		elif x >= side_length ** 2:
			col_idx = (col_idx + 1) % side_length
		elif x < side_length ** 2:
			row_idx = (row_idx + 1) % side_length

	return sum(diagonals(matrix))

def diagonals(matrix):
	return [matrix[0][0], *line,  matrix[-1][-1]]

def solution_part2(side_length, spiral_type):
	# this funciton finds a diagonals in spiral way
	# with length greater as $n$

	center = (0, (side_length - 1) // 2)
	diag_a = (0, 0)
	diag_b = (0, 0)

	matrix = []
	row_idx = 0
	col_idx = 0

	for x in range(1, side_length * side_length + 1):
		if row_idx == center[0] and col_idx!= side_length - 1:
			matrix.extend([diag_a] * (side_length - 1))
			matrix.append(diag_a)
			col_idx += 1
		elif col_idx == center[1] and row_idx < side_length - 1:
			matrix.extend([diag_b] * (side_length - 1))
			matrix.append(diag_b)
			row_idx += 1
		elif x >= side_length ** 2:
			col_idx = (col_idx + 1) % side_length
		elif x < side_length ** 2:
			row_idx = (row_idx + 1) % side_length

	return sum(diagonals(matrix, n))

answer = solution_part1(1001, (1, 5, 7, 8, 9, 10, 12, 16, 17, 18, 19, 20, 
18, 6, 5, 4, 3, 1217, 16, 15, 14, 13))

print(answer)