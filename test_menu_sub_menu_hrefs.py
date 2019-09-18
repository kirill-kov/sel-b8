import unittest
from selenium import webdriver

class needFunc():

    def setUp_func(self, driver, server):
        driver.get(server)
        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        pswd_field = driver.find_element_by_name('password')
        pswd_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    def menu_sub_menu_hrefs_func(self, driver):

        menu_hrefs = driver.find_elements_by_xpath("//*[@id='app-']/a/span[2]")

        for i in range(len(menu_hrefs)):

            menu_hrefs_chap = driver.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
            menu_hrefs_chap[i].click()
            driver.implicitly_wait(1)

            sub_menu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")

            for j in range(len(sub_menu)):

                sub_menu_chap = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
                sub_menu_chap[j].click()

                page_title = driver.title
                head_title = driver.find_element_by_xpath(".//*[@id='content']/h1").text

                assert(head_title in page_title)


server = 'http://localhost/litecart/admin/'
nf = needFunc()

class Test_menu_sub_menu_hrefs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        run = nf.setUp_func(driver, server)


    def test_login_local(self):
        driver = self.driver

        nf.menu_sub_menu_hrefs_func(driver)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)