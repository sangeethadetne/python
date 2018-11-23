
employee_file = open("employee.txt" , "r") # a-append the contents,r+ - gives reading and writing content to file,

for employee in employee_file.readlines():
    print(employee)
 
employee_file.close()