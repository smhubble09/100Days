import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()

day_of_week = now.weekday()

if day_of_week == 0:
    with open("Day32/quotes.txt") as data_file:
        data = data_file.readlines()

    quote = choice(data)

    my_email = "test@email.com"
    password = "notApassword!"

    with smtplib.SMTP("smtp.email.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="test@email.com", 
            msg=f"Subject:Monday Quote\n\n{quote}")
