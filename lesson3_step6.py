import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/redirect_accept.html")
  time.sleep(5)
  btn_element = browser.find_element_by_css_selector("button[type=submit]")
  btn_element.click()
  new_window = browser.window_handles[1]
  window = browser.switch_to.window(new_window)

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)
  element = browser.find_element_by_id("answer")
  element.send_keys(y)

  submit_button_elem = browser.find_element_by_css_selector("button[type=submit]")
  submit_button_elem.click()
  

finally:
  time.sleep(20)
  browser.quit()