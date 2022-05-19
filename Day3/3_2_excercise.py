# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float = float(height)
weight_float = float(weight)

bmi = round(weight_float / height_float ** 2,2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underwight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")