#Real-World Task: Create a function-driven system to process orders in an online store using core Python concepts.
# to learn core concept of python 
#Mini Ecommerce Console App with Login + Qunatity + Remove Items

#Login Part
valid_user = ["anoj,", "rawal", "Paru"]

def login():
    user_name = input("Enter userName: ")
    if user_name in valid_user:
        print("Login successfully")
        return True
    else:
        print("Authoried deined")
        return False


# Product List = Each product is a dictionary with list like id, name, and price

products = [
    {"id":1, "name":"laptop", "price":128.2},
    {"id":2, "name":"mouse", "price":20.5},
    {"id":3, "name":"keyboard", "price":35.6},
    {"id":4, "name":"Samsung S25 ultra", "price":250.4},
    {"id":5, "name":"HeadPhone", "price":44.6},
] 

# cart to hold items addes by user- conatins list of dectionaries with products and quantity
cart = []

#function to display available products
def show_product():
    print("Available product")
    for product in products:
        print(f"{product["id"]} {product["name"]} Rs.{product["price"]}")
    print()


#function to add a product to cart (with quantity support)
def add_to_cart(product_id, quantity):
    for p in products:
        if p["id"] == product_id: # if user input matches p['id'] 
             # if product is already in cart, increase qunatity
             for item in cart:
                 if item["product"]["id"] == product_id: 
                     item["quantity"] += quantity
                     print(f"Added {quantity} more {p['name']} to cart.\n")
                     return

                # if not there it will add     
             cart.append({"product": p, "quantity": quantity})
             print(f"{p['name']} (X{quantity}) added to cart!\n")
             return
    print("Product not found \n")

#function to view all items in the cart
def view_cart():
    if not cart:
        print("Your cart is empty! \n")
        return
    
    print("\n your cart")
    total = 0 # track total cost

