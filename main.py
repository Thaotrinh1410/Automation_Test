from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

email = "thaotrinh242917@gmail.com"
password = "chinhchinh1410200"
driver = webdriver.Chrome("chromedriver")
#Step1: Open web
driver.get("https://github.com/login")
#Step2: input email
driver.find_element(By.ID, "login_field").send_keys(email)
# driver.find_element(By.id,"login_field").send_keys('thaotrinh242917@gmail.com')

#Step3: input password
driver.find_element(By.ID, "password").send_keys(password)
# driver.find_element_by_id("password").send_keys('chinhchinh14102000')

#Step4: click login
driver.find_element(By.NAME, "commit").click()
# driver.find_element_by_name("commit").click()
time.sleep(10)

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."

errors = driver.find_elements(By.CLASS_NAME,"flash-error")
if any(error_message in e.text for e in errors):
    print("Login failed")
else:
    print("Login successful")

# driver.close()
