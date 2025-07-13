cafe_menu = {"Tea": 20,
             "Coffee": 30,
             "Chess_pasta": 110,
             "Bread": 50,
             "Pizza": 250,
             "Franch_fryes": 100,
             "Soda_water": 40,}

total_order = []

# print(cafe_menu["Tea"])

while True: 
    order = input("Entre your order sir:= ").title().strip().replace(" ", "_").capitalize()

    if order == "No":
        print("Thank you for the order sir")
        break
    elif order in cafe_menu:
        total_order.append(order)
        print(order, "is added in your order. Anything else sir ?...")
    else:
        print("Sorry sir", order, "is not available right now.")

    
print("your final oredr is ", total_order)
print("This is your bill sir....", "please came again")

price = []
sum = 0 

for i in total_order:
    price = cafe_menu[i] 
    sum = price + sum
    
final_bill = sum
print("Thank you sir your final bill is", final_bill)
