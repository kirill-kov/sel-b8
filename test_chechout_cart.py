import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, random

class needFunc():

    def test_add_prod_to_cart(self, driver):
        print()

        for i in range(1,4):
            print(str(i) + '.')

            ducks = driver.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")

            random_index = random.randint(0, len(ducks)-1)

            go = ducks[random_index].find_element_by_xpath("./a[@class='link']")
            go.click()
            cart_prod = driver.find_element_by_name('add_cart_product')
            cart_prod.click()
            time.sleep(1)

            wait = WebDriverWait(driver, 10)

            element = wait.until(EC.text_to_be_present_in_element((By.XPATH, ".//*[@id='cart']//a//span[@class='quantity']"), str(i)))

            driver.get("http://localhost/litecart/en/")

        driver.get("http://localhost/litecart/en/checkout")
        time.sleep(5)
        order = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")

        for i in range(len(order)):
            driver.find_element_by_name('remove_cart_item').click()
            wait = WebDriverWait(driver, 10)
            wait.until(EC.staleness_of(order[0]))


nf = needFunc()


class Test_checkout_cart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/litecart/en/")
        self.driver.implicitly_wait(60)

    def test_checkout(self):
        driver = self.driver

        nf.test_add_prod_to_cart(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)