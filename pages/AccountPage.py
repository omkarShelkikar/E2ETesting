import time

from selenium.webdriver.common.by import By

from E2ETesting.pages.LoginPage import LoginPage


class AccountPage(LoginPage):
    xpath_logout = "//a[@class='list-group-item'][normalize-space()='Logout']"
    xpath_desktop = "//a[normalize-space()='Desktops']"
    xpath_showAllDesktop = "//a[normalize-space()='Show All Desktops']"
    xpath_selectFirstitem = "//div[@class='row'][4]//div[@class='product-thumb'][1]"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        time.sleep(5)

    def logout(self):
        #self.login()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.xpath_logout).click()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Continue']").click()
        time.sleep(5)

    def seachDesktopItems(self):
        self.driver.find_element(By.XPATH, self.xpath_desktop).click()
        self.driver.find_element(By.XPATH, self.xpath_showAllDesktop).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_selectFirstitem).click()









