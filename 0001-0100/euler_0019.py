# date: 08/01/2018
# problem: how many Sundays fell on the first of the month during
	# the 20th century (01/01/1901-12/31/2000)

century = {19000101 : "Monday"}

# define a function create_key that adds a date to the dictionary
def create_key(year, month, day) :
	date = year * 10000 + month * 100 + day
	century[date] = ""

# add all dates to the dictionary
for year in range(1900, 2001) :
	for month in range(1, 13) :
		if month in [4, 6, 9, 11] :
			for day in range(1, 31) :
				create_key(year, month, day)
		elif month == 2 :
			if year % 4 == 0 and year % 100 != 0 :
				for day in range(1, 30) :
					create_key(year, month, day)
			elif year % 400 == 0 :
				for day in range(1, 30) :
					create_key(year, month, day)
			else :
				for day in range(1, 29) :
					create_key(year, month, day)
		else :
			for day in range(1, 32) :
				create_key(year, month, day)
print(len(century)) # check whether the number of days during the 101 years seems right

# update the values for the dates
for date in century :
	num_days = sorted(century).index(date) + 1
	weekday = num_days % 7
	if weekday == 1 :
		century[date] = "Monday"
	elif weekday == 2 :
		century[date] = "Tuesday"
	elif weekday == 3 :
		century[date] = "Wednesday"
	elif weekday == 4 :
		century[date] = "Thursday"
	elif weekday == 5 :
		century[date] = "Friday"
	elif weekday == 6 :
		century[date] = "Saturday"
	elif weekday == 0 :
		century[date] = "Sunday"

# find the answer
i = 0
for date in century :
	if date >= 19010101 and date % 100 == 1 and century[date] == "Sunday" :
		print(date)
		i = i + 1
print(i)