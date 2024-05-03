from selenium.webdriver.common.by import By
import time
class iPhonePage():
    def __init__(self, driver):
        self.driver = driver
        self.iphone_image_xpath = "//ul[@class='thumbnails']//li[1]//a[1]"
        self.next_arrow_xpath = "//button[@title='Next (Right arrow key)']"
        self.close_button_xpath = "//button[normalize-space()='×']"
        self.input_quantity_textbox_xpath = "//input[@id='input-quantity']"
        self.add_to_cart_xpath = "//button[@id='button-cart']"

    def click_iphone_image(self):
        self.driver.find_element(By.XPATH, self.iphone_image_xpath).click()

    def click_next_arrow(self):
        self.driver.find_element(By.XPATH, self.next_arrow_xpath).click()

    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.close_button_xpath).click()

    def input_quantity(self, quantity):
        quantity_input = self.driver.find_element(By.XPATH, self.input_quantity_textbox_xpath)
        quantity_input.clear()
        quantity_input.send_keys(quantity)

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()