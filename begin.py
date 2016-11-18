__author__ = 'yangh_000'

import FreeCAD
import FreeCADGui
import os
import Part
import Drawing
import sys
from PySide import QtGui, QtCore
import cPickle
import SearchAgent
import time
import ITSGui
import myWedget_Ui

begin = []
begin_time = []
submit = []
testtime = []
scores = []
testlogs = []
# timesup=0
extratest = 0

class Start_pretest:
    def Activated(self):
        self.click = True
        begin.append(1)
        begin_time.append(time.time())
        # FreeCAD.Console.PrintMessage(begin)
        # FreeCAD.Console.PrintMessage(begin_time)
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        welcome = widget.getWelcome(mw)
        mw.removeDockWidget(welcome)
        dialog = myWedget_Ui.inputdialog()
        dialog.exec_()
        while len(myWedget_Ui.filename) == 0:
            QtGui.QMessageBox.warning(None, "input wrong",
                                      "Please enter your age, group and major if applicable." + '\n')
            dialog.exec_()
        mb = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, "Pre-test Intro", None)
        mb.setIconPixmap("./Mod/ITS_test00/Pre-test intro.png")
        mb.exec_()
        mb = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, "Mouse model", None)
        mb.setIconPixmap("./Mod/ITS_test00/mouse_model.png")
        mb.exec_()
        dia = QtGui.QMessageBox()
        dia.setText('Pretest description')
        dia.setInformativeText(
            'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
        dia.exec_()
        pretest = QtGui.QDockWidget("Pretest")
        pretest.ui = myWedget_Ui.myWidget_Ui()
        pretest.ui.pretest(pretest)
        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, pretest)

        '''
        digitclock=QtGui.QDockWidget("clock")
        digitclock.ui=clockwidget()
        digitclock.ui.clock(digitclock)
        mw.addDockWidget(QtCore.Qt.DockWidgetArea.NoDockWidgetArea,digitclock)
        '''
        reportview = widget.getReportview(mw)
        va = reportview.toggleViewAction()
        va.setChecked(True)
        reportview.setVisible(False)

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Start_pretest',
                'ToolTip': ''}

    def IsActive(self):
        if len(begin) < 1:
            return True
        else:
            return False


