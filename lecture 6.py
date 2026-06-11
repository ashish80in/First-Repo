# DICTIONARY =======================================
# dictionary- {},key : value_pairs

# dict1={"name":"ashish","age":20,"class":"python"}
# print(dict1)
# print(dict1["class"])


# dict1.update(name="ashish sharma")
# print(dict1)

# dict1["class"]="py"
# print(dict1)

# dict1.pop("class")
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# dict2 ={"name":{"first name":"ashish","last name":"sharma"}
#         ,"class":{"first class":"python","second class":"c++"}
#         }
# print(dict2["class"]["second class"])

# dict3={i**2:i for i in range (5)if i%2==0}
# print(dict3)

# a=["a","b","c"]
# b=[1,2,3]
# combine={i:j for i ,j in  zip(a,b)}
# print(combine)

dict={}
for i in range(5):
   dict[int(input("enter the index value"))]=input("enter the name")
print(dict)
print(dict[3])
