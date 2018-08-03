# date: 08/02/2018
# problem: find the sum of all positive integers
	# which cannot be written as the sum of two abundant numbers
	# an abundant number is one whose sum of its proper divisors
	# is greater than itself

def prop_div(n) :
	if n in [0, 1]:
		prop_div = []
	else :
		prop_div = [1]
		for i in range(2, int(n**0.5) + 1) :
			if n % i == 0 :
				prop_div.append(i)
				if n / i != i :
					prop_div.append(n / i)
	return prop_div

threshold = 28124
abun_num = []
for i in range(2, threshold) :
	if sum(prop_div(i)) > i :
		abun_num.append(i)

abun_num_sum = []
for i in abun_num :
	remainder = threshold - i
	for j in abun_num :
		if j < remainder :
			abun_num_sum.append(i + j) 
			# yes there will be duplicates but for the sake of speed I omitted
			# the if condition

bad_num_sum = 1
for i in range(2, threshold) :
	if not i in abun_num_sum :
		bad_num_sum += i

print(bad_num_sum)