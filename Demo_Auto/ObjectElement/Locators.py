from selenium.webdriver.common.by import By

from selenium import webdriver

class Locator():
    
    #Input Name
    firstName = "//*[@id='firstName']"
    lastName = "//*[@id='lastName']"
    #Input Email
    userEmail = "//*[@id='userEmail']"
    #Select RadioButton
    gender_male = ".//*[@id='genterWrapper']//label[contains(text(),'Male')]"
    gender_female = ".//*[@id='genterWrapper']//label[contains(text(),'Female')]"
    gender_Other = ".//*[@id='genterWrapper']//label[contains(text(),'Other')]"
    #Input Phone
    userNumber = "//*[@id='userNumber']"
    #Select Date of Birth
    date_of_birth = "//*[@id='dateOfBirthInput']"
    #Input Subjects
    subjects = "//*[@id='subjectsContainer']/div/div[1]"
    #Select Checkbox
    hobby_sports = ".//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]"
    hobby_read = ".//*[@id='hobbiesWrapper']//label[contains(text(),'Reading')]"
    hobby_music = ".//*[@id='hobbiesWrapper']//label[contains(text(),'Music')]"
    
    
        
    def Register_Page(self):
        self.add_firstname(self.firstName,"trinh")
        self.add_lastname(self.lastName,"nguyen")
        self.add_email(self.userEmail,"trinh@gmail.com")
        self.click()
        
        
        
        