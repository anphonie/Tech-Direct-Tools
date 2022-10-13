from operator import truediv
import maya.cmds as cmds
import os
global path
global objCategory
global seqCategory

path = "C:/Users/Anthony/Documents/Assessment2_GroupX/scenes/wip"

def SavePublishTool():
    if cmds.window('SavePublishTool', exists = True):
        cmds.deleteUI('SavePublishTool')
        
    cmds.window('SavePublishTool', resizeToFitChildren=True)
    
 #   cmds.window('SavePublishTool', widthHeight=(200, 450))

    cmds.columnLayout(adjustableColumn = True)
    
    cmds.separator(h=10)
    cmds.text(label = "Selected Object's Name", align = "center")
    cmds.text(label = "-Assetname-", align = "center", font = "boldLabelFont")
    cmds.separator(h=10)
    
    cmds.text(label = "Asset department selection")
    
    cmds.button(label = "SetPiece", align = "center")
    cmds.button(label = "Set", align = "center")
    cmds.button(label = "Props", align = "center")
    cmds.button(label = "Character", align = "center")
    cmds.separator(h=10)
    
    cmds.text(label = "Current Department Selected", align = "center")
    cmds.text(label = "-SetPiece-", align = "center", font = "boldLabelFont")
    cmds.separator(h=10)

    cmds.separator(h=10)
    cmds.button(label = "Save scene", align = "center", command=SaveFile)
    cmds.button(label = "Publish", align = "center")
    cmds.separator(h=10)
    
    cmds.showWindow('SavePublishTool')

def saveAssetButton():
	obj = cmds.ls(selection = True)[0] #get selected object

	if (objCategory == "setPiece"):
		filePath = filePath + "C:/Users/Anthony/Documents/Assessment2_GroupX/scenes/wip/assets/setPiece" + obj
		#export surface + model
		surVer = len(os.listdir(filePath + "/surfacing/")) + 1

		#check number of files in directory to determine version number
		modelVer = len(os.listdir(filePath + "/model/")) + 1
		objList = cmds.listRelatives(obj)
		for i in objList:
			if (cmds.objectType(i, isType='surface')): #check child is surface
				cmds.file(filePath + obj + "_surface.v" + surVer + ".mb", type="mayaBinary", exportAsReference=True)
			if (cmds.objectType(i, isType='model')): #check child is model
				cmds.file(filePath + obj + "_model.v" + modelVer + ".mb", type="mayaBinary", exportAsReference=True)


def saveSeqButton():
	filePath = cmds.textField("fileDirectory", q=True, v=True)
	seqNum = cmds.textField("seqTF", q=True, v=True)
	shotNum = cmds.textField("shotNum", q=True, v=True)
	filePath = filePath + "/wip/seqeunce" + seqNum + "/" + shotNum
	if (seqCategory == "Animation"):
		animVer = len(os.listdir(filePath + '/animation/'))  + 1 #check how many files in folder to determine vers num
		file.save(filePath + '/animation.v' + animVer + '.mb', type="mayaBinary", save=True)
	if (seqCategory == "Lighting"):
		lightVer = len(os.listdir(filePath + '/light/'))  + 1 #check how many files in folder to determine vers num
		file.save(filePath + '/light.v' + lightVer + '.mb', type="mayaBinary", save=True)
	if (seqCategory == "Layout"):
		layoutVer = len(os.listdir(filePath + '/layout/'))  + 1 #check how many files in folder to determine vers num
		file.save(filePath + '/layout.v' + lightVer + '.mb', type="mayaBinary", save=True)


def SaveFile(*args):
    result = cmds.promptDialog(title = 'Save As new version', message='Please enter the version number you would like to save as', button= ['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    
    if result == 'OK':
        fileName = cmds.promptDialog(query=True, text=True)
	    
        cmds.file( rename = fileName)
        cmds.file( save=True , type = 'mayaAscii')
        cmds.confirmDialog(m='New version saved to Project Folder')
    
SavePublishTool()