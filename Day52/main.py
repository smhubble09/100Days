from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "spacex"
INSTA_USERNAME = "USERNAME"
INSTA_PASSWORD = "PASSWORD"
CHROME_DRIVER_PATH = "DRIVER PATH"

class InstaFollower:
    def __init__(self) -> None:
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        login_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        pwd = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_name.send_keys(INSTA_USERNAME)
        pwd.send_keys(INSTA_PASSWORD)
        #Click login
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        #Don't save login info
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        #Don't allow notifications
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "._a9-z ._a9_1").click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(3)
        #Scrolling to the bottom no longer works in Instagram
        # popup = self.driver.find_element(By.CSS_SELECTOR, "._aano")
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        print(all_buttons)
        for button in all_buttons:
            try:
                print(button)
                button.click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.CSS_SELECTOR, "button ._a9_1").click()
            finally:
                sleep(1)


bot = InstaFollower()


bot.login()

bot.find_followers()

bot.follow()

