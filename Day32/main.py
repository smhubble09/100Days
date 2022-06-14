import datetime as dt
from random import choice, randint
import pandas
import smtplib
##################### Extra Hard Starting Project ######################
PLACEHOLDER = "[NAME]"
# 1. Update the birthdays.csv
data = pandas.read_csv("Day32/birthdays.csv")  
birthdays_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

today_date = now.day
today_month = now.month

for item in birthdays_dict:
    if today_month == item["month"]:
        if today_date == item["day"]:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            letter_choice = randint(1,3)
            with open(f"Day32/letter_templates/letter_{letter_choice}.txt") as letter_file:
                starting_letter = letter_file.read()
                stripped_name = item["name"].strip()
                email_text = starting_letter.replace(PLACEHOLDER, stripped_name)
            
            # 4. Send the letter generated in step 3 to that person's email address.
            my_email = "test@email.com"
            password = "FAKEpassword2!"

            with smtplib.SMTP("smtp.test.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="test@email.com", 
                    msg=f"Subject:Happy Birthday!\n\n{email_text}")
