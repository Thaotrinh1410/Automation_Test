from selenium.webdriver.common.by import By
from Demo_Auto.ObjectElement.Locators import Locator


class Register(object):
    def __init__(self, driver):
        self.driver = driver
        self.firstname = driver.find_element(By.XPATH, Locator.firstName)
        self.lastname = driver.find_element(By.XPATH, Locator.lastName)
        self.useremail = driver.find_element(By.XPATH, Locator.userEmail)
        self.gender = driver.find_element(By.XPATH, Locator.gender_female)
        self.phone = driver.find_element(By.XPATH, Locator.userNumber)
        
    def getFirstName(self):
        return self.firstname
    
    def getLasrName(self):
        return self.lastname
    
    def getUserEmail(self):
        return self.useremail
        
        
    def getGender(self):
        return self.gender
    
    def getPhone(self):
        return self.phone