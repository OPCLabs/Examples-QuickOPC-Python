# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to unsubscribe from all event notifications.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *


# Notification event handler
def notification(sender, e):
    if not e.Succeeded:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
        return
    else:
        if e.EventData is not None:
            print(e.EventData.Message)


# Instantiate the client object
client = EasyAEClient()

client.Notification += notification

print('Subscribing events...')
IEasyAEClientExtension.SubscribeEvents(client, '', 'OPCLabs.KitEventServer.2', 1000)

print('Waiting for 10 seconds...')
time.sleep(10)

print('Unsubscribing events...')
client.UnsubscribeAllEvents()

print('Waiting for 10 seconds...')
time.sleep(10)

client.Notification -= notification

print('Finished.')

##endregion Example
