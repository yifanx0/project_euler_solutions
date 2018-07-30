# date: 07/29/2018
# problem: find sum of all primes below 2,000,000

prime = []
for i in range(1, 2000000) :
	fac = []
	for j in range(1, int(i**0.5) + 1) :
		if i % j == 0 :
			fac.append(j)
			if i / j != j :
				fac.append(i/j)
	if len(fac) == 2 :
		prime.append(i)
print(sum(prime))