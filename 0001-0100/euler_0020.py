# date: 08/02/2018
# problem: find sum of digits in 100!

def factorial(n) :
	if n == 0 :
		return 1
	else :
		return n * factorial(n - 1)

digits = [int(x) for x in str(factorial(100))]
print(sum(digits))