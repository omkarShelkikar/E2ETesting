import time

from selenium.webdriver.common.by import By

from E2ETesting.helpers.commonmethods import invokebrowser
from selenium.webdriver.chrome import webdriver



class LoginPage():
    loginURL = "https://naveenautomationlabs.com/opencart/index.php?route=account/login"
    id_loginemail = "input-email"
    id_password = "input-password"
    xpath_login = "//input[@value='Login']"
    email = "Test1234@yahoo.com"
    password = "Test@1234"


    def __init__(self,driver):
        self.driver = driver
        time.sleep(5)

    def login(self):

        self.driver.find_element(By.ID,self.id_loginemail).send_keys(self.email)
        self.driver.find_element(By.ID, self.id_password).send_keys(self.password)
        self.driver.find_element(By.XPATH, self.xpath_login).submit()
        time.sleep(5)
        # title = self.driver.title
        # print(title)
        # assert "Account" in title








