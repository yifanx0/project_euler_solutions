# date: 08/12/2018
# problem: find the sum of all numbers that can be written as the sum of 
	# fifth powers of their digits

# to get a rough estimate for the range of numbers desired, observe that 
	# 6*9**5, 7*9**5, 8*9**5 are all 6-digit numbers, which means after 
	# 6 digits, the number is too large for the sum of fifth power of each 
	# digit to be equal to the number itself
good = []
for i in range(2, 500000) :
	fifth_order = [int(x)**5 for x in str(i)]
	if sum(fifth_order) == i :
		good.append(i)
print(good)
print(sum(good))