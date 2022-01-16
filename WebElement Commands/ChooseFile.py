from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
# import pyautogui

# imagepath = "C:\Picture\fall.PNG"
driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(0.5)
driver.maximize_window()
location = "https://demoqa.com/upload-download"
driver.get(location)

time.sleep(3)
WebDriverWait(driver, 10)
file = driver.find_element(By.XPATH,"//div[@class='form-file']/input[@id='uploadFile']")
file.send_keys("C:\Users\asus_vienthonga\Pictures\exam.PNG")
# file.click()

