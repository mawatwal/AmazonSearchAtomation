# import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
# enter the url of Amazon
url = "https://www.amazon.in"
# enter the name of the product you want to search for
search_term = "The Subtle Art of Not Giving a Fuck"
# give a link to the chromedriver.exe file, an example is shown, replace it with your own path
driver = webdriver.Chrome(executable_path = "C:/Users/mawat/Desktop/Downloads/project/chromedriver.exe")
# to maximise the browser to whole screen
driver.maximize_window()
# wait for the window to open and pass the url 
driver.implicitly_wait(10) # here '10' is in seconds
driver.get(url)
# test whether correct URL/ Web Site has been loaded or not
assert "Amazon" in driver.title
# locate the search text-box
searchTextBox=driver.find_element_by_id("twotabsearchtextbox")
# clear the text-box
searchTextBox.clear()
# pass the search term in the text-box and hit search
searchTextBox.send_keys(search_term)
searchTextBox.send_keys(Keys.RETURN)
time.sleep(10)
