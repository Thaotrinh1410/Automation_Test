from selenium.webdriver.common.by import By

class RegisterPage():
    def __init__(self, driver):
        self.driver = driver
        
        self.firstname = "//*[@id='firstName']"
        self.lastname = "//*[@id='lastName']"
        self.gender =".//*[@id='genterWrapper']//label[contains(text(),'Female')]"
        self.phone_id = "userNumber"
        self.submit = "//button[@id='submit']"
        
        
    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH,(self.firstname)).clear()
        self.driver.find_element(By.XPATH,(self.firstname)).send_keys(firstname)
        
    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH,(self.lastname)).clear()
        self.driver.find_element(By.XPATH,(self.lastname)).send_keys(lastname)
        
    def enter_gender(self):
        self.driver.find_element(By.XPATH,(self.gender)).click()
        
    def enter_phone(self, phone):
        self.driver.find_element(By.ID,(self.phone_id)).clear()
        self.driver.find_element(By.ID,(self.phone_id)).send_keys(phone)
        
    def enter_submit(self):
        self.driver.find_element(By.XPATH,(self.submit)).click()