from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

userName = "Thảo Trinh"
password = "123456"

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"

# mở trang web
driver.get(url)

#input username
driver.find_element(By.ID, "user-name").send_keys(userName)
#input password
driver.find_element(By.ID, "password").send_keys(password)


driver.find_element_by_id("login-button").click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Epic sadface: Username and password do not match any user in this service"

errors = driver.find_elements(By.CLASS_NAME,"error-message-container error")
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

time.sleep(10)  
