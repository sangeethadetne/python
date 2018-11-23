 
try:
    value = 10/0
    number = int(input("Enter the number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("Divison by zero error")
except InvalidInputError:
    print("Invalid number")

