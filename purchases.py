print "hello, world!"
print 'hello, bearcat!'
print '\n'

total=0
f1 = open("purchases.txt","r") # open file, read-only
for line in f1.readlines()[1:200]:
      data = line.strip().split("    ")
      
      if len(data) == 6:
            date, time, store, item, cost, payment = data #assign each entry to a variable
            samp = store
            #payment1=payment
            if samp == "Indianapolis" :
                  print "\n"+line
                  total = total + float(cost)
                  print ""
print "total cost - " ,total
f1.close()

result = open("result.txt", "r")
data = open("data.txt","w") 

for line in result()[1:200]: 
    data = line.strip().split("    ") 
    #print data
   # print len(data)
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
        data.write("{0}\t{1}\n".format(store, cost))
data.close()
result.close()











