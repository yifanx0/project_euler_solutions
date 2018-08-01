# date: 07/28/2018
# problem: largest palindrome made from the product of two 3-digit numbers

palindrome = []

for i in range(100, 1000) :
	for j in range(100, 1000) :
		if int(str(i * j)[::-1]) == i * j :
			palindrome.append(i * j)

print(palindrome)
print(max(palindrome))