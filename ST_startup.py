import sys
import maya.OpenMayaMPx as ommpx
import maya.cmds as cmds

kPluginCmdName='connectST'

class STstartup(ommpx.MPxCommand):
    def __init__(self):
        ommpx.MPxCommand.__init__(self)
    def doIt(self, args):
        try:
            cmds.commandPort(name=":7001", close=True)
        except:
            cmds.warning('Could not close port 7001 (maybe it is not opened yet...)')
        try:
            cmds.commandPort(name=":7002", close=True)
        except:
            cmds.warning('Could not close port 7002 (maybe it is not opened yet...)')
        cmds.commandPort(name=":7001", sourceType="mel")
        cmds.commandPort(name=":7002", sourceType="python")

def creator():
    return ommpx.asMPxPtr(STstartup())
    
def initializePlugin(mObject):
    mPlugin=ommpx.MFnPlugin(mObject,'Calven Gu','1.0')
    try:
        mPlugin.registerCommand(kPluginCmdName,creator)
    except:
        sys.stderr.write('Failed load plugin : %s' %kPluginCmdName)
        raise

def uninitializePlugin(mObject):
    mPlugin=ommpx.MFnPlugin(mObject)
    try:
        mPlugin.deregisterCommand(kPluginCmdName)
    except:
        sys.stderr.write('Failed unload plugin : %s' %kPluginCmdName)
        raise