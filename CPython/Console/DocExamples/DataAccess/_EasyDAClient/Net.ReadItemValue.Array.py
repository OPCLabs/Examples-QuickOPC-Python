# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to read an OPC item that is of array type.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyDAClient()

print('Reading array value...')
try:
    # UInt16 is returned as Int32, because UInt16 is not a CLS-compliant type (and is not supported in VB.NET).
    value = IEasyDAClientExtension.ReadItemValue(client, '', 'OPCLabs.KitServer.2', 'Simulation.ReadValue_ArrayOfUI2')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
if value is not None:
    print(value[0])
    print(value[1])
    print(value[2])

##endregion Example
