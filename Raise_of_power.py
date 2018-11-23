# print(2 ** 3)

def Raise_of_power(base_num , pow_num):
	result = 1
	for index in range(pow_num):
		result = result * base_num
	return result


print (Raise_of_power(2,0))