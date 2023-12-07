# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to subscribe to complex data with OPC UA Complex Data plug-in.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def dataChangeNotification(sender, e):
    # Display value.
    if e.Succeeded:
        print('Value: ', e.AttributeData.Value, sep='')
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
    #
    # For processing the internals of the data, refer to examples for GenericData and DataType classes.


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# [ObjectsFolder]/Data.Dynamic.Scalar.StructureValue
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10867')

# Instantiate the client object and hook events.
client = EasyUAClient()
client.DataChangeNotification += dataChangeNotification

# Subscribe to a node which returns complex data. This is done in the same way as regular subscribes - just
# the data returned is different.
print('Subscribing...')
IEasyUAClientExtension.SubscribeDataChange(client,
    endpointDescriptor,
    nodeDescriptor,
    1000)   # samplingInterval

print('Processing data change events for 30 seconds...')
time.sleep(30)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

# Unhook the event handler.
client.DataChangeNotification -= dataChangeNotification

print('Finished.')

##endregion Example