class Start_training:
    def Activated(self):
        mb = QtGui.QMessageBox(QtGui.QMessageBox.NoIcon, "Training Intro", None)
        mb.setIconPixmap("./Mod/ITS_test00/Training_intro.png")
        mb.exec_()
        dia = QtGui.QMessageBox()
        dia.setText('Training description')
        dia.setInformativeText('Task: Learn to use 3 distinct methods to sketch the 3D model shown on the right.'
                               '\n\nTime limit: 20 minutes\n')
        dia.exec_()
        begin.append(2)
        begin_time.append(time.time())
        # FreeCAD.Console.PrintMessage(myWedget_Ui.starttime)
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        pretest = widget.getPretest(mw)
        mw.removeDockWidget(pretest)
        # trainintro=QtGui.QDockWidget("trainingintro")
        # trainintro.ui=myWedget_Ui.myWidget_Ui()
        # trainintro.ui.trainingintro(trainintro)
        # mw.addDockWidget(QtCore.Qt.TopDockWidgetArea,trainintro)
        training = QtGui.QDockWidget("Training")
        training.ui = myWedget_Ui.myWidget_Ui()
        training.ui.training(training)
        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, training)
        # FreeCAD.Console.PrintMessage(ITSGui.Board)
        if ITSGui.Board and ITSGui.Board[0] and myWedget_Ui.tutoring[0] == '1':
            QtGui.QMessageBox.warning(None, "Alternative action",
                                      "Please use method different from your previous one, which will be shown on right side window.")
            FreeCAD.Console.PrintMessage("Please use method")
            FreeCAD.Console.PrintError(" different")
            FreeCAD.Console.PrintMessage(" from your previous one: \n")
            for i in range(0, len(ITSGui.Board[0])):
                action = ITSGui.Board[0][i]
                operation = ITSGui.tutor.FindActionName(action[0])
                baseshape = ITSGui.tutor.FindShapeName(action[1])
                toolshape = ITSGui.tutor.FindShapeName(action[2])
                FreeCAD.Console.PrintMessage(
                    "\nstep " + str(1 + i) + " " + operation + " " + baseshape + " " + toolshape + "\n")
        else:
            if myWedget_Ui.tutoring[0] == '1':
                QtGui.QMessageBox.warning(None, "",
                                          "Please select basic primitives and pick Boolean Operation you think is correct.\n")
                FreeCAD.Console.PrintMessage("\n Please select")
                FreeCAD.Console.PrintError("  basic primitives")
                FreeCAD.Console.PrintMessage(" and pick")
                FreeCAD.Console.PrintError(" Boolean Operation ")
                FreeCAD.Console.PrintMessage("you think is correct.\n")
            else:
                if myWedget_Ui.tutoring[0] == '3':
                    QtGui.QMessageBox.warning(None, "", "Please follow steps shown in suggestion window. \n")
                    '''
                    method1=[[6,1,2],[7,6,3],[9,5,7],[8,9,4]]
                    method2=[[8,4,5],[6,1,2],[7,6,3],[9,8,7]]
                    Steps=[]
                    Steps.append(method1)
                    Steps.append(method2)
                    for j in range(0,len(Steps)):
                        FreeCAD.Console.PrintMessage("Method_"+str(j+1)+" : \n")
                        FreeCAD.Console.PrintMessage("Please follow steps shown below: \n")
                    #steps=[[6,1,2],[7,6,3],[9,5,7],[8,9,4]]
                        stepnum=1
                        steps=Steps[j]
                        for i in range(0,len(steps)):
                            action=steps[i]
                            operation=ITSGui.tutor.FindActionName(action[0])
                            baseshape=ITSGui.tutor.FindShapeName(action[1])
                            toolshape=ITSGui.tutor.FindShapeName(action[2])
                            if action[1]<=5:
                                FreeCAD.Console.PrintMessage("\nstep "+str(stepnum)+" Please add ")
                                FreeCAD.Console.PrintWarning(baseshape+".")
                                stepnum+=1
                            if action[2]<=5:
                                FreeCAD.Console.PrintMessage("\nstep "+str(stepnum)+" Please add ")
                                FreeCAD.Console.PrintWarning(toolshape+".")
                                stepnum+=1
                            FreeCAD.Console.PrintMessage("\nstep "+str(stepnum))
                            FreeCAD.Console.PrintError(" "+operation)
                            FreeCAD.Console.PrintMessage(" to ")
                            FreeCAD.Console.PrintWarning(baseshape)
                            FreeCAD.Console.PrintMessage(" as base object and ")
                            FreeCAD.Console.PrintWarning(toolshape)
                            FreeCAD.Console.PrintMessage(" as tool object. \n")
                            stepnum+=1
                    '''
                    self.Steps=[]
                    if ITSGui.Board:
                        self.findmethod()
                        self.Steps.append(self.tutormethod[0])
                        self.Steps.append(self.tutormethod[1])
                    else:
                        method1 = [[6, 1, 2], [7, 6, 3], [9, 5, 7], [8, 9, 4]]
                        method2 = [[8, 4, 5], [6, 1, 2], [7, 6, 3], [9, 8, 7]]
                        self.Steps.append(method1)
                        self.Steps.append(method2)
                    self.tutorial(0)
                    self.method = 1

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Start_training',
                'ToolTip': ''}

    def IsActive(self):
        if len(begin) == 1 and len(submit) == 1 and (myWedget_Ui.tutoring[0] == '1' or myWedget_Ui.tutoring[0] == '3'):
            return True
        else:
            if ITSGui.completetrain == 1 and myWedget_Ui.tutoring[0] == '3' and self.method == 1:
                QtGui.QMessageBox.warning(None, "",
                                          "Please follow the alternative method shown in suggestion window. \n")
                self.tutorial(1)
                self.method += 1

            if ITSGui.completetrain== 2 and myWedget_Ui.tutoring[0]=='3' and self.method==2:
                dia = QtGui.QMessageBox()
                dia.setText(
                    'Great!\n You finish learning two methods already.\n Now please figure out the third one by yourself.')
                dia.exec_()
                self.method+=1
            return False

    def findmethod(self):
        boardaction = ITSGui.Board[0]
        treelen = len(ITSGui.Tree)
        self.tutormethod = []
        # find=True
        for i in range(0, treelen):
            if len(self.tutormethod) == 2:
                break
            else:
                treeaction = ITSGui.Tree[i]
                treeactionlen = len(treeaction)
                if treeaction[treeactionlen - 1][0] != 7:
                    for j in range(0, treeactionlen):
                        action = boardaction[j]
                        taction = treeaction[treeactionlen - j - 1]
                        if action[0] != taction[0] and action[1] != taction[1] and action[2] != taction[2]:
                            find = True
                        else:
                            find = False
                            break
                    if self.tutormethod:
                        if treeaction[treeactionlen - 1][0] != self.tutormethod[0][0][0] and \
                                        treeaction[treeactionlen - 2][0] != self.tutormethod[0][1][0]:
                            find = True
                        else:
                            find = False
                    if find:
                        methodaction = []
                        for j in range(0, treeactionlen):
                            methodaction.append(treeaction[treeactionlen - j - 1])
                        self.tutormethod.append(methodaction)
    def tutorial(self, methodNum):
        '''
        if ITSGui.Board:
            method1 = self.tutormethod[0]
            method2 = self.tutormethod[1]
        else:
            method1 = [[6, 1, 2], [7, 6, 3], [9, 5, 7], [8, 9, 4]]
            method2 = [[8, 4, 5], [6, 1, 2], [7, 6, 3], [9, 8, 7]]

        Steps = []
        Steps.append(method1)
        Steps.append(method2)
        '''
        j = methodNum
        FreeCAD.Console.PrintMessage("\nMethod_" + str(j + 1) + " : \n")
        FreeCAD.Console.PrintMessage("Please follow steps shown below: \n")
        # steps=[[6,1,2],[7,6,3],[9,5,7],[8,9,4]]
        stepnum = 1
        steps = self.Steps[j]
        # FreeCAD.Console.PrintMessage(steps)
        for i in range(0, len(steps)):
            action = steps[i]
            # FreeCAD.Console.PrintMessage(action)
            operation = ITSGui.tutor.FindActionName(action[0])
            baseshape = ITSGui.tutor.FindShapeName(action[1])
            toolshape = ITSGui.tutor.FindShapeName(action[2])
            if action[1] <= 5:
                FreeCAD.Console.PrintMessage("\nstep " + str(stepnum) + " Please add ")
                FreeCAD.Console.PrintWarning(baseshape + ".")
                stepnum += 1
            if action[2] <= 5:
                FreeCAD.Console.PrintMessage("\nstep " + str(stepnum) + " Please add ")
                FreeCAD.Console.PrintWarning(toolshape + ".")
                stepnum += 1
            FreeCAD.Console.PrintMessage("\nstep " + str(stepnum))
            FreeCAD.Console.PrintError(" " + operation)
            FreeCAD.Console.PrintMessage(" to ")
            FreeCAD.Console.PrintWarning(baseshape)
            FreeCAD.Console.PrintMessage(" as base object and ")
            FreeCAD.Console.PrintWarning(toolshape)
            FreeCAD.Console.PrintMessage(" as tool object.")
            stepnum += 1


