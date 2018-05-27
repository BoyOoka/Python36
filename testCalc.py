from appium import webdriver
import HTMLReport
import unittest


desired_caps = { }
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '3487e851'
desired_caps['app'] = 'G:/Python36/apk/jisuanqi_1292.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['noReset'] = 'true'
#desired_caps['unicodeKeyboard'] ='true'
desired_caps['resetKeyboard'] ='true'
#desired_caps['newCommandTimeout'] =6000

class testAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
    def testA(self):
        '''测试加法'''
        num8 = self.driver.find_element_by_id("com.ibox.calculators:id/digit8")
        num7 = self.driver.find_element_by_id("com.ibox.calculators:id/digit7")
        plus = self.driver.find_element_by_id("com.ibox.calculators:id/plus")
        equal = self.driver.find_element_by_id("com.ibox.calculators:id/equal")
        Result = self.driver.find_element_by_xpath(
            "//android.widget.RelativeLayout//android.widget.RelativeLayout//android.widget.LinearLayout//android.widget.RelativeLayout//android.widget.TextView[2]")
        num8.click()
        plus.click()
        num7.click()
        equal.click()
        a = Result.text
        self.assertEqual(a, "15", "相等")
        print(a)


#driver.find_element_by_android_uiautomator("")#uiautomator选择

# 测试套件
suite = unittest.TestSuite()
# 测试用例加载器
loader = unittest.TestLoader()
# 把测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(testAdd))

# 测试用例执行器
runner = HTMLReport.TestRunner(report_file_name='testAdd',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                               output_path='report',  # 保存文件夹名，默认“report”
                               title='测试报告',  # 报告标题，默认“测试报告”
                               description='线上功能监控',  # 报告描述，默认“测试描述”
                               thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                               thread_start_wait=3,  # 各线程启动延迟，默认 0 s
                               sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                               # 会等待一个addTests执行完成，再执行下一个，默认 False
                               # 如果用例中存在 tearDownClass ，建议设置为True，
                               # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                               # lang='en'
                               lang='cn'  # 支持中文与英文，默认中文
                               )
# 执行测试用例套件
runner.run(suite)



