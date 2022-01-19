
import email
from selenium.webdriver.common.by import By

class Locators():
        
        firstname = "//*[@id='firstName']"
        lastname = "//*[@id='lastName']"
        email = "userEmail"
        gender =".//*[@id='genterWrapper']//label[contains(text(),'Female')]"
        phone_id = "userNumber"
        check_box = ".//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]"
        choose_file = "//div[@class='form-file']/input[@id='uploadPicture']"
        submit = "//*[@id='submit']"
        title_submit_success = "//*[@id='example-modal-sizes-title-lg']"
        