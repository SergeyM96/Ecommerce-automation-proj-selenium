from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
import unittest
import HtmlTestRunner
import sys
import os
# NOTE: I have used time.sleeps in the code, so you could see how the automation works, and in other cases it`s used
#                   like await so the request/respond could load in time for taking the action.

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directory containing the "Pages" folder to the Python path
#                     -------------------------- REPLACE WITH YOUR DIRECTORY --------------------------
pages_dir = os.path.join(script_dir, 'C:\\Users\\User31.8.23\\Desktop\\Scripts in python\\scripts\\eCommerce-Web-Selenium Automation')
sys.path.append(pages_dir)

from Pages.HomePage import HomePage
from Pages.PhonePDAPage import PhonePDAPage
from Pages.iPhonePage import iPhonePage
from Pages.LaptopPage import LaptopPage
from Pages.HPpage import HPpage
from Pages.CheckoutPage import CheckoutPage
from Pages.SuccessPage import SuccessPage

class EcomTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize webdriver
        #                -------------------------- REPLACE WITH YOUR DIRECTORY --------------------------
        chrome_service = Service(r"E:\Programming\chromedriver-win64\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01(self):
        # Initialize driver and open URL
        driver = self.driver
        driver.get('http://tutorialsninja.com/demo/')

        # Initialize Home Page Object and click phone and pda option
        home = HomePage(driver)
        home.click_phone_pda_option()
        time.sleep(3)

        # Select iphone - quantity 2
        phone_pda = PhonePDAPage(driver)
        phone_pda.click_iphone_option()
        time.sleep(3)
        # Iterate through the iphone images
        iphone = iPhonePage(driver)
        iphone.click_iphone_image()
        time.sleep(3)
        # Click next arrow 5 times (the amount of the pictures)
        for i in range(5):
            iphone.click_next_arrow()
            time.sleep(2)
        # Take screenshot of the last image and close it
        #                                   -------------------------- REPLACE WITH YOUR DIRECTORY --------------------------
        driver.save_screenshot('C:\\Users\\User31.8.23\\Desktop\\Scripts in python\\scripts\\eCommerce-Web-Selenium Automation\\Screenshots/'+'screenshot#'+str(random.randint(0,101))+'.png')
        iphone.click_close_button()
        time.sleep(3)
        # Add input quantity and add to cart
        iphone.input_quantity(2)
        #time.sleep(3) // wait before adding to the cart for the user to see the steps.
        #iphone.click_add_to_cart_button()  // ---> NOTE: There is no quantity available, so I commented this out so the program will run until the end.

        time.sleep(3)

        # Select laptops section - quantity 1
        home.hover_laptop_notebook_option()
        home.click_show_all_laptop_notebook_option()
        time.sleep(3)
        # Select the hp laptop
        lap = LaptopPage(driver)
        lap.click_hp_option()
        time.sleep(3)
        # Once in the laptops page, scroll down (in case if needed)
        hp = HPpage(driver)
        hp.scroll_to_add_to_cart_button()
        time.sleep(3)
        # Click calendar and choose delivery date, then add it to cart
        hp.click_delivery_date_calendar()
        hp.change_delivery_date_calendar("18", "May 2024")
        time.sleep(3)
        hp.click_add_to_cart_button()
        time.sleep(3)

        # Checkout Process
        # Click cart and then checkout
        home.click_cart_button()
        time.sleep(3)
        home.click_checkout_cart_button()
        # Filling in checkout details
        cp = CheckoutPage(driver)
        cp.complete_checkout_options()
        cp.complete_billing_details('fname', 'lname', 'testing@hotmail.com', '5555555555', 'Halutz 22', 'TestCity', '12342', 'Israel', 'Haifa')
        time.sleep(3)
        cp.complete_delivery_method()
        time.sleep(3)
        cp.complete_payment_method()
        time.sleep(3)
        cp.confirm_order_method()
        time.sleep(3)
        # Show success message
        sp = SuccessPage(driver)
        time.sleep(3)
        sp.print_message()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed successfully !")

if __name__ == '__main__':
    #                         -------------------------- REPLACE WITH YOUR DIRECTORY --------------------------
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\User31.8.23\\Desktop\\Scripts in python\\scripts\\eCommerce-Web-Selenium Automation\\Reports"))
