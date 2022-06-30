import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TIMEOUT = time.time() + 60*5

service = Service("Driver Location")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")
money = driver.find_element(By.ID, "money")

#Get upgrade item ids
store_items = store.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in store_items]

item_prices = []

for item in store_items:
    item_ids.append(f'buy{item.text.split(" - ")[0]}')

check_now = time.time() + 3

while True:
    cookie.click()
    #Quit at 5 min
    if time.time() > TIMEOUT:
        cookies_per_s = driver.find_element(By.ID, "cps")
        print(cookies_per_s.text)
        break
    #Every 5 seconds
    elif time.time() > check_now:
         #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        try:
            highest_price_affordable_upgrade = max(affordable_upgrades)
        except ValueError:
            pass
        else:
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        check_now = time.time() + 3
    
driver.quit()