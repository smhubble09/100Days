import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.com/EVGA-GeForce-10G-P5-3897-KL-Technology-Backplate/dp/B097S6JDMV"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    "Accept-Language": "en-US,en;q=0.9",
}
LOWEST_PRICE = 800.00
MY_EMAIL = "test@email.com"
PASSWORD = "NotA Password#41"

response = requests.get(url=PRODUCT_URL, headers=HEADERS)
webpage = response.text

#Get price and name of item
soup = BeautifulSoup(webpage, "lxml")

product_name_span = soup.find(name="span", id="productTitle")
product_name = product_name_span.text.strip()

price_span = soup.find(name="span", class_="a-offscreen")
price = float(price_span.text.split("$")[1])

if price <= LOWEST_PRICE:
    message = f"The price for '{product_name}' is currently ${price}. Buy now!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=MY_EMAIL, 
                msg=f"Subject:Low Price on Amazon\n\n{message}")