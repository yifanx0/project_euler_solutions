# date: 08/12/2018
# problem: find the number of different ways in which 2 pounds (200 pences) 
	# can be divided into 1-pence, 2-pence, 5-pence, 10-pence, 20-pence, 
	# 50-pence, 1-pound and 2-pound coins

import itertools as it
import numpy as np 

total = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

max_num = []
for i in range(len(coins)) :
	max_num.append(total/coins[i])

# get all possible values <= 200 that each coin can yield
sub_total_coins = []
for i in range(len(coins)) :
	coin = coins[i]
	sub_total_coin = []
	for j in range(int(max_num[i]) + 1) :
		sub_total_coin.append(coin * j)
	sub_total_coins.append(sub_total_coin)

# define a function that can expand the sublists or tuples inside a list
# which will be useful in the loop afterwards
def expand_list(ls) :
	expanded = []
	for x in ls :
		if type(x) == tuple or type(x) == list :
			for i in range(len(x)) :
				expanded.append(x[i])
		else :
			expanded.append(x)
	return expanded

num_combos = 0
combos = sub_total_coins[0]
for i in range(1, len(coins)) :
	combos = list(it.product(combos, sub_total_coins[i]))
	combos = [expand_list(x) for x in combos]
	good_combos = [x for x in combos if sum(x) == total]
	num_combos += len(good_combos)
	# we need a filter to shorten the combination operation
	# o/w Python will die :)
	# assign a divisor for the coins
	if i < len(coins) - 1 :
		if coins[i] == 2 :
			divisor = 5
		elif coins[i] == 5 or coins[i] == 10 :
			divisor = 10
		else :
			divisor = coins[i+1]
		# filter out the combos where 200 - sum cannot be divided by
		# the divisor
		# e.g., we know that after the combo of 1p and 2p, the remaining
		# part, 200 - sum must be able to be divided by 5 b/c the coins 
		# left are all multiples of 5
		combos_filtered = [x for x in combos if sum(x) < total and 
		sum(x) % divisor == 0]
		combos = combos_filtered

print(num_combos)