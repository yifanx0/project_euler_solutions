# date: 07/29/2018
# problem: find the product of the only Pythagorean triplet whose sum is 1000
	# Pythagorean triplet: a, b, c w/ a^2 + b^2 = c^2

for c in range(2, 1001) :
	for b in range(1, c) :
		a = 1000 - b - c
		if a > 0 and a < b and a ** 2 + b ** 2 == c ** 2 :
			print([a, b, c])
			prod = a * b * c
			break
print(prod)