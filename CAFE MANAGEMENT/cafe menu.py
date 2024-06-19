# menu of cafe
# in dictionary 
menu={
    'Pizza':250,
    'Pasta':200,
    'Coffee':90,
    'Burger':150,
    'ColdDrinks':50,
    'GarlicBread':200,
    'ChocoLavaCake':120,
    'ColdCoco':100,
    'Shakes':250
}

#greetings and menu
print("Hello...\n****************************\nWelcome to Urben Cafe")
print("Pizza :: 250\nPasta :: 200\nCoffee :: 90\nBurger :: 150\nColddrinks :: 50\nGarlicBread :: 200\nChocoLavaCake :: 120\nColdCoco :: 100\nShakes ::250")

ordre_total=0

# order 
item_1=input("Enter the name of item witch you want to order :: ")

if item_1 in menu:
    ordre_total+=menu[item_1]
    print(f"Your item {item_1} has been added into your order..")
    
else:
    print(f"Ordered item {item_1} is not available now...")
    
# oredr another item
print("****************************")

another_order=input("Do you want to add another item ?? (Yes/No)")
print("****************************")

if another_order=="Yes":
    item_2=input("Enter the another item name of witch you want to order :: ")
    
    if item_2 in menu:
        ordre_total+=menu[item_2]
        print(f"Your item {item_2} has been added into your order..")
        
    else:
        print(f"Ordered item {item_2} is not available now...")
    
# grand total of item
print(f"Total amount of item is {ordre_total}")
print("****************************")

print(f"You want to pay {ordre_total} Rs.")