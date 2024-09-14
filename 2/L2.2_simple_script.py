from selenium import webdriver
import time

browser = webdriver.Chrome()

# browser.execute_script("alert('Robots at work');")

# browser.execute_script('document.title="Script executing";')

browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(10)