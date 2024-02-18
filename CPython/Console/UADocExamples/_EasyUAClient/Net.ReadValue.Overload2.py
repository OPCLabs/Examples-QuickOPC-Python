# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read a value of a specific attribute of a single node, and display it.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853')

# Instantiate the client object.
client = EasyUAClient()

# Obtain value of a DataType attribute.
try:
    value = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, nodeDescriptor, UAAttributeId.DataType)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('value type: ', type(value), sep='')  # The output will differ from pure .NET languages such as C# or VB.NET.
print('value: ', value, sep='')

print()
print('Finished.')

##endregion Example
