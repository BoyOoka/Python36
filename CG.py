from appium import webdriver
import time

desired_caps = {
        'app': 'G:/git/java-client-4.1.2/java-client-4.1.2/app/bili.apk',
        'appPackage': 'tv.danmaku.bili',
        'appActivity': 'tv.danmaku.bili.MainActivity',
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': '192.168.199.102:5555',
        'noReset':'true'
}
print(desired_caps)
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
time.sleep(5)
#a = driver.contexts()WEBVIEW_tv.danmaku.bili:web

contexts = driver.contexts
print (contexts)
#driver.switch_to.window(contexts[0])
driver.switch_to.default_content()
driver.context(contexts[0])
print(driver.current_url)