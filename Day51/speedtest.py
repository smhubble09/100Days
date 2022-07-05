from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "DRIVER LOCATION"

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        #Start speed test
        self.driver.find_element(By.CLASS_NAME, ".js-start-test").click()
        #Wait and get results
        sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, ".download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, ".upload-speed").text

        self.driver.quit()

    def tweet_at_provider(self, useremail, password, up , down):
        self.driver.get("https://twitter.com/i/flow/login")
        #Enter email
        sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(useremail)
        email.send_keys(Keys.ENTER)
        #Enter password
        sleep(2)
        pwd = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pwd.send_keys(password)
        pwd.send_keys(Keys.ENTER)

        #Tweet
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {down}down/{up}up?")
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
        
        sleep(2)
        self.driver.quit()