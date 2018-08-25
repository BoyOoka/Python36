import uiautomator2 as u


d = u.connect('192.168.13.46')
d.app_start("com.bianla.app")

d(resourceId='com.bianla.app:id/btn_register_login').click()
d(resourceId='com.bianla.app:id/tv_login').click()
d(resourceId='com.bianla.app:id/login_account_et').clear_text()
d(resourceId='com.bianla.app:id/login_account_et').send_keys('13281549858')
d.press("back")
d(resourceId='com.bianla.app:id/login_password_et').send_keys('123456')
d.press("back")
d(resourceId='com.bianla.app:id/login').click()
d(resourceId='com.bianla.app:id/imageView5').click()
d(resourceId='com.bianla.app:id/bt_abstract_check_fail').click()
d(resourceId='com.bianla.app:id/tv_content').send_keys('hsdkahg粉红色调宏观jksdakl!@#$%^&*()_+，。fsl////429-53gl')
d.press("back")
#d(resourceId='com.bianla.app:id/bt_abstract_check_fail').click()
#d(resourceId='com.bianla.app:id/bt_abstract_check_conform').click()
d(resourceId='com.bianla.app:id/confirm').click()

