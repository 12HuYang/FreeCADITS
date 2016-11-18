__author__ = 'yangh_000'

# import PySide
# from Pyside import QtCore, QtGui
import FreeCAD
import FreeCADGui
import os
import Part
import Drawing
import sys
# from termcolor import colored, cprint
from PySide import QtGui, QtCore
import cPickle
import SearchAgent
import begin
import myWedget_Ui
import time

App = FreeCAD
App.newDocument()
v = FreeCADGui.activeDocument().activeView()
useditems = []
existitem = []
restartcontrol = []
gobackcontrol = []
correctnum = []
completetrain = 0
log = []
Board = []

uniontime=2
commontime=1
cuttime=1

uniontime_2=1
commontime_2=2
cuttime_2=1

class Cy_x:
    def Activated(self):
        cy1 = Part.makeCylinder(2.0, 10.00, App.Base.Vector(-1, 4, 4), App.Base.Vector(1, 0, 0), 360)
        App.ActiveDocument.addObject("Part::Feature", "cy_x")
        App.ActiveDocument.cy_x.Shape = cy1
        # App.Console.PrintMessage('X axis cylinder initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        existitem.append("cy_x")
        log.append('cy_x')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/cy_x.png', 'MenuText': 'Cy_x', 'ToolTip': 'Create X axis Cylinder'}

    def IsActive(self):
        if myWedget_Ui.tutoring[0] != '2':
            if len(begin.begin) < 1 or (len(begin.submit) < 3 and len(begin.begin) - len(begin.submit) != 1) or len(
                    begin.submit) >= 4:
                return False
        if myWedget_Ui.tutoring[0] == '2':
            if len(begin.begin) < 1 or len(begin.submit) >= 4:
                return False
        objs = App.ActiveDocument.Objects
        for obj in objs:
            a = obj.Name
            if a == "cy_x":
                self.action = True
                return False
        self.action = False
        return True


class Cy_y:
    def Activated(self):
        cy2 = Part.makeCylinder(2.0, 10.00, App.Base.Vector(4, 4, -1), App.Base.Vector(0, 0, 1), 360)
        App.ActiveDocument.addObject("Part::Feature", "cy_y")
        App.ActiveDocument.cy_y.Shape = cy2
        # App.Console.PrintMessage('Y axis cylinder initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        existitem.append("cy_y")
        log.append('cy_y')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/cy_y.png', 'MenuText': 'Cy_y', 'ToolTip': 'Create Y axis Cylinder'}

    def IsActive(self):
        if myWedget_Ui.tutoring[0] != '2':
            if len(begin.begin) < 1 or (len(begin.submit) < 3 and len(begin.begin) - len(begin.submit) != 1) or len(
                    begin.submit) >= 4:
                return False
        if myWedget_Ui.tutoring[0] == '2':
            if len(begin.begin) < 1 or len(begin.submit) >= 4:
                return False
        objs = App.ActiveDocument.Objects
        for obj in objs:
            a = obj.Name
            if a == "cy_y":
                self.action = True
                return False
        self.action = False
        return True


class Cy_z:
    def Activated(self):
        cy3 = Part.makeCylinder(2.0, 10.00, App.Base.Vector(4, -1, 4), App.Base.Vector(0, 1, 0), 360)
        App.ActiveDocument.addObject("Part::Feature", "cy_z")
        App.ActiveDocument.cy_z.Shape = cy3
        # App.Console.PrintMessage('Z axis cylinder initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        existitem.append("cy_z")
        log.append('cy_z')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/cy_z.png', 'MenuText': 'Cy_z', 'ToolTip': 'Create Z axis Cylinder'}

    def IsActive(self):
        if myWedget_Ui.tutoring[0] != '2':
            if len(begin.begin) < 1 or (len(begin.submit) < 3 and len(begin.begin) - len(begin.submit) != 1) or len(
                    begin.submit) >= 4:
                return False
        if myWedget_Ui.tutoring[0] == '2':
            if len(begin.begin) < 1 or len(begin.submit) >= 4:
                return False
        objs = App.ActiveDocument.Objects
        for obj in objs:
            a = obj.Name
            if a == "cy_z":
                self.action = True
                return False
        self.action = False
        return True


class Sphere:
    def Activated(self):
        sphere = Part.makeSphere(5, App.Base.Vector(4, 4, 4))
        App.ActiveDocument.addObject("Part::Feature", "sphere")
        App.ActiveDocument.sphere.Shape = sphere
        # App.Console.PrintMessage('sphere initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        existitem.append("sphere")
        log.append('sphere')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/sphere.png', 'MenuText': 'Sphere', 'ToolTip': 'Create Sphere'}

    def IsActive(self):
        if myWedget_Ui.tutoring[0] != '2':
            if len(begin.begin) < 1 or (len(begin.submit) < 3 and len(begin.begin) - len(begin.submit) != 1) or len(
                    begin.submit) >= 4:
                return False
        if myWedget_Ui.tutoring[0] == '2':
            if len(begin.begin) < 1 or len(begin.submit) >= 4:
                return False
        objs = App.ActiveDocument.Objects
        for obj in objs:
            a = obj.Name
            if a == "sphere":
                self.action = True
                return False
        self.action = False
        return True


