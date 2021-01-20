# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
small_pizza_pepperoni = 2
medium_to_large_pizza_pepperoni = 3

if size == "S" or size == "s":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill = small_pizza + small_pizza_pepperoni
    elif add_pepperoni == "N" or add_pepperoni == "n":
        final_bill += small_pizza
    print(f"Your final bill is: {final_bill}")

if size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill = medium_pizza + medium_to_large_pizza_pepperoni
    elif add_pepperoni == "N" or add_pepperoni == "n":
        final_bill += medium_pizza
    print(f"Your final bill is: {final_bill}")

if size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill = large_pizza + medium_to_large_pizza_pepperoni
    elif add_pepperoni == "N" or add_pepperoni == "n":
        final_bill += large_pizza
    print(f"Your final bill is: ${final_bill}")