class End_training:
    def Activated(self):
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[1] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[1]
        # time.time()-begin_time[1]
        # if len(ITSGui.completetrain)<3 and eclipse_time<300.0:
        if ITSGui.completetrain < 3 and eclipse_time <= 1202.0:
            QtGui.QMessageBox.warning(None, "", "There are " + str(
                3 - ITSGui.completetrain) + " methods you have not learned yet.")
        else:
            submit.append(1)
            fname = myWedget_Ui.filename[0]
            f = open('./Log/' + fname, 'a')
            # f.write('Pret score '+str(score)+'\n')
            f.write('Tran score 0      ')
            f.write('Tran time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
            f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
            f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
            f.write('Board  ' + str(ITSGui.Board) + '   ')
            f.write('Log    ' + str(ITSGui.log) + ' \n')
            f.close()
            for i in range(0, len(ITSGui.restartcontrol)):
                ITSGui.restartcontrol.pop()
            for i in range(0, len(ITSGui.gobackcontrol)):
                ITSGui.gobackcontrol.pop()
            for i in range(0, len(ITSGui.log)):
                ITSGui.log.pop()
            testtime.append(eclipse_time)
            restart = Restart()
            restart.activate()
            mw = FreeCADGui.getMainWindow()
            widget = GetWidget()
            pretest = widget.getTraining(mw)
            mw.removeDockWidget(pretest)
            for i in range(0, len(ITSGui.Board)):
                ITSGui.Board.pop()

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'End_Training',
                'ToolTip': ''}

    def IsActive(self):
        eclipse_time = 0
        if myWedget_Ui.starttime[1] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[1]
        timesup = 0
        # FreeCAD.Console.PrintMessage(str(time.time())+"\n")
        # FreeCAD.Console.PrintMessage(str(eclipse_time)+"\n")
        if eclipse_time <= 1202 and myWedget_Ui.tutoring[0] != '2' and ITSGui.completetrain <= 3 and len(
                submit) == 1 and len(begin) == 2:
            return True
        else:
            if eclipse_time > 1202 and timesup < 1 and len(submit) == 1 and len(begin) == 2 and myWedget_Ui.tutoring[
                0] != '2':
                # if len(submit)<2:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Please start post-test. \n")
                submit.append(1)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                # f.write('Pret score '+str(score)+'\n')
                f.write('Tran score 0      ')
                f.write('Tran time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                restart = Restart()
                restart.activate()
                for i in range(0, len(ITSGui.Board)):
                    ITSGui.Board.pop()
            return False


class Start_posttest:
    def Activated(self):
        if myWedget_Ui.tutoring[0] == '2':
            eclipse_time = 0
            if myWedget_Ui.starttime[1] is not 0:
                eclipse_time = time.time() - myWedget_Ui.starttime[1]
            begin.append(2)
            submit.append(1)
            begin_time.append(0)
            fname = myWedget_Ui.filename[0]
            f = open('./Log/' + fname, 'a')
            # f.write('Pret score '+str(score)+'\n')
            f.write('Tran score 0      ')
            # f.write('Board  '+str(ITSGui.Board)+'   ')
            f.write('Tran time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
            f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
            f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
            f.write('Board  ' + str(ITSGui.Board) + '   ')
            f.write('Log    ' + str(ITSGui.log) + ' \n')
            f.close()
            for i in range(0, len(ITSGui.restartcontrol)):
                ITSGui.restartcontrol.pop()
            for i in range(0, len(ITSGui.gobackcontrol)):
                ITSGui.gobackcontrol.pop()
            for i in range(0, len(ITSGui.log)):
                ITSGui.log.pop()
            restart = Restart()
            restart.activate()
        begin.append(3)
        begin_time.append(time.time())
        # FreeCAD.Console.PrintMessage(begin)
        # FreeCAD.Console.PrintMessage(submit)
        # FreeCAD.Console.PrintMessage(begin_time)
        restart = Restart()
        restart.activate()
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        if myWedget_Ui.tutoring[0] != '2':
            training = widget.getTraining(mw)
            mw.removeDockWidget(training)
        if myWedget_Ui.tutoring[0] == '2':
            training = widget.getTextbooktrain(mw)
            mw.removeDockWidget(training)
        dia = QtGui.QMessageBox()
        dia.setText('Posttest_1 description')
        dia.setInformativeText(
            'Task: Sketch a 3D model with two distinct methods.\n\n After using one method, click "Submit_model 1", after using another method, click "Submit_model_2"\n\nTime limit: 5 minutes for two methods\n')
        dia.exec_()
        posttest1 = QtGui.QDockWidget("Posttest1")
        posttest1.ui = myWedget_Ui.myWidget_Ui()
        posttest1.ui.post_test1(posttest1)
        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest1)

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Start_posttest',
                'ToolTip': ''}

    def IsActive(self):
        eclipse_time = 0
        if myWedget_Ui.starttime[1] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[1]
        timesup = 0
        if (len(begin) == 2 and len(submit) == 2
            and myWedget_Ui.tutoring[0] != '2') or (myWedget_Ui.tutoring[0] == '2' and len(begin) == 1 and len(
            submit) == 1 and eclipse_time <= 1202):
            # FreeCAD.Console.PrintMessage(begin)
            # FreeCAD.Console.PrintMessage(submit)
            # FreeCAD.Console.PrintMessage(timesup)
            return True
        else:
            if myWedget_Ui.tutoring[0] == '2' and len(begin) == 1 and len(
                    submit) == 1 and timesup < 1 and eclipse_time > 1202:
                # timesup.pop()
                timesup += 1
                QtGui.QMessageBox.warning(None, "Time up!", "Times up! start post-test !")
                begin.append(2)
                submit.append(1)
                begin_time.append(0)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Tran score 0      ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Tran time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                restart = Restart()
                restart.activate()
                begin.append(3)
                begin_time.append(time.time())
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                training = widget.getTextbooktrain(mw)
                mw.removeDockWidget(training)
                posttest1 = QtGui.QDockWidget("Posttest1")
                posttest1.ui = myWedget_Ui.myWidget_Ui()
                posttest1.ui.post_test1(posttest1)
                mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest1)
                return False


