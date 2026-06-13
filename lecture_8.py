def separate_section(title):
    print("\n" + " " + "="*20 + title + " " + "="*20)

print("===============functions====================")

# # 1. Lambda Functions
separate_section("1. Lambda Functions")
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression

# # Example: A simple lambda to double a number
double = lambda x:x * 2

print("Double of 5 is:", double(5))

# # # # Example: A lambda to add two numbers
add = lambda a, b, c : a + b + c
print("Sum is:", add(3, 4, 5))

# # # Example: Lambda with if-else
# # # Syntax: lambda arguments : value_if_true if condition else value_if_false


check = lambda a : "even" if a%2==0 else "odd"
print(check(7))




# # 2. Map Function
separate_section("2. Map Function")
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# Syntax: map(function, iterables)


l = ['1','2','3']
convert = map(int, l)
print(tuple(convert))


numbers = [1, 2, 3, 4, 5]

# # Example: Square every number in the list using a normal function
def square(n):
    return n * n

# print(square(5))
squared_numbers = map(square, numbers)
print("Squared with function:", set(squared_numbers))

# Example: Square every number using lambda
# Often used together with map
squared_lambda = map(lambda x: x*x, numbers) # Note: map returns an iterator, so we cast to list
print("Squared with lambda:", list(squared_lambda))


# 3. Filter Function
separate_section("3. Filter Function")
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# Syntax: filter(function, iterable)

ages = (5, 12, 17, 18, 24, 32)

# # Example: Filter adults (>= 18)
def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
print("Adults (using function):", list(adults))

# # Example: Filter even numbers using lambda
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers_list)
print("Even numbers (using lambda):", list(even_numbers))


# 4. Enumerate Function
separate_section("4. Enumerate Function")
# The enumerate() funct ion takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate object yields pairs containing a count (from start, which defaults to 0) and a value yielded by the iterable argument.
# Syntax: enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'cherry']
nset = {"apple", "orange", "banana"}

# Example: Standard enumerate
print("Standard enumerate:")
for index, fruit in enumerate(nset):
    print(index, fruit)

# Example: Enumerate with a custom start index
print("\nEnumerate starting at 1:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)





# students = [("Alice", 25), ("Bob", 20), ("Charlie", 30), ("David", 22)]

# result = sorted(students, key=lambda x: x[1], reverse=True)

# print(result)


# # 5. Zip Function
# separate_section("5. Zip Function")
# # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# # If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# # Syntax: zip(iterable1, iterable2, ...)

# keys = ['name', 'age', 'country']
# values = ['Alice', 25, 'Canada']

# # Example: Zipping two lists into a dictionary or list of tuples
# zipped = zip(keys, values)
# print("Zipped list:", list(zipped))

# # Re-zipping to show dict conversion
# zipped_dict = dict(zip(keys, values))
# print("Zipped dictionary:", zipped_dict)

# # Example: Unzipping using the * operator
# pairs = [('a', 1), ('b', 2), ('c', 3)]
# letters, numbers = zip(*pairs)
# print("Unzipped letters:", letters)
# print("Unzipped numbers:", numbers)

print(separate_section("hello"))












