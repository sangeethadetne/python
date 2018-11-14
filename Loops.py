is_male = True
is_tall = False

if is_male or is_tall:
	print("You are Female or tall or both")
elif is_male and not(is_tall):
	print("You are Female or tall or both")
elif not(is_male) and is_tall:
	print("You are male or tall or both")
else:
	print("You are neither Male neither tall")