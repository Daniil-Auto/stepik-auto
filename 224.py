from selenium import webdriver
import time

  
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_css_selector(".custom-select"))

    # Ваш код
    sum1 = str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text))
    print(sum1)
    select.select_by_visible_text(sum1)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()