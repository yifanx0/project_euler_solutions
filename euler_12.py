# date: 07/30/2018
# problem: find the first triangle number that has over 500 divisors
	# triangle numbers are the sum of nutural numbers, e.g. 1, 3, 6, 10, ...

a = 1
b = 0
fac = []

while len(fac) <= 500 :
	fac = []
	b = b + a
	a = a + 1
	for i in range(1, int(b**0.5) + 1) :
		if b % i == 0:
			fac.append(i)
			if b / i != i :
				fac.append(int(b/i))

print(b)