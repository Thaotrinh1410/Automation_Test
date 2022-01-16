from selenium import webdriver
# from selenium.webdriver.common.by import By
import time


# chạy trình duyệt Chrome
driver = webdriver.Chrome("chromedriver")
url = "https://demoqa.com/browser-windows/"

# mở trang web
driver.get(url)

driver.find_element_by_id("tabButton").click()
time.sleep(3)
driver.forward()
Verifi = driver.find_element_by_xpath(".//h1")
Verifi1 = "This is a sample page"
Verifi = Verifi.text
if(Verifi == Verifi1):
    print("Pass")
else:
    print("Failed")

time.sleep(10)
# driver.quit()