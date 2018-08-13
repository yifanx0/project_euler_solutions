# date: 08/04/2018
# problem: find the product of a and b (|a| < 1000, |b| <= 1000), for
	# the quadratic expression n^2 + an + b that produces the maximum
	# number of primes for consecutive values of n starting with n = 0

def divisor(x) :
	divisors = []
	for i in range(1, int(x**0.5) + 1) :
		if x % i == 0 :
			divisors.append(i)
			if x / i != i :
				divisors.append(int(x / i))
	return divisors

list_a = []
list_b = []
num_primes = []
for a in range(-1000, 1000) :
	for b in range(0, 1001) :
		list_a.append(a)
		list_b.append(b)
		primes = []
		n = 0
		while n**2 + a * n + b > 0 and len(divisor(n**2 + a * n + b)) == 2 :
			primes.append(n**2 + a * n + b)
			n += 1
		num_primes.append(len(primes))

max_index = num_primes.index(max(num_primes))
product = list_a[max_index] * list_b[max_index]
print(product)