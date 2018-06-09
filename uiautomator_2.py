import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport

d = u2.connect('192.168.1.54')
#d = u2.connect_usb("3487e851")
hrp = htmlreport.HTMLReport(d)
hrp.patch_click()
d.app_start("com.ibox.calculators")
#sleep(3)
d(resourceId="com.ibox.calculators:id/digit7").click()
d(resourceId="com.ibox.calculators:id/mul").click()
d(resourceId="com.ibox.calculators:id/digit9").click()
equal = d(resourceId="com.ibox.calculators:id/equal")
equal.click()
print(equal.get_text())
print(d.info)