import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()

def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    # get value and calc answer
    value = int(browser.find_element(By.ID, "input_value").text)
    answer = calc(value)

    # find input field and put answer
    browser.find_element(By.TAG_NAME, "input").send_keys(answer)

    # find and click checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    # find and click radiobutton
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radiobutton)
    robot_radiobutton.click()

    # find and click submit button
    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()