class Cube:
    def Activated(self):
        cube = Part.makeBox(8, 8, 8)
        App.ActiveDocument.addObject("Part::Feature", "cube")
        App.ActiveDocument.cube.Shape = cube
        # App.Console.PrintMessage('Cube initialized...\n')
        App.ActiveDocument.recompute()
        existitem.append("cube")
        log.append('cube')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/cube.png', 'MenuText': 'Cube', 'ToolTip': 'Create Cube'}

    def IsActive(self):
        if myWedget_Ui.tutoring[0] != '2':
            if len(begin.begin) < 1 or (len(begin.submit) < 3 and len(begin.begin) - len(begin.submit) != 1) or len(
                    begin.submit) >= 4:
                return False
        if myWedget_Ui.tutoring[0] == '2':
            if len(begin.begin) < 1 or len(begin.submit) >= 4:
                return False
        objs = App.ActiveDocument.Objects
        for obj in objs:
            a = obj.Name
            if a == "cube":
                self.action = True
                return False
        self.action = False
        return True


class Union:
    def Activated(self):
        basename = None
        baseobj = None
        toolname = None
        toolobj = None
        objs = App.ActiveDocument.Objects
        objnum = len(existitem)
        '''
        if len(useditems)>0:
            objnum-=len(useditems)
        '''
        Fusionname = "Fusion1"
        if objnum >= 2:
            dialog = Dialog()
            dialog.exec_()
            if dialog.baseitem != None and dialog.baseitemname != None and dialog.toolitemname != None and dialog.toolitem != None:
                baseobj = dialog.baseitem
                basename = baseobj.Name
                toolobj = dialog.toolitem
                toolname = toolobj.Name
                action = 6
                if len(begin.submit) <= 5:
                    for obj in objs:
                        a = obj.Name
                        if a == "Fusion1":
                            Fusionname = "Fusion2"
                            action = 7
                tutor.ActionSearch(basename, toolname, action)
        else:
            word = "Right now number of shapes is less than 2, create 2 shapes first."
            QtGui.QMessageBox.warning(None, "", "Union needs two shapes.\n" + word)

        if basename != None and toolname != None:
            App.activeDocument().addObject("Part::Fuse", Fusionname)
            union = dialog.GetItem(Fusionname)
            union.Base = baseobj
            union.Tool = toolobj
            unionshape = baseobj.Shape.fuse(toolobj.Shape)
            union.Shape = unionshape
            useditems.append(basename)
            useditems.append(toolname)
            # FreeCAD.Console.PrintMessage(existitem)
            existitem.append(Fusionname)
            existitem.remove(basename)
            existitem.remove(toolname)
            log.append(['Union', basename, toolname])
            global uniontime,uniontime_2
            uniontime-=1
            uniontime_2-=1
            # FreeCAD.Console.PrintMessage(existitem)
            if tutor.win == False and len(begin.begin) == 2:
                Action = tutor.Board[len(tutor.Board) - 1]
                tutor.Suggestions(Action)
        tutor.TrainAfter()


    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/Fuse.png', 'MenuText': 'Union', 'ToolTip': 'Create a union'}

    def IsActive(self):
        objs = App.ActiveDocument.Objects
        if len(begin.submit) < 5:
            for obj in objs:
                if obj.Name:
                    a = obj.Name
                    if a == "Fusion2":
                        self.action = True
                        return False
        if len(begin.submit) == 5:
            for obj in objs:
                if obj.Name:
                    a = obj.Name
                    if a == "Fusion1":
                        self.action = True
                        return False
        if len(begin.begin) < 1 or len(begin.submit) >= 6:
            return False
        else:
            return True