class Submit_pre:
    def Activated(self):
        submit.append(1)
        eclipse_time = 0
        if myWedget_Ui.starttime[0] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[0]
        testtime.append(eclipse_time)
        QtGui.QMessageBox.warning(None, "", "Submitted.Time used: \n {0:.2f}".format(
            eclipse_time) + " seconds.\n" + "Please start training. \n")
        score = 25 * ITSGui.correctnum.count(1)
        # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
        fname = myWedget_Ui.filename[0]
        f = open('./Log/' + fname, 'a')
        f.write('Pret score ' + str(score) + '      ')
        # f.write('Board  '+str(ITSGui.Board)+'   ')
        f.write('Pret time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
        f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
        f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
        f.write('Board  ' + str(ITSGui.Board) + '   ')
        f.write('Log    ' + str(ITSGui.log) + ' \n')
        f.close()
        for i in range(0, len(ITSGui.restartcontrol)):
            ITSGui.restartcontrol.pop()
        for i in range(0, len(ITSGui.gobackcontrol)):
            ITSGui.gobackcontrol.pop()
        for i in range(0, len(ITSGui.log)):
            ITSGui.log.pop()
        scores.append(score)
        restart = Restart()
        restart.activate()
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        pretest = widget.getPretest(mw)
        mw.removeDockWidget(pretest)
        if myWedget_Ui.tutoring[0] == '2':
            textbooktrain = QtGui.QDockWidget("TextbookTrain")
            textbooktrain.ui = myWedget_Ui.myWidget_Ui()
            textbooktrain.ui.textbooktrain(textbooktrain)
            mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, textbooktrain)

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Submit_Pre_test',
                'ToolTip': ''}

    def IsActive(self):
        eclipse_time = 0
        if myWedget_Ui.starttime[0] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[0]
        timesup = 0
        if begin[0] == 1 and len(submit) == 0 and eclipse_time <= 302:
            # FreeCAD.Console.PrintMessage(str(eclipse_time)+" ")
            # FreeCAD.Console.PrintMessage(submit)
            return True
        else:
            # if eclipse_time>300.0 and eclipse_time<301.5 and len(submit)==0:
            if timesup < 1 and len(submit) == 0 and eclipse_time > 302:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Please start training. \n")
                # FreeCAD.Console.PrintMessage("Time up!"+str(eclipse_time))
                testtime.append(eclipse_time)
                submit.append(1)
                score = 25 * ITSGui.correctnum.count(1)
                # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Pret score ' + str(score) + '      ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Pret time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                scores.append(score)
                restart = Restart()
                restart.activate()
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                pretest = widget.getPretest(mw)
                mw.removeDockWidget(pretest)
                # timesup.pop()
                if myWedget_Ui.tutoring[0] == '2':
                    mw = FreeCADGui.getMainWindow()
                    textbooktrain = QtGui.QDockWidget("TextbookTrain")
                    textbooktrain.ui = myWedget_Ui.myWidget_Ui()
                    textbooktrain.ui.textbooktrain(textbooktrain)
                    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, textbooktrain)

            return False


