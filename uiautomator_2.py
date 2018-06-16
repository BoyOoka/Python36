import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import unittest
import HTMLReport
from HTMLReport import logger
import atx

#

#sleep(3)



class TestStringMethods(unittest.TestCase):
    d = u2.connect('192.168.191.2')
    hrp = htmlreport.HTMLReport(d)
    hrp.patch_click()
    def setUp(self):
        logger().info("打开计算器")
        self.d.app_start("com.ibox.calculators")
    def testPlus(self):
        '''乘法运算'''
        logger().info("点击7")
        self.d(resourceId="com.ibox.calculators:id/digit6").click()
        logger().info("点击X")
        self.d(resourceId="com.ibox.calculators:id/mul").click()
        logger().info("点击9")
        self.d(resourceId="com.ibox.calculators:id/digit8").click()
        logger().info("点击=")
        equal = self.d(resourceId="com.ibox.calculators:id/equal")

        equal.click()
        print(equal.get_text())
        print(self.d.info)
        logger().info("断言")
       # ans = self.d(resourceId="com.ibox.calculators:id/cv", className="android.widget.TextView", instance="2")
        ans = self.d(resourceId="com.ibox.calculators:id/cv").child_selector\
            (className="android.widget.TextView", instance=1)

        ans_text = ans.get_text()
        self.assertEqual(ans_text, "48")
    def testAdd(self):
        '''加法运算'''
        logger().info("点击7")
        self.d(resourceId="com.ibox.calculators:id/digit7").click()
        logger().info("点击+")
        self.d(resourceId="com.ibox.calculators:id/plus").click()
        logger().info("点击9")
        self.d(resourceId="com.ibox.calculators:id/digit9").click()
        logger().info("点击=")
        equal = self.d(resourceId="com.ibox.calculators:id/equal")

        equal.click()
        print(equal.get_text())
        print(self.d.info)
        logger().info("断言")
       # ans = self.d(resourceId="com.ibox.calculators:id/cv", className="android.widget.TextView", instance="2")
        ans = self.d(resourceId="com.ibox.calculators:id/cv").child_selector\
            (className="android.widget.TextView", instance=1)

        ans_text = ans.get_text()
        self.assertEqual(ans_text, "16")
    def testMinus(self):
        '''减法运算'''
        logger().info("点击7")
        self.d(resourceId="com.ibox.calculators:id/digit7").click()
        logger().info("点击-")
        self.d(resourceId="com.ibox.calculators:id/minus").click()
        logger().info("点击9")
        self.d(resourceId="com.ibox.calculators:id/digit9").click()
        logger().info("点击=")
        equal = self.d(resourceId="com.ibox.calculators:id/equal")

        equal.click()
        print(equal.get_text())
        print(self.d.info)
        logger().info("断言")
       # ans = self.d(resourceId="com.ibox.calculators:id/cv", className="android.widget.TextView", instance="2")
        ans = self.d(resourceId="com.ibox.calculators:id/cv").child_selector\
            (className="android.widget.TextView", instance=1)

        ans_text = ans.get_text()
        self.assertEqual(ans_text, "16")
    def tearDown(self):
        self.d.app_stop("com.ibox.calculators")
        print (1)

# 测试套件
suite = unittest.TestSuite()
# 测试用例加载器
loader = unittest.TestLoader()
# 把测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(TestStringMethods))

# 测试用例执行器
runner = HTMLReport.TestRunner(report_file_name='计算器',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                               output_path='report',  # 保存文件夹名，默认“report”
                               title='计算器测试报告',  # 报告标题，默认“测试报告”
                               description='无测试描述',  # 报告描述，默认“测试描述”
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
