from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")
time.sleep(3)
driver.maximize_window()
url = "https://demoqa.com/automation-practice-form"
driver.get(url)

firstName =""

WebDriverWait(driver, 7)
driver.find_element(By.XPATH,"//div[@id='userName-wrapper']//input[@id='firstName']").send_keys(firstName)
if not firstName:
    print("TestCase Fail")

driver.refresh()





time.sleep(1)
driver.execute_script("window.scrollTo(0, 400)")
# driver.switch_to.frame(2)
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(3)
# driver.find_element(By.ID,"close-fixedban").click()
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 300)")
# time.sleep(2)
# driver.find_element(By.ID,"closeLargeModal").click()
# time.sleep(5)