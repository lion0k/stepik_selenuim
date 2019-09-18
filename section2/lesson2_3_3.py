import os
import time

import pyperclip
from selenium import webdriver
# import send_to_stepik


def get(remote: webdriver.Remote, url):
    remote.get(url)


def send(remote: webdriver.Remote, s, keys):
    remote.find_element_by_css_selector(s).send_keys(keys)


def click(remote: webdriver.Remote, s):
    remote.find_element_by_css_selector(s).click()


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    pyperclip.copy(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    get(browser, "http://suninjuly.github.io/file_input.html")

    send(browser, 'div[class="form-group"] > input[name="firstname"]', 'FirstName')
    send(browser, 'div[class="form-group"] > input[name="lastname"]', 'LastName')
    send(browser, 'div[class="form-group"] > input[name="email"]', 'test@test.com')

    current_dir = os.path.abspath(os.path.dirname('test.txt'))
    file_path = os.path.join(current_dir, 'test.txt')

    send(browser, '#file', file_path)

    # Отправляем заполненную форму
    click(browser, "button.btn")

    print_answer(browser)
    browser.quit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла