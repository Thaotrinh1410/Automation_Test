from Demo_Auto.TestCase.Page import Register
from ObjectElement.WebDriverSetup import WebDriverSetup
import unittest
from selenium import webdriver
import time


class Register_Page(WebDriverSetup):
    def test_Form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        driver.set_page_load_timeout(30)
        
        register = Register(driver)
        register.firstname.send_keys("trinh")
        time.sleep(2)
        register.lastname.send_keys("ng")
        register.useremail.send_keys("r@gmail.com")
        register.gender.click()
        register.phone.send_keys("0954738245")
        time.sleep(5)
        
        
if __name__ =='__main__':
    unittest.main()
        