class Intersect:
    def Activated(self):
        basename = None
        baseobj = None
        toolname = None
        toolobj = None
        objs = App.ActiveDocument.Objects
        objnum = len(existitem)
        '''
        if len(useditems)>0:
            objnum-=len(useditems)
        '''
        Fusionname = "Common"
        if objnum >= 2:
            dialog = Dialog()
            dialog.exec_()
            if dialog.baseitem != None and dialog.baseitemname != None and dialog.toolitemname != None and dialog.toolitem != None:
                baseobj = dialog.baseitem
                basename = baseobj.Name
                toolobj = dialog.toolitem
                toolname = toolobj.Name
                action = 8
                if len(begin.submit) == 5:
                    action = 7
                    for obj in objs:
                        if obj.Name:
                            a = obj.Name
                            if a == "Common":
                                Fusionname = "Common2"
                                action = 8
                tutor.ActionSearch(basename, toolname, action)

        else:
            word = "Right now number of shapes is less than 2, create 2 shapes first."
            QtGui.QMessageBox.warning(None, "", "Intersect needs two shapes.\n" + word)

        if basename != None and toolname != None:
            App.activeDocument().addObject("Part::Common", Fusionname)
            union = dialog.GetItem(Fusionname)
            union.Base = baseobj
            union.Tool = toolobj
            unionshape = baseobj.Shape.common(toolobj.Shape)
            union.Shape = unionshape
            useditems.append(basename)
            useditems.append(toolname)
            existitem.append(Fusionname)
            existitem.remove(basename)
            existitem.remove(toolname)
            log.append(['Intersect', basename, toolname])
            global commontime,commontime_2
            commontime-=1
            commontime_2-=1
            if tutor.win == False and len(begin.begin) == 2:
                Action = tutor.Board[len(tutor.Board) - 1]
                tutor.Suggestions(Action)
        tutor.TrainAfter()

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/Common.png', 'MenuText': 'Intersect', 'ToolTip': 'Create an intersection'}

    def IsActive(self):
        objs = App.ActiveDocument.Objects
        if len(begin.submit) < 5:
            for obj in objs:
                if obj.Name:
                    a = obj.Name
                    if a == "Common":
                        self.action = True
                        return False
        if len(begin.submit) == 5:
            for obj in objs:
                if obj.Name:
                    a = obj.Name
                    if a == "Common2":
                        self.action = True
                        return False
        if len(begin.begin) < 1 or len(begin.submit) >= 6:
            return False
        else:
            return True


class Substract:
    def Activated(self):
        basename = None
        baseobj = None
        toolname = None
        toolobj = None
        objs = App.ActiveDocument.Objects
        objnum = len(existitem)
        '''
            if len(useditems)>0:
            objnum-=len(useditems)
         '''

        if objnum >= 2:
            dialog = Dialog()
            dialog.exec_()
            if dialog.baseitem != None and dialog.baseitemname != None and dialog.toolitemname != None and dialog.toolitem != None:
                baseobj = dialog.baseitem
                basename = baseobj.Name
                toolobj = dialog.toolitem
                toolname = toolobj.Name
                action = 9
                tutor.ActionSearch(basename, toolname, action)

        else:
            word = "Right now number of shapes is less than 2, create 2 shapes first."
            QtGui.QMessageBox.warning(None, "", "Subtraction needs two shapes.\n" + word)

        Fusionname = "Cut"

        if basename != None and toolname != None:
            App.activeDocument().addObject("Part::Cut", Fusionname)
            union = dialog.GetItem(Fusionname)
            union.Base = baseobj
            union.Tool = toolobj
            unionshape = baseobj.Shape.cut(toolobj.Shape)
            union.Shape = unionshape
            useditems.append(basename)
            useditems.append(toolname)
            existitem.append(Fusionname)
            existitem.remove(basename)
            existitem.remove(toolname)
            log.append(['Subtract', basename, toolname])
            global cuttime,cuttime_2
            cuttime-=1
            cuttime_2-=1
            if tutor.win == False and len(begin.begin) == 2:
                Action = tutor.Board[len(tutor.Board) - 1]
                tutor.Suggestions(Action)
        tutor.TrainAfter()

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/Cut.png', 'MenuText': 'Subtract', 'ToolTip': 'Create a subtraction'}

    def IsActive(self):
        objs = App.ActiveDocument.Objects
        for obj in objs:
            if obj.Name:
                a = obj.Name
                if a == "Cut":
                    self.action = True
                    return False
        if len(begin.begin) < 1 or len(begin.submit) >= 6:
            return False
        else:
            return True


