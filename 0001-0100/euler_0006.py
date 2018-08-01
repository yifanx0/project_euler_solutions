# date: 07/29/2018
# problem: find the difference b/w 
	# the sum of squares of the first 100 natural numbers and
	# the square of the sum

import numpy as np
seq = np.array(range(1, 101))
total = sum(seq)
square_of_sum = total ** 2
squared = seq ** 2
sum_of_square = sum(squared)
diff = square_of_sum - sum_of_square
print(diff)