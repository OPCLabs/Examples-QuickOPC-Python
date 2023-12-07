# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to event notifications and display each incoming event
# using a callback method that is provided as lambda expression.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Instantiate the client object.
client = EasyUAClient()

print('Subscribing...')
# The callback is a lambda expression the displays the event.
IEasyUAClientExtension.SubscribeEvent(
    client,
    endpointDescriptor,
    UANodeDescriptor(UAObjectIds.Server),
    1000,
    EasyUAEventNotificationEventHandler(lambda server, eventArgs: print(eventArgs)))
# Remark: Production code needs to check eventArgs.Exception before accessing eventArgs.EventData.

print('Processing event notifications for 30 seconds...')
time.sleep(30)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
