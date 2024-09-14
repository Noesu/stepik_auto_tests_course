from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    result = int(num1.text) + int(num2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()