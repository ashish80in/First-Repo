# Input:
# "python is easy and python is very easy"
# Output:
# {'python': 2, 'easy': 2, 'is': 1, 'and': 1, 'very': 1}
sentence = "python is easy and python is very easy"
words = sentence.split()
print(words)

freq = {} 

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# Create a dictionary with student names as keys and their marks as values.
# Write a program that:
# •	Calculates the average marks
# •	Prints names of students scoring above average
# dict1={"ashish":89,
#        "manjot":88,
#        "tanish":87,
#        "sukh":85,
#        "dikshit":85,
# }
# average=sum(dict1.values())/len(dict1)
# print(average)
# above=[marks: for marks in dict1.values() if marks>average]
# print(above)
# above1=[name for name,marks in dict1.items()if marks>average]
# print(above1)

first={'a': 50, 'b': 30, 'c': 70}
second={'b': 60, 'c': 65, 'd': 40}
third={}
comb={}
print(comb)




