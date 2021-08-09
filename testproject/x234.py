import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"


# függvény a kitöltéshez
def fill_fields(a, b):
    driver.find_element_by_id("a").send_keys(a)
    driver.find_element_by_id("b").send_keys(b)


# függvény a beküldéshez
def submit():
    driver.find_element_by_id("submit").click()
    time.sleep(2)
    return driver.find_element_by_id("result").text


# TC01 - helyes kitöltés
driver.get(URL)
fill_fields(99, 12)
assert submit() == "222"

# TC02 - nem számokkal történő kitöltés
driver.get(URL)
fill_fields("kiskutya", 12)
assert submit() == "NaN"

# TC03 - üres kitöltés
driver.get(URL)
assert submit() == "NaN"

# Quit
driver.quit()
