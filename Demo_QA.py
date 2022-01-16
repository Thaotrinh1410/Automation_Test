from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

firstName ="    trinh"
list_firstName = list(firstName)
list_regex = [' ','2','3','@','#','$']
lastName ="Nguyễn"
list_lastName = list(lastName)
userEmail ="trinh@gmail.com"
userNumber = "0387242917"

month = "October 2000"
days = "14"
year = "2000"

driver = webdriver.Chrome("chromedriver")
# time.sleep(3)
driver.maximize_window()
# driver.set_window_size(2000, 800)
url = "https://demoqa.com/automation-practice-form"
driver.get(url)

WebDriverWait(driver, 7)
# driver.execute_script("window.scrollTo(0, 200)")

# driver.find_element(By.XPATH, "//div[@class='category-cards']/div[2]").click() 
WebDriverWait(driver, 7)
driver.find_element(By.XPATH, "//div[@id='userName-wrapper']//input[@id='firstName']").send_keys(firstName)
for i in range(len(list_firstName)):
    if(list_firstName[i] in list_regex ):
        print ("Failed - Không được nhập số và kí tự đặc biệt")
    else:
        print("TestCase1 - Passed")
        
WebDriverWait(driver, 7)
driver.find_element(By.ID, "lastName").send_keys(lastName)   
for i in range(len(list_lastName)):
    if(list_lastName[i] in list_regex):
        print("Failed - Không được nhập số và kí tự đặc biệt")
    else:
        print("TestCase2 - Passed")

WebDriverWait(driver, 7)
driver.find_element(By.ID, "userEmail").send_keys(userEmail) 

 
WebDriverWait(driver, 7)
driver.find_element(By.XPATH, ".//*[@id='genterWrapper']//label[contains(text(),'Female')]").click()

WebDriverWait(driver, 7)
driver.find_element(By.ID, "userNumber").send_keys(userNumber)

if len(userNumber) == 10:
    print("Passed")
else:
    print("Yêu cầu nhập đủ 10 kí tự")
    
driver.find_element(By.ID, "dateOfBirthInput").click()
time.sleep(1)
target_month_year = driver.find_element(By.XPATH, "//div[@class='react-datepicker__header']/div[1]")
target_month_year = target_month_year.text
target_month = target_month_year.split()
target_month = target_month[0]
target_year = target_month_year.split()
target_year = target_year[1]
    
while(target_month_year != month):
    if(((int(target_year)) > int(year))):
        previous = driver.find_element(By.XPATH, "//div[@class='react-datepicker']//button[1]")
        previous.click()
            
    else:
        next = driver.find_element(By.XPATH, "//div[@class='react-datepicker']//button[2]")
        next.click()
    break
              
day = driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']/div[@class='react-datepicker__week']/div[contains(string(),'"+days+"')]")
day.click()
    
            
    # if(target_month == month):
    #     day = driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']/div[@class='react-datepicker__week']/div[contains(string(),'"+days+"')]")
    #     day.click()
    # else:
    #     previous = driver.find_element(By.XPATH, "//div[@class='react-datepicker']/button[1]")
    #     previous.click()
    #     time.sleep(2)
    #     target_month = driver.find_element(By.XPATH, "//div[@class='react-datepicker__header']/div[1]")
    #     target_month = target_month.text
    #     if(target_month == month):
    #         day = driver.find_element(By.XPATH, "//div[@class='react-datepicker__month']/div[@class='react-datepicker__week']/div[contains(string(),'"+days+"')]")
    #         day.send_keys(Keys.ENTER)
    
WebDriverWait(driver, 10)
driver.find_element(By.XPATH,".//*[@id='hobbiesWrapper']//label[contains(text(),'Sports')]").click()
driver.find_element(By.XPATH,".//*[@id='hobbiesWrapper']//label[contains(text(),'Reading')]").click()
    
time.sleep(1)
driver.execute_script("window.scrollTo(0, 400)")
# driver.switch_to.frame(2)
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(3)
driver.find_element(By.ID, "close-fixedban").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(2)
driver.find_element(By.ID, "closeLargeModal").click()
time.sleep(5)



    


