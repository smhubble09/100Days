from speedtest import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 20
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

print(f"Down: {bot.down}")
print(f"Up: {bot.up}")

if bot.down < PROMISED_DOWN:
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_UP, PROMISED_DOWN)