#Putting Variables Into Excel

import xlsxwriter

#Variables
FMD1 = 15

#Creating workbook wb
wb = xlsxwriter.Workbook('example.xlsx')

#Creating Sheet for Subject Summary
subsum = wb.add_worksheet("Subject Summary")

#Filling in the Cells for the subject summary sheet

header_format = subsum.add_format()
header_format.set_bold()



subsum.write('A1', 'Study Name')



wb.close()