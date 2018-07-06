import atx, time
from atx.ext.report import Report

d = atx.connect('3487e851')
#d = atx.connect('cf76c2f3')
d.start_app('com.bianla.international')
appInfo = d.current_app()
c = atx.adb_client
print(c.devices())
print(appInfo)
pid = str(appInfo['package'])


show_btn_login_in = d(resourceId='com.bianla.international:id/show_btn_login_in')
show_btn_login_in.click()
time.sleep(2)
login_password_et = d(resourceId='com.bianla.international:id/login_password_et')
login_account_et = d(resourceId='com.bianla.international:id/login_account_et')
login_account_et.clear_text()
login_account_et.set_text("13200000001")
login_password_et.set_text("123456")
login_button = d(resourceId = 'com.bianla.international:id/login')
login_button.click()
d.adb_shell('kill '+pid)
d.stop_app("com.bianla.international")


