print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

sizeCost = 0
if size == "S":
   sizeCost = 15
elif size == "M":
    sizeCost = 20
else:
    sizeCost = 25

pepperoniCost = 0;
if size == "S":
   pepperoniCost = 2
elif size == "M":
    pepperoniCost = 3
else:
    pepperoniCost = 3

cheeseCost = 1
totalCost = sizeCost;

if pepperoni == "Y":
    totalCost += pepperoniCost

if extra_cheese == "Y":
    totalCost += cheeseCost

print(f"Your final bill is: ${totalCost}.")