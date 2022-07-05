import maya.cmds as cmds

# This Class copies objects and materials, the scene can be heavy.
class AFTERIMAGE():
    def __init__(self):
        self.setupUI()

    # popUp windows
    def setupUI(self):
        if cmds.window('aftImg', exists=True):
            cmds.deleteUI('aftImg')
        else:
            win = cmds.window('aftImg', t='Afterimage Tools', s=True, rtf=True)
            cmds.columnLayout(cat=('both',2), rs=5, cw=250)
            tsMin = cmds.playbackOptions(q=True, min=True)
            tsMax = cmds.playbackOptions(q=True, max=True)
            cmds.separator(h=10)
            self.startFrame = cmds.intFieldGrp(l="Start : ", v1=tsMin)
            self.endFrame = cmds.intFieldGrp(l="End : ", v1=tsMax)
            self.interVal = cmds.intFieldGrp(l="interVal : ", v1=5)
            self.chkBox = cmds.checkBoxGrp(l="with Transparency : ", v1=False)
            cmds.separator(h=10)
            cmds.button(l='Make afterimage', c=self.afterImage)
            cmds.separator(h=10)
            cmds.showWindow(win)
    
    # Copy the object every frame and put a key in the visibility channel
    def afterImage(self, *args):
        # check the shape nodes
        isShape = [i for i in cmds.ls(sl=True, typ='transform') or [] if cmds.listRelatives(i, s=True)]
        if not isShape:
            cmds.error('Select non-group objects')
        else:
            staFra = cmds.intFieldGrp(self.startFrame, q=True, v1=True)
            endFra = cmds.intFieldGrp(self.endFrame, q=True, v1=True)
            interV = cmds.intFieldGrp(self.interVal, q=True, v1=True)
            chk = cmds.checkBoxGrp(self.chkBox, q=True, v1=True)
            for i in range(staFra, endFra):
                cmds.currentTime(i)
                for j in isShape:
                    dupObj = cmds.duplicate(j, n=j+'_%04d' % i, rr=True)
                    cmds.setKeyframe(dupObj, at='visibility', v=0, t=[1])
                    cmds.setKeyframe(dupObj, at='visibility', v=1, t=[i+1])
                    cmds.setKeyframe(dupObj, at='visibility', v=0, t=[i+interV])
                    # checkBox is True
                    if chk:
                        shapeNode = cmds.ls(j, dag=True, s=True)
                        shadeEng = cmds.listConnections(shapeNode, type='shadingEngine')
                        materials = cmds.ls(cmds.listConnections(shadeEng), mat=True)
                        # Since lambert1 cannot be cloned, I create a lambert node.
                        if shadeEng[0][0] == 'i':
                            dupMat = cmds.shadingNode('lambert', asShader=True)
                        # If it is not a Lambert node, it is cloned.
                        else:
                            dupMat = cmds.duplicate(materials, un=True)[0]
                        # Assign to Objects
                        cmds.sets(r=True, nss=True, em=True, n= dupMat + 'SG')
                        cmds.connectAttr(dupMat + '.outColor', dupMat + 'SG.surfaceShader', f=True)
                        cmds.select(dupObj)
                        cmds.hyperShade(a=dupMat)
                        # Every shader has a different connection name.
                        if shadeEng[0][0] == 'a': mtl = 'aiStandardSurface'
                        elif shadeEng[0][0] == 'V': mtl = 'VRayMtl'
                        else: mtl = 'lambert' 
                        dic = {"lambert":".transparency", "aiStandardSurface":".transmission", "VRayMtl":".om"}
                        cmds.setKeyframe(dupMat + dic[mtl], v = 1 if mtl == 'VRayMtl' else 0, t=[i+1])
                        cmds.setKeyframe(dupMat + dic[mtl], v = 0 if mtl == 'VRayMtl' else 1, t=[i+interV])
                    else:
                        pass

AFTERIMAGE()
