__author__ = 'yangh_000'

import sys
from PySide import QtCore,QtGui
import FreeCAD
import FreeCADGui
from time import strftime
import begin
import ITSGui
import os
import types
import time
import WebGui

filename=[]
tutoring=[]
starttime=[0,0,0,0,0]
textbooktrain=[]

def mouseview():
     mb = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, "Mouse model", None)
     mb.setIconPixmap("./Mod/ITS_test00/mouse_model.png")
     mb.exec_()




class extratest_dialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(extratest_dialog,self).__init__(parent)
        self.question=QtGui.QLabel("Do you want to continue to do next test ?")
        self.info=QtGui.QLabel("It is not required. If you want, please click 'Yes', or you can click 'No' to quit.")
        self.yes=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Yes)
        self.no=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.No)
        self.yes.clicked.connect(self.extratest)
        self.no.clicked.connect(self.quit)
        layout=QtGui.QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 100)
        layout.addWidget(self.question,0,0)
        layout.addWidget(self.info,1,0)
        layout.addWidget(self.yes,3,0)
        layout.addWidget(self.no,3,1)
        self.setLayout(layout)
        self.setWindowTitle("Extra Test")

    def extratest(self):
        begin.extratest+=1
        self.close()

    def quit(self):
        self.close()

class inputdialog(QtGui.QDialog):
    def __init__(self,parent=None):
        super(inputdialog,self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.age=None
        self.major=None
        self.group=None
        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.Panel
        self.ageLabel=QtGui.QLabel("Age  ")
        #self.agetext=QtGui.QLabel("")
        self.agetext=QtGui.QLineEdit()
        #self.agetext.setFrameStyle(frameStyle)
        #self.agebutton=QtGui.QPushButton("click...")
        self.majorLabel=QtGui.QLabel("Major(if applicable)")
        #self.majortext=QtGui.QLabel("")
        self.majortext=QtGui.QLineEdit()
        #self.majorbutton=QtGui.QPushButton("click...")
        #self.majortext.setFrameStyle(frameStyle)
        self.groupLabel=QtGui.QLabel("Group ")
        self.grouptext=QtGui.QComboBox()
        groups=['1','2','3']
        self.grouptext.addItems(groups)
        #self.grouptext.setFrameStyle(frameStyle)
        #self.groupbutton=QtGui.QPushButton("choose a group...")
        self.buttonBox=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.ok)
        #self.agebutton.clicked.connect(self.slotAge)
        #self.majorbutton.clicked.connect(self.slotMajor)
        #self.groupbutton.clicked.connect(self.slotGroup)

        layout=QtGui.QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 200)
        layout.addWidget(self.ageLabel,0,0)
        layout.addWidget(self.agetext,0,1)
        #layout.addWidget(self.agebutton,0,2)
        layout.addWidget(self.majorLabel,1,0)
        layout.addWidget(self.majortext,1,1)
        #layout.addWidget(self.majorbutton,1,2)
        layout.addWidget(self.groupLabel,2,0)
        layout.addWidget(self.grouptext,2,1)
        #layout.addWidget(self.groupbutton,2,2)
        layout.addWidget(self.buttonBox,4,1)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog")

    def slotAge(self):
         age,ok=QtGui.QInputDialog.getInteger(self,"Age","Select your age",20,18,100,1)
         if ok:
            self.agetext.setText(str(age))

    def slotMajor(self):
        major,ok=QtGui.QInputDialog.getText(self,"Major","Type in your major")
        if ok:
            self.majortext.setText(major)

    def slotGroup(self):
        groups=['1','2','3']
        group,ok=QtGui.QInputDialog.getItem(self,"Select your group","Group:",groups,0,False)
        if ok:
            self.grouptext.setText(group)

    def ok(self):
        if self.agetext.text() and self.grouptext.currentText():
                self.age=self.agetext.text()
                self.major=self.majortext.text()
                self.group=self.grouptext.currentText()
                dia=QtGui.QMessageBox()
                dia.setText('Input Information')
                dia.setInformativeText('Age is: '+self.age+'\n'+'Major is: '+str(self.major)+'\n'+'Group is: '+str(self.group)+'\n\n'+'If the above input are correct, please click "Yes" to continue.')
                dia.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
                ret=dia.exec_()
                if ret==QtGui.QMessageBox.Yes:
                    self.addinfo()
                else:
                    return
        else:
                if self.majortext.text() or self.grouptext.currentText():
                    QtGui.QMessageBox.warning(None, "input info", "Please enter your age."+'\n')
                else:
                    QtGui.QMessageBox.warning(None,"input info","Please enter your age, "
                                                                "group and major if applicable."+'\n')

    def addinfo(self):
        if not os.path.exists('./Log/'):
            os.makedirs('./Log/')
        for i in range(1,201):
            fname='Participant_'+str(i)+'.txt'
            exist=os.path.isfile('./Log/'+fname)
            if exist==False:
                f=open('./Log/'+fname,'w')
                f.write('Age    '+str(self.age)+'\n')
                f.write('Major  '+str(self.major)+'\n')
                f.write('Group  '+str(self.group)+'\n')
                f.close()
                filename.append(fname)
                break
        tutoring.append(self.group)
        self.close()

