import unittest
from selenium import webdriver
import time


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        
    def tearDown(self):
        if(self.driver != None):
            print(" Set up environment!!!")
            self.driver.close()
            self.driver.quit()