__author__ = 'yangh_000'

import FreeCAD
import FreeCADGui
from PySide import QtGui,QtCore

#import time
#import sys
#from PySide import QtGui, QtCore


class ITSWorkbench(Workbench):
    """Workbench for ITS."""

    MenuText="I.T.S"
    ToolTip="Intelligent tutoring system"

    def Initialize(self):
        #import PartGui
        #import Part
        import begin
        import ITSGui
        import Post_test
        import Post_test_02
        import Operations
        from PySide import QtGui,QtCore
        import myWedget_Ui
        import sys

        #WebGui.openBrowser("file:///D:/Program Files (x86)/FreeCAD 0.15/Mod/ITS_test00/test.htm")
        self.traininglist =["Cy_x","Cy_y","Cy_z","Sphere","Cube"]
        self.posttest =["Cy_1","Cy_2","Sphere_1","Sphere_2","Cube_"]
        self.posttest2=["small_sphere_01","small_sphere_02","small_sphere_03","sphere","cube"]
        self.operation=["Union","Intersect","Subtract","Restart","GoBack"]
        self.start_pre=["Start_Pre_test","Submit_Pre_test"]
        self.start_train=["Start_Training","End_Training"]
        self.start_post=["Start_Post_test","Submit_model_1","Submit_model_2","Submit_model_3","Submit_model_4"]


        def QT_TRANSLATE_NOOP(scope, text): return text

        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","training"),self.traininglist)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","posttest2"),self.posttest2)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","posttest"),self.posttest)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","operation"),self.operation)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","startpretest"),self.start_pre)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","starttrainingt"),self.start_train)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","startposttest"),self.start_post)
        #FreeCAD.Console.PrintMessage(ITSGui.existitem)




    def Activated(self):
        #import WebGui
        #WebGui.openBrowser("file:///D:/Program Files (x86)/FreeCAD 0.15/Mod/ITS_test00/test.htm")
        import FreeCAD
        import FreeCADGui
        import sys
        from PySide import QtGui,QtCore
        import myWedget_Ui
        import os
        mw=FreeCADGui.getMainWindow()
        bars=mw.findChildren(QtGui.QToolBar)
        for i in bars:
            if i.objectName()=='startposttest':
                bar=i
                break
        #QtGui.QMessageBox.information(None,bar.objectName(),bar.objectName())
        Gui.getMainWindow().insertToolBarBreak(bar)
        welcomewidget=QtGui.QDockWidget("Welcome")
        welcomewidget.ui=myWedget_Ui.myWidget_Ui()
        welcomewidget.ui.welcome(welcomewidget)
        mb=QtGui.QMessageBox(QtGui.QMessageBox.NoIcon,"Welcome Intro",None)
        mb.setIconPixmap("./Mod/ITS_test00/welcome_intro001.png")
        mb.exec_()
        mb2=QtGui.QMessageBox(QtGui.QMessageBox.NoIcon,"Welcome Intro",None)
        mb2.setIconPixmap("./Mod/ITS_test00/welcome_intro002.png")
        mb2.exec_()
        QtGui.QMessageBox.information(None,"Start pretest","Please click 'Start_pretest' to start the program.")
        #mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,welcomewidget)
        #post_survey=myWedget_Ui.postsurvey_ui("Post_survey")
        #post_survey.ui=myWedget_Ui.myWidget_Ui()
        #post_survey.ui.post_survey(post_survey)
        #mw.addDockWidget(QtCore.Qt.TopDockWidgetArea,post_survey)
        #QtGui.QMessageBox.warning(None, "", "Substraction needs two shapes.\n" )




        return


def getMainWindow():
    toplevel=QtGui.qApp.topLevelWidgets()
    for i in toplevel:
        if i.metaObject().className()=="Gui::MainWindow":
            return i
    raise Exception("No main window found")

    #def GetClassName(self):
		#return "PartGui::Workbench"

Gui.addWorkbench(ITSWorkbench())



