from selenium.webdriver.common.by import By
class SuccessPage():
    def __init__(self, driver):
        self.driver = driver
        self.message_xpath = "//h1[normalize-space()='Your order has been placed!']"

    def print_message(self):
        msg = self.driver.find_element(By.XPATH, self.message_xpath).text
        print(msg)