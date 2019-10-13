import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class needFunc():

    def setUp_func(self, driver, server):
        driver.get(server)
        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        pswd_field = driver.find_element_by_name('password')
        pswd_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    def logs_func(self, driver):
        driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')

        elements = driver.find_elements_by_css_selector('td > a:not([title=Edit])')
        ducks = []

        for element in elements:
            ducks.append(element.text)

        for duck in ducks:
            driver.find_element_by_link_text(duck).click()
            time.sleep(0.5)
            for l in driver.get_log('browser'):
                print('Browser logs:', l)
            driver.back()

server = 'http://localhost/litecart/admin/'
nf = needFunc()

class MyListener(AbstractEventListener):

  def before_find(self, by, value, driver):
        print(by, value)

  def after_find(self, by, value, driver):
        print(by, value, 'found')

  def on_exception(self, exception, driver):
        print(exception)

class Test_browser_logs(unittest.TestCase):

    def setUp(self):
        self.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        driver = self.driver

        run = nf.setUp_func(driver, server)

    def test_brow_logs(self):
        driver = self.driver

        nf.logs_func(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)