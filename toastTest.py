from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'YHQGORTWJV5SAQOV',  #'77a3c838'
    'platformVersion': '7.1',
    'appPackage': 'com.bianla.tangba',     # apk包名
    'appActivity': 'com.bianla.tangba.activity.StartActivity',      # apk的launcherActivity
    'noReset': 'false',
    # 'unicodeKeyboard': 'true',
    # 'resetKeyboard': 'true',
    'automationName':'uiautomator2'
    # 'automationName':'Selendroid'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(2)
driver.find_element_by_id("com.bianla.tangba:id/btnEnter").click()  # 点击“注册登陆”按钮
WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, 'com.bianla.tangba:id/etPhone')))
driver.find_element_by_id('com.bianla.tangba:id/etPhone').clear()
driver.find_element_by_id("com.bianla.tangba:id/etPhone").send_keys('13281549858')  #输入账号 来自表格
driver.find_element_by_id("com.bianla.tangba:id/btnNext").click()  #点击“下一步”
driver.find_element_by_id("com.bianla.tangba:id/etPassword").send_keys('21')  #输入密码 来自表格
driver.find_element_by_id("com.bianla.tangba:id/btnEnter").click()  #点击“登陆”
toast = '用户名或密码错误'
ele = WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, './/*[contains(@text,'+'\''+toast+'\''+')]')))
print(ele.text)