class BooleanOperation(QtGui.QHBoxLayout):
    def __init__(self,parent=None):
        super(BooleanOperation,self).__init__(parent)
        self.union=QtGui.QLabel()
        self.union.setText(str(ITSGui.uniontime))
        self.union.setFixedWidth(30)
        self.common=QtGui.QLabel()
        self.common.setText(str(ITSGui.commontime))
        self.common.setFixedWidth(30)
        self.cut=QtGui.QLabel()
        self.cut.setText(str(ITSGui.cuttime))
        self.cut.setFixedWidth(30)
        font1=QtGui.QFont("Times")
        font1.setPixelSize(15)
        self.union.setFont(font1)
        self.common.setFont(font1)
        self.cut.setFont(font1)
        self.addWidget(self.union)
        self.addWidget(self.common)
        self.addWidget(self.cut)
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(300)

    def update(self):
        self.union.setText(str(ITSGui.uniontime))
        self.common.setText(str(ITSGui.commontime))
        self.cut.setText(str(ITSGui.cuttime))

class ExtraBooleanOperation(QtGui.QHBoxLayout):
    def __init__(self,parent=None):
        super(ExtraBooleanOperation,self).__init__(parent)
        self.union=QtGui.QLabel()
        self.union.setText(str(ITSGui.uniontime_2))
        self.union.setFixedWidth(30)
        self.common=QtGui.QLabel()
        self.common.setText(str(ITSGui.commontime_2))
        self.common.setFixedWidth(30)
        self.cut=QtGui.QLabel()
        self.cut.setText(str(ITSGui.cuttime_2))
        self.cut.setFixedWidth(30)
        font1=QtGui.QFont("Times")
        font1.setPixelSize(15)
        self.union.setFont(font1)
        self.common.setFont(font1)
        self.cut.setFont(font1)
        self.addWidget(self.union)
        self.addWidget(self.common)
        self.addWidget(self.cut)
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(300)

    def update(self):
        self.union.setText(str(ITSGui.uniontime_2))
        self.common.setText(str(ITSGui.commontime_2))
        self.cut.setText(str(ITSGui.cuttime_2))



'''
class Common(QtGui.QLabel):
    def __init__(self,parent=None):
        super(Common,self).__init__(parent)
        self.setText(str(ITSGui.commontime))
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(300)

    def update(self):
        self.setText(str(ITSGui.commontime))

class Cut(QtGui.QLabel):
    def __init__(self,parent=None):
        super(Cut,self).__init__(parent)
        self.setText(str(ITSGui.cuttime))
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(300)

    def update(self):
        self.setText(str(ITSGui.cuttime))
'''


class DigitClock(QtGui.QLCDNumber):
    def __init__(self,parent=None):
        super(DigitClock,self).__init__(parent)
        self.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.setFixedHeight(100)
        self.time=5
        doublezero=':00'
        self.secondnumber=0
        if (len(begin.begin)==2 and len(begin.submit)==1) or (tutoring[0]=='2' and len(begin.begin)==1 and len(begin.submit)==1):
            self.time=20
            doublezero=':00'
            self.secondnumber=0
        self.display(str(0)+str(self.time)+doublezero)
        self.timer = QtCore.QTimer(self)
        self.minnumber=self.time
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.setWindowTitle("Digital Clock")
        self.resize(150, 60)



    def showTime(self):
        self.zeroMin = '0'
        self.zeroSecond = '0'
        if self.secondnumber == 0:
            self.secondnumber = 59
            if self.minnumber == 0:
                if tutoring[0]=='2' and len(begin.begin)==1 and len(begin.submit)==1:
                    #QtGui.QMessageBox.warning(None,"","Times up!")
                    textbooktrain.append(1)
                #begin.timesup+=1
                self.timer.stop()
                return
            else:
                self.minnumber-=1
        else:
            self.secondnumber-=1
        if self.secondnumber>=10:
            time=self.zeroMin+str(self.minnumber)+':'+str(self.secondnumber)
        else:
            time=self.zeroMin+str(self.minnumber)+':'+self.zeroSecond+str(self.secondnumber)
        self.display(time)