class Submit_model1:
    def Activated(self):
        submit.append(1)
        begin_time.append(time.time())
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[2] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[2]
        testtime.append(eclipse_time)
        QtGui.QMessageBox.warning(None, "", "Submitted.Time used: \n {0:.2f}".format(
            eclipse_time) + " seconds.\n Please start model 2.\n")
        score = 25 * ITSGui.correctnum.count(1)
        fname = myWedget_Ui.filename[0]
        f = open('./Log/' + fname, 'a')
        f.write('Pos1 score  ' + str(score) + '     ')
        # f.write('Board  '+str(ITSGui.Board)+'   ')
        f.write('Pos1 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
        f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
        f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
        f.write('Board  ' + str(ITSGui.Board) + '   ')
        f.write('Log    ' + str(ITSGui.log) + ' \n')
        f.close()
        for i in range(0, len(ITSGui.restartcontrol)):
            ITSGui.restartcontrol.pop()
        for i in range(0, len(ITSGui.gobackcontrol)):
            ITSGui.gobackcontrol.pop()
        for i in range(0, len(ITSGui.log)):
            ITSGui.log.pop()
        # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
        dia = QtGui.QMessageBox()
        dia.setText('Posttest_2 description')
        dia.setInformativeText('Task: Sketch the 3D model using alternative method.\n\nTime limit: 5 minutes\n')
        dia.exec_()
        FreeCAD.Console.PrintMessage(str(len(begin)) + " " + str(len(submit)))
        scores.append(score)
        restart = Restart()
        restart.activate()

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Submit_model_1',
                'ToolTip': ''}

    def IsActive(self):
        eclipse_time = 0
        if myWedget_Ui.starttime[2] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[2]
        timesup = 0
        if len(begin) == 3 and len(submit) < 3 and eclipse_time <= 302:
            # FreeCAD.Console.PrintMessage(str(eclipse_time)+
            return True
        else:
            if timesup < 1 and len(begin) == 3 and len(submit) == 2 and eclipse_time > 302:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Model 1 and Model 2 tests end. \n")
                FreeCAD.Console.PrintMessage("Time up!" + str(eclipse_time))
                restart = Restart()
                restart.activate()
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                posttest1 = widget.getPosttest1(mw)
                if posttest1:
                    mw.removeDockWidget(posttest1)
                testtime.append(eclipse_time)
                submit.append(1)
                submit.append(1)
                begin_time.append(time.time())
                score = 25 * ITSGui.correctnum.count(1)
                # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
                scores.append(score)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Pos1 score  ' + str(score) + '     ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Pos1 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.write('Pos2 time  0   sec ')
                f.write('Restart    0    times   ')
                f.write('Goback     0  times   ')
                f.write('Board  []  ')
                f.write('Log    []  ')
                f.close()
                # submit.append(1)
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                epost2 = widget.getPosttest2(mw)
                if not epost2:
                    dia = QtGui.QMessageBox()
                    dia.setText('Posttest_3 description')
                    dia.setInformativeText(
                        'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
                    dia.exec_()
                    posttest2 = QtGui.QDockWidget("Posttest2")
                    posttest2.ui = myWedget_Ui.myWidget_Ui()
                    posttest2.ui.post_test2(posttest2)
                    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest2)
                # FreeCAD.Console.PrintMessage(begin)
                # FreeCAD.Console.PrintMessage(submit)
                for i in range(0, len(ITSGui.Board)):
                    ITSGui.Board.pop()
                    # timesup.pop()
            return False


