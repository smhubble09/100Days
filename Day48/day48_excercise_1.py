from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("Driver Location")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

event_html = driver.find_element(By.CSS_SELECTOR, "div.event-widget")

#Put event dates in list
dates = event_html.find_elements(By.CSS_SELECTOR, "time")
event_dates = [date.get_attribute("datetime").split("T")[0] for date in dates]

#Put event names in list
names = event_html.find_elements(By.CSS_SELECTOR, "li a")
event_names = [name.get_attribute('innerHTML') for name in names]

#Put name and dates in dict
events = {x: {"date": event_dates[x],"name": event_names[x]} for x in range(len(event_dates))}

print(events)
driver.quit()