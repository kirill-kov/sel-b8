import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class needFunc():

    def setUp_func(self, driver, server):
        driver.get(server)
        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        pswd_field = driver.find_element_by_name('password')
        pswd_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    def open_links_func(self, driver):

        driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
        driver.find_element_by_link_text('Austria').click()

        links = driver.find_elements_by_css_selector("td > a:not(#address-format-hint)")
        main_window = driver.current_window_handle
        new_window = []

        for i in range(0, len(links)):
            links[i].click()
            new_window = driver.window_handles
            new_window.remove(main_window)
            WebDriverWait(driver, 15).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(new_window[0])
            driver.close()
            driver.switch_to.window(main_window)

server = 'http://localhost/litecart/admin/'
nf = needFunc()

class Test_open_links_in_new_window(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        run = nf.setUp_func(driver, server)

    def test_open_links_new_window(self):
        driver = self.driver

        nf.open_links_func(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)