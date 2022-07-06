from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from types import NoneType
from bs4 import BeautifulSoup
import requests
import lxml
import json

GOOGLE_FORM = "FORM PATH"
CHROME_DRIVER_PATH = "DRIVER PATH"
ZILLOW_URL = "https://www.zillow.com/marietta-ga/houses/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Marietta%2C%20GA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.73156631103515%2C%22east%22%3A-84.32987868896484%2C%22south%22%3A33.84983122976891%2C%22north%22%3A34.07819882370733%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12562%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A670000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2929%7D%2C%22hoa%22%3A%7B%22max%22%3A0%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A3%7D%2C%22sqft%22%3A%7B%22min%22%3A1500%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22gar%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    "Accept-Language": "en-US,en;q=0.9",
}

class GoogleForm:
    def __init__(self) -> None:
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def input_listings(self, listings):
        for item in listings:
            self.driver.get(GOOGLE_FORM)
            sleep(1)

            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

            address_input.send_keys(item["address"])
            price_input.send_keys(item["price"])
            link_input.send_keys(item["link"])
            submit_button.click()
        self.driver.quit()
        
class ZillowGrab:
    def __init__(self) -> None:
        self.all_listings = []
        self.get_listings()


    def get_listings(self):
        response = requests.get(url=ZILLOW_URL, headers=HEADERS)
        zillow_webpage = response.text
        soup = BeautifulSoup(zillow_webpage, "lxml")

        listings = []
        for item in soup.find_all("li"):
            if isinstance(item.script, NoneType):
                pass
            else:
                listings.append(json.loads(item.script.text))

        for item in listings:
            new_dict = {
                "address": item["name"],
                "price": f'${item["floorSize"]["value"]}',
                "link": item["url"],
            }
            self.all_listings.append(new_dict)

zill = ZillowGrab()
form = GoogleForm()

form.input_listings(zill.all_listings)