class Submit_model2:
    def Activated(self):
        submit.append(1)
        eclipse_time = 0
        if myWedget_Ui.starttime[2] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[2]
        begin_time.append(time.time())
        testtime.append(eclipse_time)
        QtGui.QMessageBox.warning(None, "", "Submitted.Time used: \n {0:.2f}".format(
            eclipse_time) + " seconds.\n Please start model3. \n")
        score = 25 * ITSGui.correctnum.count(1)
        fname = myWedget_Ui.filename[0]
        f = open('./Log/' + fname, 'a')
        f.write('Pos2 score  ' + str(score) + '     ')
        # f.write('Board  '+str(ITSGui.Board)+'   ')
        f.write('Pos2 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
        f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
        f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
        f.write('Board  ' + str(ITSGui.Board) + '   ')
        f.write('Log    ' + str(ITSGui.log) + ' \n')
        f.close()
        for i in range(0, len(ITSGui.restartcontrol)):
            ITSGui.restartcontrol.pop()
        for i in range(0, len(ITSGui.gobackcontrol)):
            ITSGui.gobackcontrol.pop()
        for i in range(0, len(ITSGui.log)):
            ITSGui.log.pop()
        # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
        scores.append(score)
        restart = Restart()
        restart.activate()
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        posttest1 = widget.getPosttest1(mw)
        mw.removeDockWidget(posttest1)
        epost2 = widget.getPosttest2(mw)
        if not epost2:
            dia = QtGui.QMessageBox()
            dia.setText('Posttest_3 description')
            dia.setInformativeText(
                'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
            dia.exec_()
            posttest2 = QtGui.QDockWidget("Posttest2")
            posttest2.ui = myWedget_Ui.myWidget_Ui()
            posttest2.ui.post_test2(posttest2)
            mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest2)
            # FreeCAD.Console.PrintMessage(begin)
            # FreeCAD.Console.PrintMessage(submit)
        for i in range(0, len(ITSGui.Board)):
            ITSGui.Board.pop()

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Submit_model_2',
                'ToolTip': ''}

    def IsActive(self):
        eclipse_time = 0
        if myWedget_Ui.starttime[2] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[2]
        timesup = 0
        # if len(begin)==3 and len(submit)==3 and (eclipse_time+testtime[len(testtime)-1])<=300.0:
        if len(begin) == 3 and len(submit) == 3 and eclipse_time <= 302:
            # FreeCAD.Console.PrintMessage(str(eclipse_time)+
            return True
        else:
            # if eclipse_time+testtime[len(testtime)-1]>300.0 and eclipse_time+testtime[len(testtime)-1]<301.5 and len(submit)==3:
            if timesup < 1 and len(submit) == 3 and eclipse_time > 302:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Model2 test ends. \n")
                FreeCAD.Console.PrintMessage("Time up! ")
                restart = Restart()
                restart.activate()
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                posttest1 = widget.getPosttest1(mw)
                if posttest1:
                    mw.removeDockWidget(posttest1)
                testtime.append(eclipse_time)
                submit.append(1)
                begin_time.append(time.time())
                score = 25 * ITSGui.correctnum.count(1)
                # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
                scores.append(score)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Pos2 score  ' + str(score) + '     ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Pos2 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                epost2 = widget.getPosttest2(mw)
                if not epost2:
                    dia = QtGui.QMessageBox()
                    dia.setText('Posttest_3 description')
                    dia.setInformativeText(
                        'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
                    dia.exec_()
                    posttest2 = QtGui.QDockWidget("Posttest2")
                    posttest2.ui = myWedget_Ui.myWidget_Ui()
                    posttest2.ui.post_test2(posttest2)
                    mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest2)
                # FreeCAD.Console.PrintMessage(begin)
                # FreeCAD.Console.PrintMessage(submit)
                for i in range(0, len(ITSGui.Board)):
                    ITSGui.Board.pop()
                    # timesup.pop()
            return False


