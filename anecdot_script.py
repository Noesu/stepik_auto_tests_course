from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.anekdot.ru/last/anekdot/"

browser = webdriver.Chrome()

try:
    browser.get(link)
    release_date = browser.find_element(By.CLASS_NAME, "subdate").text
    topics = browser.find_elements(By.CLASS_NAME, "topicbox")
    topics.pop(0)

    topics_dict = {}
    for topic in topics:
        text, votingbox = topic.text.rsplit("\n", 1)
        rating = votingbox.split("+", 1)
        topics_dict[int(rating[0])] = text
    print(topics_dict)




finally:
    # time.sleep(10)
    browser.quit()
