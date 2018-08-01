# date: 07/31/2018
# problem: count number of letters when 1 to 1000 (one thousand) (inclusive)
	# were written out in words (spaces or hyphens do not count)

import math

# create a dictionary to store number-letter pairs
# first store 1-20, 30, 40, 50, 60, 70, 80, 90
num_let = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
		6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
		11 : "eleven", 12 : "twelve", 13: "thirteen", 14 : "fourteen",
		15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 
		18 : "eighteen", 19 : "nineteen", 20 : "twenty", 
		30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty",
		70 : "seventy", 80 : "eighty", 90 : "ninety"}

# 21-99
for i in range(21, 100) :
	if i % 10 != 0 :
		first_digit = math.floor(i / 10)
		second_digit = i - 10 * first_digit
		num_let[i] = num_let[first_digit * 10] + num_let[second_digit]

# 100-999
for i in range(100, 1000) :
	if i % 100 == 0 :
		num_let[i] = num_let[i/100] + "hundred"
	else :
		first_digit = math.floor(i / 100)
		remainder = i - 100 * first_digit
		num_let[i] = num_let[first_digit] + "hundredand" + num_let[remainder]

# 1000
num_let[1000] = "onethousand"

sum = 0
for i in range(1, 1001) :
	sum += len(num_let[i])
print(sum)