import time

from selenium import webdriver

from E2ETesting.utils.readenv import readenvfile


def invokebrowser():
    env = readenvfile()
    baseURL = env["baseurl"]
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.maximize_window()
    time.sleep(2)
    return driver


