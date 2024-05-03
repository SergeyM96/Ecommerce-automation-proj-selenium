from selenium.webdriver.common.by import By

class PhonePDAPage():
    def __init__(self, driver):
        self.driver = driver
        self.iphone_xpath = "//a[normalize-space()='iPhone']"

    def click_iphone_option(self):
        self.driver.find_element(By.XPATH,self.iphone_xpath).click()

