#Putting Variables Into Excel
#This progam generates the excel template and also places the data into an excel-viewable format
import sys

sys.path.append('../')  # could be hacky, need to figure out how to share between files
import Global.gbl_fmd_class_list as gbl_fmd
import xlsxwriter

def PrintHi():
    print(gbl_fmd.i_class)

def ExcelReport():

#Variables (regardless of i_class val)
    img_num = gbl_fmd.i_class
    studyname = gbl_fmd.class_list[img_num].study_name
    nombre = gbl_fmd.class_list[img_num].patient_name
    studyid = '11'
    studytype = ''
    subjectid = '123456789'
    patid = '123456789'
    stagename = ''
    gender = 'other'
    dob = 'A While Back'
    date = 'Today'
    imagingdate = 'Yesterday'
    machineID = 'GE Ultrasound'
    probeID = ''
    sonographerID = ''
    interpreterID = ''
    baseimgfilename = ''
    basesdyfilename = ''

    roilength = ''
    frameinitial = ''

    framevalid = ''
    framereject = ''
    frameexclud = ''
    frameedit = ''
    framenotanal = ''
    confidence = ''
    trend = ''
    trendmse = ''
    reproduc = ''
    readingnum = ''
    fps = 10
    mspf = fps*10  #milliseconds per frame

    rhimgfilename = ''
    rhdyfilename = ''
    rhframeinitial = ''
    rhframetotal = 500
    rhframevalid = ''
    rhframereject = ''
    rhframeexclud = ''
    rhframeedit = ''
    rhframenotanal = ''





    #Creating workbook fmd_report
    wb = xlsxwriter.Workbook('fmd_report_example.xlsx')

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
    subsum.write('E1','Reader ID'); subsum.write('E2', interpreterID)
    subsum.write('F1','Date Scanned'); subsum.write('F2', imagingdate)
    subsum.write('G1','Date Analyzed'); subsum.write('G2', date)
    subsum.write('H1','Condition'); subsum.write('H2', 'Baseline'); subsum.write('H3', 'Deflation')
    subsum.write('I1','Image File'); subsum.write('I2', baseimgfilename), subsum.write('I3', rhimgfilename)
    subsum.write('J1','Image Frames'); subsum.write('J2', frametotal); subsum.write('J3', rhframetotal)
    subsum.write('K1','Length(sec.)'); subsum.write('K2', frametotal/fps); subsum.write('K3', rhframetotal/fps)
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



    #Table Summary
    subsum.write('A7','No AVG')
    subsum.write('A8','3-sec AVG')
    subsum.write('A9','5-sec AVG')
    subsum.write('A10','10-sec AVG')
    subsum.write('B6','Unscaled %FMD')
    subsum.write('C6','Allometrically Scaled %FMD')
    subsum.write('D6','Time to peak (s)')



    for i in range(gbl_fmd.i_class + 1):
        img_num = i





        #Variables
        frametotal = len(gbl_fmd.class_list[img_num].diameter_arr)
        pixelsize = gbl_fmd.class_list[img_num].pixel2real_conversion



        studynametest = gbl_fmd.class_list[img_num].study_name +  ' - ' + gbl_fmd.class_list[img_num].test_name
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
        sumb.write('A4','Pat-ID-type'); sumb.write('B4',patid)
        sumb.write('A5','Study-ID'); sumb.write('B5',studyid)
        sumb.write('A6','Study-type'); sumb.write('B6',studytype)
        sumb.write('A7','Condition'); sumb.write('B7','Baseline')
        sumb.write('A8','StageName'); sumb.write('B8',stagename)
        sumb.write('A9','Subject-Gender'); sumb.write('B9',gender)
        sumb.write('A10','Name'); sumb.write('B10',nombre)
        sumb.write('A11','Date-of-birth'); sumb.write('B11',dob)
        sumb.write('A12','Imaging-date'); sumb.write('B12',imagingdate)
        sumb.write('A13','Analysis-date'); sumb.write('B13',date)
        sumb.write('A14','Machine-ID'); sumb.write('B14',machineID)
        sumb.write('A15','Probe-ID'); sumb.write('B15',probeID)
        sumb.write('A16','Sonographer-ID'); sumb.write('B16',sonographerID)
        sumb.write('A17','Interpreter-ID'); sumb.write('B17',interpreterID)
        sumb.write('A18','SDY-filename'); sumb.write('B18',basesdyfilename)
        sumb.write('A19','Image-filename'); sumb.write('B19',baseimgfilename)
        sumb.write('A20','Pixel-siz-mm/p'); sumb.write('B20',pixelsize)
        sumb.write('A21','ROI-length-mm'); sumb.write('B21',roilength)
        sumb.write('A22','Frame-initialized'); sumb.write('B22',frameinitial)
        sumb.write('A23','Frames-total'); sumb.write('B23',frametotal)
        sumb.write('A24','Frames-valid'); sumb.write('B24',framevalid)
        sumb.write('A25','Frames-reject'); sumb.write('B25',framereject)
        sumb.write('A26','Frames-exclud'); sumb.write('B26',frameexclud)
        sumb.write('A27','Frames-edited'); sumb.write('B27',frameedit)
        sumb.write('A28','Frames-notanal'); sumb.write('B28',framenotanal)
        sumb.write('A29','Confid-thresh'); sumb.write('B29',confidence)
        sumb.write('A30','Trend-thresh'); sumb.write('B30',trend)
        sumb.write('A31','Trend-MSE-mm'); sumb.write('B31',trendmse)
        sumb.write('A32','Reproduc-round'); sumb.write('B32',reproduc)
        sumb.write('A33','Reading-number'); sumb.write('B33',readingnum)


    #Worksheet Baseline Data
        datab = wb.add_worksheet(datastudyname)

        #Formatting
        datab.set_column('A:AC',25)
        datab.set_row(0,20,headerf)

        # Writing Pixel Diameters in Second Column
        datab.write_column(1, 1, gbl_fmd.class_list[img_num].diameter_arr)
        #datab.write_column(1, 2, gbl_fmd.class_list[-1].REALDIAMARR)


        #Formatting and Frame #
        for row_num in range(1,frametotal,1):
            datab.write(row_num, 0, row_num)  #Writing frame number
            datab.write(row_num,7,row_num*mspf-mspf)  #Writing MSEC
            if (row_num%2 == 1):
                datab.set_row(row_num,15,bg)


        #Upper Labels
        datab.write('A1','Frame'); datab.write('B1','AVG Pixel Diameter'); datab.write('C1','BDIAMM')
        datab.write('D1','Patient ID'); datab.write('E1','STYPE'); datab.write('F1','SDATE')
        datab.write('G1','STIME'); datab.write('H1','MSEC'); datab.write('I1','COND')

        basechart = wb.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})
        basechartystr = '=\'' + datastudyname + '\'!$B$2:$B$' + str(frametotal)
        basechartxstr = '=\'' + datastudyname + '\'!$H$2:$H$' + str(frametotal)
        basechart.add_series({'values': basechartystr, 'categories': basechartxstr})
        basechart.set_x_axis({'name': 'Time (ms)'});basechart.set_y_axis({'name': 'Diameter (pixels)'})
        basechart.set_title({'name':'Baseline Test Diameter'})
        sumb.insert_chart('D1', basechart)



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