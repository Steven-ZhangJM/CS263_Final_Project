


def num_of_rows(row_list):

	row = 0
	ways = []
	
	while row < len(row_list):
		if row + row_list[row] < row_list[-1]:
			ways.append(row)
			row += row_list[row]
		else:
			row_list.pop(row)
	
	if len(row_list) > 0:
		if row + row_list[-1] >= row_list[-1]:
			ways.append(len(row_list) - 1)
	
	return ways

print(len(num_of_rows([0, 0, 1, 1, 1, 4, 1, 1])))


"""
# Method 2

def num_of_rows(row_lengths):
	row = 0
	return row_lengths.count(row) + row + min(row_lengths[row]) - 1
"""