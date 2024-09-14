import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    # get the value and calculate answer
    x_value = browser.find_element(By.CSS_SELECTOR, ".form-group [id='input_value']")
    x = int(x_value.text)
    answer = calc(x)

    # get the input field and put the answer
    answer_field = browser.find_element(By.TAG_NAME, "input")
    answer_field.send_keys(answer)

    # find and click checkbox
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, ".form-check.form-check-custom #robotCheckbox")
    robot_checkbox.click()

    # find and click radiobutton
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, ".form-radio-custom #robotsRule")
    robot_radiobutton.click()

    #find and click submit button
    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()