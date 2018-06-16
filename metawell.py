import uiautomator2.ext.htmlreport as htmlreport
import uiautomator2 as u2
import unittest, time, atx
import HTMLReport,operator
from HTMLReport import logger
import atx


class Control(object):
        # 包名
        packagename = "com.bianla.international"
        # 登录
        login_button_id = "com.bianla.international:id/show_btn_login_in"
        # 注册
        sign_button_id = "com.bianla.international:id/show_btn_sign_up"
        # 注册输入框
        register_phone_field = "com.bianla.international:id/signup_phone_num_et"
        # 注册国家
        register_country = "com.bianla.international:id/tv_area"
        # 国家区号
        register_num = "com.bianla.international:id/tv_area_num"
        # 发送验证码按钮
        send_verification = "com.bianla.international:id/signup_sent_verificationcode_btn"
        # 国家列表
        contry_list = "com.bianla.international:id/listView"
        # 国家class
        contry_class = "android.widget.LinearLayout"
        #地区列表
        contry = {'中国': '+86', '阿联酋': '+971', '缅甸': '+95', '台湾': '+886', '香港': '+852', '波兰': '+48',\
                  '新加坡': '+65', '加拿大': '+1', '墨西哥': '+52', '美国': '+1', '法国': '+33', '英国': '+44', \
                  '意大利': '+39', '荷兰': '+31', '巴西': '+55', '菲律宾': '+63', '俄罗斯': '+7', '南非': '+27', \
                  '日本': '+81', '泰国': '+66', '马来西亚': '+60', '新西兰': '+64', '澳大利亚': '+61', '哈萨克斯坦': \
                      '+7', '奥地利': '+43', '越南': '+84', '老挝': '+856', '柬埔寨': '+855', '印度尼西亚': '+62', \
                  '文莱': '+673', '东帝汶': '+670', '塞尔维亚': '+381', '叙利亚': '+963', '巴基斯坦': '+92', '巴林':\
                      '+973', '埃及': '+20', '伊朗': '+98', '伊拉克': '+964', '以色列': '+972', '约旦': '+962', \
                  '科威特': '+965', '黎巴嫩': '+961', '突尼斯': '+216', '卡塔尔': '+974', '沙特阿拉伯': '+966', \
                  '巴勒斯坦': '+970', '苏丹': '+249', '也门': '+967', '土耳其': '+90', '塞浦路斯': '+357', '利比亚': \
                      '+218', '阿尔及利亚': '+213', '摩洛哥': '+212', '毛里塔尼亚': '+222', '吉布提': '+253', '索马里':\
                      '+252', '阿富汗': '+93', '科摩罗': '+269', '印度': '+91', '澳门': '+853'}


class TestStringMethods(unittest.TestCase):
    d = atx.connect('3487e851')
    #d = u2.connect('192.168.191.2')
    #d = u2.connect('192.168.191.3')
    hrp = htmlreport.HTMLReport(d)
    #hrp.patch_click()
    cnt = Control
    def setUp(self):
        #self.d.app_start("com.bianla.international")
        self.d.start_app("com.bianla.international")

    def testRegisterPagecheck(self):
        logger().info("启动页面元素断言")
        # 启动页检查
        lognin = self.d(resourceId=self.cnt.login_button_id)
        signup = self.d(resourceId=self.cnt.sign_button_id)
        self.assertEqual(lognin.get_text(), "登录")
        self.assertEqual(signup.get_text(), "注册")
        # 进入注册页面
        signup.click()
        # 地区页面元素检查
        logger().info("地区获取")
        self.d(resourceId=self.cnt.register_country).click()
        #self.d(resourceId="com.bianla.international:id/listView").scroll(steps=64)
        contry = {}
        count = self.d(resourceId=self.cnt.contry_list).info
        go = 1
        while go == 1:
            for i in range(count['childCount']*2-1):
                ins = i+1
                print(ins)
                city = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class, instance\
                    = ins).child_selector(resourceId=self.cnt.register_country).get_text()
                number = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class, instance\
                    = ins).child_selector(resourceId=self.cnt.register_num).get_text()
                # print(city)
                # print(number)
                contry[city] = number
                if(ins == count['childCount']*2-1):
                    self.d(resourceId="com.bianla.international:id/listView").scroll(steps=count['childCount']*7)
                    #self.d.swipe(size[0]/2, size[1]-20, size[0]/2, 300, 0.5)
                    if(contry.__contains__('澳门')):
                        go = 0
        logger().info(contry)
        logger().info("注册地区断言")
        logger().info(operator.eq(self.cnt.contry,contry))
        self.assertEqual(self.cnt.contry, contry, "注册列表国家对比")

    def tearDown(self):
        #self.d.app_stop("com.bianla.international")
        self.d.stop_app("com.bianla.international")

# 测试套件
suite = unittest.TestSuite()
# 测试用例加载器
loader = unittest.TestLoader()
# 把测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(TestStringMethods))

# 测试用例执行器
runner = HTMLReport.TestRunner(report_file_name='MetaWell',  # 报告文件名，如果未赋值，将采用“test+时间戳”
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
