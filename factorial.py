input=int(raw_input('Enter a number to find its factorial : '))
number=input
factorial=1
while (number>0) :
	factorial = factorial * number
	number=number-1

print "Factorial of",input," is ",factorial 
