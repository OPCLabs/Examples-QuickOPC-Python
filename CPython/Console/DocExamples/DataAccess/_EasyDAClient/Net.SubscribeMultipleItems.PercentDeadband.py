# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how subscribe to changes of multiple items with percent deadband.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed event handler.
def itemChanged(sender, e):
    if e.Succeeded:
        print(e.Arguments.ItemDescriptor.ItemId, ': ', e.Vtq, sep='')
    else:
        print(e.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Subscribing item changes with different percent deadbands...')
IEasyDAClientExtension.SubscribeMultipleItems(client, [
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Ramp 0:100 (10 s)',
                         VarType(VarTypes.Empty), 100, 10.0, None),
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Ramp 0:100 (1 min)',
                         VarType(VarTypes.Empty), 100, 5.0, None),
    ])

print('Processing item change notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
