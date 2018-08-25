from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class bianlaDemoTest(unittest.TestCase):

    def setUp(self):
        desir_caps = {
            'platformName':'Android',
            'platformVersion':'8.1',
            'deviceName':'cf76c2f3',
            'app':'F:/bianla_3.2.1.apk',
            'appPackage':'com.bianla.app',
            'noReset':'true'
           # 'unicodeKeyboard':'true'
           # 'resetKeyboard':'true'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desir_caps)
        self.driver.implicitly_wait(30)
    def test_a_login(self):
        self.driver.find_element_by_id('com.bianla.app:id/btn_register_login').click()
        self.driver.find_element_by_id('com.bianla.app:id/tv_login').click()
        self.driver.find_element_by_id('com.bianla.app:id/login_account_et').clear()
        self.driver.find_element_by_id('com.bianla.app:id/login_account_et').send_keys('13281549858')
        self.driver.back()
        self.driver.find_element_by_id('com.bianla.app:id/login_password_et').clear()
        self.driver.find_element_by_id('com.bianla.app:id/login_password_et').send_keys('123456')
        self.driver.back()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="登录"]').click()

     #   self.driver.find_element_by_id('com.bianla.app:id/imageView5').click()
     #   self.driver.background_app(1)
     #   self.driver.find_element_by_id('com.bianla.app:id/bt_abstract_check_fail').click()
     #   self.driver.find_element_by_id('com.bianla.app:id/tv_content').send_keys('test')
     #   WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(
     #       (By.ID,'com.bianla.app:id/bt_abstract_check_fail')))
     #   self.driver.find_element_by_id('com.bianla.app:id/bt_abstract_check_fail').click()
     #   self.driver.find_element_by_id('com.bianla.app:id/confirm').click()
        while 1:
            self.driver.shake()

    def tearDown(self):
        print('ok')
       # self.driver.quit()