from selenium import webdriver
import math
import os 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link1 = "http://suninjuly.github.io/alert_accept.html?"
link2 = "http://suninjuly.github.io/alert_redirect.html?"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(link1)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(int(x))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    time.sleep(1)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
