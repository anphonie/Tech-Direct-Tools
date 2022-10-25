import maya.cmds as cmds
from maya.common.ui import LayoutManager
import os.path
import json
global path
global objCategory
global seqCategory

#Location data

filepath = cmds.file(q=True, sn=True)
filename = filepath.split('/')[-1]
filepathname = filepath.split('/')[-2]
upperPath = filepath.split('/')[-3]
sequencePath = filepath.split('/')[-5]
objname = filename.split('_')[0]
folderpath = '/'.join(filepath.split('/')[:-1])+'/'
location = filepath.split('/')[-6]
pubFolderpath = folderpath.split(location)[0]+'publish'+folderpath.split(location)[1]
saveFolderpath = folderpath.split(location)[0]+'wip'+folderpath.split(location)[1]
selected = cmds.ls(sl=True)

version = int(filename.split('v')[1].split('.')[0])

def SavePublishTool():
    if cmds.window('SavePublishTool', exists = True):
        cmds.deleteUI('SavePublishTool')
        
    cmds.window('SavePublishTool', widthHeight = (300, 225), sizeable = False, resizeToFitChildren=True)
    with LayoutManager(cmds.columnLayout(adj=True, rowSpacing=10)) as col:

        cmds.columnLayout(adjustableColumn = True)
    
        cmds.separator(h=35)
        cmds.text(label = "Save and Publish Tool", align = "center", font = "boldLabelFont")
        cmds.separator(h=35)
    
      
        cmds.text(label = "File Name", align = "center")
        cmds.text(filename, align = "center", font = "smallObliqueLabelFont")
        cmds.button(label = "Save", align = "center", command=checkFileAndSave)
        cmds.separator(h=15)
    
        cmds.text(label = "Selected items", align = "center")
        cmds.text(selected, align = "center", font = "smallObliqueLabelFont")
        cmds.button(label = "Publish", align = "center", command=publish)
        cmds.separator(h=15)
    
        cmds.showWindow('SavePublishTool')


def SaveFile(*args):
    result = cmds.promptDialog(title = 'Save As new version', message='Please enter the version number you would like to save as', button= ['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    
    if result == 'OK':
        fileName = cmds.promptDialog(query=True, text=True)
	    
        cmds.file( rename = fileName)
        cmds.file( save=True , type = 'mayaAscii')
        cmds.confirmDialog(m='New version saved to Project Folder')
    
def checkFileAndSave(list):
#Assets
    #WIP surfacing
    if  "surfacing" in filepathname:
            s = "surface"
            naming = objname + "_" + s + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
    #WIP models
    if  "model" in filepathname:
            m = "model"
            naming = objname + "_" + m + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
    #WIP anim
    if "spiderBot" in upperPath:
            a = "anim"
            naming = objname + "_" + a + "_" + a + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
    #WIP rig
    if "rig" in filepathname:
        if "rigImportScene" in filename:
            naming = objname + "_" + "rigImportScene" + "_v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
            if "_" and "_" and "rig" in filename:
                naming = objname + "_" + filepathname + "_v" + version1(filename, "mayaBinary")
                cmds.file(rename = saveFolderpath + naming)
                cmds.file(s=True,f=True)
                print("File saved! Version"+str(version+1))
        else:
            naming = objname + "_" + filepathname + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
    # WIP sequence Animation
    if "sequence" in sequencePath and "animation" in filepathname:
            naming = upperPath + "_anim.v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))
    #WIP sequence Layout 
    if "sequence" in sequencePath and "layout" in filepathname:
            naming = upperPath + "_" + filepathname + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+str(version+1))

    if "sequence" in sequencePath and "light" in filepathname:
            naming = upperPath + "_" + filepathname + ".v" + version1(filename, "mayaBinary")
            cmds.file(rename = saveFolderpath + naming)
            cmds.file(s=True,f=True)
            print("File saved! Version"+ version1(filename, "mayaBinary"))

            
    
    
def sameJson(oldfile, new):
    old = json.load(open(oldfile))
    if old == new:
        return True
    else:
        return False

def publish(list):
    print(version1(filename, "mayaBinary"))
    
def version1(obj, type):
    if obj == "": return "001"
    else:
        if (type == 'mayaBinary'): vers = int(filename.split('v')[1].split('.')[0])
        else: vers = int(obj.split('.')[1].split('v')[1])+1
    if vers < 10: return "00" + str(vers+1)
    elif vers < 100: return "0" + str(vers+1)
    return str(vers)


SavePublishTool()
