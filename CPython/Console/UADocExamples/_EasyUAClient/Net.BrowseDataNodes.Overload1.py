# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain all data nodes (objects and variables) under a given node of the OPC-UA address space. 
# For each node, it displays its browse name and node ID.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain data nodes under "Objects" node.
try:
    nodeElementCollection = IEasyUAClientExtension.BrowseDataNodes(client, endpointDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElementCollection:
    print()
    print('nodeElement.DisplayName: ', nodeElement.DisplayName, sep='')
    print('nodeElement.NodeId: ', nodeElement.NodeId, sep='')
    print('nodeElement.NodeId.ExpandedText: ', nodeElement.NodeId.ExpandedText, sep='')

print()
print('Finished.')

##endregion Example
