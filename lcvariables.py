f=101
print (f)

def somefunction():
	global f	# for declaring the variable globally we use keyword global
	print (f)
	f="i am learning python"
	print (f)

somefunction()
print (f)






f1 = open("purchases.txt","r") # open file, read-only
for line in f1.readlines()[1:200]:
      data = line.strip().split("    ")
      
      if len(data) == 6:
            date, time, store, item, cost, payment = data #assign each entry to a variable
            samp = item
print "Number of v's in the store name: " ,item.count('en')
print "Number of items in the store name: " ,max(samp2)
#print "average of the cost for Kansas city stores: " ,average