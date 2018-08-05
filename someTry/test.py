import xlrd
import openpyxl

workbook = xlrd.open_workbook('test.xlsx')
wb = openpyxl.load_workbook('test.xlsx')

print(workbook.sheet_names())
workbook.release_resources()

sheet1 = wb.active
sheet1['C4']= '运行成功第3次'
print(sheet1['C2'].value)
wb.save('test.xlsx')
