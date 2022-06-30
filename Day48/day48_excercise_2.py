from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("Driver Location")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname_input = driver.find_element(By.NAME, "fName")
lname_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.CSS_SELECTOR, "button")

fname_input.send_keys("My First Name")
lname_input.send_keys("My Last Name")
email_input.send_keys("myemail@email.com")
btn.click()

#driver.quit()