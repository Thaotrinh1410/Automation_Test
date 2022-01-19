from lib2to3.pgen2 import driver
from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import re
import time
import unittest
import sys

sys.path.append("../")
from Pagess import RegisterPage
from Pagess import Locators

class RegisterTest(unittest.TestCase):
       
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Selenium_AutoTest\chromedriver.exe")
        # self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
    
        
    def test_case1(self):
        
        driver = self.driver
        # driver.get("https://demoqa.com/automation-practice-form")        
        register = RegisterPage(driver)
        firstname = register.enter_firstname("trinh")       
        register.enter_lastname("ng")
        useremail = register.enter_useremail("trinh@gmail.com")
        register.enter_gender()       
        phone = register.enter_phone("1234567892")
        checkbox = register.click_checkbox()
        # register.choose_file()
        path_file = "C:\\Users\\asus_vienthonga\\Pictures\\Capture.PNG"
        register.choose_file(path_file)
        register.enter_submit()
        time.sleep(10)
    
        
        # color = driver.find_element(By.XPATH,"").value_of_css_property('color')       
        # print(color)
        # hex = Color.from_string(color).hex
        # print(hex)
        # color_pass = "#28a745"
        
        value_file = driver.find_element(By.XPATH,"//tbody/tr[8]/td[2]")
        get_file = value_file.text
        print(get_file)
        
        if(path_file == get_file):
            print("Testcase Pass")
        else:
            print("Testcase Fail")
        
       
                    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()
          