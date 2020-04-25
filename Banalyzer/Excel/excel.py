#Putting Variables Into Excel
#This progam generates the excel template and also places the data into an excel-viewable format
import sys
import numpy as np
import datetime
sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd
import xlsxwriter

def PrintHi():
    print("printing %dif")
    print(gbl_fmd.i_class)
def ExcelReport(folder_path, excel_file_name):

#Variables (regardless of i_class val)
    img_num = gbl_fmd.i_class
    studyname = gbl_fmd.class_list[0].study_name
    nombre = gbl_fmd.class_list[0].patient_name
    studyid = '11'
    studytype = ''
    subjectid = gbl_fmd.class_list[0].patient_name
    gender = 'other'
    rawdate = datetime.datetime.today()
    date = rawdate.strftime('%b %d, %Y  (%m-%d-%y)')
    print(date)
    imagingdate = 'Yesterday'



    pixelsize = .06    #mm/pixel # gbl_fmd.class_list[img_num].pixel2real_conversion
    roilength = ''
    frameinitial = ''

    framevalid = ''
    framereject = ''
    frameexclud = ''
    frameedit = ''
    framenotanal = ''
    confidence = '40%'
    fps = 10
    mspf = fps*10  #milliseconds per frame


    #Creating workbook fmd_report
    excel_path = folder_path + excel_file_name + '.xlsx'
    wb = xlsxwriter.Workbook(excel_path)
    # wb = xlsxwriter.Workbook('fmd_report_example.xlsx')

    #Workbook Formats
    headerf = wb.add_format()
    bg = wb.add_format()

    headerf.set_bold()
    headerf.set_italic()
    headerf.set_font_color('brown')
    headerf.set_bg_color('#C0C0C0')
    headerf.set_center_across()
    headerf.set_text_wrap()
    bg.set_bg_color('#C0C0C0')
    bg.set_text_wrap()

    #Creating Sheet for Subject Summary
    subsum = wb.add_worksheet('Subject Summary')
    subsum.set_column('A:CC',15)

    #Worksheet Formats
    subsum.set_row(0,50,headerf)
    subsum.set_row(1,20,bg)

    #Filling in the Cells for the subject summary sheet
    subsum.write('A1', 'Study Name'); subsum.write('A2', studyname); subsum.write('A3',studyname)
    subsum.write('B1','First Name'); subsum.write('B2', nombre)
    subsum.write('C1','Last Name'); subsum.write('C2',nombre)
    subsum.write('D1','Study ID'); subsum.write('D2', studyid)




    #Table Summary
    subsum.write('A7','No AVG')
    subsum.write('A8','3-sec AVG')
    subsum.write('A9','5-sec AVG')
    subsum.write('A10','10-sec AVG')
    subsum.write('B6','Unscaled %FMD')
    subsum.write('C6','Allometrically Scaled %FMD')
    subsum.write('D6','Time to peak (s)')



    for i in range(gbl_fmd.i_class):
        img_num = i

        #Variables
        frametotal = len(gbl_fmd.class_list[img_num].diameter_arr)
        studynametest = gbl_fmd.class_list[img_num].study_name +  ' - ' + gbl_fmd.class_list[img_num].test_name
        filename = gbl_fmd.class_list[img_num].file_path
        #baselineflag = gbl_fmd.class_list[img_num].base_flag
        #if (baselineflag == 1):
        #    condition = "Baseline"
        #else:
        #    condition = gbl_fmd.class_list[img_num].test_name

        # Names
        sumstudyname = 'Summary - ' + studynametest
        datastudyname = 'Data - ' + studynametest
    #Worksheet Baseline Summary
        sumb = wb.add_worksheet(sumstudyname)

    #Format
        sumb.set_column('A:A',25)
        sumb.set_column('B:B',50)

        sumb.set_row(0,20,headerf)
        for x in range(1,frametotal,1):
             if (x%2 == 1):
                 sumb.set_row(x,15,bg)

    #Cells
        sumb.write('A1','BRACHIAL-REPORT',headerf)
        sumb.write('A2','Report-date'); sumb.write('B2',date)
        sumb.write('A3','Subject-ID'); sumb.write('B3',subjectid)
        sumb.write('A4','Study-ID'); sumb.write('B4',studyid)
        sumb.write('A5','Study-type'); sumb.write('B5',studytype)
        sumb.write('A6','Condition'); sumb.write('B6','Baseline')
        sumb.write('A7','Subject-Gender'); sumb.write('B7',gender)
        sumb.write('A8','Name'); sumb.write('B8',nombre)
        sumb.write('A9','Imaging-date'); sumb.write('B9',imagingdate)
        sumb.write('A10','Analysis-date'); sumb.write('B10',date)
        sumb.write('A11','SDY-filename'); sumb.write('B11',filename)
        sumb.write('A12','Image-filename'); sumb.write('B12',filename)
        sumb.write('A13','Pixel-siz-mm/p'); sumb.write('B13',pixelsize)
        sumb.write('A14','ROI-length-mm'); sumb.write('B14',roilength)
        sumb.write('A15','Frame-initialized'); sumb.write('B15',frameinitial)
        sumb.write('A16','Frames-total'); sumb.write('B16',frametotal)
        sumb.write('A17','Frames-valid'); sumb.write('B17',framevalid)
        sumb.write('A18','Frames-reject'); sumb.write('B18',framereject)
        sumb.write('A19','Frames-exclud'); sumb.write('B19',frameexclud)
        sumb.write('A20','Frames-edited'); sumb.write('B20',frameedit)
        sumb.write('A21','Frames-notanal'); sumb.write('B21',framenotanal)
        sumb.write('A22','Confid-thresh'); sumb.write('B22',confidence)




    #Worksheet Baseline Data
        datab = wb.add_worksheet(datastudyname)

        #Formatting
        datab.set_column('A:AC',25)
        datab.set_row(0,20,headerf)

        # Writing Columnar Data
        datab.write_column(1, 1, gbl_fmd.class_list[img_num].diameter_arr)
        #datab.write_column(1, 2, (gbl_fmd.class_list[img_num].diameter_arr *(1.0/pixelsize)))
        #datab.write_column(1, 2, gbl_fmd.class_list[-1].REALDIAMARR)
        datab.write_column(1,6,gbl_fmd.class_list[img_num].percent_dif)
        datab.write_column(1,7,gbl_fmd.class_list[img_num].percent_dif_flag)

        #Formatting and Frame #
        for row_num in range(1,frametotal,1):
            datab.write(row_num, 0, row_num)  #Writing frame number
            datab.write(row_num,4, row_num*mspf-mspf)  #Writing MSEC
            datab.write(row_num,2, gbl_fmd.class_list[img_num].diameter_arr[row_num] * pixelsize)
            if (row_num%2 == 1):
                datab.set_row(row_num,15,bg)


        #Upper Labels
        datab.write('A1','Frame'); datab.write('B1','AVG Pixel Diameter'); datab.write('C1','BDIAMM')
        datab.write('D1','Patient ID'); datab.write('E1','MSEC'); datab.write('F1','COND');
        datab.write('G1','Percent Dif'); datab.write('H1','Dif Flag'); datab.write('G1',' ')

        #Chart
        basechart = wb.add_chart({'type': 'scatter', 'subtype': 'straight'})
        basechartystr = '=\'' + datastudyname + '\'!$C$2:$C$' + str(frametotal)
        basechartxstr = '=\'' + datastudyname + '\'!$A$2:$A$' + str(frametotal)
        basechart.add_series({'values': basechartystr, 'categories': basechartxstr})
        basechart.set_x_axis({'name': 'Frame Index'});basechart.set_y_axis({'name': 'Diameter (mm)'})
        basechart.set_title({'name':'Diameter'})
        sumb.insert_chart('D1', basechart)

        #Subject Summary Information (Dependent on Trial)
        subsum.write('F1','Date Scanned'); subsum.write(img_num + 1, 5, imagingdate)
        subsum.write('G1','Date Analyzed'); subsum.write(img_num + 1, 6, date)
        #subsum.write('H1','Condition'); subsum.write(img_num + 1, 7, condition)
        subsum.write('I1','Image File'); subsum.write(img_num + 1, 8, filename)
        subsum.write('J1','Image Frames'); subsum.write(img_num + 1, 9, frametotal)  #commented for now for frame total
        subsum.write('K1','Length(sec.)'); subsum.write(img_num + 1, 10, frametotal/fps) #commented for now for frame total

        subsum.write('L1', 'DIAMETER')
        subsum.write('M1', 'Average Diameter'); subsum.write(img_num + 1, 12, np.mean(gbl_fmd.class_list[img_num].diameter_arr))
        subsum.write('N1', 'Minimum Diameter'); subsum.write(img_num + 1, 13, np.min(gbl_fmd.class_list[img_num].diameter_arr))
        subsum.write('O1', 'Maximum Diameter'); subsum.write(img_num + 1, 14, np.max(gbl_fmd.class_list[img_num].diameter_arr))
        subsum.write('P1', 'Diameter Max (3-sec-smoothed)')
        subsum.write('Q1', 'Diameter Max (5-sec-smoothed)')
        subsum.write('R1', 'Diameter Max (10-sec-smoothed)')
        subsum.write('S1', 'Flow Velocity Avg (meter/sec)')
        subsum.write('T1', 'Flow Velocity Max (meter/sec)')
        subsum.write('U1', 'Flow velocity integral avg (meters')



    wb.close()

def ExcelTemplate():
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