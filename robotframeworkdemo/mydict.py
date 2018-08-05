
def xiaomi():
    print('why')
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0.2'
    desired_caps['deviceName'] = '192.168.199.101:5555'
    desired_caps['appPackge'] = 'com.bianla.international'
    desired_caps['app'] = ('G:/Python36/apk/Bianla-debug_dev_1.1.2.apk')
    # desired_caps['automationName'] = 'Selendroid'
    return desired_caps