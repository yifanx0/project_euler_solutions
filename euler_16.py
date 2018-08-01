# date: 07/31/2018
# problem: sum of digits of the number 2^1000

data = 2 ** 1000
digits = [int(x) for x in str(data)]
print(sum(digits))