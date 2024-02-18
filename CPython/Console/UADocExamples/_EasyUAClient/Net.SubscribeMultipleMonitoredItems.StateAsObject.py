# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to changes of multiple monitored items
# and display each change, identifying the different subscriptions by an
# object.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


class CustomObject(object):
    def __init__(self, name):
        self.name = name


def dataChangeNotification(sender, eventArgs):
    # Obtain the custom object we have passed in.
    stateAsObject = eventArgs.Arguments.State
    # Display value.
    if eventArgs.Succeeded:
        print(stateAsObject.name, ': ', eventArgs.AttributeData.Value, sep='')
    else:
        print(stateAsObject.name, ' *** Failure: ', eventArgs.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object and hook events.
client = EasyUAClient()
client.DataChangeNotification += dataChangeNotification

print('Subscribing...')
monitoredItemArguments1 = EasyUAMonitoredItemArguments(
    None,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845'),
    UAMonitoringParameters(1000))
monitoredItemArguments1.State = CustomObject('First')    # a custom object that corresponds to the subscription
monitoredItemArguments2 = EasyUAMonitoredItemArguments(
    None,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    UAMonitoringParameters(1000))
monitoredItemArguments2.State = CustomObject('Second')    # a custom object that corresponds to the subscription
monitoredItemArguments3 = EasyUAMonitoredItemArguments(
    None,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855'),
    UAMonitoringParameters(1000))
monitoredItemArguments3.State = CustomObject('Third')    # a custom object that corresponds to the subscription

client.SubscribeMultipleMonitoredItems([
    monitoredItemArguments1,
    monitoredItemArguments2,
    monitoredItemArguments3,
    ])

print('Processing data change events for 10 seconds...')
time.sleep(10)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
