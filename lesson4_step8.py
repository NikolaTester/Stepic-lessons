from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
  WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))
  button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
  button.click()
  value = browser.find_element_by_id("input_value").text
  answer = calc(value)
  input_element = browser.find_element_by_id("answer")
  input_element.send_keys(answer)
  solve_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
  solve_button.click()
  WebDriverWait(browser, 5).until_not(EC.alert_is_present())
finally:
  browser.quit()