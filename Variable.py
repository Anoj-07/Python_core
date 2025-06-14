# name = "Anoj"
# age = 22
# price = 19.99
# is_active = True

# print ("My name is" ,name ,"\n","I am", age, "I bought apple price of ", price)
# print(type(name))


#Assignment 1 :
# #Create variables for your favorite book (title, pages, rating).

# Print: "My favorite book is [title] with [pages] pages. Rating: [rating]/5."

title = "Love"
pages = 22
rating = 2.4

print("My favorite book is", title , "with", pages, "pages. Rating:",rating,"/5.")

#---------------------------------------------------------
#Assignment 2: If else 
# Write code that checks if a number is positive, negative, or zero
a = 1
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else :
    print("Zero")


#------------------------------------------------------------
# Assignment 3: loops
# Print number 1 -10 using for and while

for i in range(1, 11):
    print("for loop", i )

print()

i = 1
while i < 11:
    print("while loop", i)
    i +=1 


#Task => Create a program to process items in a shopping cart using loops and python foundations.
# Requirements
'''
1. create a shopping cart with items(each item is a dictionary with name, price, and quantity)
2. use loops to:
- Calculate the total cost
- Apply discounts
- Generate a receipt
- print an itemized bill with the grand total
'''

# disctionary in list
carts = [{"name": "Tshirt", "price": 28.4, "quantity": 5},
         {"name": "Pant", "price": 30.32, "quantity": 3},
         {"name": "shoes", "price": 22.23, "quantity": 2}
         ]


total_cost = 0
discount_apply = 0.10

print()
print("======RECEIPT======")

for items in carts:
    sub_total = items["price"] * items["quantity"]
    total_cost += sub_total # used for discount purpose
    print(f"{items["name"]} X {items['quantity']}: ${sub_total:.2f}")
   
print("--------------------") 
print(f"Total Cost: ${total_cost:.2f}")

#Apply for discount
if total_cost > 100:
    discount_amount = total_cost * discount_apply
    total_cost -= discount_amount
    print(f"\nDiscount (10%): -${discount_amount:.2f}")

print("---------------------")
print(f"TOTAL: $ {total_cost:.2f}")
print("=--------------------=")


# -----------------------------------------------------------
#Function 
# Example : Create a function area_rectangle(length, width) that returns the area.

def area_rectangele(length, width):
    return f"Area: {length * width}"

print(area_rectangele(12, 7))