class Submit_model3:
    def Activated(self):
        submit.append(1)
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[3] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[3]
        testtime.append(eclipse_time)
        QtGui.QMessageBox.warning(None, "", "Submited.Totally used: \n {0:.2f}".format(eclipse_time) + " seconds.\n")
        score = 25 * ITSGui.correctnum.count(1)
        fname = myWedget_Ui.filename[0]
        f = open('./Log/' + fname, 'a')
        f.write('Pos3 score  ' + str(score) + '     ')
        # f.write('Board  '+str(ITSGui.Board)+'   ')
        f.write('Pos3 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
        f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
        f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
        f.write('Board  ' + str(ITSGui.Board) + '   ')
        f.write('Log    ' + str(ITSGui.log) + ' \n')
        f.close()
        for i in range(0, len(ITSGui.restartcontrol)):
            ITSGui.restartcontrol.pop()
        for i in range(0, len(ITSGui.gobackcontrol)):
            ITSGui.gobackcontrol.pop()
        for i in range(0, len(ITSGui.log)):
            ITSGui.log.pop()
        # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
        scores.append(score)
        restart = Restart()
        restart.activate()
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        posttest2 = widget.getPosttest2(mw)
        mw.removeDockWidget(posttest2)
        dialog = myWedget_Ui.extratest_dialog()
        dialog.exec_()
        if extratest == 0:
            QtGui.QMessageBox.warning(None, "", "Thank you!\n We appreciate your time and effort.\n")
            post_survey = myWedget_Ui.postsurvey_ui("Post_survey")
            mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, post_survey)
        else:
            epost2 = widget.getExtratest(mw)
            if not epost2:
                dia = QtGui.QMessageBox()
                dia.setText('Extra-test description')
                dia.setInformativeText(
                    'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
                dia.exec_()
                posttest2 = QtGui.QDockWidget("Extra Test")
                posttest2.ui = myWedget_Ui.myWidget_Ui()
                posttest2.ui.extratest(posttest2)
                mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest2)
                # FreeCAD.Console.PrintMessage(begin)
                # FreeCAD.Console.PrintMessage(submit)
            for i in range(0, len(ITSGui.Board)):
                ITSGui.Board.pop()

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Submit_model_3',
                'ToolTip': ''}

    def IsActive(self):
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[3] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[3]
        timesup = 0
        # if len(begin)==3 and len(submit)==4 and eclipse_time<300.0:
        if len(begin) == 3 and len(submit) == 4 and eclipse_time <= 302:
            return True
        else:
            # if eclipse_time>300.0 and eclipse_time<301.5 and len(begin)==3 and len(submit)==4:
            if timesup < 1 and len(begin) == 3 and len(submit) == 4 and eclipse_time > 302:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Post test ends. \n")
                FreeCAD.Console.PrintMessage("Time up!" + str(eclipse_time - 2))
                testtime.append(eclipse_time)
                submit.append(1)
                begin_time.append(time.time())
                score = 25 * ITSGui.correctnum.count(1)
                # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
                scores.append(score)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Pos3 score  ' + str(score) + '     ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Pos3 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                restart = Restart()
                restart.activate()
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                posttest2 = widget.getPosttest2(mw)
                mw.removeDockWidget(posttest2)
                dialog = myWedget_Ui.extratest_dialog()
                dialog.exec_()
                if extratest == 0:
                    QtGui.QMessageBox.warning(None, "", "Thank you!\n We appreciate your time and effort.\n")
                    post_survey = myWedget_Ui.postsurvey_ui("Post_survey")
                    mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, post_survey)
                else:
                    epost2 = widget.getExtratest(mw)
                    if not epost2:
                        dia = QtGui.QMessageBox()
                        dia.setText('Extra-test description')
                        dia.setInformativeText(
                            'Task: Sketch a 3D model, which will be shown after this window closed.\n\nTime limit: 5 minutes\n')
                        dia.exec_()
                        posttest2 = QtGui.QDockWidget("Extra Test")
                        posttest2.ui = myWedget_Ui.myWidget_Ui()
                        posttest2.ui.extratest(posttest2)
                        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, posttest2)
                        # FreeCAD.Console.PrintMessage(begin)
                        # FreeCAD.Console.PrintMessage(submit)
                    for i in range(0, len(ITSGui.Board)):
                        ITSGui.Board.pop()

            return False


