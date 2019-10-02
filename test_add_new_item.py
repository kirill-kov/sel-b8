import unittest
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, random, os

class needFunc():

    def setUp_func(self, driver, server):
        driver.get(server)
        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        pswd_field = driver.find_element_by_name('password')
        pswd_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    def get_random_name(self, letters, length):

        return ''.join(random.choice(letters) for i in range(length))

    def new_product_add_func(self, driver):

        name_new_prod = nf.get_random_name(letters, 15)

        driver.find_element_by_link_text("Catalog").click()
        driver.find_element_by_link_text("Add New Product").click()

        driver.find_element_by_css_selector("label").click()
        if not driver.find_element_by_name("status").is_selected():
            driver.find_element_by_name("status").click()

        driver.find_element_by_name('name[en]').click()
        driver.find_element_by_name('name[en]').send_keys(name_new_prod)
        driver.find_element_by_name('code').click()
        driver.find_element_by_name('code').send_keys('5')
        driver.find_element_by_name('quantity').click()
        driver.find_element_by_name('quantity').send_keys('10')
        driver.find_element_by_name('new_images[]').send_keys(os.getcwd()+'\\1-yellow-duck-1.png')

        driver.find_element_by_name('date_valid_from').click()
        driver.find_element_by_name('date_valid_from').send_keys('2015-02-10')
        driver.find_element_by_name('date_valid_to').click()
        driver.find_element_by_name('date_valid_to').send_keys('2019-02-10')

        driver.find_element_by_link_text("Information").click()
        if not driver.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").is_selected():
            driver.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").click()

        driver.find_element_by_name('keywords').click()
        driver.find_element_by_name('keywords').send_keys('my_duck')
        driver.find_element_by_name('short_description[en]').click()
        driver.find_element_by_name('short_description[en]').send_keys('my_duck')

        driver.find_element_by_link_text("Prices").click()
        driver.find_element_by_name("purchase_price").send_keys('22')

        if not driver.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").is_selected():
            driver.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").click()

        driver.find_element_by_name('prices[USD]').click()
        driver.find_element_by_name('prices[USD]').send_keys('32')
        time.sleep(2)
        driver.find_element_by_name("save").click()
        driver.find_element_by_id("content").click()

        driver.find_element_by_link_text("Catalog").click()
        test = '{0}{1}{2}'.format("//a[text()='", str(name_new_prod), "']")
        assert_element = driver.find_elements_by_xpath(test)
        print (len(assert_element))
        assert (len(assert_element) == 1)


letters = 'abcdefghijklmnopqrstuvwxyz'
server = 'http://localhost/litecart/admin/'
nf = needFunc()

class Test_add_new_item(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        run = nf.setUp_func(driver, server)

    def test_add_new_item(self):
        driver = self.driver

        nf.new_product_add_func(driver)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)