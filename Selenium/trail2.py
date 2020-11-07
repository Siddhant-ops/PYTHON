from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")

path = "D:\\Main_Folders\\siddhant work\\Setup Files\\ChromeDriver\\chromedriver.exe"

driver = webdriver.Chrome(path)
# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url

driver.get('https://www.dropbox.com/login')

time.sleep(0.2)
email = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div[2]/input')
email.send_keys('siddhantdalvi3@gmail.com')

time.sleep(0.2)
passw = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div[2]/input')
passw.send_keys('ZOG\'SOTF')

time.sleep(0.4)
sign_in = driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/form/div[2]/button')
sign_in.send_keys(Keys.ENTER)


time.sleep(160)
all_files = driver.find_element_by_xpath('/html/body/div[2]/div/nav/div/div/div[2]/div[1]/div/ul/li[2]/div/ul/li[1]/div/span/a')
all_files.send_keys(Keys.ENTER)

time.sleep(10)

# close the browser
driver.close()
driver.quit()

print("sample test case successfully completed")