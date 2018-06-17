import commands
import time
print "printing connected system's ip..."
time.sleep(2)
print commands.getoutput("arp -a | cut -d'(' -f2 | cut -d')' -f1")
