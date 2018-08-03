# date: 08/02/2018
# problem: calculate the sum of name scores
	# name score = index of name after sorting + sum of alphabetical value

import numpy as np 
names = np.chararray.split(open("euler_0022_names.txt").read().replace('"', ""),
	sep = ",")
#print(names)
names_sorted = sorted(names.tolist())
print(len(names_sorted))

name_score = 0
for name in names_sorted:
	name_index = names_sorted.index(name) + 1
	alpha_value = 0
	for letter in name:
		alpha_value += ord(letter) - 64 # see unicode for uppercase letters
	name_score += name_index * alpha_value

print(name_score)
