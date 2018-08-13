# date: 08/04/2018
# problem: find the sum of the numbers on the diagonals in
	# a 1001 x 1001 spiral formed by starting w/ 1 in the center
	# and moving to the right in a clockwise direction

# a 1001 x 1001 spiral contains (1001 + 1) / 2 layers
# if we consider 1 as the first layer
size = 1001
num_layers = (size + 1) / 2

layer = 1
end = 1
sum = 1
while layer < num_layers :
	layer += 1
	start = end
	step = 2 * (layer - 1)
	for i in range(1, 5) :
		num = start + i * step
		print(num)
		sum += num
	end = num

print(sum)