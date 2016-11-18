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
import begin
import ITSGui

App=FreeCAD
#App.newDocument()
v=FreeCADGui.activeDocument().activeView()
#existitem=["test"]

class small_sphere_01:
    def Activated(self):
        ssph1=Part.makeSphere(1.0)
        pos=App.Vector(0,0,4.5)
        rot=App.Rotation(App.Vector(0,0,1),0)
        newplace=App.Placement(pos,rot)
        ssph1.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","small_sphere_01")
        App.ActiveDocument.small_sphere_01.Shape=ssph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("small_sphere_01")
        ITSGui.log.append('small_sphere_01')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/sphere1.png', 'MenuText': 'small_sphere_01', 'ToolTip': 'Create a small sphere at center'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<4 or len(begin.submit)==5:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="small_sphere_01":
                return False
        return True

class small_sphere_02:
    def Activated(self):
        ssph1=Part.makeSphere(1.0)
        pos=App.Vector(3,3,4.5)
        rot=App.Rotation(App.Vector(0,0,1),0)
        newplace=App.Placement(pos,rot)
        ssph1.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","small_sphere_02")
        App.ActiveDocument.small_sphere_02.Shape=ssph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("small_sphere_02")
        ITSGui.log.append('small_sphere_02')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/sphere2.png', 'MenuText': 'small_sphere_02', 'ToolTip': 'Create a small sphere at side'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<4 or len(begin.submit)==5:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="small_sphere_02":
                return False
        return True

class small_sphere_03:
    def Activated(self):
        ssph1=Part.makeSphere(1.0)
        pos=App.Vector(-3,-3,4.5)
        rot=App.Rotation(App.Vector(0,0,1),0)
        newplace=App.Placement(pos,rot)
        ssph1.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","small_sphere_03")
        App.ActiveDocument.small_sphere_03.Shape=ssph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("small_sphere_03")
        ITSGui.log.append('small_sphere_03')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/sphere3.png', 'MenuText': 'small_sphere_03', 'ToolTip': 'Create a small sphere at side'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<4 or len(begin.submit)==5:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="small_sphere_03":
                return False
        return True

class sphere:
    def Activated(self):
        ssph1=Part.makeSphere(7.5)
        App.ActiveDocument.addObject("Part::Feature","sphere")
        App.ActiveDocument.sphere.Shape=ssph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("sphere")
        ITSGui.log.append('sphere')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/sphere_big.png', 'MenuText': 'sphere', 'ToolTip': 'Create a sphere'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<4 or len(begin.submit)==5:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="sphere":
                return False
        return True

class cube:
    def Activated(self):
        ssph1=Part.makeBox(10,10,10)
        pos=App.Vector(-5,-5,-5)
        rot=App.Rotation(App.Vector(0,0,1),0)
        newplace=App.Placement(pos,rot)
        ssph1.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","cube")
        App.ActiveDocument.cube.Shape=ssph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("cube")
        ITSGui.log.append('cube')

    def GetResources(self):
        return {'Pixmap': './Mod/ITS_test00/cube.png', 'MenuText': 'cube', 'ToolTip': 'Create a cube'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<4 or len(begin.submit)==5:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="cube":
                return False
        return True

FreeCADGui.addCommand('small_sphere_01',small_sphere_01())
FreeCADGui.addCommand('small_sphere_02',small_sphere_02())
FreeCADGui.addCommand('small_sphere_03',small_sphere_03())
FreeCADGui.addCommand('sphere',sphere())
FreeCADGui.addCommand('cube',cube())