class postsurvey_ui(QtGui.QDockWidget):
    def __init__(self,parent=None):
        super(postsurvey_ui,self).__init__(parent)
        self.answer=[0]*15
        self.questiongroup=[]
        self.setObjectName("Post_survey")
        #self.setFeatures(self.NoDockWidgetFeatures)
        self.setFixedWidth(800)
        self.setAutoFillBackground(True)
        self.pal=QtGui.QPalette()
        self.pal.setColor(self.pal.Background,QtCore.Qt.white)
        self.setPalette(self.pal)
        self.wii=QtGui.QWidget()
        self.scr=QtGui.QScrollArea()
        self.scr.setWidgetResizable(True)
        self.scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.layout=QtGui.QGridLayout(self.wii)
        self.wii.setLayout(self.layout)
        self.setWidget(self.scr)
        self.scr.setWidget(self.wii)
        font1=QtGui.QFont()
        font1.setPixelSize(14)
        font1.setBold(True)
        font2=QtGui.QFont()
        font2.setPixelSize(12)
        lab1=QtGui.QLabel("FreeCAD Intelligent Tutoring System Survey")
        lab1.setWordWrap(True)
        lab1.setFont(font1)
        lab2=QtGui.QLabel("*Note: You may leave any answer blank if you wish not to answer* \n\nPlease answer the following questions to the best of your ability:\nWhen you are done, please click 'Submit' at the end.\n ")
        lab2.setWordWrap(True)
        lab2.setFont(font2)
        self.layout.addWidget(lab1,0,1)
        self.layout.addWidget(lab2,1,1)
        lab3=QtGui.QLabel("1.What is your gender?\n")
        lab3.setFont(font2)
        self.layout.addWidget(lab3,2,1)
        self.radiobutton11=QtGui.QRadioButton("Male")
        self.radiobutton12=QtGui.QRadioButton("Female")
        self.buttongroup1=QtGui.QButtonGroup()
        self.buttongroup1.addButton(self.radiobutton11,0)
        self.buttongroup1.addButton(self.radiobutton12,1)
        self.layout.addWidget(self.radiobutton11,3,1)
        self.layout.addWidget(self.radiobutton12,4,1)
        lab4=QtGui.QLabel("2.Have you ever used any Computer-Aided-Design (CAD) software before?\n")
        lab4.setFont(font2)
        self.layout.addWidget(lab4,5,1)
        self.radiobutton21=QtGui.QRadioButton("Yes")
        self.radiobutton22=QtGui.QRadioButton("No")
        self.buttongroup2=QtGui.QButtonGroup()
        self.buttongroup2.addButton(self.radiobutton21,0)
        self.buttongroup2.addButton(self.radiobutton22,1)
        self.layout.addWidget(self.radiobutton21,6,1)
        self.layout.addWidget(self.radiobutton22,7,1)
        lab5=QtGui.QLabel("3.Only answer this question if you answered YES to question 2:\n  To your best knowledge,what is your skill level at using CAD software?\n")
        lab5.setFont(font2)
        self.layout.addWidget(lab5,8,1)
        self.radiobutton31=QtGui.QRadioButton("Beginner ")
        self.radiobutton32=QtGui.QRadioButton("Intermediate")
        self.radiobutton33=QtGui.QRadioButton("Expert")
        self.radiobutton34=QtGui.QRadioButton("Professional")
        self.buttongroup3=QtGui.QButtonGroup()
        self.buttongroup3.addButton(self.radiobutton31,0)
        self.buttongroup3.addButton(self.radiobutton32,1)
        self.buttongroup3.addButton(self.radiobutton33,2)
        self.buttongroup3.addButton(self.radiobutton34,3)
        self.layout.addWidget(self.radiobutton31,9,1)
        self.layout.addWidget(self.radiobutton32,10,1)
        self.layout.addWidget(self.radiobutton33,11,1)
        self.layout.addWidget(self.radiobutton34,12,1)
        lab6=QtGui.QLabel("4.Were you interested in geometry when you took it as a math class?\n")
        lab6.setFont(font2)
        self.layout.addWidget(lab6,13,1)
        self.radiobutton41=QtGui.QRadioButton("Not interested at all ")
        self.radiobutton42=QtGui.QRadioButton("A little")
        self.radiobutton43=QtGui.QRadioButton("Normal")
        self.radiobutton44=QtGui.QRadioButton("More than normal")
        self.radiobutton45=QtGui.QRadioButton("Very interested in")
        self.radiobutton46=QtGui.QRadioButton("Did not take a geometry math class")
        self.buttongroup4=QtGui.QButtonGroup()
        self.buttongroup4.addButton(self.radiobutton41,0)
        self.buttongroup4.addButton(self.radiobutton42,1)
        self.buttongroup4.addButton(self.radiobutton43,2)
        self.buttongroup4.addButton(self.radiobutton44,3)
        self.buttongroup4.addButton(self.radiobutton45,4)
        self.buttongroup4.addButton(self.radiobutton46,5)
        self.layout.addWidget(self.radiobutton41,14,1)
        self.layout.addWidget(self.radiobutton42,15,1)
        self.layout.addWidget(self.radiobutton43,16,1)
        self.layout.addWidget(self.radiobutton44,17,1)
        self.layout.addWidget(self.radiobutton45,18,1)
        self.layout.addWidget(self.radiobutton46,19,1)
        fname='./Mod/ITS_test00/post_survey.txt'
        with open(fname) as f:
            content=f.readlines()
        labels=[]
        for i in range(0,len(content)):
            if content[i]:
                templab=QtGui.QLabel(content[i])
                templab.setWordWrap(False)
                templab.setFont(font2)
                labels.append(templab)
        self.btugroups=[]
        for i in range(0,len(labels)):
            tmpbtugroup=QtGui.QButtonGroup()
            rbutton1=QtGui.QRadioButton("Strongly Agree")
            rbutton2=QtGui.QRadioButton("Agree")
            rbutton3=QtGui.QRadioButton("Undecided")
            rbutton4=QtGui.QRadioButton("Disagree")
            rbutton5=QtGui.QRadioButton("Strongly Disagree")
            tmpbtugroup.addButton(rbutton1,0)
            tmpbtugroup.addButton(rbutton2,1)
            tmpbtugroup.addButton(rbutton3,2)
            tmpbtugroup.addButton(rbutton4,3)
            tmpbtugroup.addButton(rbutton5,4)
            self.btugroups.append(tmpbtugroup)
        count=0
        count2=0
        for i in range(0,len(labels)):
            self.layout.addWidget(labels[i],i+20+count,1)
            btus=self.btugroups[i].buttons()
            for j in range(0,len(btus)):
                self.layout.addWidget(btus[j],j+21+count2,1)
            count+=5
            count2+=6

        self.linelable=QtGui.QLabel("If you have any suggestions or comments, please leave below, we  appreciate that.")
        self.layout.addWidget(self.linelable,87,1)
        self.line_edit=QtGui.QTextEdit()
        self.line_edit.width=200
        self.line_edit.height=100
        self.layout.addWidget(self.line_edit,88,1)

        self.button=QtGui.QPushButton("Submit")
        self.button.setFixedWidth(110)
        self.button.clicked.connect(self.getanswer)
        self.layout.addWidget(self.button,89,1)


    def getanswer(self):
        btugroup=self.buttongroup1.buttons()
        if btugroup[0].isChecked():
            self.answer[0]='Q1:     Male\n'
        if btugroup[1].isChecked():
            self.answer[0]='Q1:     Female\n'
        btugroup1=self.buttongroup2.buttons()
        if btugroup1[0].isChecked():
            self.answer[1]='Q2:     Yes\n'
        if btugroup1[1].isChecked():
            self.answer[1]='Q2:     No\n'
        btugroup2=self.buttongroup3.buttons()
        if btugroup2[0].isChecked():
            self.answer[2]='Q3:     Beginner        1\n'
        if btugroup2[1].isChecked():
            self.answer[2]='Q3:     Intermediate        2\n'
        if btugroup2[2].isChecked():
            self.answer[2]='Q3:     Expert      3\n'
        if btugroup2[3].isChecked():
            self.answer[2]='Q3:     Professional        4\n'
        btugroup3=self.buttongroup4.buttons()
        if btugroup3[0].isChecked():
            self.answer[3]='Q4:     Not interested at all       1\n'
        if btugroup3[1].isChecked():
            self.answer[3]='Q4:     A little        2\n'
        if btugroup3[2].isChecked():
            self.answer[3]='Q4:     Normal        3\n'
        if btugroup3[3].isChecked():
            self.answer[3]='Q4:     More than normal        4\n'
        if btugroup3[4].isChecked():
            self.answer[3]='Q4:     Very interested in        5\n'
        if btugroup3[5].isChecked():
            self.answer[3]='Q4:     Did not take a geometry math class        -0\n'
        for i in range(0,len(self.btugroups)):
            tmpbtus=self.btugroups[i].buttons()
            for j in range(0,len(tmpbtus)):
                if tmpbtus[0].isChecked():
                    self.answer[i+4]='Q'+str(i+5)+":    StronglyAgree   5\n"
                if tmpbtus[1].isChecked():
                    self.answer[i+4]='Q'+str(i+5)+":    Agree   4\n"
                if tmpbtus[2].isChecked():
                    self.answer[i+4]='Q'+str(i+5)+":    Undecided   3\n"
                if tmpbtus[3].isChecked():
                    self.answer[i+4]='Q'+str(i+5)+":    Disagree    2\n"
                if tmpbtus[4].isChecked():
                    self.answer[i+4]='Q'+str(i+5)+":    Strongly Disagree   1\n"
        for i in range(1,201):
                fname='Surveyanswer_'+str(i)+'.txt'
                exist=os.path.isfile('./Log/'+fname)
                if exist==False:
                    FreeCAD.Console.PrintMessage(fname+'not exist at '+str(os.path))
                    f=open('./Log/'+fname,'w')
                    f.write(filename[0])
                    f.write("\n")
                    #f.write('./Log/'+fname)
                    for j in range(0,len(self.answer)):
                        f.write(str(self.answer[j]))
                        f.write("\n")
                    f.write("User comments: \n")
                    f.write(str(self.line_edit.document().toPlainText()))
                    f.close()
                    break

        #QtGui.QMessageBox.warning(None,"",str(self.answer))

        #QtGui.QMessageBox.information(None,"",str(self.line_edit.document().toPlainText()))
        QtGui.QMessageBox.information(None,"","Thank you for joining our project!\n Have a nice day!\n")
        self.close()







