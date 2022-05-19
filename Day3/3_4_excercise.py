# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill_total = 0

if size == "S":
    bill_total += 15
    if add_pepperoni == "Y":
        bill_total += 2
elif size == "M":
    bill_total += 20
    if add_pepperoni == "Y":
        bill_total += 3
else:
    bill_total += 25
    if add_pepperoni == "Y":
        bill_total += 3

if extra_cheese == "Y":
    bill_total += 1

print(f"Your final bill is: ${bill_total}.")