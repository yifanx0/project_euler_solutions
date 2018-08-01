# date: 07/30/2018
# problem: find the number of routes that only move to the right or down
	# through the 20x20 grid (from the NW corner to the SE corner)

# I cheated for this question. I figured out the solution should be
# 40 choose 20, so I just calculated it.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(40)/(factorial(40-20)*factorial(20)))