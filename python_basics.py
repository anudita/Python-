
#Immutable data

var1 = 2
print "var1 is of",type(var1)
var2 = 128.132
print "var2 is of",type(var2)
str = "hello"
print "str is of",type(str)
tup = (1,2,4,5)
print "tup is of",type(tup)
tup1 = (2,34.2,"hello",24)
print "tup1 is of",type(tup1)

#operations on tuple
print "length of tuple : ",len(tup1)
print 2 in tup1
print 3 in tup
print tup[1] #indexing
print tup[2]+tup[3]
print type(tup[2])
print tup1[2][-1]
print tup1[-2]*5

#Mutable data

ls = [1,2,3.4,'hi']
print "ls is of",type(ls) 

#operations on list
t=(1,6,9)
print "List: ",ls
ls.append(t)
print "Appended list : ",ls
print "last element on list:", ls[-1]
ls.insert(3, 9999)
print "Inserted 9999 in list :",ls
ls.remove(9999)
print "Removed 9999 from list :",ls


#swapping of two numbers
x=327
y=78
print "Swapping:"
print "Before swap: x=",x," y=",y
x,y=y,x
print "After swap: x=",x," y=",y

