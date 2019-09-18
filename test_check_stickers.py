import unittest
from selenium import webdriver

class needFunc():

    def check_stickers_func(self, driver):

        products = driver.find_elements_by_css_selector("li.product > a.link")

        i = 0
        for product in products:
            have_sticker = product.find_elements_by_css_selector("div.sticker")
            if len(have_sticker) == 1:
                i += 1

        assert(i == len(products))

server = 'http://localhost/litecart/'
nf = needFunc()

class Test_check_stickers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(server)


    def test_check_stickers(self):
        driver = self.driver

        nf.check_stickers_func(driver)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)