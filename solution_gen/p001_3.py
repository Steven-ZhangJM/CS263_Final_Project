

from timeit import 	Timer

# Solution #1 - O(n^2) / O(1)

if __name__ == "__main__":
	
	# Get number to sum
	number = 1000
	# Get starting and ending point for sublist
	ending_point =  number + 1 
	sub_list_length = end - start

	t1 = Timer("for i in range(start, end): if i % 3 or i % 5: print(i)", "from __main__ import i, start, end")
	print("All multiples, 3 and 5 below N:")
	print(t1.timeit(number=sub_list_length))

	t2 = Timer("for i in range(start, ending_point):", "from __main__ import i, start, end")
	print("Sublist 3:")
	print(t2.timeit(number=sub_list_length))

	t3 = Timer("for i in range(starting_point-sublist_length, ending_point): if i % 3 or i % 5: print(i)", "from __main__ import i, starting_point, end")
	print("Sublist 5:")
	print(t3.timeit(number=sub_list_length))