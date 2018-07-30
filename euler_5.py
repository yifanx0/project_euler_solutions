# date: 07/29/2018
# problem: the smallest positive number that is 
	# evenly divisible by all of the numbers from 1 to 20
	# evenly divisible meaning dividing w/ no remainder

for i in range(10**3, 10**10) :
	fac = 1
	for j in range(1, 21) :
		if i % j == 0 :
			fac = j
		else :
			break
	if fac == 20 :
		good = i
		break
print(good)