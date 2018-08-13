# date: 08/03/2018
# problem: find the number < 1000 w/ the longest recurring cycle
	# when 1 is divided by it

# use long division to find recurring cycles 
# (https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence)

len_cycles = []

for denom in range(1, 1000) :
	numer = 1
	remainders = []
	remainder = numer - int(numer / denom) * denom
	while not remainder in remainders :
		if remainder == 0 :
			break
		else :
			remainders.append(remainder)
			numer = remainder
			while int(numer / denom) == 0 :
				numer *= 10
			remainder = numer - int(numer / denom) * denom
	remainders.append(remainder)
	len_cycle = len(remainders) - (remainders.index(remainder) + 1)
	len_cycles.append(len_cycle)

gold = len_cycles.index(max(len_cycles)) + 1
print(max(len_cycles))
print(gold)
