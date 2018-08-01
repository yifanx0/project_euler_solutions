# date: 07/31/2018
# problem: find maximum path sum through triangle

import numpy as np 
data = np.chararray.split(
'''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.replace("\n", " "))

# transfer triangle into one-line array
data_int = np.array(data.tolist()).astype(int)

# essentially, a path in triangle means at row i, can jump i or i+1 steps
# to reach the next number

n_row = 15
paths_index = [[0] * n_row for n in range(2 ** (n_row - 1))]

# create a tree of paths
for i in range(1, n_row) :
	for j in range(2 ** (n_row - 1)) :
		if j % (2 ** (n_row - i)) < 2 ** (n_row - i - 1) :
			paths_index[j][i] = paths_index[j][i-1] + i
		else :
			paths_index[j][i] = paths_index[j][i-1] + i + 1

paths_sum = [sum(data_int[x]) for x in paths_index]
print(max(paths_sum))