import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()

def calc(x: int) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    first_page = browser.window_handles[0]
    second_page = browser.window_handles[1]
    browser.switch_to.window(second_page)


    input_value = browser.find_element(By.ID, "input_value").text
    answer = calc(int(input_value))

    browser.find_element(By.ID, "answer").send_keys(str(answer))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()