MU Brachial Analyzer for Research   ***This file is not read-only and if you make (and save) changes
					  they will be permanent!!!

Created by: Haley Kleinhans, Allison Goetz, Emma Moravec, Daniel Pederson & Daniel Pederson
Last Edit: 04/28/2020

This program automatically calculates Brachial Flow-Mediated Dilation measurements from 
recorded ultrasound images. The current program is able to receive AVI video file inputs, 
and output the Flow-Mediated Dilation measurements in an excel file. 

Instructions for Use:
Click on "Flow Mediated Dilation" to begin.
On the file page, input the files wished to be used for analysis using the "Choose File"
button. Test Names, Study Name, and Patient ID fields should be filled (although not necessary). 
Press "Run" 
The first frame of the first file will appear. Click on the location in the artery where diameter
is desired to be measured. Adjust the top slider to decrease the width of the diameter used for
measurement. Adjust the bottom slider to adjust the threshold of the automatic edge detection.
When the desired area for diameter measurement is surrounded by a green box, click "Acceptable"
If there is another video, repeat the same process for the first frame of each video. 
After all the frames are completed, the program will run through all the diameters of each video.
Frames for which the diameter changes more than 1% from the previous frame and frames which are
more than 5% from the first frame are flagged and can be manually re-adjusted using "Manual" mode.  
After flagged images are re-adjusted, the file can be saved to excel. The user can select a 
location for the file to be saved as well as a name for the file. 

Known Bugs/Issues: 
- Dicom files are not compatible.
- Width of detection can only be decreased from the edges, not adjusted individually.
- If the excel file where the save is desired is open, the excel cannot save. 
- Frame-Rate is hardcoded at 16 fps.
- Number of Edited and Discarded Frames is not shown in Excel
- Manual Adjustment is pretty inaccurate. Discarding is recommended. 

Future Update Necessities:
- Make compatible with Dicom.
- Increase accuracy of manual adjustment.