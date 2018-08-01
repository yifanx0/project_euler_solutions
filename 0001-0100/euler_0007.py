# date: 07/29/2018
# problem: find the 10001st prime number

prime = []
a = 1
while len(prime) < 10001 :
	fac = []
	for i in range(1, int(a ** 0.5) + 1) :
		if a % i == 0 :
			fac.append(i)
			if a / i != i :
				fac.append(a/i)
	if len(fac) == 2 :
		prime.append(a)
	a = a + 1

print(prime[-1])
