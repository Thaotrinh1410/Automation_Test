from selenium import webdriver
import time

# chạy trình duyệt Chrome
driver = webdriver.Chrome("chromedriver")
url = "https://demoqa.com/"

# mở trang web
driver.get(url)

# Khởi tạo 1 biến và in ra tiêu đề và độ dài tiêu đề trang web
get_title = driver.title
print(get_title , " " ,len(get_title)) 

# print(driver.current_url) # đọc url web

# Lấy Url trang web và xác minh xem đó có phải là một trang chính xác được mở hay không
actualUrl = driver.current_url
if (actualUrl == url):
    print (" Chinh xac ròi")
else:
    print("Sai ròi kia")
print(actualUrl)
print(url)


# print(driver.page_source) # đọc source 

time.sleep(10)
# driver.quit()
# driver.close()
