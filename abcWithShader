#
#    Alembic Export Tool by hongJinKi - 2021.09.25 v1.0
#    Note : Match the Alembic file to the existing material.
#
#    Export Options checked : -uvWrite -worldSpace -writeColorSets -writeUVSets -dataFormat ogawa
#    program used : "qt Designer" for uiFile
#

import maya.cmds as cmds
import difflib
import os

# Project folder
# projDir = cmds.workspace(q=True, rd=True) + 'cache/alembic/'
projDir = 'C:/Users/hjk03/Documents/maya/projects/default/cache/alembic/'
# time value of the time slider
timeMin = int(cmds.playbackOptions(q=True, min=True))
timeMax = int(cmds.playbackOptions(q=True, max=True))
# get file name
filepath = cmds.file(q=True, sn=True)
filename = os.path.basename(filepath)
raw_name, extension = os.path.splitext(filename)
saveName = projDir + raw_name + '.abc'
# GUI
# with open("C:/Users/hjk03/Documents/Qt Designer/abcExp.ui") as uiFile:
#    uiLines = uiFile.readlines()
#    uiLine = ''
#    for i in uiLines:
#        uiLine += i
uiLine = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>abcExp</class>
 <widget class="QDialog" name="abcExp">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>390</width>
    <height>140</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>290</width>
    <height>0</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>2880</width>
    <height>1200</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="Line" name="line_4">
     <property name="orientation">
      <enum>Qt::Horizontal</enum>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="startText">
       <property name="text">
        <string>start Frame : </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="startField">
       <property name="minimumSize">
        <size>
         <width>50</width>
         <height>0</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>100</width>
         <height>40</height>
        </size>
       </property>
       <property name="text">
        <string>{0}</string>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer_2">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>40</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QLabel" name="endText">
       <property name="text">
        <string>end Frame :</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="endField">
       <property name="minimumSize">
        <size>
         <width>50</width>
         <height>0</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>100</width>
         <height>40</height>
        </size>
       </property>
       <property name="text">
        <string>{1}</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <widget class="QLineEdit" name="pathField">
     <property name="text">
      <string>{2}</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="Line" name="line_3">
     <property name="orientation">
      <enum>Qt::Horizontal</enum>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <widget class="QCheckBox" name="impChkBox">
       <property name="text">
        <string>import</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="assChkBox">
       <property name="enabled">
        <bool>false</bool>
       </property>
       <property name="text">
        <string>assign</string>
       </property>
       <property name="checked">
        <bool>true</bool>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>40</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QPushButton" name="submitButton">
       <property name="minimumSize">
        <size>
         <width>100</width>
         <height>0</height>
        </size>
       </property>
       <property name="text">
        <string>export to abc</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <spacer name="verticalSpacer">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>153</height>
      </size>
     </property>
    </spacer>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>impChkBox</sender>
   <signal>clicked(bool)</signal>
   <receiver>assChkBox</receiver>
   <slot>setChecked(bool)</slot>
   <hints>
    <hint type="sourcelabel">
     <x>39</x>
     <y>90</y>
    </hint>
    <hint type="destinationlabel">
     <x>112</x>
     <y>91</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>impChkBox</sender>
   <signal>clicked(bool)</signal>
   <receiver>assChkBox</receiver>
   <slot>setEnabled(bool)</slot>
   <hints>
    <hint type="sourcelabel">
     <x>39</x>
     <y>91</y>
    </hint>
    <hint type="destinationlabel">
     <x>104</x>
     <y>91</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>""".format(timeMin,timeMax, saveName)


class ABC():
    def __init__(self):
        self.setupUI()

    # pop up windows
    def setupUI(self):
        if cmds.window("abcExp", q=True, ex=True):
            cmds.deleteUI("abcExp")
        else:
            _win = cmds.loadUI(s=uiLine)
            cmds.button("submitButton", e=True, c=self.abcAssign)
            cmds.showWindow(_win)
    
    # Export and import Alembic files.
    def abcExpImp(self, *args):
        sel = cmds.ls(sl=True, long=True, fl=True)
        # field value.
        try:
            self._s = int(cmds.textField("startField", q=True, tx=True))
            self._e = int(cmds.textField("endField", q=True, tx=True))
            self._p = str(cmds.textField("pathField", q=True, tx=True))
        except:
            cmds.error('Check the Fields')
        self._i = cmds.checkBox("impChkBox", q=True, v=True)
        self._a = cmds.checkBox("assChkBox", q=True, v=True)
        # variable again.
        startFrame = self._s
        endFrame = self._e
        importChk = self._i
        desPath = self._p
        objList = ''
        for i in sel:
            objList += '-root ' + i + ' '
        # Options for exporting abc files.
        melExport = "-frameRange " + str(startFrame) + " " + str(endFrame) + " -uvWrite -worldSpace -writeColorSets -writeUVSets -dataFormat ogawa " + objList + "-file " + desPath
        currObj = cmds.ls(assemblies=True)
        cmds.AbcExport(j = melExport)
        if importChk:
            cmds.AbcImport(desPath, m='import')
            # Listing imported files.
            addObj = cmds.ls(assemblies=True)
            newObjSet = set(addObj).difference(currObj)
            newObj = list(newObjSet)
            return newObj
        else:
            return False
    
    # Match the Alembic file to the existing material.
    def abcAssign(self, *args):
        sel = cmds.ls(sl=True, fl=True)
        if sel:
            abc = self.abcExpImp()
            ass = self._a
            # checked import option.
            if abc:
                abcList = []
                for m in sel:
                    # reArrange selected files with similar names.
                    dl = difflib.get_close_matches(m, abc, cutoff=0.8, n=1)
                    for n in dl:
                        abcList.append(n)
                # checked assign option.
                if ass:
                    for j, k in enumerate(sel):
                        shapeNode = cmds.ls(k, dag=True, s=True)
                        shadeEng = cmds.listConnections(shapeNode, type='shadingEngine')
                        materials = cmds.ls(cmds.listConnections(shadeEng), mat=True)
                        try:
                            dupMat = cmds.duplicate(materials, un=True)[0]
                        except:
                            dupMat = cmds.shadingNode('lambert', asShader=True)
                        cmds.select(abcList[j])
                        cmds.hyperShade(a=dupMat)
                else:
                    print('Unchecked assign option.')
                # Naming groups with namespaces
                nSpace = abcList[0].split(':')[0]
                cmds.group(abcList, n=nSpace)
            else:
                print('Export only.')
        else:
            cmds.error('Nothing selected')


ABC()
