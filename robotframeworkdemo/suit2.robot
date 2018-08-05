*** Settings ***
Library           AppiumLibrary
Library           mydict.py
Library           Collections

*** Variables ***
${REMOTE_URL}     http://127.0.0.1:4723:4723/wd/hub
${PLATFORM_NAME}    platformName=Android
${PLATFORM_VERSION}    platformVersion=7.1.1
${DEVICE_NAME}    deviceName=Android
${appPackge}      appPackge=com.bianla.international
${APP}            G:/Python36/apk/Bianla-debug_dev_1.1.2.apk

*** Test Cases ***
testcase1
    log to console    xiaomi
    ${list}=    Create List
    APPEND TO LIST    ${list}    hello
    log to console    ${list}
    ${dict}=    create dictionary    platformName=Android    platformVersion=7.1.1    deviceName=test    appPackge=com.bianla.international    app=G:/Python36/apk/Bianla-debug_dev_1.1.2.apk
    log to console    ${dict}
    #    Open Application    http://127.0.0.1:4723/wd/hub    ${dict}
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=7.1.1    deviceName=test    appPackge=com.bianla.international    app=G:/Python36/apk/Bianla-debug_dev_1.1.2.apk
    click element    com.bianla.international:id/show_btn_login_in

testcase2
    log variables

testcase3
    log variables
