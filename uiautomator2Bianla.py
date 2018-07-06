import uiautomator2 as u


d = u.connect('192.168.12.46')
d.app_start("com.bianla.app")
d(resourceId='com.bianla.app:id/imageView5').click()
# d(resourceId='com.bianla.app:id/bt_abstract_check_fail').click()
d(resourceId='com.bianla.app:id/bt_abstract_check_conform').click()
#d(resourceId='com.bianla.app:id/tv_content').send_keys('hsdkahg粉红色调宏观jksdakl!@#$%^&*()_+，。fsl////429-53gl')
