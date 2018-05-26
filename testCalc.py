import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


desired_caps = { }
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '3487e851'
desired_caps['app'] = 'G:/Python36/apk/jisuanqi_1292.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['noReset'] = 'true'
desired_caps['unicodeKeyboard'] ='true'
desired_caps['resetKeyboard'] ='true'
desired_caps['newCommandTimeout'] =6000

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
num8 = driver.find_element_by_xpath("//android.widget.RelativeLayout//android.support.v4.view.ViewPager//android.widget.LinearLayout[2]//android.widget.Button[2]")
num7 = driver.find_element_by_id("com.ibox.calculators:id/digit7")
plus = driver.find_element_by_id("com.ibox.calculators:id/plus")
equal = driver.find_element_by_id("com.ibox.calculators:id/equal")
Result = driver.find_element_by_xpath("//android.widget.RelativeLayout//android.widget.RelativeLayout//android.widget.LinearLayout//android.widget.RelativeLayout//android.widget.TextView[2]")
num8.click()
plus.click()
num7.click()
equal.click()
a = Result.text
print(a)