class Restart:
    def Activated(self):
        dia = QtGui.QMessageBox()
        dia.setText('This action will erase everything, do you still want to do that ?')
        dia.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        ret = dia.exec_()
        if ret == QtGui.QMessageBox.No:
            return
        else:
            restartcontrol.append(1)
            log.append('Restart')
            numitem = len(useditems)
            numexist = len(existitem)
            for i in range(0, numitem):
                useditems.pop()
            for i in range(0, numexist):
                existitem.pop()
            corrctNum = len(correctnum)
            for i in range(0, corrctNum):
                correctnum.pop()
            objs = App.ActiveDocument.Objects
            numobjs = len(objs)
            doc = App.ActiveDocument
            docname = doc.Name
            tutor.step = 0
            for j in range(0, numobjs):
                App.getDocument(docname).removeObject(objs[j].Name)
            if len(tutor.Board) > 0:
                # FreeCAD.Console.PrintMessage(tutor.Board)
                tutor.Board = []
                # FreeCAD.Console.PrintMessage(tutor.Board)
            global uniontime,commontime,cuttime,uniontime_2,commontime_2,cuttime_2
            uniontime=2
            commontime=1
            cuttime=1
            uniontime_2=1
            commontime_2=2
            cuttime_2=1

    def activate(self):
        numitem = len(useditems)
        numexist = len(existitem)
        for i in range(0, numitem):
            useditems.pop()
        for i in range(0, numexist):
            existitem.pop()
        corrctNum = len(correctnum)
        for i in range(0, corrctNum):
            correctnum.pop()
        objs = FreeCAD.ActiveDocument.Objects
        numobjs = len(objs)
        doc = FreeCAD.ActiveDocument
        docname = doc.Name
        tutor.step = 0
        for j in range(0, numobjs):
            FreeCAD.getDocument(docname).removeObject(objs[j].Name)
        if len(tutor.Board) > 0:
            # FreeCAD.Console.PrintMessage(tutor.Board)
            tutor.Board = []
            # FreeCAD.Console.PrintMessage(tutor.Board)
        global uniontime,commontime,cuttime,uniontime_2,commontime_2,cuttime_2
        uniontime=2
        commontime=1
        cuttime=1
        uniontime_2=1
        commontime_2=2
        cuttime_2=1

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/restart.png', 'MenuText': 'Restart', 'ToolTip': 'Restart'}

    def IsActive(self):
        if len(begin.begin) < 1 or len(begin.submit) >= 6:
            return False
        else:
            return True


class GoBack:
    def Activated(self):
        objs = App.ActiveDocument.Objects
        numitem = len(objs)
        gobackcontrol.append(1)
        log.append('GoBack')
        # FreeCAD.Console.PrintMessage(objs)
        if numitem > 0:
            # FreeCAD.Console.PrintMessage(existitem)
            lastitem = existitem.pop()
            # FreeCAD.Console.PrintMessage(existitem)
            doc = App.ActiveDocument
            docname = doc.Name
            lastobj = App.ActiveDocument.getObject(lastitem)
            if lastitem == "Fusion1" or lastitem == "Fusion2" or lastitem == "Cut" or lastitem == "Common" or lastitem == "Common2":
                lastobjlist = lastobj.OutList
                FreeCADGui.getDocument(docname).getObject(lastobjlist[0].Name).Visibility = True
                useditems.remove(lastobjlist[0].Name)
                existitem.append(lastobjlist[0].Name)
                FreeCADGui.getDocument(docname).getObject(lastobjlist[1].Name).Visibility = True
                existitem.append(lastobjlist[1].Name)
                useditems.remove(lastobjlist[1].Name)
                tutor.Board.pop()
                tutor.step -= 1
                correctnum.pop()
            if lastitem=="Fusion1" or lastitem=="Fusion2":
                global uniontime,uniontime_2
                uniontime+=1
                uniontime_2+=1
            if lastitem=="Cut":
                global cuttime,cuttime_2
                cuttime+=1
                cuttime_2+=1
            if lastitem=="Common":
                global commontime,commontime_2
                commontime+=1
                commontime_2+=1
            App.getDocument(docname).removeObject(lastitem)



    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/undo.png', 'MenuText': 'GoBack', 'ToolTip': 'Go back to last step'}

    def IsActive(self):
        if len(begin.begin) < 1 or len(begin.submit) >= 6:
            return False
        else:
            return True


class ViewObserver:
    def logPosition(self, info):
        left = (info["Button"] == "BUTTON1")
        pos = info["Position"]
        if left:
            info = v.getObjectInfo(pos)
            if info:
                #sel=FreeCADGui.Selection.getSelection()
                #FreeCAD.Console.PrintMessage(sel)
                FreeCAD.Console.PrintMessage("Object Selected: ")
                FreeCAD.Console.PrintWarning(str(info["Object"]))
                FreeCAD.Console.PrintMessage("\n")
                #if sel:
                FreeCADGui.Selection.clearSelection()
                #
                #FreeCADGui.Selection.clearSelection()
                #sel=FreeCADGui.Selection.getSelection()
                #FreeCAD.Console.PrintMessage(str(sel))



