# date: 07/28/2018
# problem: largest prime factor of the number 600851475143

import math
a = 600851475143
fac = []
prime_fac = []

for i in range(1, round(math.sqrt(a)) + 1) :
	if a % i == 0 :
		fac.append(i)
		if int(a / i) != i :
			fac.append(int(a / i))
		sub_fac = []
		for j in range(1, round(math.sqrt(i)) + 1) :
			if i % j == 0 :
				sub_fac.append(j)
				if int(i / j) != j :
					sub_fac.append(int(i / j))
		if len(sub_fac) == 2 : # defn of prime numbers: having exactly two positive divisors
			prime_fac.append(i)

print(fac)
print(prime_fac)
print(max(prime_fac))