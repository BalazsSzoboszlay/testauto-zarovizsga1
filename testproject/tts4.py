import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

# TC01
driver.get(URL)
x = range(100)
for n in x:
    driver.find_element_by_id("submit").click()

childrenlist = driver.find_element_by_id("results").find_elements_by_tag_name("li")
resultList = []
x = range(100)
for n in x:
    resultList.append(childrenlist.__getitem__(n).text)

assert resultList.count("fej") >= 30