class Tutor:
    def __init__(self):
        self.step = 0
        self.Board = []

    def ActionSearch(self, shape1, shape2, action):
        self.step += 1
        Action = [-1, 0, 0]
        Action[0] = action
        Action[1] = self.FindShapeNum(shape1)
        Action[2] = self.FindShapeNum(shape2)
        # FreeCAD.Console.PrintMessage("step: "+str(self.step)+"\n")
        # FreeCAD.Console.PrintMessage(Action)
        self.Board.append(Action)
        self.win = None
        self.win = self.Possible_correct()
        # FreeCAD.Console.PrintMessage(correctnum)
        # FreeCAD.Console.PrintMessage(self.win)
        # FreeCAD.Console.PrintMessage(str(correctnum))
        if self.win == True and correctnum.count(1) == 4:
            if (len(begin.submit) == 1 and completetrain == 0) or len(begin.submit) == 2:
                for i in range(0, len(Board)):
                    Board.pop()
            Board.append(self.Board)
            QtGui.QMessageBox.information(None, "", "\n" + "Congratulations!! \n You made it!!\n")
        if self.win == True and len(begin.begin) == 2 and begin.scores[0] < 100 and correctnum.count(1) < 4:
            QtGui.QMessageBox.information(None, "", "\n" + "Great! Correct step !! \n")
        if self.win == False and len(begin.begin) == 2:
            if self.step == 1:
                QtGui.QMessageBox.information(None, "",
                                              "\n" + "current step is incorrect, restart and try other operations.\n")
                FreeCAD.Console.PrintError("\n current step is incorrect, restart and try other operations.\n")
            if self.step > 1:
                QtGui.QMessageBox.information(None, "",
                                              "\n" + "current step is incorrect, go back to last step and try other operations.\n")
                FreeCAD.Console.PrintError(
                    "\n current step is incorrect, go back to last step and try other operations.\n")

    def TrainAfter(self):
        if correctnum.count(1) == 4 and len(begin.begin) == 2 and len(begin.submit) < 2:
            global completetrain
            completetrain += 1
            QtGui.QMessageBox.information(None, "", "No." + str(completetrain) + " training finished.\n")
            # FreeCAD.Console.PrintMessage("No."+str(completetrain)+" training finished.\n")
            #time.sleep(1)
            clean = Restart()
            clean.activate()
            '''
            if completetrain==1 and myWedget_Ui.tutoring[0]=='3':
                dia=QtGui.QMessageBox()
                dia.setInformativeText('Please follow the alternative method shown in suggestion window. \n')
                dia.exec_()
                trainingtutor=begin.Start_training()
                trainingtutor.tutorial(1)
                #begin.Start_training.tutorial(1)
            '''
            if completetrain == 3:
                QtGui.QMessageBox.information(None, "",
                                              "Congratulations! You finished the training.\n Please click End_Training and click Start_Posttest.")
                FreeCAD.Console.PrintMessage(
                    "Congratulations! You finished the training.\n Please click End_Training and click Start_Posttest.")
            else:
                if (Board and completetrain < 3 and myWedget_Ui.tutoring[0] == '1') or (
                                Board and completetrain == 2 and myWedget_Ui.tutoring[0] == '3'):
                    # if Board and completetrain<3:
                    QtGui.QMessageBox.information(None, "",
                                                  "Please use different sequence of Boolean operations from your previous ones.\n")
                    FreeCAD.Console.PrintMessage("\nPlease use")
                    FreeCAD.Console.PrintError(" different sequence ")
                    FreeCAD.Console.PrintMessage(" of Boolean operations from your history.\n")
                    for i in range(0, len(Board)):
                        FreeCAD.Console.PrintMessage("\nHistory Method 0" + str(i + 1) + " :\n\n")
                        for j in range(0, len(Board[i])):
                            action = Board[i][j]
                            operation = self.FindActionName(action[0])
                            shape1 = self.FindShapeName(action[1])
                            shape2 = self.FindShapeName(action[2])
                            FreeCAD.Console.PrintMessage(
                                "step " + str(j + 1) + " " + operation + " " + shape1 + " " + shape2 + "\n\n")

    def Possible_correct(self):
        actionnum = len(Tree)
        if len(begin.submit) == 5:
            actionnum = len(Tree_post)
        # QtGui.QMessageBox.warning(None,"",str(actionnum))
        '''
        for i in range(0,actionnum):
            treeaction=Tree[i]
            f.write(str(treeaction)+'\n')
        f.close()
        '''
        correct = [False, False, False, False]
        corrctness = 0
        for i in range(0, actionnum):
            if len(begin.submit) < 5:
                treeaction = Tree[i]
            if len(begin.submit) == 5:
                treeaction = Tree_post[i]
            treeactionlen = len(treeaction)
            # FreeCAD.Console.PrintMessage(treeaction)
            for j in range(0, self.step):
                Action = self.Board[j]
                # FreeCAD.Console.PrintMessage(Action)
                action = treeaction[treeactionlen - j - 1]
                if Action[0] == action[0] and Action[1] == action[1] and Action[2] == action[2]:
                    correct[j] = True
                    # FreeCAD.Console.PrintMessage(j)
        # FreeCAD.Console.PrintMessage(correct)

        if len(begin.begin) == 2 and len(begin.submit) < 2:
            for j in range(0, self.step):
                if Board:
                    for i in range(0, len(Board)):
                        baction = Board[i][j]
                        Action = self.Board[j]
                        if (correct.count(True) < 3 and Action[0] == baction[0] and (
                                        Action[1] == baction[1] or Action[1] == baction[2])
                            and (Action[2] == baction[2] or Action[2] == baction[1])):
                            correct[j] = False
                            action = self.FindActionName(Action[0])
                            shape1 = self.FindShapeName(Action[1])
                            shape2 = self.FindShapeName(Action[2])
                            QtGui.QMessageBox.warning(None, "",
                                                      "\n Current step\n" + "[" + action + " ," + shape1 + ", " + shape2 + "] " + "has been chosen before, "
                                                                                                                                  "please use other option.\n")
                            FreeCAD.Console.PrintMessage(
                                "\n Current step\n" + "[" + action + " ," + shape1 + ", " + shape2 + "] " + "has been chosen before, "
                                                                                                            "please use other option.\n")

        if len(begin.begin) == 3 and len(begin.submit) == 3:
            for j in range(0, self.step):
                if Board:
                    i = len(Board) - 1
                    baction = Board[i][j]
                    Action = self.Board[j]
                    if (correct.count(True) < 3 and Action[0] == baction[0] and (
                                    Action[1] == baction[1] or Action[1] == baction[2])
                        and (Action[2] == baction[2] or Action[2] == baction[1])):
                        correct[j] = False
                        action = self.FindActionName(Action[0])
                        shape1 = self.FindShapeName(Action[1])
                        shape2 = self.FindShapeName(Action[2])
                        QtGui.QMessageBox.warning(None, "",
                                                  "\n Current step\n" + "[" + action + " ," + shape1 + ", " + shape2 + "] " + "has been chosen before, "
                                                                                                                              "please use other option.\n")
                        FreeCAD.Console.PrintMessage(
                            "\n Current step\n" + "[" + action + " ," + shape1 + ", " + shape2 + "] " + "has been chosen before, "
                                                                                                        "please use other option.\n")
                    else:
                        correct[j] = True

        for i in range(0, self.step):
            if correct[i] == True:
                corrctness += 1
        # FreeCAD.Console.PrintMessage(corrctness)
        if corrctness == self.step:
            correctnum.append(1)
            '''
            for i in range(0,len(Board)):
                Board.pop()
            Board.append(self.Board)
            '''
            return True
        else:
            correctnum.append(0)
            '''
            for i in range(0,len(Board)):
                Board.pop()
            Board.append(self.Board)
            '''
            return False

    def Suggestions(self, Action):
        self.win = None
        RelateCorrect = []
        # actionnum=len(Tree.BestActions)
        actionnum = len(Tree)
        availableshape = []
        # FreeCAD.Console.PrintMessage(Tree.BestActions)
        # FreeCAD.Console.PrintMessage(Tree)
        # FreeCAD.Console.PrintMessage(actionnum)
        for item in existitem:
            itemlabel = self.FindShapeNum(item)
            if itemlabel != Action[0]:
                availableshape.append(itemlabel)
        availableshape.append(Action[1])
        availableshape.append(Action[2])
        # FreeCAD.Console.PrintMessage("Available shapes: ")
        # FreeCAD.Console.PrintMessage(availableshape)
        for j in range(0, self.step):
            BAction = self.Board[j]
            if len(RelateCorrect) <= 0:
                for i in range(0, actionnum):
                    treeaction = Tree[i]
                    # treeaction=Tree.BestActions[i]
                    treeactionlen = len(treeaction)
                    action = treeaction[treeactionlen - j - 1]
                    if BAction[0] == action[0] and BAction[1] == action[1] and BAction[2] == action[2]:
                        RelateCorrect.append(treeaction)
                if len(RelateCorrect) <= 0:
                    correctsol = []
                    for k in range(0, len(availableshape)):
                        shape1 = availableshape[k]
                        for l in range(k + 1, len(availableshape)):
                            shape2 = availableshape[l]
                            for i in range(0, actionnum):
                                # treeaction=Tree.BestActions[i]
                                treeaction = Tree[i]
                                treeactionlen = len(treeaction)
                                action = treeaction[treeactionlen - j - 1]
                                if shape1 == action[1] and shape2 == action[2]:
                                    # FreeCAD.Console.PrintMessage("\n"+"Go back and try ")
                                    actionword = []
                                    actionword.append(self.FindActionName(action[0]))
                                    actionword.append(self.FindShapeName(action[1]))
                                    actionword.append(self.FindShapeName(action[2]))
                                    # FreeCAD.Console.PrintMessage(actionword[0]+" to "+actionword[1]+" as base object and "+actionword[2]+" as tool object \n")
                                    correctsol.append(actionword)
                                    break
                                else:
                                    if shape1 == action[2] and shape2 == action[1]:
                                        # FreeCAD.Console.PrintMessage("\n"+"Go back and try ")
                                        actionword = []
                                        actionword.append(self.FindActionName(action[0]))
                                        actionword.append(self.FindShapeName(action[1]))
                                        actionword.append(self.FindShapeName(action[2]))
                                        # FreeCAD.Console.PrintMessage(actionword[0]+" to "+actionword[1]+" as base object and "+actionword[2]+" as tool object \n")
                                        correctsol.append(actionword)
                                        break

                    if len(correctsol) <= 0:
                        # suggestion=color.BOLD+'Go back to last step and create a new shape, since no correct operation for existing shapes.\n'+color.END
                        FreeCAD.Console.PrintMessage(
                            "\n" + "Suggestions " + "\n" + "Go back to last step and create a new shape, since no correct operation for existing shapes.\n")
                        # FreeCAD.Console.PrintMessage("\n"+"Suggestions "+suggestion)
                    else:
                        FreeCAD.Console.PrintMessage("\n" + "Suggestion:\n")
                        for i in range(0, len(correctsol)):
                            FreeCAD.Console.PrintMessage("Option." + str(i + 1) + ". " + "Go back and try ")
                            FreeCAD.Console.PrintError(correctsol[i][0])
                            FreeCAD.Console.PrintMessage(" to ")
                            FreeCAD.Console.PrintWarning(correctsol[i][1])
                            FreeCAD.Console.PrintMessage(" as base object and ")
                            FreeCAD.Console.PrintWarning(correctsol[i][2])
                            FreeCAD.Console.PrintMessage(" as tool object. \n\n")
                else:
                    RelateCorrect = []

    def FindShapeNum(self, shape):
        if shape == "cy_x" or shape == "cy_1" or shape == "small_sphere_01":
            return 1
        if shape == "cy_y" or shape == "cy_2" or shape == "small_sphere_02":
            return 2
        if shape == "cy_z" or shape == "sphere_1" or shape == "small_sphere_03":
            return 3
        if (shape == "cube" and len(begin.submit) < 5) or (shape == "sphere_2" and len(begin.submit) == 5):
            return 4
        if shape == "sphere" or (shape == "cube" and len(begin.submit) == 5):
            return 5
        if shape == "Fusion1":
            return 6
        if (shape == "Fusion2" and len(begin.submit) < 5) or (shape == "Common" and len(begin.submit) == 5):
            return 7
        if (shape == "Common" and len(begin.submit) < 5) or shape == "Common2":
            return 8
        if shape == "Cut":
            return 9

    def FindShapeName(self, num):
        if num == 1:
            if len(begin.submit) < 5:
                if len(begin.submit) < 4:
                    return "cy_x"
                else:
                    return "small_sphere_01"
            else:
                return "cy_1"
        if num == 2:
            if len(begin.submit) < 5:
                if len(begin.submit) < 4:
                    return "cy_y"
                else:
                    return "small_sphere_02"
            else:
                return "cy_2"
        if num == 3:
            if len(begin.submit) < 5:
                if len(begin.submit) < 4:
                    return "cy_z"
                else:
                    return "small_sphere_03"
            else:
                return "sphere_1"
        if num == 4:
            if len(begin.submit) < 5:
                return "cube"
            else:
                return "sphere_2"
        if num == 5:
            if len(begin.submit) < 5:
                return "sphere"
            else:
                return "cube"
        if num == 6:
            return "Fusion1"
        if num == 7:
            if len(begin.submit) < 5:
                return "Fusion2"
            else:
                return "Common"
        if num == 8:
            if len(begin.submit) < 5:
                return "Common"
            else:
                return "Common2"
        if num == 9:
            return "Cut"

    def FindActionName(self, num):
        if num == 6:
            return "Union"
        if num == 7:
            return "Union"
        if num == 8:
            return "Intersect"
        if num == 9:
            return "Subtract"


