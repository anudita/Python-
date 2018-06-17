import commands
print 
print '''Press
1. for Date
2. for calander of month
3. for calander of year
'''
choice = int (raw_input('Enter a choice : '))
if choice == 1 :
	print 
	print "Today's date is :", commands.getoutput('date')
elif choice == 2 :
	print
	print "This months calander is as follows:"
	print commands.getoutput('cal')
elif choice == 3 :
	print
	print commands.getoutput('cal 2018')
else :
	print
	print "Invalid choice"
