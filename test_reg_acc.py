import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class needFunc():

    def reg_check_acc_func(self, driver, first_name, last_name, street, email, phone, postal_code, city):

        driver.find_element_by_css_selector("span.select2-selection__rendered").click()
        driver.find_element_by_css_selector("input.select2-search__field").send_keys("United States",Keys.ENTER)

        driver.find_element_by_name("firstname").send_keys(first_name)
        driver.find_element_by_name("lastname").send_keys(last_name)

        driver.find_element_by_name("address1").send_keys(street)
        driver.find_element_by_name("postcode").send_keys(postal_code)
        driver.find_element_by_name("city").send_keys(city)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("phone").send_keys(phone)

        driver.find_element_by_name("password").send_keys(first_name)
        driver.find_element_by_name("confirmed_password").send_keys(first_name)
        driver.find_element_by_css_selector("[type=submit]").click()
        time.sleep(1)
        driver.find_element_by_link_text("Logout").click()
        time.sleep(1)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").send_keys(first_name)
        driver.find_element_by_link_text("Login").click()


    def assert_func(self, driver):

        title = driver.find_element_by_css_selector('#box-login > h1')
        h1 = title.text

        assert(h1 == 'Login')


nf = needFunc()

first_name = 'Arnold'
last_name =  'Schwarzenegger'
street = 'Hollywood st'
email = 'mr_universe@gmail.com'
phone = '+1234567890'
postal_code = '10001'
city = 'Los Angeles'

class Test_registration_random_user(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://litecart.stqa.ru/en/create_account')

    def test_reg_rand_user(self):
        driver = self.driver

        nf.reg_check_acc_func(driver, first_name, last_name, street, email, phone, postal_code, city)
        nf.assert_func(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)