class myWidget_Ui(object):
    def __init__(self):
        self.time=5
        self.creatCountDown()


    def welcome(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QGridLayout(wii)
        lab1=qtg.QLabel("Welcome to FreeCAD I.T.S")
        #lab1=qtg.QLabel("FreeCAD Intelligent Tutoring System Survey \n *Note: You may leave any answer blank you do not wish to answer* \n")
        lab1.setWordWrap(True)
        widget.setObjectName("Welcome")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        widget.setAutoFillBackground(True)
        pal=QtGui.QPalette()
        pal.setColor(pal.Background,QtCore.Qt.white)
        widget.setPalette(pal)
        #widget.setFixedWidth(2000)
        #widget.setFixedHeight(1000)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)
        font1=qtg.QFont("Times")
        font1.setPixelSize(20)
        font1.setItalic(True)
        font1.setBold(True)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        f=open("./Mod/ITS_test00/welcome01.txt","rb")
        text01=f.read()
        lab2=qtg.QLabel(text01)
        lab2.setWordWrap(True)
        lab2.setFixedWidth(380)
        font2=qtg.QFont("Times")
        font2.setPixelSize(17)
        lab2.setFont(font2)
        layout.addWidget(lab2,1,0)
        lab3=qtg.QLabel()
        pix01=qtg.QPixmap("./Mod/ITS_test00/welcome01.png")
        lab3.setPixmap(pix01)
        layout.addWidget(lab3,2,0)
        '''
        postsurvey='./Mod/ITS_test00/post_survey.txt'
        with open(postsurvey) as f:
            content=f.readlines()
        for i in range(0,len(content)):
            if content[i]:
                QtGui.QMessageBox.warning(None,"",content[i])
        '''
        #WebGui.openBrowser("./Mod/ITS_test00/test.htm")

    def addstarttime(self,currenttime):
        for i in range(0,6):
            if starttime[i] is 0:
                starttime[i]= currenttime
                break

    def pretest(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        toplayout=qtg.QHBoxLayout()
        layout=qtg.QVBoxLayout(wii)
        widget.setObjectName("Pretest")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        reminderbutton=QtGui.QPushButton('Task Reminder')
        reminderbutton.clicked.connect(self.pretestreminder)
        reminderbutton.setFixedWidth(100)
        mousemodelreminderbutton=QtGui.QPushButton('Rotation view')
        mousemodelreminderbutton.clicked.connect(mouseview)
        mousemodelreminderbutton.setFixedWidth(100)
        toplayout.addWidget(reminderbutton)
        toplayout.addWidget(mousemodelreminderbutton)
        layout.addLayout(toplayout)

        #layout.addWidget(self.countDown)
        '''
        f=open("./Mod/ITS_test00/pretest01.txt","rb")
        text01=f.read()
        lab1=qtg.QLabel(text01)
        lab1.setWordWrap(True)
        lab1.setFixedWidth(380)
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        '''
        lab2=qtg.QLabel()
        movie=QtGui.QMovie("./Mod/ITS_test00/model1.gif")
        pix01=qtg.QPixmap("./Mod/ITS_test00/pretest01.png")
        #lab2.setPixmap(pix01)
        lab2.setMovie(movie)
        movie.start()
        #layout.addWidget(reminderbutton,0,0)
        layout.addWidget(lab2)
        lab3=qtg.QLabel()
        lab3.setPixmap(pix01)
        layout.addWidget(lab3)

        #layout.addWidget(mousemodelreminderbutton,0,1)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        booleanoperation=BooleanOperation()
        empty=qtg.QHBoxLayout()
        emptylabel=qtg.QLabel(' Operation can be used:           ')
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        emptylabel.setFont(font1)
        empty.addWidget(emptylabel)
        emptyright=qtg.QHBoxLayout()
        emptyrightlable=qtg.QLabel('   ')
        emptyright.addWidget(emptyrightlable)
        tlayout=qtg.QHBoxLayout()
        tlayout.addLayout(empty)
        tlayout.addLayout(booleanoperation)
        tlayout.addLayout(emptyright)
        layout.addLayout(tlayout)
        lab4=qtg.QLabel()
        pix02=qtg.QPixmap("./Mod/ITS_test00/pretest02.png")
        lab4.setPixmap(pix02)
        layout.addWidget(lab4)
        layout.addWidget(timewidget)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)

    def pretestreminder(self):
        dia=QtGui.QMessageBox()
        dia.setText('Pretest description')
        dia.setInformativeText('Task: Sketch the 3D model shown on the right. '
                               'Click Submit_Pre_test, when you done. \n\nTime limit: 5 minutes\n')
        dia.exec_()

    def textbooktrain(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QGridLayout(wii)
        widget.setObjectName("Textbooktrain")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        #pix01=qtg.QPixmap("./Mod/ITS_test00/training.png")
        lab1=qtg.QLabel("Please use the textbook to finish training in this section.\n\n "
                        "Time limit: 20 minutes \n\n "
                        "Click Start_posttest when you were done.\n\n "
                        "NOTE: Post-test will automatically start if you used all 20 minutes!\n\n ")
        lab1.setWordWrap(True)
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        lab1.setFont(font1)
        #lab1.setPixmap(pix01)
        layout.addWidget(lab1,0,0)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        layout.addWidget(timewidget,2,0)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)
        '''
        mw=FreeCADGui.getMainWindow()
        gwidget=begin.GetWidget()
        reportview=gwidget.getReportview(mw)
        reportview.setFixedSize(400,300)
        reportview.setFeatures(widget.NoDockWidgetFeatures)
        va=reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(True)
        layout.addWidget(reportview,3,0)
        '''


    def training(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QGridLayout(wii)
        widget.setObjectName("Training")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(420)
        reminderbutton=QtGui.QPushButton('Task reminder')
        reminderbutton.clicked.connect(self.trainingreminder)
        reminderbutton.setFixedWidth(100)
        #layout.addWidget(reminderbutton,0,0)
        mousemodelreminderbutton=QtGui.QPushButton('Rotation view')
        mousemodelreminderbutton.clicked.connect(mouseview)
        mousemodelreminderbutton.setFixedWidth(100)
        toplayout=qtg.QHBoxLayout()
        toplayout.addWidget(reminderbutton)
        toplayout.addWidget(mousemodelreminderbutton)
        layout.addLayout(toplayout,0,0)

        #pix01=qtg.QPixmap("./Mod/ITS_test00/training01.png")
        #lab1=qtg.QLabel()
        #lab1.setPixmap(pix01)
        #layout.addWidget(lab1,0,0)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        lab2=qtg.QLabel()
        movie=qtg.QMovie("./Mod/ITS_test00/training_model1.gif")
        lab2.setMovie(movie)
        movie.start()
        layout.addWidget(lab2,1,0)
        lab3=qtg.QLabel()
        pix02=qtg.QPixmap("./Mod/ITS_test00/training04.png")
        lab3.setPixmap(pix02)
        layout.addWidget(lab3,1,0)
        #lab4=qtg.QLabel()
        #pix03=qtg.QPixmap("./Mod/ITS_test00/training03.png")
        #lab4.setPixmap(pix03)
        #layout.addWidget(lab4,2,0)
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        layout.addWidget(timewidget,2,0)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)
        mw=FreeCADGui.getMainWindow()
        gwidget=begin.GetWidget()
        reportview=gwidget.getReportview(mw)
        reportview.setFixedSize(350,250)
        reportview.setFeatures(widget.NoDockWidgetFeatures)
        va=reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(True)
        r=mw.findChild(QtGui.QTextEdit,"Report view")
        r.clear()
        layout.addWidget(reportview,3,0)

    def trainingreminder(self):
        dia=QtGui.QMessageBox()
        dia.setText('Training description')
        dia.setInformativeText('Task: Learn to use 3 distinct methods to sketch the 3D model shown on the right.'
                               '\n\nTime limit: 20 minutes\n')
        dia.exec_()

    def post_test1(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QVBoxLayout(wii)
        widget.setObjectName("Posttest1")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        '''
        f=open("./Mod/ITS_test00/posttest01.txt","rb")
        text01=f.read()
        lab1=qtg.QLabel(text01)
        lab1.setWordWrap(True)
        lab1.setFixedWidth(380)
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        '''
        reminderbutton=QtGui.QPushButton('Task Reminder')
        reminderbutton.clicked.connect(self.posttestreminder)
        reminderbutton.setFixedWidth(100)
        mousemodelreminderbutton=QtGui.QPushButton('Rotation view')
        mousemodelreminderbutton.clicked.connect(mouseview)
        mousemodelreminderbutton.setFixedWidth(100)
        toplayout=qtg.QHBoxLayout()
        toplayout.addWidget(reminderbutton)
        toplayout.addWidget(mousemodelreminderbutton)
        layout.addLayout(toplayout)
        lab2=qtg.QLabel()
        movie=QtGui.QMovie("./Mod/ITS_test00/model1.gif")
        pix01=qtg.QPixmap("./Mod/ITS_test00/pretest01.png")
        #lab2.setPixmap(pix01)
        lab2.setMovie(movie)
        movie.start()
        #layout.addWidget(reminderbutton,0,0)
        layout.addWidget(lab2)
        lab3=qtg.QLabel()
        lab3.setPixmap(pix01)
        layout.addWidget(lab3)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        booleanoperation=BooleanOperation()
        empty=qtg.QHBoxLayout()
        emptylabel=qtg.QLabel(' Operation can be used:           ')
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        emptylabel.setFont(font1)
        empty.addWidget(emptylabel)
        emptyright=qtg.QHBoxLayout()
        emptyrightlable=qtg.QLabel('   ')
        emptyright.addWidget(emptyrightlable)
        tlayout=qtg.QHBoxLayout()
        tlayout.addLayout(empty)
        tlayout.addLayout(booleanoperation)
        tlayout.addLayout(emptyright)
        layout.addLayout(tlayout)
        lab4=qtg.QLabel()
        pix02=qtg.QPixmap("./Mod/ITS_test00/pretest02.png")
        lab4.setPixmap(pix02)
        layout.addWidget(lab4)
        layout.addWidget(timewidget)
        '''
        mw=FreeCADGui.getMainWindow()
        gwidget=begin.GetWidget()
        reportview=gwidget.getReportview(mw)
        reportview.setFixedSize(400,300)
        reportview.setFeatures(widget.NoDockWidgetFeatures)
        va=reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(True)
        layout.addWidget(reportview,3,0)
        '''
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)

    def posttestreminder(self):
        dia=QtGui.QMessageBox()
        dia.setText('Posttest description')
        dia.setInformativeText('Task: Sketch the 3D model shown on right hand side. Use two distinct method to sketch the model. \n\n     Click "Submit_model 1", when you done the first model. Click "Submit_model_2, when you done the second one."\n\nTime limit: 5 minutes for two methods\n')
        dia.exec_()

    def post_test2(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QVBoxLayout(wii)
        widget.setObjectName("Posttest2")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        reminderbutton=QtGui.QPushButton('Task Reminder')
        reminderbutton.clicked.connect(self.posttest2reminder)
        reminderbutton.setFixedWidth(100)
        mousemodelreminderbutton=QtGui.QPushButton('Rotation view')
        mousemodelreminderbutton.clicked.connect(mouseview)
        mousemodelreminderbutton.setFixedWidth(100)
        toplayout=qtg.QHBoxLayout()
        toplayout.addWidget(reminderbutton)
        toplayout.addWidget(mousemodelreminderbutton)
        layout.addLayout(toplayout)
        '''
        f=open("./Mod/ITS_test00/posttest02.txt","rb")
        text01=f.read()
        lab1=qtg.QLabel(text01)
        lab1.setWordWrap(True)
        lab1.setFixedWidth(380)
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        '''
        lab2=qtg.QLabel()
        movie=QtGui.QMovie("./Mod/ITS_test00/model3.gif")
        pix01=qtg.QPixmap("./Mod/ITS_test00/Post_test2.png")
        #lab2.setPixmap(pix01)
        lab2.setMovie(movie)
        movie.start()
        layout.addWidget(lab2)
        lab3=qtg.QLabel()
        lab3.setPixmap(pix01)
        layout.addWidget(lab3)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        booleanoperation=BooleanOperation()
        empty=qtg.QHBoxLayout()
        emptylabel=qtg.QLabel(' Operation can be used:           ')
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        emptylabel.setFont(font1)
        empty.addWidget(emptylabel)
        emptyright=qtg.QHBoxLayout()
        emptyrightlable=qtg.QLabel('   ')
        emptyright.addWidget(emptyrightlable)
        tlayout=qtg.QHBoxLayout()
        tlayout.addLayout(empty)
        tlayout.addLayout(booleanoperation)
        tlayout.addLayout(emptyright)
        layout.addLayout(tlayout)
        lab4=qtg.QLabel()
        pix02=qtg.QPixmap("./Mod/ITS_test00/pretest02.png")
        lab4.setPixmap(pix02)
        layout.addWidget(lab4)
        layout.addWidget(timewidget)
        '''
        mw=FreeCADGui.getMainWindow()
        gwidget=begin.GetWidget()
        reportview=gwidget.getReportview(mw)
        reportview.setFixedSize(400,300)
        reportview.setFeatures(widget.NoDockWidgetFeatures)
        va=reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(True)
        layout.addWidget(reportview,3,0)
        '''
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)

    def posttest2reminder(self):
        dia=QtGui.QMessageBox()
        dia.setText('Post-test 2 description')
        dia.setInformativeText('Task: Sketch the 3D model shown on the right. '
                               'Click Submit_model_3, when you done. \n\nTime limit: 5 minutes\n')
        dia.exec_()

    def extratest(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QVBoxLayout(wii)
        widget.setObjectName("Extra Test")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(400)
        reminderbutton=QtGui.QPushButton('Task Reminder')
        reminderbutton.clicked.connect(self.extrataskreminder)
        reminderbutton.setFixedWidth(100)
        mousemodelreminderbutton=QtGui.QPushButton('Rotation view')
        mousemodelreminderbutton.clicked.connect(mouseview)
        mousemodelreminderbutton.setFixedWidth(100)
        toplayout=qtg.QHBoxLayout()
        toplayout.addWidget(reminderbutton)
        toplayout.addWidget(mousemodelreminderbutton)
        layout.addLayout(toplayout)
        '''
        f=open("./Mod/ITS_test00/posttest02.txt","rb")
        text01=f.read()
        lab1=qtg.QLabel(text01)
        lab1.setWordWrap(True)
        lab1.setFixedWidth(380)
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        '''
        lab2=qtg.QLabel()
        movie=QtGui.QMovie("./Mod/ITS_test00/model2.gif")
        pix01=qtg.QPixmap("./Mod/ITS_test00/Post-test.png")
        #lab2.setPixmap(pix01)
        lab2.setMovie(movie)
        movie.start()
        layout.addWidget(lab2)
        lab3=qtg.QLabel()
        lab3.setPixmap(pix01)
        layout.addWidget(lab3)
        '''
        if len(begin.timesup)>0:
            for i in range(0,len(begin.timesup)):
                begin.timesup.pop()
        '''
        timewidget=DigitClock()
        start_time=time.time()
        self.addstarttime(start_time)
        booleanoperation=ExtraBooleanOperation()
        empty=qtg.QHBoxLayout()
        emptylabel=qtg.QLabel(' Operation can be used:           ')
        font1=qtg.QFont("Times")
        font1.setPixelSize(17)
        emptylabel.setFont(font1)
        empty.addWidget(emptylabel)
        emptyright=qtg.QHBoxLayout()
        emptyrightlable=qtg.QLabel('   ')
        emptyright.addWidget(emptyrightlable)
        tlayout=qtg.QHBoxLayout()
        tlayout.addLayout(empty)
        tlayout.addLayout(booleanoperation)
        tlayout.addLayout(emptyright)
        layout.addLayout(tlayout)
        lab4=qtg.QLabel()
        pix02=qtg.QPixmap("./Mod/ITS_test00/pretest02.png")
        lab4.setPixmap(pix02)
        layout.addWidget(lab4)
        layout.addWidget(timewidget)
        '''
        mw=FreeCADGui.getMainWindow()
        gwidget=begin.GetWidget()
        reportview=gwidget.getReportview(mw)
        reportview.setFixedSize(400,300)
        reportview.setFeatures(widget.NoDockWidgetFeatures)
        va=reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(True)
        layout.addWidget(reportview,3,0)
        '''
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)

    def extrataskreminder(self):
        dia=QtGui.QMessageBox()
        dia.setText('Extra-task description')
        dia.setInformativeText('Task: Sketch the 3D model shown on the right. '
                               'Click Submit_model_4, when you done. \n\nTime limit: 5 minutes\n')
        dia.exec_()

    def post_survey(self,widget):
        qtg=QtGui
        qtc=QtCore
        widget.setObjectName("Post_survey")
        widget.setFeatures(widget.NoDockWidgetFeatures)
        widget.setFixedWidth(1800)
        widget.setAutoFillBackground(True)
        pal=QtGui.QPalette()
        pal.setColor(pal.Background,QtCore.Qt.white)
        widget.setPalette(pal)
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QGridLayout(wii)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)
        font1=qtg.QFont()
        font1.setPixelSize(14)
        font1.setBold(True)
        font2=qtg.QFont()
        font2.setPixelSize(12)
        lab1=qtg.QLabel("FreeCAD Intelligent Tutoring System Survey")
        lab1.setWordWrap(True)
        lab1.setFont(font1)
        lab2=qtg.QLabel("*Note: You may leave any answer blank you do not wish to answer* \n\nPlease answer the following questions to the best of your ability:\nWhen you were done, please click 'Submit' at the end.\n ")
        lab2.setWordWrap(True)
        lab2.setFont(font2)
        layout.addWidget(lab1,0,1)
        layout.addWidget(lab2,1,1)
        lab3=qtg.QLabel("1.What is your gender?\n")
        lab3.setFont(font2)
        layout.addWidget(lab3,2,1)
        radiobutton11=QtGui.QRadioButton("Male")
        radiobutton12=QtGui.QRadioButton("Female")
        buttongroup1=QtGui.QButtonGroup()
        buttongroup1.addButton(radiobutton11,0)
        buttongroup1.addButton(radiobutton12,1)
        layout.addWidget(radiobutton11,3,1)
        layout.addWidget(radiobutton12,4,1)
        lab4=qtg.QLabel("2.What is your age (in years)?\n")
        lab4.setFont(font2)
        layout.addWidget(lab4,5,1)
        fname='./Mod/ITS_test00/post_survey.txt'
        with open(fname) as f:
            content=f.readlines()
        labels=[]
        for i in range(0,len(content)):
            if content[i]:
                templab=qtg.QLabel(content[i])
                templab.setWordWrap(True)
                templab.setFont(font2)
                labels.append(templab)
        for i in range(0,len(labels)):
            layout.addWidget(labels[i],i+6,1)

    def trainingintro(self,widget):
        qtg=QtGui
        qtc=QtCore
        wii=qtg.QWidget()
        scr=qtg.QScrollArea()
        scr.setWidgetResizable(True)
        scr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout=qtg.QGridLayout(wii)
        widget.setObjectName("trainingintro")
        #widget.setFeatures(widget.NoDockWidgetFeatures)
        #widget.setFixedWidth(400)
        lab1=qtg.QLabel("Training Introduction")
        lab1.setWordWrap(True)
        #lab1.setFixedWidth(380)
        font1=qtg.QFont("Times")
        font1.setPixelSize(20)
        lab1.setFont(font1)
        layout.addWidget(lab1,0,0)
        lab2=qtg.QLabel()
        pix01=qtg.QPixmap("./Mod/ITS_test00/Training_intro.png")
        lab2.setPixmap(pix01)
        layout.addWidget(lab2,0,1)
        wii.setLayout(layout)
        widget.setWidget(scr)
        scr.setWidget(wii)




    def signal(self):
        QtGui.QMessageBox.warning(None, "", "Time up!!")

    def creatCountDown(self):
        self.countDown = QtGui.QLCDNumber()
        self.countDown.display('0'+str(self.time)+":00")
