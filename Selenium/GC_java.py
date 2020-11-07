from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import time

print("sample test case started")

path = "D:\\Main_Folders\\siddhant work\\Setup Files\\ChromeDriver\\chromedriver.exe"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://www.udemy.com/")  # opening google.com

time.sleep(5)

driver.find_element_by_xpath('//*[@id="udemy"]/div[1]/div[1]/div[3]/div[5]/a').send_keys(Keys.ENTER)

time.sleep(5)

login_bx = driver.find_elements_by_xpath('//*[@id="identifierId"]')
login_bx[0].send_keys("siddhantdalvi3@gmail.com")

time.sleep(30)

driver.get("classroom.google.com")

time.sleep(5)

driver.close()

driver.quit()
