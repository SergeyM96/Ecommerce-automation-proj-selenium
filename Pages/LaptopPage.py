from selenium.webdriver.common.by import By
class LaptopPage():
    def __init__(self, driver):
        self.driver = driver
        self.hp_xpath = "//a[normalize-space()='HP LP3065']"

    def click_hp_option(self):
        self.driver.find_element(By.XPATH, self.hp_xpath).click()
