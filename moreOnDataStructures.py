#create a new list out of transformation 

orders_amount =[100,200,300,400,500,600,700,112,113,114]
orders_gst =[]

for x in orders_amount:
    orders_gst.append(x+x*0.18)
print(f" The GST list is : {orders_gst}")

#List Comprehension:

orders_gst_new = [y+y*.18 for y in orders_amount]
print(f"Using List comprehension way :{orders_gst_new}")


orders_amount1 =[(100,5),(200,10),(300,15),(400,10),(500,18),(600,25),(700,30),(112,5),(113,5),(114,5)]
orders_gst1=[]

for x in orders_amount1:
    orders_gst1.append(x[0]+x[0]*x[1]/100)
print(f" tuples in List :{orders_gst1}")

#List Comprehension:

orders_gst1_new =[(x[0],x[1],x[0]+x[0]*x[1]/100) for x in orders_amount1]
print(f"Using List comprehension way while using Tuple :{orders_gst1_new}")
