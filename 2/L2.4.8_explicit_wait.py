import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

def calc(x: str) -> str:
    print(f'calc: value = {x}\ncalc: answer = {str(math.log(abs(12*math.sin(int(x)))))}')
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    book_button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button.click()
    value = browser.find_element(By.ID, "input_value").text
    print(value)
    answer = calc(value)
    # print(answer)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()


finally:
    # print(browser.switch_to.alert.text)
    # print(browser.switch_to.alert.text.split(': ')[-1])
    sleep(10)
    browser.quit()
