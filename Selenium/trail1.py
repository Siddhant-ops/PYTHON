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
driver.get("https://www.google.com/")
# identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(30)
# click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(30)
# close the browser
driver.close()
driver.quit()
print("sample test case successfully completed")

# import time
# from selenium import webdriver

# driver = webdriver.Chrome(
#     "D:\\Main_Folders\\siddhant work\\Setup Files\\ChromeDriver\\chromedriver.exe"
# )  # Optional argument, if not specified will search path.
# driver.get("http://www.google.com/")
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name("q")
# search_box.send_keys("ChromeDriver")
# search_box.submit()
# time.sleep(5)  # Let the user actually see something!
# driver.quit()
