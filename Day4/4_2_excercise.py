# Split string method
from random import randint

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number = randint(0,(len(names) -1))
winner = names[number]

print(f"{winner}'s going to buy the meal today!")