from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

EMAIL = "LOGIN EMAIL"
PASSWORD = "LOGIN PASSWORD"

service = Service("Driver Location")
driver = webdriver.Chrome(service=service)
#Sign in
driver.get("https://www.linkedin.com/jobs/search/?distance=25.0&f_AL=true&f_E=1&geoId=103644278&keywords=software%20engineer")
sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/a[1]").click()
#Input username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(EMAIL)
#Input password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)
#Sign in
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

all_listings = driver.find_element(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    #Click the job on side panel
    listing.click()
    sleep(2)
    #Find Easy Apply button
    try:
        driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
        #Don't follow company
        driver.find_element(By.ID, "follow-company-checkbox").click()
        #Submit application
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        #If submit button is a "next" button, then skip
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
            sleep(1)
            driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn").click()
            print("Complex application - Skipped.")
            continue
        else:
            submit_button.click()

        #Once application completed, close the pop-up window.
        sleep(1)
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
    
    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button - Skipped.")
        continue

sleep(5)
driver.quit()