class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.items = None
        self.baseitem = None
        self.baseitemname = None
        self.toolitem = None
        self.toolitemname = None
        self.ObjItems()
        frameStyle = QtGui.QFrame.Sunken | QtGui.QFrame.Panel
        self.itemLabel_base = QtGui.QLabel()
        self.itemLabel_base.setFrameStyle(frameStyle)
        self.itemButton_base = QtGui.QPushButton("Pick base object")
        self.itemButton_base.clicked.connect(self.setItem_base)

        self.itemLabel_tool = QtGui.QLabel()
        self.itemLabel_tool.setFrameStyle(frameStyle)
        self.itemButton_tool = QtGui.QPushButton("Pick tool object")
        self.itemButton_tool.clicked.connect(self.setItem_tool)

        self.buttonBox = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Apply | QtGui.QDialogButtonBox.Reset | QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.apply)
        self.buttonBox.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.reset)
        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.cancel)

        layout = QtGui.QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.itemButton_base, 0, 0)
        layout.addWidget(self.itemLabel_base, 0, 1)
        layout.addWidget(self.itemButton_tool, 1, 0)
        layout.addWidget(self.itemLabel_tool, 1, 1)
        layout.addWidget(self.buttonBox, 2, 1)

        self.setLayout(layout)
        self.setWindowTitle("Boolean Operation Dialog")

    def apply(self):
        if self.baseitemname == self.toolitemname:
            QtGui.QMessageBox.warning(None, "Same base-object and tool-object",
                                      "base-object and tool-object should be different.")
            self.reset()
        else:
            if self.baseitemname and self.toolitemname:
                self.baseitem = self.GetItem(self.baseitemname)
                self.toolitem = self.GetItem(self.toolitemname)
                self.close()
            else:
                self.close()

    def reset(self):
        self.itemLabel_base.setText("")
        self.baseitemname = None
        self.itemLabel_tool.setText("")
        self.toolitemname = None

    def cancel(self):
        self.baseitemname = None
        self.toolitemname = None
        self.close()

    def ObjItems(self):
        objnum = len(existitem)
        # FreeCAD.Console.PrintMessage(existitem)
        if objnum >= 2:
            self.items = []
            for i in range(0, objnum):
                item = existitem[i]
                self.items.append(item)

    def GetItem(self, itemname):
        objs = App.ActiveDocument.Objects
        for obj in objs:
            if obj.Name == itemname:
                return obj

    def setItem_base(self):
        item, ok = QtGui.QInputDialog.getItem(self, "Pick base object", "Object:", self.items, 0, False)
        if ok and item and item != self.toolitem:
            self.itemLabel_base.setText(item)
            self.baseitemname = item
            # QtGui.QMessageBox.warning(None, "", self.baseitemname)

    def setItem_tool(self):
        item, ok = QtGui.QInputDialog.getItem(self, "Pick tool object", "Object:", self.items, 0, False)
        if ok and item and item != self.baseitem:
            self.itemLabel_tool.setText(item)
            self.toolitemname = item
            # QtGui.QMessageBox.warning(None, "", self.toolitemname)

