# date: 08/04/2018
# problem: find distinct terms in the sequence generated by
	# a^b for 2 <= a <= 100 and 2 <= b <= 100

combi = []
for a in range(2, 101) :
	for b in range(2, 101) :
		combi.append(a**b)
print(len(set(combi)))