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


class Cy_1:
    def Activated(self):
        pos=App.Vector(-5,0,5)
        rot=App.Rotation(App.Vector(0,1,0),90)
        newplace=App.Placement(pos,rot)
        cyx=Part.makeCylinder(2.0,10.0)
        cyx.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","cy_1")
        App.ActiveDocument.cy_1.Shape=cyx
        App.Console.PrintMessage('X axis cylinder initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("cy_1")
        ITSGui.log.append('cy_x')


    def GetResources(self):
        return {'Pixmap':'./Mod/ITS_test00/cy_x.png', 'MenuText': 'Cy_1', 'ToolTip': 'Create X axis cylinder'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<5 or begin.extratest==0 or len(begin.submit)==6:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="cy_1":
                return False
        return True


class Cy_2:
    def Activated(self):
        cy2=Part.makeCylinder(0.5,0.5)
        pos=App.Vector(2.25,0.25,4)
        rot=App.Rotation(App.Vector(1,0,0),90)
        newplace=App.Placement(pos,rot)
        cy2.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","cy_2")
        App.ActiveDocument.cy_2.Shape=cy2
        App.Console.PrintMessage('Y axis cylinder initialized...\n')
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        ITSGui.existitem.append("cy_2")
        ITSGui.log.append('cy_y')

    def GetResources(self):
        return {'Pixmap':'./Mod/ITS_test00/cy_y.png', 'MenuText': 'Cy_2', 'ToolTip': 'Create Y axis cylinder'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<5 or begin.extratest==0 or len(begin.submit)==6:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="cy_2":
                return False
        return True

class Sphere_1:
    def Activated(self):
        sph1=Part.makeSphere(5.0)
        App.ActiveDocument.addObject("Part::Feature","sphere_1")
        App.ActiveDocument.sphere_1.Shape=sph1
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        App.Console.PrintMessage('Small sphere initialized...\n')
        ITSGui.existitem.append("sphere_1")
        ITSGui.log.append('sphere_1')

    def GetResources(self):
        return {'Pixmap':'./Mod/ITS_test00/sphere1.png', 'MenuText': 'Sphere_1', 'ToolTip': 'Create small sphere'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<5 or begin.extratest==0 or len(begin.submit)==6:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="sphere_1":
                return False
        return True

class Sphere_2:
    def Activated(self):
        sph2=Part.makeSphere(5.5)
        pos=App.Vector(2,0,2)
        rot=App.Rotation(App.Vector(0.74,-0.66,0.15),105.772)
        newplace=App.Placement(pos,rot)
        sph2.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","sphere_2")
        App.ActiveDocument.sphere_2.Shape=sph2
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        App.Console.PrintMessage('Bigger sphere initialized...\n')
        ITSGui.existitem.append("sphere_2")
        ITSGui.log.append('sphere_2')


    def GetResources(self):
        return {'Pixmap':'./Mod/ITS_test00/sphere2.png', 'MenuText': 'Sphere_2', 'ToolTip': 'Create bigger sphere'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<5 or begin.extratest==0 or len(begin.submit)==6:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="sphere_2":
                return False
        return True

class Cube_:
    def Activated(self):
        cube=Part.makeBox(1,0.5,4)
        pos=App.Vector(2,-0.25,4)
        rot=App.Rotation(App.Vector(0,0,1),0)
        newplace=App.Placement(pos,rot)
        cube.Placement=newplace
        App.ActiveDocument.addObject("Part::Feature","cube")
        App.ActiveDocument.cube.Shape=cube
        App.ActiveDocument.recompute()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        App.Console.PrintMessage('A cube initialized...\n')
        ITSGui.existitem.append("cube")
        ITSGui.log.append('cube')


    def GetResources(self):
        return {'Pixmap':'./Mod/ITS_test00/cube.png', 'MenuText': 'Cube', 'ToolTip': 'Create a cube'}

    def IsActive(self):
        if len(begin.begin)<3 or len(begin.submit)<5 or begin.extratest==0 or len(begin.submit)==6:
            return False
        objs=App.ActiveDocument.Objects
        for obj in objs:
            a=obj.Name
            if a=="cube":
                return False
        return True


FreeCADGui.addCommand('Cy_1',Cy_1())
FreeCADGui.addCommand('Cy_2',Cy_2())
FreeCADGui.addCommand('Sphere_1',Sphere_1())
FreeCADGui.addCommand('Sphere_2',Sphere_2())
FreeCADGui.addCommand('Cube_',Cube_())
