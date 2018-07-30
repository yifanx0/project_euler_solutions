# date: 07/27/2018
# problem: find the sum of even-valued Fibonacci numbers smaller than 4 million

a = 1
b = 2
sum = 0
while a <= 4000000 and b <= 4000000 :
	c = a + b
	a = b
	b = c
	if a % 2 == 0 :
		sum += a
print(sum)