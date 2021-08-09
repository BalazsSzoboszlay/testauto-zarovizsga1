from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"


def calc(operator, a, b):
    if operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '+':
        return a + b
    elif operator == '-':
        return a - b


driver.get(URL)
num1 = int(driver.find_element_by_id("num1").text)
num2 = int(driver.find_element_by_id("num2").text)
op = driver.find_element_by_id("op").text
driver.find_element_by_id("submit").click()
result = calc(op, num1, num2)

assert int(driver.find_element_by_id("result").text) == result

driver.quit()
