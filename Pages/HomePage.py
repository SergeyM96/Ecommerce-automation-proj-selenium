from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.phone_pda_option_xpath = "//a[normalize-space()='Phones & PDAs']"
        self.laptop_notebook_xpath = "//a[normalize-space()='Laptops & Notebooks']"
        #self.show_all_laptop_notebook_xpath = "//a[normalize-space()='Show All Laptops & Notebooks']"
        self.cart_button_xpath = "//span[@id='cart-total']"
        self.checkout_button_xpath = "//strong[normalize-space()='Checkout']"
        self.wait = WebDriverWait(driver, 10)


    def click_phone_pda_option(self):
        self.driver.find_element(By.XPATH, self.phone_pda_option_xpath).click()

    def hover_laptop_notebook_option(self):
        laptops = self.driver.find_element(By.XPATH, self.laptop_notebook_xpath)
        self.action.move_to_element(laptops).perform()

    def click_show_all_laptop_notebook_option(self):
        # Wait for the element to be clickable
        show_all_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(text(), 'Show AllLaptops & Notebooks')]")))
        show_all_button.click()
    def click_cart_button(self):
        self.driver.find_element(By.XPATH, self.cart_button_xpath).click()

    def click_checkout_cart_button(self):
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()
