from selenium import webdriver
import time


def SetupBrowser():
        baseurl = "https://the-internet.herokuapp.com/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        return driver



SetupBrowser()