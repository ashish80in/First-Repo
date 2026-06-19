# inheritance

# class animal:
#     def eat(self):
#         print("animal is eating")

# class dog(animal):
#      def bark(self):
#         print("dog is barking")

# Dog=dog()

# Dog.eat()
# Dog.bark()

# 2.

# class person:
#     def man():
#         print("i am a man")

# class student(person):
#     def study():
#         print("i am studying")

# Student=student()
# student.man()
# student.study()

# Create a class Animal with attributes name and age.
# Create a child class Dog that inherits these attributes and adds a method bark().

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"may name is{self.name}")
#         print(f"may age is{self.age}")
# class dog(Animal):
#     def bark(self):
#         print("dog is barking")

# Dog = dog("ashish",22)
# Dog.display()
# Dog.bark()

# 3.

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"Name: {self.name}")


# class Employee(Person):
#     def __init__(self, name):
#         super().__init__(name)

#     def work(self):
#         print("Employee is working")


# class Manager(Employee):
#     def manage(self):
#         print("Manager is managing the team")


# manager = Manager("Ashish")
# manager.display()
# manager.work()
# manager.manage()


# ======================================= Encapsulation ======================================
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
    
#     def set_marks(self,marks):
#         if 0<= marks <=100:
#            self.__marks=marks
#         else:
#             print("invalid marks")



# BANK ACCOUNT

# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposite(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#         else:
#             print("no sufficient balance")
#     def show_balance(self):
#         print("balance",self.__balance)

# account=bankaccount(1000)

# account.deposite(500)
# account.withdraw(900)
# account.show_balance()


# CAR SPEED


# class car:
#     def __init__(self,speed):
#         self.__speed=speed
#     def set_speed(self,speed):
#         if speed<=200:
#             self.__speed=speed
#         else:
#             print("error")

#     def show_speed(self):
#         print("speed",self.__speed)
# c=car(100)

# c.show_speed()
# c.set_speed(150)
# c.show_speed()
# c.set_speed(250)
# c.show_speed()

# 

class car:
    def __init__(self,speed):
        self.__speed=speed
        
    def accelerate(self):
        self.__speed+=20
    def brake(self):
        self.__speed -=20
    def show_speed(self):
        print("speed",self.__speed)

c=car(50)
c.show_speed()
c.accelerate()
c.show_speed()
c.brake()
c.show_speed()

        

    
    
        

    










    




        

    






