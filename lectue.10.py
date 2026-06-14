# =============================REGEX OPERATION=========================================
import re
# numbers=input("enter your numbers").split(" ")
# print(numbers)
# pattern=r"^\d{10}$"
# if re.match(pattern, numbers):
#  print(numbers,"number is valid")
# else:
#  print(numbers, "is NOT valid")


gmail="[a-zA-z0-9._]+@gmail.com"
st1="mail id is ashish@gmail.com and wefew@codermail.com"
print(re.findall(gmail,st1))