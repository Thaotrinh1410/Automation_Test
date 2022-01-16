from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("chromedriver")
#Step1: Open web

driver.get("https://demoqa.com/automation-practice-form")

WebDriverWait(driver, 10)
driver.find_element(By.XPATH, ".//*[@id='genterWrapper']//label[contains(text(),'Male')]").click()
time.sleep(3)
# var = driver.find_element(By.XPATH, ".//*[@id='genterWrapper']//label[contains(text(),'Male')]")
# print(var.is_selected())
