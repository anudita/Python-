def factorial(num) :
	if num == 1:
		return num
	else:
		return num*factorial(num-1)
str = 'y'
while (str == 'y' or str =='Y'):

	num = int(raw_input("Enter a number"))

	if num < 0:
		print("Cannot find factorial of negative number")
	elif num > 0:
		print "Factorial of number is",factorial(num)
	elif num == 0:
		print "Factorial of number is 0"
	print
	print "Do you want to find another factorial? (y/n)"
	choice = raw_input()
	if(choice == 'n' or choice == 'N'):
		exit()
