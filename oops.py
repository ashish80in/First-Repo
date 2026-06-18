
# ------------------------------------------------------------------------------
# 1. Classes, Objects, and 2. Constructors & Instance Attributes
# ------------------------------------------------------------------------------
# - Class: A blueprint for creating objects.
# - Object (Instance): A specific realization of any object.
# - Constructor: The __init__ method is called when creating a new instance.
# - 'self': Refers to the instance itself. It's the first parameter of instance methods.

# class Student:
#     # Constructor
#     def __init__(self, name, age):
#         # Instance attributes (unique to every object)
#         self.name = name
#         self.age = age

#     # Instance Method
#     def introduce(self):
#         return f"Hi, my name is {self.name} and I am {self.age} years old."

# print("--- 1 & 2: Classes, Objects, Constructors ---")
# s1 = Student("Alice", 20)
# s2 = Student("Bob", 22)
# print(s1.introduce())
# print(s2.introduce())


# # ------------------------------------------------------------------------------
# # 3. Class Attributes vs. Instance Attributes
# # ------------------------------------------------------------------------------
# # - Instance attributes are owned by the specific object (defined inside __init__).
# # - Class attributes are shared by ALL instances of the class (defined directly in the class).

# class Employee:
#     # Class attribute: shared by all employees
#     company_name = "Tech Solutions Inc."
#     employee_count = 0

#     def __init__(self, name, salary):
#         self.name = name          # Instance attribute
#         self.salary = salary      # Instance attribute
#         Employee.employee_count += 1  # Access class attribute using the Class name

# print("\n--- 3: Class vs Instance Attributes ---")
# e1 = Employee("John", 50000)
# e2 = Employee("Jane", 60000)

# print(f"Company: {Employee.company_name}") # Access via class
# print(f"e1 works at {e1.company_name}")    # Access via instance
# print(f"Total Employees: {Employee.employee_count}")





        
    