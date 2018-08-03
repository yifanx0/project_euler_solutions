# date: 08/03/2018
# problem: find the millionth lexicographic permutation of 
	# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	# lexicographic order: listed numerically

perm = []
limit = 10
digits_0 = [x for x in range(limit)]
for first in digits_0 :
	digits_1 = digits_0[:]
	digits_1.remove(first)

	for second in digits_1 :
		digits_2 = digits_1[:]
		digits_2.remove(second)

		for third in digits_2 :
			digits_3 = digits_2[:]
			digits_3.remove(third)

			for fourth in digits_3 :
				digits_4 = digits_3[:]
				digits_4.remove(fourth)

				for fifth in digits_4 :
					digits_5 = digits_4[:]
					digits_5.remove(fifth)

					for sixth in digits_5 :
						digits_6 = digits_5[:]
						digits_6.remove(sixth)

						for seventh in digits_6 :
							digits_7 = digits_6[:]
							digits_7.remove(seventh)

							for eighth in digits_7 :
								digits_8 = digits_7[:]
								digits_8.remove(eighth)

								for nineth in digits_8 :
									digits_9 = digits_8[:]
									digits_9.remove(nineth)

									for tenth in digits_9 :
										perm.append(
											str(first) + str(second) +
											str(third) + str(fourth) +
											str(fifth) + str(sixth) +
											str(seventh) + str(eighth) + 
											str(nineth) + str(tenth))
print(perm[1000000-1])
