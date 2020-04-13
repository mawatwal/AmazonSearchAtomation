from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
url = "https://www.amazon.in"
search_term="The Subtle Art of Not Giving a Fuck"
driver = webdriver.Chrome(executable_path="C:/Users/mawat/Desktop/Downloads/project/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10) #10 is in seconds
driver.get(url)
# test whether correct URL/ Web Site has been loaded or not
assert "Amazon" in driver.title
# to enter the search term, we need to locate the search textbox
searchTextBox=driver.find_element_by_id("twotabsearchtextbox")
searchTextBox.clear()
searchTextBox.send_keys(search_term)
searchTextBox.send_keys(Keys.RETURN)
time.sleep(10)