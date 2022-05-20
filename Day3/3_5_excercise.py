# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2
lowecase_name = combined_string.lower()

t_count = lowecase_name.count("t")
r_count = lowecase_name.count("r")
u_count = lowecase_name.count("u")
e_count = lowecase_name.count("e")
true_count = t_count + r_count + u_count + e_count
l_count = lowecase_name.count("l")
o_count = lowecase_name.count("o")
v_count = lowecase_name.count("v")
love_count = l_count + o_count + v_count + e_count
score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
