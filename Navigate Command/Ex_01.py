from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

url = "https://demoqa.com/"

# mở trang web
driver.get(url)
# driver.get("https://toolsqa.com/selenium-webdriver/selenium-navigation-commands/")
driver.forward()
time.sleep(10)

# driver.navigate().to("https://toolsqa.com/selenium-webdriver/")