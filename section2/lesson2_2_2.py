from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from math import log, sin


def calc(x):
  return str(log(abs(12 * sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    val1 = int(browser.find_element_by_css_selector("#input_value").text)

    input1 = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(calc(val1))

    check_box = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()

    radio = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
    browser.quit()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла