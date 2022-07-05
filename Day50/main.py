from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

FB_EMAIL = "FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "FACEBOOK PASSWORD"

service = Service("Driver Location")
driver = webdriver.Chrome(service=service)

driver.get("http://www.tinder.com")

#Login to Tinder
sleep(2)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
#Login via Facebook
sleep(2)
driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
#Switch screen to FB login page
sleep(2)
tinder_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
#Type in email and password
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
#Switch back to Tinder window
driver.switch_to.window(tinder_window)

sleep(5)
#Allow location
driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
#Disallow notifications
driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
#Allow cookies
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

#Tinder free only allows 100 likes per day
for n in range(100):
    #Add 1 second delay between swipes
    sleep(1)

    try:
        #Click like button
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    #Catches when the "Matched" pop-up shows
    except ElementClickInterceptedException:
        try:
            #Clear pop-up
            driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
            
driver.quit()