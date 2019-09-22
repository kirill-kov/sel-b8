import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class needFunc():

    def setUp_func(self, driver, server):
        driver.get(server)
        login_field = driver.find_element_by_name('username')
        login_field.send_keys('admin')
        psdriver_field = driver.find_element_by_name('password')
        psdriver_field.send_keys('admin')
        login_btn = driver.find_element_by_name('login')
        login_btn.click()

    # 1)
    def countries_func(self, driver):
        driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

        countrs = driver.find_elements_by_css_selector('[name=countries_form] a:not([title])')
        countr_hrefs = []
        for c in countrs:
            countr_hrefs.append(c.text)

        zones = driver.find_elements_by_css_selector('[name=countries_form] td:nth-child(6)')
        zone_links = []
        for zone in zones:
            zone_links.append(zone.text)

        assert(countr_hrefs == sorted(countr_hrefs))

        i = 0
        wait = WebDriverWait(driver, 20)

        for href in countr_hrefs:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="disable"]')))
            if int(zone_links[i]) != 0:
                driver.find_element_by_link_text(href).click()
                wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

                sub_elements = driver.find_elements_by_css_selector('form td:nth-child(3)')
                sub_text = []
                for sub_element in sub_elements:
                    if sub_element.text != '':
                        sub_text.append(sub_element.text)

                assert(sub_text == (sub_text))

                driver.back()
            i += 1

    # 2)
    def geo_zones_func(self, driver):

        driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')

        countrs = driver.find_elements_by_css_selector('[name=geo_zones_form] a:not([title])')

        geo_links = []
        for c in countrs:
            geo_links.append(c.text)

        for link in geo_links:
            driver.find_element_by_link_text(link).click()

            sub_elements = driver.find_elements_by_css_selector('[name=form_geo_zone] td:nth-child(3) option[selected]')
            sub_text = []
            for sub_element in sub_elements:
                sub_text.append(sub_element.text)

            assert(sub_text == sorted(sub_text))

            driver.back()


server = 'http://localhost/litecart/admin/'
nf = needFunc()

class Test_countries_and_geo_zones(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver

        run = nf.setUp_func(driver, server)

    def test_countries(self):
        driver = self.driver

        nf.countries_func(driver)

    def test_geo_zones(self):
        driver = self.driver

        nf.geo_zones_func(driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)