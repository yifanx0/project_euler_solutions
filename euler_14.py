# date: 07/30/2018
# problem: find the starting number <1,000,000 that gives the longest chain
	# using the algorithm n -> n/2 if n is even and n -> 3n + 1 if n is odd

chain_len = []
for i in range(1, 1000000) :
	chain = [i]
	while i != 1 :
		if i % 2 == 0 :
			i = i / 2
		else :
			i = 3 * i + 1
		chain.append(i)
	chain_len.append(len(chain))
print(chain_len.index(max(chain_len)) + 1)
