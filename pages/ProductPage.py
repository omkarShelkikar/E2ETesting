import time

from selenium.webdriver.common.by import By


class ProductPage():
    xpath_camera = "(//a[contains(text(),'Cameras')])[1]"
    xpath_tablet = "(//a[contains(text(),'Tablets')])[1]"
    xapth_addToCart = "//button[@id='button-cart']"




    def __init__(self,driver):
        self.driver = driver
        time.sleep(5)

    def searchproduct(self):
        self.driver.find_element(By.XPATH, self.xpath_tablet).click()
        self.driver.find_element(By.XPATH, self.xapth_addToCart).click()



