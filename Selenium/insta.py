from selenium import webdriver
from Pass import returnpass
import time
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.remote.webelement

print("sample test case started")

path = "D:\\Main_Folders\\siddhant work\\Setup Files\\ChromeDriver\\chromedriver.exe"

driver = webdriver.Chrome(path)

# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size

driver.maximize_window()

# navigate to the url
driver.get("https://www.instagram.com/")

time.sleep(5)

uid = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
uid.send_keys("siddhantdalvi3@gmail.com")
time.sleep(5)

uid = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
uid.send_keys(returnpass())
time.sleep(5)

login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login.send_keys(Keys.ENTER)
time.sleep(15)


# close the browser
driver.close()
driver.quit()
print("sample test case successfully completed")
