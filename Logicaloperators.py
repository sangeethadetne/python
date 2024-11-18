age = int(input("Enter the age :"))
Criminal_Records = str(input("Enter if you have nay criminal records - Y/N : "))

# and, or and 
if (age >18 and Criminal_Records =='N' ):
    print("eligible for vote")
else:
    print("Not eligble to vote")