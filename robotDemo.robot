*** Settings ***
Documentation    Suite description
Library  AppiumLibrary

*** Variables ***
${yanzheng}       8888
${password}       1

*** Test Cases ***
$robot$
    Open Application    http://127.0.0.1:4723/wd/hub    platformName=Android    platformVersion=8.0.0  deviceName=localhost:4723  automationName=appium   appActivity=com.bianla.app.enter.splash.SplashActivity   appPackage=com.bianla.app   unicodeKeyboard=True    resetKeyboard=True   noReset=True

Register and Login
    Click Element    com.bianla.app:id/signup    #点击注册按钮
    Wait Until Element Is Visible    com.bianla.app:id/signup_phone_num_et    \    \    #等待元素可见
    ${ran}    Evaluate    random.randint(1000,9999)    random
    Input Text    com.bianla.app:id/signup_phone_num_et    1330000${ran}    #输入手机号
    Click Element    com.bianla.app:id/signup_sent_verificationcode_btn    #点击获取验证码
    Input Text    com.bianla.app:id/signup_input_verificationcode_et    ${yanzheng}    #输入验证码
    Input Text    com.bianla.app:id/signup_input_newpasswore_et    ${password}    #输入密码
    Input Text    com.bianla.app:id/signup_input_newpassword_again_et    ${password}    #重复输入密码
    Click Element    com.bianla.app:id/signup_commit    #点击提交
    Wait Until Element Is Visible    com.bianla.app:id/login    #等待登录按钮
    Click Element    com.bianla.app:id/login    #点击登录按钮
    Wait Until Element Is Visible    com.bianla.app:id/login_account_et    \    \    #等待输入账号框
    Clear Text    com.bianla.app:id/login_account_et    #清空账号输入框
    Input Text    com.bianla.app:id/login_account_et    15669977730    #输入账号
    Comment    Input Text    com.bianla.app:id/login_account_et    1330000${ran}    #输入账号
    Input Text    com.bianla.app:id/login_password_et    ${password}    #输入密码
    Click Element    com.bianla.app:id/login    #点击登录