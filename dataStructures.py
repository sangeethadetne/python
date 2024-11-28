#Collection types as these holds more than 1 value
#sequence types - List,Tuple,String,Range - order is important as index is being used 
#Sequence doesn't matter Dictionary,Set - order is not  important as index is not being used 
#List = [1,2,3,4]
#Tuple = (1,2,3,4)
#Set = {1,2,3,4} {4,3,1,3} -> number sequence doesn't matter
#Dictionanary = {"brand":"Iphone"} -> number sequence doesn't matter

orders_df ="1,2013-07-25 00:00:00,11599,  CLOSED  "

new_order_df = orders_df.split(",")[3]
print(new_order_df.lower().strip())


# Immutable Vs Immutable 
# String,Tuples are Immutable - cannot be chnaged
# List,Set, Dictionarary are Mutable  - can be changed

#List can hold  values of any type

orders_df_list =[1,"2013-07-25 00:00:00,11599",115599,"CLOSED"]
orders_df_tuple =(1,"2013-07-25 00:00:00,11599",115599,"CLOSED")
print(orders_df)
print(type(orders_df_list))
print(type(orders_df_tuple))
print(orders_df_list[2])
orders_df_list[3] ='Completed'
print(orders_df_list)
#orders_df.append(100.00)
#print(orders_df)
orders_df_list.insert(1,100)
print(f"The new list : {orders_df_list}")
print(len(orders_df_list))
print(f"The tuple length: {len(orders_df_tuple)}")
print(f" The element that is removed :{orders_df_list.pop()}")
print(orders_df_list)
