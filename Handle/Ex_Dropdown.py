from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select



class DemoDropdown():
    def demo_dropdown(self):
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://demoqa.com/automation-practice-form")
        WebDriverWait(driver, 10)
        
        Select(driver.find_element(By.XPATH, "")).select_by_index(2)
        
       
        time.sleep(3)    
        
dddemo = DemoDropdown()
dddemo.demo_dropdown()