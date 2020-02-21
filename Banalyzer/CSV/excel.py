#Putting Variables Into Excel

import xlwt


wb = xlwt.Workbook()
ws = wb.add_sheet("Test Sheet!")
ws.write(0, 0,

wb.save('example.xls')