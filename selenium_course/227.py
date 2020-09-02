import os 


from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_name("firstname").send_keys("Name")
    browser.find_element_by_name("lastname").send_keys("Last")
    browser.find_element_by_name("email").send_keys("email@dd.rt")
    attach = browser.find_element_by_id("file")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test_file.txt')
    attach.send_keys(file_path)
    
    
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()