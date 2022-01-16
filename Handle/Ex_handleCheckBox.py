# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# driver = webdriver.Chrome("chromedriver")
# #Step1: Open web

# driver.get("https://demoqa.com/automation-practice-form")

# WebDriverWait(driver, 10)
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[3]/div[2]/div[1]/label').click()

# # driver.find_element(By.ID, "hobbies-checkbox-2").click()
# # driver.find_element(By.ID, "hobbies-checkbox-3").click()

# time.sleep(3)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

class DemoCheckbox():
    def demo_checkbox(self):
        driver = webdriver.Chrome("chromedriver")
        driver.get("https://demoqa.com/automation-practice-form")
        
        WebDriverWait(driver, 10)
        driver.find_element(By.XPATH,".//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]").click()
        # time.sleep(4)
        # var1 = driver.find_element(By.XPATH,".//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]").is_selected()
        # print(var1)
        time.sleep(3)
        
          
checkbox = DemoCheckbox()
checkbox.demo_checkbox()
        

