from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    # Ваш код
    y = calc(browser.find_element_by_id("input_value").text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox1.click()
    radio1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    