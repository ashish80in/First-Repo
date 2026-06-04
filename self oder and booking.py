# name=input("enter you name")
# print("Choose your class:")
# print("1first Class-1500")
# print("2second Class-100")
# print("3sleeper Class-500")
# choice = int(input("enter your choice (1-3): "))
# if choice == 1:
#     fare = 1500
#     print("You selected first Class.")
# elif choice == 2:
#     fare = 100
#     print("You selected second Class.")
# elif choice == 3:
#     fare = 500
#     print("You selected sleeper Class.")

# age = int(input("Enter passenger age:"))

# if age < 5:
#     fare = 0
#     print("ticket is free")
# elif age >= 60:
#     fare = fare * 0.8 
#     print(" discount applied ")

# meal = input("Do you want to add a meal")
# if meal == "yes":
#     fare += 200
#     print("Meal added ")
# print(f"Final Ticket Price = {fare}")

# questation last

# print("1.whopper burger is of 150")
# print("2.crisp veg is of 100")
# print("3.chicken wings is of 120")
# choice = int(input("Enter your choice (1-3):"))

# if choice == 1:
#     price = 150
#     print("whopper burger is added")
# elif choice == 2:
#     price = 100
#     print("Crisp veg is added")
# elif choice == 3:
#     price = 120
#     print("Chicken wings are added")

# quan = int(input("Enter your quantity: "))
# price = price * quan
# code = input("Do you have any coupon code ")

# if code == "yes":
#     coupon = input("Enter your coupon code: ")
#     if coupon == "KING50":
#         print("discount applied of 50%")
#         price = price - (price * 50 / 100)
        
# print("Final price:", price)
# print("thank you for coming PLEASE COME AGAIN 🍟")



#applying different code

print("1.whopper burger is of 150")
print("2.crisp veg is of 100")
print("3.chicken wings is of 120")
choice = int(input("Enter your choice (1-3):"))

if choice == 1:
    price = 150
    print("whopper burger is added")
elif choice == 2:
    price = 100
    print("Crisp veg is added")
elif choice == 3:
    price = 120
    print("Chicken wings are added")

quan = int(input("Enter your quantity: "))
price = price * quan
code = input("Do you have any coupon code ")

if code == "yes":
    coupon = input("Enter your coupon code: ")
    if coupon == "KING50":
        print("discount applied of 50%")
        price = price - (price * 50 / 100)
    elif coupon == "KING60":
         print("discount applied of 60%")
         price = price - (price*60/100)
        
print("Final price:", price)
print("thank you for coming PLEASE COME AGAIN 🍟")
