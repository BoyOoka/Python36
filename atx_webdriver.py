import atx
from selenium import webdriver
from atx.ext.chromedriver import ChromeDriver

d = atx.connect("3487e851")
#d = atx.connect("a9870a1e")

#driver = webdriver.Chrome()
d.start_app("com.bianla.international")
print(d.current_app())
d(resourceId="com.bianla.international:id/icon", className="android.widget.ImageView", instance=4).click()
driver = ChromeDriver(d).driver("com.bianla.international", True, ".activity.StartActivity", "com.bianla.international")
driver.find_element_by_css_selector("button").click()
url = driver.current_url
print(url.toString())
