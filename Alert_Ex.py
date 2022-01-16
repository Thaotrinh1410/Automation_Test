from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
location = "https://demoqa.com/alerts"
driver.get(location)

#Click on the "Alert" button to generate the Confirmation Alert
button = driver.find_element(By.ID,"promtButton")
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

time.sleep(2)

obj_text = obj.text
print("Hiển thi "+ obj_text)
obj.send_keys('Trinh')

time.sleep(2)

#Section 1
#use the accept() method to accept the alert``
obj.accept()

#Retrieve the message on the```````` Alert window
# message = obj.text
# print ("Alert shows following message: "+ message )

# time.sleep(2)

# obj.accept()


#get the text returned when OK Button is clicked.
txt = driver.find_element(By.ID,"promptResult")
print(txt.text)

time.sleep(2)

#refresh the webpage
driver.refresh()

# Section 2
# Re-generate the Confirmation Alert
button = driver.find_element(By.ID,"promtButton")
button.click()

time.sleep(2)

#Switch the control to the Alert window
obj = driver.switch_to.alert

# Dismiss the Alert using
obj.dismiss()

# #get the text returned when Cancel Button is clicked.
# txt = driver.find_element_by_id('msg')
# print(txt.text)

driver.close