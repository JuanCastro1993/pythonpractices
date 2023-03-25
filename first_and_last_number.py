
def first_and_last (numberlist):
	print("Given list",numberlist)

	first_num = numberlist [0]
	last_number = numberlist [-1]

	if first_num == last_number:
		return True

	else:
		return False

numbers_y =[75,65,35,75,30]
print("Result is", first_and_last(numbers_y))

numbers_x =[10,20,30,40,10]
print("Result is ", first_and_last(numbers_x))