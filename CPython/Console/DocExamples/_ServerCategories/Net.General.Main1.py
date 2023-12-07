# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows all information available about categories that particular OPC servers do support.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


def dumpServerElements(serverElements):
    for serverElement in serverElements:
        print('Categories of ', serverElement.ProgId, ':', sep='')
        serverCategories = serverElement.ServerCategories
        print('    .OpcAlarmsAndEvents10: ', serverCategories.OpcAlarmsAndEvents10, sep='')
        print('    .OpcDataAccess10: ', serverCategories.OpcDataAccess10, sep='')
        print('    .OpcDataAccess20: ', serverCategories.OpcDataAccess20, sep='')
        print('    .OpcDataAccess30: ', serverCategories.OpcDataAccess30, sep='')
        print('    .ToString(): ', serverCategories, sep='')

# Instantiate the OPC-DA client object.
daClient = EasyDAClient()

print()
print('OPC DATA ACCESS')
try:
    daServerElements = IEasyDAClientExtension.BrowseServers(daClient)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()
dumpServerElements(daServerElements)

# Instantiate the OPC-A&E client object.
aeClient = EasyAEClient()

print()
print('OPC ALARMS AND EVENTS')
try:
    aeServerElements = IEasyAEClientExtension.BrowseServers(aeClient)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()
dumpServerElements(aeServerElements)

##endregion Example
