from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.text
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

upvotes = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.text.split()[0]) for score in upvotes]

largest_num = max(article_upvotes)

index = article_upvotes.index(largest_num)

print(article_links[index])
print(article_texts[index])
print(article_upvotes[index])