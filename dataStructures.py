#Collection types as these holds more than 1 value
#sequence types - List,Tuple,String,Range - order is important as index is being used 
#Sequence doesn't matter Dictionary,Set - order is not  important as index is not being used 
#List = [1,2,3,4]
#Set = {1,2,3,4}
#Tuple = (1,2,3,4)
#Dictionanary = {"brand":"Iphone"}

orders_df ="1,2013-07-25 00:00:00,11599,  CLOSED  "

new_order_df = orders_df.split(",")[3]
print(new_order_df.lower().strip())