import time
# import pyperclip
from selenium import webdriver
from math import log, sin
# from send_to_stepik import send_to_stepik
from selenium.webdriver.support.wait import WebDriverWait
import sys


LINK_LESSON = 'https://stepik.org/lesson/184253/step/6?unit=158843'
LINK_TO_STEPIK = 'https://stepik.org/catalog?auth=login'
LOGIN = ''
PASSWORD = ''


def get(remote: webdriver.Remote, url):
    remote.get(url)


def get_text(remote: webdriver.Remote, s):
    return remote.find_element_by_css_selector(s).text


def send(remote: webdriver.Remote, s, keys):
    remote.find_element_by_css_selector(s).send_keys(keys)


def click(remote: webdriver.Remote, s):
    remote.find_element_by_css_selector(s).click()


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    answer = alert.text.split()[-1]
    # print(answer)
    alert.accept()
    return answer


def stepik_auth(remote: webdriver.Remote):
    remote.get(LINK_TO_STEPIK)
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_name("login"))
    remote.find_element_by_name("login").send_keys(LOGIN)
    remote.find_element_by_name("password").send_keys(PASSWORD)
    remote.find_element_by_class_name("sign-form__btn").click()
    WebDriverWait(
        remote,
        3).until(lambda x: x.find_element_by_class_name("navbar__profile-img"))


def stepik_send_answer(remote: webdriver.Remote, answer: str):
    remote.get(LINK_LESSON)
    WebDriverWait(remote,
                  3).until(lambda x: x.find_element_by_tag_name("textarea"))
    remote.find_element_by_tag_name("textarea").send_keys(answer)
    remote.find_element_by_class_name("submit-submission").click()
    # WebDriverWait(remote, 5).until(lambda x: x.find_element_by_id("correct"))


def calc(x):
  return str(log(abs(12 * sin(x))))


browser = webdriver.Chrome()
try:
    get(browser, "http://suninjuly.github.io/redirect_accept.html")

    click(browser, "button.trollface")
    windows = browser.window_handles
    if len(windows) < 2:
        sys.exit('Not found second window')

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = int(get_text(browser, '#input_value'))
    send(browser, '#answer', calc(value))

    # Отправляем заполненную форму
    click(browser, "button.btn")
    time.sleep(2)

    answer = print_answer(browser)

    stepik_auth(browser)
    stepik_send_answer(browser, answer)
    browser.quit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла