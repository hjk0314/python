import MASH.api as mapi
import maya.cmds as cmds


org = 'pCube1'
sel = cmds.ls(sl=True, fl=True)
num = 1

# create MASH Network with curves
def createMNet(src, cuv, ratio):
    cmds.select(src)
    mashNetwork = mapi.Network()
    mashNetwork.createNetwork(name='MASH')
    # mNet = mashNetwork.waiter
    mDis = mashNetwork.distribute
    # mRepro mashNetwork.instancer
    # mReproMesh = cmds.listConnections(mashNetwork.instancer, s=False)[0]
    mCurve = mashNetwork.addNode("MASH_Curve")
    cmds.connectAttr(cuv + '.worldSpace[0]', mCurve.name + '.inCurves[0]', force=1)
    cmds.setAttr(mDis + '.amplitudeX', 0)
    cmds.setAttr(mCurve.name + '.timeStep', 1)
    cmds.setAttr(mCurve.name + '.timeSlide', 0)
    cmds.setAttr(mCurve.name + '.equalSpacing', 1)
    cmds.setAttr(mCurve.name + '.stopAtEnd', 1)
    cmds.setAttr(mDis + '.pointCount', int(cmds.arclen(cuv)*ratio))


if sel == []:
    cmds.error('Please, Select Curves')
else:
    for i in sel:
        createMNet(org, i, num)

