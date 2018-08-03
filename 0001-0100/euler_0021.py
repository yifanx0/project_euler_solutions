# date: 08/02/2018
# problem: find sum of all amicable numbers under 10000
	# amicable numbers: a pair of distinct numbers (a, b) 
	# where the sum of proper divisors of one is equal to the other
	# proper divisors of a: divisors of a that are less than a

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

ami_num = []
for i in range(1, 10000) :
	sum_prop_div = sum(prop_div(i))
	if sum_prop_div != i :
		other_sum = sum(prop_div(sum_prop_div))
		if other_sum == i and not i in ami_num :
			ami_num.extend((i, int(sum_prop_div)))

print(sum(ami_num))