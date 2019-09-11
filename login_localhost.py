import unittest
from selenium import webdriver

class Test_login_in_localhost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/litecart/admin/')

    def test_login_local(self):
        driver = self.driver

        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        pswd_field = driver.find_element_by_name('password')
        pswd_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)