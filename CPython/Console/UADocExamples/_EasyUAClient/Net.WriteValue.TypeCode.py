# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how to write a value into a single node, specifying a type code explicitly.
#
# Reasons for specifying the type explicitly might be:
# - The data type in the server has subtypes, and the client therefore needs to pick the subtype to be written.
# - The data type that the reports is incorrect.
# - Writing with an explicitly specified type is more efficient.
#
# TypeCode is easy to use, but it does not cover all possible types. It is also possible to specify the .NET Type, using
# a different overload of the WriteValue method.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

print('Modifying value of a node...')
try:
    IEasyUAClientExtension.WriteValue(client,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10221'),
        12345,
        TypeCode.Int32)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
