import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = " https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)
#a "cites" textarea-ben lévő szöveget feldaraboljuk
citylist = driver.find_element_by_id("cites").text.split(', ', -1)
#"-ok eltávolítása
citylist = [s.strip('"') for s in citylist]

#print(len(citylist))
#print(citylist)

#randomCities lista elmentése
childrenlist = driver.find_element_by_id("randomCities").find_elements_by_tag_name("li")
resultList = []
#randomCities lista szövegeinek tárolása
x = range(len(driver.find_element_by_id("randomCities").find_elements_by_tag_name("li")))
for n in x:
    resultList.append(childrenlist.__getitem__(n).text)

#print(len(resultList))
#print(resultList)
#listák set-té konvertálása, és különbség megkeresése, eredmény strip-elése
result = str(set(citylist).difference(set(resultList))).strip('{').strip('}').strip("'")
driver.find_element_by_id("missingCity").send_keys(result)
driver.find_element_by_id("submit").click()
assert driver.find_element_by_id("result").is_displayed() and driver.find_element_by_id("result").text == "Eltaláltad."





