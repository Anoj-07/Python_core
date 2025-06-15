# Closures is a function having acess to the  scope (variable) of its parent
# Function after the parent function has retured

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins # non local is used to access or modify local variable in nested function only
        coins -= 1

        if coins > 1:
            print("\n" , person , "has" , str(coins) , " coins left.")
            
        elif coins == 1 :
            print("\n" , person , "has " + str(coins) , " coins left.")
        else:
            print("\n" , person , " is out of coins")
        
    return play_game

anoj = parent_function("Anoj")
anoj()


@parent_function
def hi():
    print("Paru")

Hi = parent_function("paru")
Hi()



#---- Don't want to create new object 
# def parent_function(person):
#     coins = 3

#     def play_game():
#         nonlocal coins
#         coins -= 1

#         person()  # Call the decorated function

#         if coins > 1:
#             print("\n", person.__name__, "has", str(coins), " coins left.")
#         elif coins == 1:
#             print("\n", person.__name__, "has" + str(coins), " coins left.")
#         else:
#             print("\n", person.__name__, " is out of coins")

#     return play_game

# @parent_function
# def hi():
#     print("paru")