class Submit_model4:
    def Activated(self):
        submit.append(1)
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[4] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[4]
        testtime.append(eclipse_time)
        QtGui.QMessageBox.warning(None, "", "Submited.Totally used: \n {0:.2f}".format(eclipse_time) + " seconds.\n")
        score = 25 * ITSGui.correctnum.count(1)
        fname = myWedget_Ui.filename[0]
        f = open('./Log/' + fname, 'a')
        f.write('Pos4 score  ' + str(score) + '     ')
        # f.write('Board  '+str(ITSGui.Board)+'   ')
        f.write('Pos4 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
        f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
        f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
        f.write('Board  ' + str(ITSGui.Board) + '   ')
        f.write('Log    ' + str(ITSGui.log) + ' \n')
        f.close()
        for i in range(0, len(ITSGui.restartcontrol)):
            ITSGui.restartcontrol.pop()
        for i in range(0, len(ITSGui.gobackcontrol)):
            ITSGui.gobackcontrol.pop()
        for i in range(0, len(ITSGui.log)):
            ITSGui.log.pop()
        # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
        scores.append(score)
        restart = Restart()
        restart.activate()
        mw = FreeCADGui.getMainWindow()
        widget = GetWidget()
        posttest2 = widget.getExtratest(mw)
        mw.removeDockWidget(posttest2)
        QtGui.QMessageBox.warning(None, "", "Thank you!\n We appreciate your time and effort.\n")
        post_survey = myWedget_Ui.postsurvey_ui("Post_survey")
        mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, post_survey)

    def GetResources(self):
        return {'Pixmap': '',
                'MenuText': 'Submit_model_4',
                'ToolTip': ''}

    def IsActive(self):
        # eclipse_time=time.time()-myWedget_Ui.starttime[len(myWedget_Ui.starttime)-1]
        eclipse_time = 0
        if myWedget_Ui.starttime[4] is not 0:
            eclipse_time = time.time() - myWedget_Ui.starttime[4]
        timesup = 0
        # if len(begin)==3 and len(submit)==4 and eclipse_time<300.0:
        if len(begin) == 3 and len(submit) == 5 and extratest == 1 and eclipse_time <= 302:
            return True
        else:
            # if eclipse_time>300.0 and eclipse_time<301.5 and len(begin)==3 and len(submit)==4:
            if timesup < 1 and len(begin) == 3 and len(submit) == 5 and extratest == 1 and eclipse_time > 302:
                timesup += 1
                QtGui.QMessageBox.warning(None, "", "Time Up! .\n" + "Post test ends. \n")
                FreeCAD.Console.PrintMessage("Time up!" + str(eclipse_time))
                testtime.append(eclipse_time)
                submit.append(1)
                begin_time.append(time.time())
                score = 25 * ITSGui.correctnum.count(1)
                # QtGui.QMessageBox.warning(None,"","Score is: "+str(score)+" out of 100")
                scores.append(score)
                fname = myWedget_Ui.filename[0]
                f = open('./Log/' + fname, 'a')
                f.write('Pos4 score  ' + str(score) + '     ')
                # f.write('Board  '+str(ITSGui.Board)+'   ')
                f.write('Pos4 time  ' + "{0:.2f}".format(eclipse_time) + '  sec ')
                f.write('Restart    ' + str(len(ITSGui.restartcontrol)) + '    times   ')
                f.write('Goback     ' + str(len(ITSGui.gobackcontrol)) + '  times   ')
                f.write('Board  ' + str(ITSGui.Board) + '   ')
                f.write('Log    ' + str(ITSGui.log) + ' \n')
                f.close()
                for i in range(0, len(ITSGui.restartcontrol)):
                    ITSGui.restartcontrol.pop()
                for i in range(0, len(ITSGui.gobackcontrol)):
                    ITSGui.gobackcontrol.pop()
                for i in range(0, len(ITSGui.log)):
                    ITSGui.log.pop()
                restart = Restart()
                restart.activate()
                mw = FreeCADGui.getMainWindow()
                widget = GetWidget()
                posttest2 = widget.getExtratest(mw)
                mw.removeDockWidget(posttest2)
                QtGui.QMessageBox.warning(None, "", "Thank you!\n We appreciate your time and effort.\n")
                post_survey = myWedget_Ui.postsurvey_ui("Post_survey")
                mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, post_survey)
                # QtGui.QMessageBox.information(None, "", "Thank you!\n We appreciate your time and effort.\n")
                # post_survey=myWedget_Ui.postsurvey_ui("Post_survey")
                # mw.addDockWidget(QtCore.Qt.TopDockWidgetArea,post_survey)
                # timesup.pop()
            return False


class Restart:
    def activate(self):
        act = ITSGui.Restart()
        act.activate()


class clockwidget(object):
    def __init__(self):
        self.time = 5

    def clock(self, widget):
        wii = QtGui.QWidget()
        widget.setObjectName("digitalcolck")
        widget.setFixedWidth(400)
        widget.setFixedHeight(200)
        layout = QtGui.QGridLayout(wii)
        digitalclock = myWedget_Ui.DigitClock()
        layout.addWidget(digitalclock, 0, 0)
        wii.setLayout(layout)
        widget.setWidget(wii)


class GetWidget:
    def getWelcome(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Welcome":
                return i

    def getPretest(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Pretest":
                return i

    def getTraining(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Training":
                return i

    def getTextbooktrain(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Textbooktrain":
                return i

    def getPosttest1(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Posttest1":
                return i

    def getReportview(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        # i=dw[0]
        for i in dw:
            if i.objectName() == 'Report view':
                return i

    def getPosttest2(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Posttest2":
                return i

    def getTrainintro(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "trainingintro":
                return i

    def getExtratest(self, mw):
        dw = mw.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Extra Test":
                return i


FreeCADGui.addCommand('Start_Pre_test', Start_pretest())
FreeCADGui.addCommand('Start_Training', Start_training())
FreeCADGui.addCommand('Start_Post_test', Start_posttest())
FreeCADGui.addCommand('Submit_Pre_test', Submit_pre())
FreeCADGui.addCommand('Submit_model_1', Submit_model1())
FreeCADGui.addCommand('Submit_model_2', Submit_model2())
FreeCADGui.addCommand('Submit_model_3', Submit_model3())
FreeCADGui.addCommand('Submit_model_4', Submit_model4())
FreeCADGui.addCommand('End_Training', End_training())
