import requests
import os
from twilio.rest import Client
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#------------------------- Video Way --------------------------------#
# stock_parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": STOCK_API_KEY,
# }
# stock_response = requests.get("https://www.alphavantage.co/query",stock_parameters)
# stock_response.raise_for_status()
# stock_data = stock_response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key,value) in stock_data.items()]
# yesterday_data = stock_data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# day_before_yesterday_data = stock_data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# #------------------------- My Way --------------------------------#
today = dt.datetime.today()

yesterday_day = today - dt.timedelta(days= 1)
day_before = today - dt.timedelta(days= 2)

yesterday_str = str(yesterday_day.strptime(str(yesterday_day),"%Y-%m-%d %H:%M:%S.%f")).split(" ")[0]
day_before_str = str(day_before.strptime(str(day_before),"%Y-%m-%d %H:%M:%S.%f")).split(" ")[0]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get("https://www.alphavantage.co/query",stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
yesterday_stock = stock_data[yesterday_str]["4. close"]
day_before_stock = stock_data[day_before_str]["4. close"]

stock_percent_difference = round((float(yesterday_stock) - float(day_before_stock))/float(day_before_stock) * 100)
if stock_percent_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(stock_percent_difference) >= 5:
    message = f"{STOCK}: {up_down}{stock_percent_difference}%\n"

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "searchIn": "title",
    }

    news_response = requests.get("https://newsapi.org/v2/everything",news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_three_news = news_data["articles"][:3]

    for item in top_three_news:
        message += f"Headline: {item['title']}\nBrief: {item['description']}\nLink: {item['url']}\n\n"

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    sms_message = client.messages \
        .create(
            body=message,
            from_="NumberGoesHere",
            to="AnotherNumberGoesHere"
        )
    print(message.status)
