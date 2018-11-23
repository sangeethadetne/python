


employee_file = open("employee.txt" , "w") # a-append the contents,r+ - gives reading and writing content to file,
# w- wil overwrite the all the contents of the file ,cretaes a file.

# for employee in employee_file.readlines():
employee_file.write("\nrakesh recruiter")
# print(employee_file.read())
 
employee_file.close()