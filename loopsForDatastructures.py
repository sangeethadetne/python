
#Collection types as these holds more than 1 value
#sequence types - List,Tuple,String,Range - order is important as index is being used 
#Sequence doesn't matter Dictionary,Set - order is not  important as index is not being used 
#List = [1,2,3,4]
#Tuple = (1,2,3,4)
#Set = {1,2,3,4} {4,3,1,3} -> number sequence doesn't matter
#Dictionanary = {"brand":"Iphone"} -> number sequence doesn't matter
# 
# # Immutable Vs Immutable 
# String,Tuples are Immutable - cannot be chnaged
# List,Set, Dictionarary are Mutable  - can be changed

#List can hold  values of any type
#
orders_df_list =[1,"2013-07-25 00:00:00,11599",115599,"CLOSED"]
orders_amt =[100,200,None,"invalid",300,400,500.5]
orders =[50,40,50,50,30,20,10]
cust_ids =[1,2,3,4,1,2,3,4,5,6,7,]
orders_new =orders.copy()

sum =0 
for x in orders_amt:
    if type(x) == int or type(x)== float:
        sum = sum+x
    else:
        continue
print(sum)



for x in orders_df_list:
    print(type(x))


# range_start = int(input("put the numbers for the start range"))
# range_end = int(input("put the numbers for the end range"))
# sum=0
# for x in range(range_start,range_end):
#     sum=sum+x
# print(sum)

print(orders_df_list.index(115599))
print(orders.count(50))
orders.sort()
print(orders)
print(orders.reverse())

orders_new[1]=200
print(orders_new)

# find unique customer ids 
unique_id = []
for i in cust_ids:
    if i in unique_id:
        continue
    else:
        unique_id.append(i)
print(unique_id)



# find unique customer ids  using set 

unique_id_new = set(cust_ids)
print(f"Using Set the unique customer ids : {unique_id_new}")




