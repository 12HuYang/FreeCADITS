# FreeCADITS
An Intelligent Tutoring system for Boolean Operations on FreeCAD, the purpose of this project is to evaluate the effectiveness of multiple solutions teaching methods. 

![screenshot](https://raw.githubusercontent.com/12HuYang/FreeCADITS/master/Training_intro.png)

The project is published to the ASEE 2016 conference, the paper includes screenshots and introduction of the training process, which is available at: https://www.researchgate.net/publication/317238436_Work_in_Progress_A_Computer-Aided_Design_Intelligent_Tutoring_System_Teaching_Strategic_Flexibility


How to use the files ? 

1) Make a folder under the path of your FreeCAD/Mod/
2) Copy all files under the folder, then run FreeCAD, you should see "I.T.S" in workbanch.

How to add your lecture/exercises ?
First, I have to say, the interface is not to facilitate this process, so you have to add your own codes to the file...
1) Build the basic shapes and operations your lecture needs, add an icon to each shape via adding your codes to the ITSGui.py file. You are welcomed to test my code in your case.
2) If you want to check the answer of your users, first make sure you compute all the available solutions, you can refer to the DP_FreeCAD.py to see my search method. After that, I use the the method in the SearchAgent.py to check answers submitted by users.
3) You can add your right side wedget to the tutorial system, take a look at myWedget_Ui.py file, all the wedget I made are under myWidget_Ui() class. 
