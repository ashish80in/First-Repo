# fruits=['apple\n','orange\n','mango\n']

# with open("fruits.txt","w")as file:
#     for fruit in fruits:
#         file.write(fruit)
    
    
# try:
#     with open("vegetable.txt","r")as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#  print("no file is found")
# finally:
#    print("code run done")

# with open("fruits.txt","a")as file:
#     file.write("\n hello")
#     file.write("\n pineapple")
# try: 
     
#  num1=int(input("enter your first number"))
#  num2=int(input("enter the second number"))
#  result=(num1/num2)
 
# except ValueError:
#  print("number is not valid ")

# except ZeroDivisionError:
#  print("number is not divided by zero")
# else:
#  print(result)
# finally:
#  print("done")


# Task 6: Dictionary and List Exceptions
# You are given the following list and dictionary:
my_colors = ["red", "blue", "green"]
student_info = {"name": "John", "grade": "A"}

# 6a. Try to print the 5th element of my_colors. Catch the IndexError and print a custom message.
# TODO: Write your code for Task 6a here
 


my_colors = ["red", "blue", "green"]
student_info = {"name": "John", "grade": "A"}

try:
 print(my_colors[5])
except IndexError:
 print("no index found")
try:
 print(student_info['age'])
except:
 print("no key value found")
finally:
 print("code done")



 




    
    

    


    