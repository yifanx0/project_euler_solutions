# date: 07/27/2018
# problem: find sum of all multiples of 3 or 5 below 1000

sum = 0
for i in range(1, 1000) :
	if i % 3 == 0 or i % 5 == 0 :
		sum = sum + i # can use sum += i instead
print(sum)