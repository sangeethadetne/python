lucky_numbers = [4,64,7,76,35,55,]
friends = ["John","Shawn","Shandy","Toby","Shandy","Shandy"]
friends.extend(lucky_numbers)# add the list to another list
friends.append("Sangeetha")# add the elements to the list
friends.insert(3,"Geetha")# Inserts the elemenst at specified position
friends.remove("Shandy")

lucky_numbers.sort()
print(lucky_numbers)
print(friends)

friends.reverse()
print(friends)
friends2=friends.copy()
print("The friends2 list is : " + str(friends2))
print("The index of the element is : " + str(friends.index("Shawn")))
print("The popped element is : " + friends.pop())
print("The count of the word from the list : " + str(friends.count("Shandy")))

#friends.clear()# clear the elements from the list
print(friends[1:3])
print(friends[1])
#print([2:])
print(friends[2:])