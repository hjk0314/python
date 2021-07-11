import maya.cmds as cmds
import random
import shutil, os

if cmds.window('hjk_win', exists=True):
    cmds.deleteUI('hjk_win')
else:
    win = cmds.window("hjk_win", t="HJK's Python Scripts. ver.0.1", s=True, rtf=True)
    tsMin = cmds.playbackOptions(q=True, min=True)
    tsMax = cmds.playbackOptions(q=True, max=True)
    cmds.columnLayout(cat=('both', 2), rowSpacing=5, columnWidth=250)#390 )
    # Introduce
    cmds.separator(h=10)
    cmds.text("This is a helpful tool for Animation")
    cmds.text("HJK's Python Scripts")
    # ccp()
    cmds.separator(h=10)
    stF = cmds.intFieldGrp(l="Start Frame : ", v1=tsMin)
    enF = cmds.intFieldGrp(l="End Frame : ", v1=tsMax)
    cmds.button(l='Create Curve on Path', c="ccp()")
    # offs()
    cmds.separator(h=10)
    gap = cmds.intFieldGrp(l="Offset : ", v1=2)
    cmds.button(l="Offset the Keys", c="offs()")
    # hmc()
    cmds.separator(h=10)    
    cpn = cmds.intFieldGrp(l="How many Copies : ", v1=1)
    chb = cmds.checkBoxGrp(l="Input Graph : ", v1=False)
    cmds.button(l="Copy", c="hmc()")
    # rora()
    cmds.separator(h=10)
    rot = cmds.intFieldGrp(l="Rotate : ", v1=360)#, v2=360, v3=360, nf=3)
    cmds.button(l="Rotate Random", c="rora()")
    # scra()
    cmds.separator(h=10)
    scl = cmds.intFieldGrp(l="Scale : ", v1=1)#, v2=360, v3=360, nf=3)
    cmds.button(l="Scale Random", c="scra()")
    # ccl()
    cmds.separator(h=10)
    cmds.button(l="Create Curve with Locator", c="ccl()")

    cmds.separator(h=10)
    cmds.showWindow(win)
    
# Create Curve on Path
def ccp():
    s = cmds.intFieldGrp(stF, q=True, v1=True)
    e = cmds.intFieldGrp(enF, q=True, v1=True)
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        for i in sel:
            pList = []
            for j in range(s, e+1):
                cmds.currentTime(j)
                try:
                    pList.append(cmds.pointPosition(i))
                except:
                    pList.append(cmds.xform(i, q=True, ws=True, rp=True))
            cmds.curve(p=pList)
    else:
        cmds.error("Please, Select Objects or Vertices")

# Offset the Keys
def offs():
    g = cmds.intFieldGrp(gap, q=True, v1=True)
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        for i in range (0, len(sel)):
            cmds.keyframe(sel[i], e=True, r=True, tc=i*int(g))
    else:
        cmds.error("Please, Select Objects.")

# How Many Copies
def hmc():
    n = cmds.intFieldGrp(cpn, q=True, v1=True)
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        for i in range(n):
            cmds.duplicate(sel, rr=True, un=cmds.checkBoxGrp(chb, q=True, v1=True))
    else:
        cmds.error("Please, Select Objects.")
        
# Rotate Random
def rora():
    rotX = cmds.intFieldGrp(rot, q=True, v1=True)
#   rotY = cmds.intFieldGrp(rot, q=True, v2=True)
#   rotZ = cmds.intFieldGrp(rot, q=True, v3=True)
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        for i in sel:
            x = random.randrange(rotX)
            y = random.randrange(rotX)
            z = random.randrange(rotX)
            cmds.rotate(x,y,z, i)
    else:
        cmds.error("Please, Select Objects.")

# Scale Random
def scra():
    sclX = cmds.intFieldGrp(scl, q=True, v1=True)
#   sclY = cmds.intFieldGrp(scl, q=True, v2=True)
#   sclZ = cmds.intFieldGrp(scl, q=True, v3=True)
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        for i in sel:
            x = random.randrange(1, sclX+1)
#           y = random.randrange(1, sclY+1)
#           z = random.randrange(1, sclZ+1)
            cmds.scale(x,x,x, i, r=False)
    else:
        cmds.error("Please, Select Objects.")

# Create Curve with Locator
def ccl():
    sel = cmds.ls(sl=True, fl=True)
    if sel:
        pList = []
        for i in sel:
            pList.append(cmds.xform(i, q=True, ws=True, rp=True))
        cuv = cmds.curve(p=pList)
        for j in range(len(sel)):
            cmds.setAttr(cmds.cluster(cuv+".cv["+str(j)+"]")[1]+".visibility", 0)
            cmds.parent(cmds.group(), sel[j])
        cmds.group(sel)
    else:
        cmds.error("Please, Create Locators First. And Copy Them.")

