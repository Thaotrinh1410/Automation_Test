from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import sys
from DEMOO.POMDemo.Pagess.RegisterPage import RegisterPage


class RegisterTest(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Selenium_AutoTest\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def test_register(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        
        register = RegisterPage(driver)
        register.enter_firstname("trinh")
        register.enter_lastname("ng")
        register.enter_gender()
        register.enter_phone("0123456789")
        register.enter_submit()
#         self.driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("trinh")
#         self.driver.find_element(By.XPATH,"//*[@id='lastName']").send_keys("ng")
#         WebDriverWait(self.driver, 7)
#         self.driver.find_element(By.XPATH, ".//*[@id='genterWrapper']//label[contains(text(),'Female')]").click()
#         WebDriverWait(self.driver, 7)
#         self.driver.find_element(By.ID, "userNumber").send_keys("0123456789")
#         time.sleep(1)
#         self.driver.execute_script("window.scrollTo(0, 400)")
# # driver.switch_to.frame(2)
#         self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
#         time.sleep(3)
#         self.driver.find_element(By.ID, "close-fixedban").click()
#         time.sleep(2)
#         self.driver.execute_script("window.scrollTo(0, 300)")
#         time.sleep(2)
#         self.driver.find_element(By.ID, "closeLargeModal").click()
#         time.sleep(5) 
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()
          







