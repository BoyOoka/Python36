from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '192.168.199.101:5555'
desired_caps['appPackge'] = 'com.bianla.tangba'
desired_caps['app'] = ('G:/Python36/apk/tangba.apk')
desired_caps['automationName'] = 'UiAutomator2'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
t = driver.get_window_size()
time.sleep(3)
driver.swipe(t['width']*0.75, t['height']/2, t['width']*0.10, t['height']/2, 1000)
time.sleep(0.5)
driver.swipe(t['width'] * 0.75, t['height'] / 2, t['width'] * 0.10, t['height'] / 2, 1000)
driver.find_element_by_id('com.bianla.tangba:id/btn_skip').click()
time.sleep(0.5)
driver.find_element_by_id('com.bianla.tangba:id/btnEnter').click()
WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, 'com.bianla.tangba:id/etPhone')))
driver.find_element_by_id('com.bianla.tangba:id/etPhone').send_keys('13281549858')
driver.find_element_by_id('com.bianla.tangba:id/btnNext').click()
driver.find_element_by_id('com.bianla.tangba:id/etPassword').send_keys('12')
driver.find_element_by_id('com.bianla.tangba:id/btnEnter').click()
ele = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(
            (By.XPATH, ".//*[contains(@text,'用户名或密码错误')]")))
print(ele.text)
#driver.close_app()
driver.quit()

