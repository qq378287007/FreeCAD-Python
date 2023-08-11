import FreeCAD
doc = FreeCAD.newDocument()
doc.supportedTypes（）


box = doc.addObject（“Part::Box”，“box”）
#box.Height
#box.Height = 5

myvec = FreeCAD.Vector（2,0,0）
#myvec
#myvec.x
#myvec.y
othervec = FreeCAD.Vector（0,3,0）
sumvec = myvec.add（othervec）

box.Placement.Base = sumvec 
'''
box.Placement
box.Placement.Base
otherpla = FreeCAD.Placement（）
box.Placement= otherpla
'''

#Object
vo = box.ViewObject
vo.Transparency = 80
vo.hide（）
vo.show()




doc.recompute（）



import Mesh
mymesh = Mesh.createSphere()
mymesh.mymesh.Facets
mymesh.Points
meshobj = doc.addObject("Mesh::Feature","MyMesh")
meshobj.Mesh= my
meshdoc.recompute()

import Part
myshape = Part.makeSphere(10)
myshape.myshape.Volume
myshape.Area
shapeobj = doc.addObject("Part::Feature","MyShape")
shapeobj.Shape = myshape
doc.recompute()

Part.show（MyShape）


import Draft
Draft.rec = Draft.makeRectangle(5,2)
mvec = FreeCAD.Vector(4,4,0)
Draft.move(rec,mvec)
Draft.move(box,mvec)

from PySide import QtGui 
QtGui.QMessageBox.information(None,"Apollo program","Houston, we have a problem")






