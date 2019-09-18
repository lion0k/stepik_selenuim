import time
import pyperclip
from selenium import webdriver
from math import log, sin
# from send_to_stepik import send_to_stepik
from selenium.webdriver.support.wait import WebDriverWait


LINK_LESSON = 'https://stepik.org/lesson/184253/step/4?unit=158843'


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
    print(answer)
    # pyperclip.copy(alert.text.split()[-1])
    alert.accept()
    return answer


def stepik_send_answer(remote: webdriver.Remote, answer: str):
    remote.get(LINK_LESSON)
    WebDriverWait(remote,
                  3).until(lambda x: x.find_element_by_tag_name("textarea"))
    remote.find_element_by_tag_name("textarea").send_keys(answer)
    remote.find_element_by_class_name("submit-submission").click()
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_id("correct"))


def calc(x):
  return str(log(abs(12 * sin(x))))


try:
    browser = webdriver.Chrome()
    get(browser, "http://suninjuly.github.io/alert_accept.html")

    click(browser, "button.btn")
    browser.switch_to.alert.accept()

    value = int(get_text(browser, '#input_value'))
    send(browser, '#answer', calc(value))

    # Отправляем заполненную форму
    click(browser, "button.btn")
    time.sleep(2)

    stepik_send_answer(browser, print_answer(browser))
    # send_to_stepik(LINK_LESSON, print_answer(browser))
    browser.quit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла