# date: 08/03/2018
# problem: find the index of the first term in the Fibonacci sequence to contain 1000 digits
	# Fibonacci starts with 1, 1

a = 1
b = 1
i = 1
while len(str(a)) < 1000 :
	c = a + b
	a = b
	b = c
	i += 1
print(i)
