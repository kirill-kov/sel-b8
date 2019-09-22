import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class needFunc():

    def assert_func(self, var1, var2):
        try:
            assert(var1 == var2)
            print('{} == {}'.format(var1, var2))

        except AssertionError:
            print('{} =/= {}'.format(var1, var2))

    def correct_page_func(self, driver):

        product = driver.find_element_by_css_selector('div#box-campaigns li.product a.link')

        index_name = product.find_element_by_css_selector('div.name').text
        index_regular_price = product.find_element_by_css_selector('s.regular-price').text
        index_color_regular_price = product.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
        index_fontsize_regular_price = product.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')

        index_sale_price = product.find_element_by_css_selector('strong.campaign-price').text
        index_color_sale_price = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
        index_fontweight_sale_price = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
        index_fontsize_sale_price = product.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')

        product.click()

        sub_name = driver.find_element_by_css_selector('h1').text
        sub_regular_price = driver.find_element_by_css_selector('s.regular-price').text
        sub_color_regular_price = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
        sub_fontsize_regular_price = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')

        sub_sale_price = driver.find_element_by_css_selector('strong.campaign-price').text
        sub_color_sale_price = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
        sub_fontweight_sale_price = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
        sub_fontsize_sale_price = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')

        nf.assert_func(index_name, sub_name)
        nf.assert_func(index_regular_price, sub_regular_price)
        nf.assert_func(index_color_regular_price, sub_color_regular_price)
        nf.assert_func(index_fontsize_regular_price, sub_fontsize_regular_price)
        nf.assert_func(index_sale_price, sub_sale_price)
        nf.assert_func(index_color_sale_price, index_color_sale_price)
        nf.assert_func(index_fontweight_sale_price, sub_fontweight_sale_price)
        nf.assert_func(index_fontsize_sale_price, sub_fontsize_sale_price)


server = 'http://localhost/litecart/'
nf = needFunc()


class Test_check_correct_page_Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(server)

    def test_correct_page(self):
        driver = self.driver

        nf.correct_page_func(driver)

    def tearDown(self):
        self.driver.close()

class Test_check_correct_page_Fox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(server)

    def test_correct_page(self):
        driver = self.driver

        nf.correct_page_func(driver)

    def tearDown(self):
        self.driver.close()

class Test_check_correct_page_IE(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.get(server)

    def test_correct_page(self):
        driver = self.driver

        nf.correct_page_func(driver)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)