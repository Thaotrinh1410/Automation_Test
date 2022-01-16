from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from .Locators import Locators

class RegisterPage(object):
    def __init__(self, driver):
        self.driver = driver
             
    def enter_firstname(self, firstname):
        
        self.driver.find_element(By.XPATH,(Locators.firstname)).clear()
        self.driver.find_element(By.XPATH,(Locators.firstname)).send_keys(firstname)
        
    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH,(Locators.lastname)).clear()
        self.driver.find_element(By.XPATH,(Locators.lastname)).send_keys(lastname)
        
    def enter_gender(self):
        self.driver.find_element(By.XPATH,(Locators.gender)).click()
        
    def enter_phone(self, phone):
        self.driver.find_element(By.ID,(Locators.phone_id)).clear()
        self.driver.find_element(By.ID,(Locators.phone_id)).send_keys(phone)
        
    def enter_submit(self):
        
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.driver.find_element(By.XPATH,(Locators.submit)).click()
        
    def find_title(self):
        self.driver.find_element(By.XPATH,(Locators.title_submit_success)).text
        
        
        