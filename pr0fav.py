from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import urllib
import time

tmp = 1

browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
url = "https://pr0gramm.com"
browser.get(url) #navigate to the page

browser.execute_script("document.getElementsByClassName('head-link')[0].click()")

username = browser.find_element_by_name("name") #username form field
password = browser.find_element_by_name("password") #password form field

username.send_keys("Your Username")
password.send_keys("Your Password")

submitButton = browser.find_element_by_id("login-button") 
submitButton.click() 

browser.get("the link from the first picture, from your favorites")

browser.execute_script("document.getElementsByClassName('user-only head-link')[0].click()")
browser.execute_script("document.getElementsByClassName('filter-setting')[1].click()")
browser.execute_script("document.getElementsByClassName('filter-setting')[2].click()")
browser.find_element_by_id("filter-save").click()

count = 1
while count != 20000:
 time.sleep(1)
 try:
  browser.find_element_by_xpath("//div[contains(@class,'stream-prev')]").click()
  img = browser.find_element_by_class_name("item-image-actual")
  src = img.get_attribute('src')
  print(src)
  urllib.urlretrieve(src, src.rsplit('/', 1)[-1])
  count = count + 1
 except:
  print("error with " + str(count))
  count = count + 1
