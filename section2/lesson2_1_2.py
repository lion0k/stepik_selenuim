from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element_by_css_selector("#treasure")
    num = x_element.get_attribute("valuex")
    y = calc(num)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    labelCheck = browser.find_element_by_css_selector('#robotCheckbox')
    labelCheck.click()

    radioCheck = browser.find_element_by_css_selector('#robotsRule')
    radioCheck.click()

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