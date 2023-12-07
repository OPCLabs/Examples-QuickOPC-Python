# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read 4 items at once synchronously, and display their values, timestamps and qualities.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Specify that only synchronous method is allowed. By default, both synchronous and asynchronous methods are
# allowed, and the component picks a suitable method automatically. Disallowing asynchronous method leaves
# only the synchronous method available for selection.
client.InstanceParameters.Mode.AllowAsynchronousMethod = False

#
vtqResultArray = client.ReadMultipleItems([
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Random')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Ramp (1 min)')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Sine (1 min)')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_I4')),
    ])

for i, vtqResult in enumerate(vtqResultArray):
    assert vtqResult is not None
    if vtqResult.Succeeded:
        print('vtqResultArray[', i, '].Vtq: ', vtqResult.Vtq, sep='')
    else:
        print('vtqResultArray[', i, '] *** Failure: ', vtqResult.ErrorMessageBrief, sep='')

##endregion Example
