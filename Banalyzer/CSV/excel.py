#Putting Variables Into Excel
#This progam generates the excel template and also places the data into an excel-viewable format
print("hi")

import xlsxwriter


#Variables
studyname = '123456789 bsl'
nombre = 'Jane Doe'
date = 'Today'

#Creating workbook fmd_report
wb = xlsxwriter.Workbook('fmd_report_example.xlsx')

#Creating Sheet for Subject Summary
subsum = wb.add_worksheet('Subject Summary')
subsum.set_column('A:CC',15)


headerf = wb.add_format()
bg = wb.add_format()

headerf.set_bold()
headerf.set_italic()
headerf.set_font_color('brown')
headerf.set_bg_color('#C0C0C0')
headerf.set_center_across()
bg.set_bg_color('#C0C0C0')

subsum.set_row(0,50,headerf)
subsum.set_row(1,20,bg)

#Filling in the Cells for the subject summary sheet
subsum.write('A1', 'Study Name')
subsum.write('B1','First Name')
subsum.write('C1','Last Name')
subsum.write('D1','Study ID')
subsum.write('E1','Reader ID')
subsum.write('F1','Date Scanned')
subsum.write('G1','Date Analyzed')
subsum.write('H1','Condition')
subsum.write('I1','Image File')
subsum.write('J1','Image Frames')
subsum.write('K1','Length(sec.)')
subsum.write('L1','DIAMETER')
subsum.write('M1','Average Diameter')
subsum.write('N1','Minimum Diameter')
subsum.write('O1','Maximum Diameter')
subsum.write('P1','Diameter Max (3-sec-smoothed)')
subsum.write('Q1','Diameter Max (5-sec-smoothed)')
subsum.write('R1','Diameter Max (10-sec-smoothed)')
subsum.write('S1','Flow Velocity Avg (meter/sec)')
subsum.write('T1','Flow Velocity Max (meter/sec)')
subsum.write('U1','Flow velocity integral avg (meters')

subsum.write('A7','No AVG')
subsum.write('A8','3-sec AVG')
subsum.write('A9','5-sec AVG')
subsum.write('A10','10-sec AVG')
subsum.write('B6','Unscaled %FMD')
subsum.write('C6','Allometrically Scaled %FMD')
subsum.write('D6','Time to peak (s)')

sumstudyname = 'Summary - ' + studyname
sumbsl = wb.add_worksheet(sumstudyname)

wb.close()


#Another workbook created for template

wb1 = xlsxwriter.Workbook('fmd_template_example.xlsx')

sheet1 = wb1.add_worksheet('Overview')
sheet1.set_column('A:B',25)

tablef = wb1.add_format()
tablefb = wb1.add_format()

tablef.set_border()
tablefb.set_border()
tablefb.set_bold()

sheet1.write('A1','Study Name')
sheet1.write('A2','Protocol #')
sheet1.write('A3','Participant Name')
sheet1.write('A4','Participant ID')
sheet1.write('A5','Date of Study')
sheet1.write('A6','Type of Participant')

sheet1.write('B9','', tablef)
sheet1.write('C9','MAX',tablefb)
sheet1.write('D9','MIN',tablefb)
sheet1.write('E9','MEAN',tablefb)
sheet1.write('F9','%DILATION',tablefb)

wb1.close()