from appium import webdriver

import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '192.168.199.101:5' \
                             '555'
desired_caps['appPackge'] = 'com.bianla.tangba'
desired_caps['app'] = ('G:/Python36/apk/tangba.apk')
# desired_caps['automationName'] = 'Selendroid'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
t = driver.get_window_size()
time.sleep(3)
driver.swipe(t['width']*0.75, t['height']/2, t['width']*0.15, t['height']/2, 1000)
driver.swipe(t['width'] * 0.75, t['height'] / 2, t['width'] * 0.15, t['height'] / 2, 1000)
driver.find_element_by_id('com.bianla.tangba:id/btn_skip').click()
driver.find_element_by_id('com.bianla.tangba:id/btnEnter').click()

driver.find_element_by_id('com.bianla.tangba:id/etPhone').send_keys('13281549858')
driver.find_element_by_id('com.bianla.tangba:id/btnNext').click()
driver.background_app(0.5)
print(t)
driver.close_app()
driver.quit()

