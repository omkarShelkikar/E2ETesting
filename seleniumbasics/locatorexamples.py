import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from urllib3.util import request

from setupbrowser import SetupBrowser


def testingheadingText():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/abtest']").click()
    var = driver.find_element(By.XPATH, "//div[@class='example']/h3").text
    print(var)


def testingaddremove():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
    driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
    listElement = driver.find_elements(By.ID, "elements")
    if len(listElement) != 0:
        print("Button added")
    # time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR, ".added-manually").click()
    # listElement = driver.find_elements(By.ID, "elements")
    # if len(listElement) == 0:
    #      print("Button deleted")


def testingStaticDropdown():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/dropdown']").click()
    dropdown = Select(driver.find_element(By.ID, 'dropdown'))
    time.sleep(2)
    dropdown.select_by_visible_text("Option 2")
    time.sleep(2)
    dropdown.select_by_value('1')


def testingBrokenImages():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/broken_images']").click()
    ListLinks = driver.find_elements(By.XPATH, "//div[@class='example']/img")
    # print(len(ListLinks))
    count = 0
    for link in ListLinks:
        href = link.get_attribute('src')
        if href:
            reponse = requests.get(href)
            if reponse.status_code != 200:
                count += 1
    print("Broken link", count)


def testingFrames():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/frames']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/iframe']").click()
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[id='mce_0_ifr']")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, 'tinymce').send_keys("Hello Ifrmae")
    time.sleep(2)
    driver.switch_to.default_content()


def testingWindows():
    driver = SetupBrowser()
    driver.find_element(By.CSS_SELECTOR, "a[href='/windows']").click()
    time.sleep(2)
    firstWindow = driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR,"a[href='/windows/new']").click()
    time.sleep(2)
    if firstWindow != driver.current_window_handle:
             driver.switch_to(driver.current_window_handle)
             print(driver.title)


testingWindows
# testingFrames()
# testingheadingText()
# testingaddremove()
# testingStaticDropdown()
# testingBrokenImages()
