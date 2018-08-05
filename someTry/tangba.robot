*** Settings ***
Library           AppiumLibrary
Library           Collections

*** Variables ***
${window_height}    ${EMPTY}
${window_width}    ${EMPTY}
${a}              2
${b}              4

*** Test Cases ***
login
    Open Application    http://127.0.0.1:4723/wd/hub    platformName=Android    platformVersion=7.1.1    deviceName=test    appPackge=com.bianla.tangba    app=G:/Python36/apk/tangba.apk
    ...    noReset=true
    ${window_height}    Get Window Height
    ${window_width}    Get Window Width
    ${startX}    evaluate    ${window_width}*0.75
    ${endX}    evaluate    ${window_width}*0.15
    ${startY}    evaluate    ${window_height}*0.5
    ${endY}    evaluate    ${window_height}*0.5
    sleep    3
    swipe    ${startX}    ${startY}    ${endX}    ${endY}    1000
    swipe    ${startX}    ${startY}    ${endX}    ${endY}    1000

    ${btn_skip}   tangba is visible    com.bianla.tangba:id/btn_skip
    run keyword if   ${btn_skip}    click element    com.bianla.tangba:id/btn_skip
    #    run keyword if    ${btn_skip}    click element    com.bianla.tangba:id/btn_skip
    #    ${btnEnter}    tangba is visible    com.bianla.tangba:id/btnEnter    3
    click element    com.bianla.tangba:id/btnEnter
    clear text      com.bianla.tangba:id/etPhone
    input value    com.bianla.tangba:id/etPhone    13600000002
    click element    com.bianla.tangba:id/btnNext
    sleep  2
    click a point    ${startX}    ${startY}
#    background app  0.1
    sleep  2
    ${btnEnter}    tangba is visible    com.bianla.tangba:id/btnEnter
    ${btnComplete}    tangba is visible    com.bianla.tangba:id/btnComplete
    run keyword if    ${btnEnter}    input value      com.bianla.tangba:id/etPassword    aaa
    run keyword if    ${btnEnter}    Click Element    com.bianla.tangba:id/btnEnter
    run keyword if    ${btnComplete}    input value    com.bianla.tangba:id/etVCode      11111
    run keyword if    ${btnComplete}    input value    com.bianla.tangba:id/etPassword   aaa
    run keyword if    ${btnComplete}    click element    com.bianla.tangba:id/btnComplete
    Run Keyword If    1    log to console    tet
    #    close application