class EventFilter(QtGui.QMainWindow):
    def eventFilter(self,o,e):
        if e.type()==QtCore.QEvent.ShortcutOverride: #and e.modifiers()==QtCore.Qt.ControlModifier and e.key()==QtCore.Qt.Key_Z:
            if e.key()==QtCore.Qt.Key_Delete:
                FreeCADGui.Selection.clearSelection()
                QtGui.QMessageBox.warning(None,"",'Shortcut delete is not valid. Please ask resercher for help.')
                return True
            else:
                QtGui.QMessageBox.warning(None,"",'Shoutcut is not valid. Please ask resercher for help.')
                return True
        #if e.type()==QtCore.QEvent.MouseButtonPress and e.button()==QtCore.Qt.MouseButton.RightButton:
            #App.Console.PrintMessage('Rightbutton pressed.')
            #QtGui.QMessageBox.warning(None,"",'Rightbutton is not valid here.')
            #App.Console.PrintMessage(str(o.objectName()))
            #e.consume()
            #return True
        else:
            return False


mw = FreeCADGui.getMainWindow()
#views=mw.findChildren(QtGui.QMainWindow)
ef=EventFilter()
mw.installEventFilter(ef)
#o=ViewObserver()
#c=v.addEventCallback("SoMouseButtonEvent",o.logPosition)


f = file('./Mod/ITS_test00/old_model.txt', 'rb')
Tree = cPickle.load(f)
tutor = Tutor()
f = file('./Mod/ITS_test00/DP_posttest.txt', 'rb')
Tree_post = cPickle.load(f)

FreeCADGui.addCommand('Cy_x', Cy_x())
FreeCADGui.addCommand('Cy_y', Cy_y())
FreeCADGui.addCommand('Cy_z', Cy_z())
FreeCADGui.addCommand('Sphere', Sphere())
FreeCADGui.addCommand('Cube', Cube())
FreeCADGui.addCommand('Union', Union())
FreeCADGui.addCommand('Intersect', Intersect())
FreeCADGui.addCommand('Subtract', Substract())
FreeCADGui.addCommand('Restart', Restart())
FreeCADGui.addCommand('GoBack', GoBack())
