import unittest
from selenium import webdriver

class Test_open_close_browser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://pypi.org')

    def test_o_c_browser(self):
        driver = self.driver
        title = driver.title

        self.assertIn('Python Package', title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)