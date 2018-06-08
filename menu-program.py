import subprocess
import os
import webbrowser
import time
import urllib2

print 
print "Press 1: To check current date and time"
print "Press 2: To create a file"
print "Press 3: To create a directory"
print "Press 4: To search on Google"
print "Press 6: To shutdown OS"

print
choice=int(raw_input("Enter a choice : "))
if choice==1 :
        print		#write a print for 1 line space
	time=time.ctime().split()
	print "Date : ",time[1]," ",time[2]," ",time[4]
	print "Day : ",time[0]
	print "Time : ",time[3]
elif choice==2 :
	print
	os.system("touch ./newfile")
	print "File created"
elif choice==3 :
	print 
	os.mkdir("./newfolder")
	print "Folder created"
elif choice==4 :
	print
	toSearch = raw_input("Enter keywords to search on Google : ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+toSearch)	

elif choice==6 :
	print
	print "Your system will shut down in 10 seconds"
	time.sleep(10)
	os.system("shutdown -h now")
else :
	print "Invalid option"

