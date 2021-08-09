from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

# TC01 - Helyes email-cím
driver.get(URL)
driver.find_element_by_id("email").send_keys("abc@def.gh")
driver.find_element_by_id("submit").click()
assert len(driver.find_elements_by_class_name("validation-error")) == 0

#TC02 - Hibás email-cím
driver.get(URL)
driver.find_element_by_id("email").send_keys("asdf@")
driver.find_element_by_id("submit").click()
assert driver.find_element_by_class_name("validation-error").is_displayed() and driver.find_element_by_class_name("validation-error").text == "Kérjük, adja meg a „@” utáni részt is. A(z) „asdf@” cím nem teljes."

driver.get(URL)
driver.find_element_by_id("email").send_keys("@asdf")
driver.find_element_by_id("submit").click()
assert driver.find_element_by_class_name("validation-error").is_displayed() and driver.find_element_by_class_name("validation-error").text == "Kérjük, adja meg a „@” előtti részt is. A „@asdf” cím nem teljes."


# TC03 - Üres beküldés
driver.get(URL)
driver.find_element_by_id("submit").click()
assert driver.find_element_by_class_name("validation-error").is_displayed() and driver.find_element_by_class_name("validation-error").text == "Kérjük, töltse ki ezt a mezőt."

driver.quit()
