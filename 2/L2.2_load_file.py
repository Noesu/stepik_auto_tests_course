import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')

data = iter(("Ivan", "Ivanov", "e@mail.ru"))
field = iter(("firstname", "lastname", "email"))


browser = webdriver.Chrome()

try:
    browser.get(link)

    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    print(len(elements))
    for e in elements:
        e.send_keys(next(data))

    browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)

    # find and click submit button
    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()





finally:
    time.sleep(10)
    browser.quit()