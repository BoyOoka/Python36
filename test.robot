*** Settings ***
Library           ExcelRobot
Resource          rc.robot
Resource          test.py
*** Variables ***
${d}              1000

*** Test Cases ***
demo
    ${a}=    evaluate    ${d}/2
    log to console    ${a}
    open excel    test.xlsx
    ${a1}   read cell data by name     Sheet1      A1
    ${cell}     read cell data     Sheet1     1        2
    @{sheetName}    get sheet names
    log to console  @{sheetName}[2]
    log to console  1
    #release resources
    open excel to write      test.xlsx
    write to cell by name    Sheet1      A2     this is a fjsdlk
    log to console  2
    save excel
    print something  我输入了一些东西