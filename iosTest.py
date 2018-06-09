import wda

c = wda.Client('http://localhost:8100')
'''
s = c.session('com.facebook.wda.integrationApp.nbn')

s(name='Alerts').click_exists(2)
s(xpath='//XCUIElementTypeButton[@name="Create App Alert"]').click_exists(3)
s.alert.accept()
s(label='Back').click_exists(2)
s(name='Scrolling').click_exists(2)
s(name='TableView').click_exists()
e = s(name='15')
e.scroll('down')
'''

s1 = c.session('com.bianla.international')
s1(name='登录').click_exists()
phone = s1(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
phone.set_text('13281549858')
pwd = s1(xpath='//XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
pwd.set_text('123456')
s1(xpath='//XCUIElementTypeButton[@name="登录"]').click_exists(2)
