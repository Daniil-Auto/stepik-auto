from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("Радиокнопка Люди выбрана: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()