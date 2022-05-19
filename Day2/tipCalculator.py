print("\nWelcome to the tip calculator.\n")
while True:
    try:
        bill_total = float(input("What was the bill total? $"))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again.")

while True:
    try:
        tip = int(input("What percentage would you like to tip? "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again.")

while True:
    try:
        num_people = int(input("How many people are paying the bill? "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again.")

amount = (tip/100 * bill_total + bill_total)/num_people
rounded_amount = "{:.2f}".format(amount)

if num_people > 1:
    print(f"Everyone will pay ${rounded_amount}")
else:
    print(f"You will pay ${rounded_amount}")