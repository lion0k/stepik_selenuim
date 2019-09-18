from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    val1 = int(browser.find_element_by_css_selector("#num1").text)
    val2 = int(browser.find_element_by_css_selector("#num2").text)

    sumx = sum([val1, val2])

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(sumx))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
    browser.quit()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла