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
        # 地区列表
        contry_register = {'中国': '+86', '阿联酋': '+971', '缅甸': '+95', '台湾': '+886', '香港': '+852', '波兰': '+48',\
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
        contry_login = {'中国': '+86', '阿联酋': '+971', '缅甸': '+95', '台湾': '+886', '香港': '+852', '波兰': '+48',\
                  '新加坡': '+65', '加拿大': '+1', '墨西哥': '+52', '美国': '+1', '法国': '+33', '英国': '+44', \
                  '意大利': '+39', '荷兰': '+31', '巴西': '+55', '菲律宾': '+63', '俄罗斯': '+7', '南非': '+27', \
                  '日本': '+81', '泰国': '+66', '马来西亚': '+60', '新西兰': '+64', '澳大利亚': '+61', '哈萨克斯坦': \
                      '+7', '奥地利': '+43', '越南': '+84', '老挝': '+856', '柬埔寨': '+855', '印度尼西亚': '+62', \
                  '文莱': '+673', '东帝汶': '+670', '塞尔维亚': '+381', '叙利亚': '+963', '巴基斯坦': '+92', '巴林':\
                      '+973', '埃及': '+20', '伊朗': '+98', '伊拉克': '+964', '以色列': '+972', '约旦': '+962', \
                  '科威特': '+965', '黎巴嫩': '+961', '突尼斯': '+216', '卡塔尔': '+974', '沙特阿拉伯': '+966', \
                  '巴勒斯坦': '+970', '苏丹': '+249', '也门': '+967', '土耳其': '+90', '塞浦路斯': '+357', '利比亚': \
                      '+218', '阿尔及利亚': '+213', '摩洛哥': '+212', '毛里塔尼亚': '+222', '吉布提': '+253', '索马里':\
                      '+252', '阿富汗': '+93', '科摩罗': '+269', '印度': '+91', '澳门': '+853', '其他': '0'}
        # 验证码输入框
        verifi_code = "com.bianla.international:id/et"
        # 密码设置
        pass_word = "com.bianla.international:id/pwd_editText"
        # 密码确认按钮
        pass_word_confirm = "com.bianla.international:id/signup_sent_verificationcode_btn"
        # 完善资料
        # 头像男
        man = "com.bianla.international:id/iv_man_mark"
        # 头像女
        women = "com.bianla.international:id/iv_woman_mark"
        # 生日栏位
        birthday = "com.bianla.international:id/tv_birthday"
        # 生日确认
        birthday_confirm = "com.bianla.international:id/confirm"
        # 身高输入
        height = "com.bianla.international:id/et_edit_height"
        # 昵称
        nick_name = "com.bianla.international:id/et_edit_nickName"
        # 资料设置完成按钮
        information_confirm = "com.bianla.international:id/btn_edit_submit"
        # 首页工具按钮
        class_home_button = "android.widget.LinearLayout"


class MetaWellTest(unittest.TestCase):
    d = atx.connect('3487e851')
    #d = u2.connect('192.168.191.2')
    #d = u2.connect('192.168.1.53')
    hrp = htmlreport.HTMLReport(d)
    #hrp.patch_click()
    cnt = Control
    def setUp(self):
        #self.d.app_start("com.bianla.international")
        self.d.start_app("com.bianla.international")

    def test_a_startPagecheck(self):
        '''登录注册页面元素检查'''
        # 启动页检查
        lognin = self.d(resourceId=self.cnt.login_button_id)
        signup = self.d(resourceId=self.cnt.sign_button_id)
        try:
            self.assertEqual("登录", lognin.get_text())
            logger().info("登录按钮检查通过")
        except AssertionError:
            raise
        try:
            self.assertEqual("注册", signup.get_text())
            logger().info("注册按钮检查通过")
        except AssertionError:
            raise
        # 进入登录页面
        lognin.click()
        self.d(resourceId=self.cnt.register_country).click()
        count_login = self.d(resourceId=self.cnt.contry_list).info
        print(count_login)
        contry_login = {}
        go = 1
        while go == 1:
            for i in range(count_login['childCount']*2-1):
                ins = i+1
                print(ins)
                city = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class, instance\
                    = ins).child_selector(resourceId=self.cnt.register_country).get_text()
                if(city=='其他'):
                    number = '0'
                else:
                    number = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class,\
                        instance = ins).child_selector(resourceId=self.cnt.register_num).get_text()
                print(city, number)
                contry_login[city] = number
                if(ins == count_login['childCount']*2-1):
                    if (contry_login.__contains__('其他')):
                        go = 0
                        break
                    self.d(resourceId="com.bianla.international:id/listView").scroll(steps=count_login['childCount']*7)
                    #self.d.swipe(size[0]/2, size[1]-20, size[0]/2, 300, 0.5)
        logger().info(contry_login)
        logger().info(operator.eq(contry_login, self.cnt.contry_login))
        try:
            self.assertDictEqual(self.cnt.contry_login, contry_login)
            logger().info("登录国家列表对比通过")
        except AssertionError:
            logger().error("登录国家列表对比失败")
            raise
        # 进入注册页面
        self.d.press("back")
        self.d.press("back")
        signup.click()
        # 地区页面元素检查
        self.d(resourceId=self.cnt.register_country).click()
        contry_register = {}
        count_register = self.d(resourceId=self.cnt.contry_list).info
        go = 1
        while go == 1:
            for i in range(count_register['childCount']*2-1):
                ins = i+1
                print(ins)
                city = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class, instance\
                    = ins).child_selector(resourceId=self.cnt.register_country).get_text()
                number = self.d(resourceId=self.cnt.contry_list).child_selector(className=self.cnt.contry_class, instance\
                    = ins).child_selector(resourceId=self.cnt.register_num).get_text()
                print(city, number)
                contry_register[city] = number
                if(ins == count_register['childCount']*2-1):
                    if (contry_register.__contains__('澳门')):
                        go = 0
                        break
                    self.d(resourceId="com.bianla.international:id/listView").scroll(steps=count_register['childCount']*7)
                    #self.d.swipe(size[0]/2, size[1]-20, size[0]/2, 300, 0.5)

        logger().info(contry_register)
        logger().info(operator.eq(contry_register, self.cnt.contry_register))
        try:
            self.assertDictEqual(contry_register, self.cnt.contry_register, "注册列表国家对比")
            logger().info("注册页面国家对比通过")
        except AssertionError:
            logger().info("注册页面国家对比失败")
            raise
        self.d.press("back")
        self.d.press("back")

    def test_b_sign(self):
        '''注册流程测试'''
        phone_number = "13"+str(int(time.time()/10))
        nick_name = "test昵称123"
        height = "167"
        birthday = "04/18/1988"
        logger().info("点击注册")
        self.d(resourceId=self.cnt.sign_button_id).click()
        logger().info("输入手机号:"+phone_number)
        self.d(resourceId=self.cnt.register_phone_field).send_keys(phone_number)
        logger().info("获取验证码")
        self.d(resourceId=self.cnt.send_verification).click()
        logger().info("输入验证码:"+"1234")
        self.d(resourceId=self.cnt.verifi_code).send_keys("1234")
        logger().info("设置密码:123456")
        self.d(resourceId=self.cnt.pass_word).send_keys("123456")
        logger().info("确认密码")
        self.d(resourceId=self.cnt.pass_word_confirm).click()
        logger().info("选择头像")
        self.d(resourceId=self.cnt.man).click()
        logger().info("设置生日")
        self.d(resourceId=self.cnt.birthday).click()
        self.d(resourceId=self.cnt.birthday_confirm).click()
        logger().info("设置身高")
        self.d(resourceId=self.cnt.height).send_keys(height)
        self.d.press("back")
        logger().info("设置昵称")
        self.d(resourceId=self.cnt.nick_name).send_keys(nick_name)
        self.d.press("back")
        logger().info("个人信息确认")
        self.d(resourceId=self.cnt.information_confirm).click()
        logger().info("进入我的页面")
        self.d(className="android.widget.LinearLayout", instance=18).click()
        self.d(text=u"编辑资料").click()
        logger().info("昵称检查")
        try:
            self.assertEqual(nick_name, self.d(resourceId="com.bianla.international:id/et_edit_nick").get_text())
            logger().info("昵称与设置一致")
        except AssertionError:
            logger().error("昵称与注册设置不一致")
            raise
        logger().info("身高检查")
        try:
            self.assertEqual(height, self.d(resourceId="com.bianla.international:id/et_edit_height").get_text())
            logger().info("身高与设置一致")
        except AssertionError:
            logger().error("身高与注册设置不一致")
            raise
        logger().info("生日检查")
        try:
            self.assertEqual(birthday, self.d(resourceId="com.bianla.international:id/tv_birthday").get_text())
            logger().info("生日与设置一致")
        except AssertionError:
            logger().error("生日与注册设置不一致")
            raise

    def tearDown(self):
        print("结束")
        #self.d.app_stop("com.bianla.international")
        self.d.stop_app("com.bianla.international")

# 测试套件
suite = unittest.TestSuite()
# 测试用例加载器
loader = unittest.TestLoader()
# 把测试用例加载到测试套件中
suite.addTests(loader.loadTestsFromTestCase(MetaWellTest))

# 测试用例执行器
runner = HTMLReport.TestRunner(report_file_name='MetaWell',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                               output_path='report',  # 保存文件夹名，默认“report”
                               title='变啦国际测试报告',  # 报告标题，默认“测试报告”
                               description='无测试描述',  # 报告描述，默认“测试描述”
                               thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                               thread_start_wait=1,  # 各线程启动延迟，默认 0 s
                               sequential_execution=True,  # 是否按照套件添加(addTests)顺序执行，
                               # 会等待一个addTests执行完成，再执行下一个，默认 False
                               # 如果用例中存在 tearDownClass ，建议设置为True，
                               # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                               # lang='en'
                               lang='cn'  # 支持中文与英文，默认中文
                               )
# 执行测试用例套件
runner.run(suite)
