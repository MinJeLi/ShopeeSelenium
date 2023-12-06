import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class shopeeSelenium(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://shopee.tw/")
        self.driver.implicitly_wait(5)
        
    def test_home_banner_in_shopee(self):
        
        driver = self.driver
        home_banner = driver.find_element(By.CLASS_NAME,'full-home-banners-wrapper')
        self.assertNotEqual(home_banner,None)
        
    def test_elements_below_home_banner(self):
        
        driver = self.driver
        home_banner = driver.find_element(By.CLASS_NAME, 'full-home-banners-wrapper')
        below_home_banner = home_banner.find_elements(By.XPATH,'div[2]/a')
        self.assertEqual(len(below_home_banner),10)
        
        for ele in below_home_banner:
            href_value = ele.get_attribute("href")
            print(href_value)
            
    def test_simple_banner(self):
        
        driver =self.driver
        # find shadow-root host
        shopee_main = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/shopee-banner-popup-stateful')
        
        # shadow-root
        first_shadow_root = shopee_main.shadow_root
        home_content = first_shadow_root.find_element(By.CSS_SELECTOR, 'div > div > div > shopee-banner-simple')
        
        # shadow-root again
        second_shadow_root = home_content.shadow_root
        target_element = second_shadow_root.find_element(By.CSS_SELECTOR, 'div > a > img')
        img_src = target_element.get_attribute("src")
        print(img_src)
            
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()