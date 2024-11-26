import math

total_Amount= -20000.06
day_Worked = 30 
day_Wages_Associate_Per_Hour = 30
day_Wages_Contractor_Per_Hour = 50 
day_Associate_Labour =20
day_Contractor_Labour =10

#string arthematic operatins
Total_Wages_all =  day_Wages_Associate_Per_Hour* day_Associate_Labour + day_Wages_Contractor_Per_Hour* day_Contractor_Labour
print(f"The Total Wages over all : {Total_Wages_all}")

print ("-----------"*6)
# Arthematic operation -  + ,* ,-,/,%,// - Precedence is left to right  BODMAS Rule 
avg_Wages_All=(day_Wages_Associate_Per_Hour* day_Associate_Labour + day_Wages_Contractor_Per_Hour* day_Contractor_Labour)/(day_Associate_Labour+day_Contractor_Labour)
print(f"The avg Wages earned over all : {avg_Wages_All} ")

#right side binding for power operator 
print(2** 2** 3)

day_Associate_Labour+=22
print(day_Associate_Labour)

print(math.floor(total_Amount))
print(math.ceil(total_Amount))
print(math.fabs(total_Amount))


""" indexing and slicing are two important concepts in python strings """

fname = "Sangeetha"
lname = "Detne"

stnce = " you are  doing python traning's"
mult_stnce ="""you are praticisning puython
from long time """

" strings can be ancapsulated in single quotes, double quotes, triple qupotes  " 

print(fname+lname)
print("Sangeetha" not in fname)
print(stnce)
print(mult_stnce)
#find the len of the string 
print(len(fname))
#indexing - help to get a particular character
#silicing - helps  to get the slice of the string 
#strings are immutable one cannot make  make chnages in strings defination
order_status = "complete order"
print("==============================")
print(order_status[-2])
print(order_status[0:7])
print(order_status[10:len(order_status)])
print(order_status[9:])
print(order_status[:8])
# this preints the words from last 5 characters
print(order_status[-5:])
# print second word after the space
print(order_status.split(" ")[1])
# print second word after the space without using split
index =order_status.find(" ")
print(order_status[index+1:])
print(order_status[0:index-1])
print("======================================")
print(order_status[-5:-1])
print(order_status[1:9:2])
#reverse the string 
print(order_status[::-1])
#find will give -1 if it doesn;t find the characters that it wants 
print(order_status.find("*"))
print(order_status.find("e"))
# this throws exception if the character is not find
#print(order_status.index("s"))
print(order_status.endswith("order"))
print(order_status.capitalize())
#remove the left and right spaces using rstrip or lstrip
print(order_status.strip())
new_string= order_status.replace("complete","compeleted")
print(new_string)
