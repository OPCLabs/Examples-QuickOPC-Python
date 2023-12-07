# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain all method nodes under a given node of the OPC-UA address space.
# For each node, it displays its browse name and node ID.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain methods under the specified node.
try:
    nodeElementCollection = IEasyUAClientExtension.BrowseMethods(client,
                                                                 endpointDescriptor,
                                                                 UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10755'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElementCollection:
    print(nodeElement.BrowseName, ': ', nodeElement.NodeId, sep='')

##endregion Example
