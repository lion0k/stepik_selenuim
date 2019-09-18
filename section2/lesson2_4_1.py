import time
from selenium import webdriver
from math import log, sin
# from send_to_stepik import send_to_stepik
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import sys


LINK_LESSON = 'https://stepik.org/lesson/181384/step/8?unit=156009'
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
    get(browser, "http://suninjuly.github.io/explicit_wait2.html")

    text = get_text(browser, '.container p:nth-child(2)')
    regx = re.search(r'\B(\$\d+)\.\B', text)
    if regx is None:
        sys.exit('Not found need price house')
    need_price = regx.group(1)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), need_price))

    click(browser, "#book")

    value = int(get_text(browser, '#input_value'))
    send(browser, '#answer', calc(value))

    # Отправляем заполненную форму
    click(browser, "#solve")
    time.sleep(2)

    answer = print_answer(browser)

    stepik_auth(browser)
    stepik_send_answer(browser, answer)
    time.sleep(2)
    browser.quit()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла