# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain all branches at the root of the address space. For each branch, it displays whether 
# it may have child nodes.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.AddressSpace import *
from OpcLabs.EasyOpc.OperationModel import *

# Instantiate the client object.
client = EasyDAClient()

try:
    branchElements = IEasyDAClientExtension.BrowseBranches(client, ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

for branchElement in branchElements:
    print('BranchElements("', branchElement.Name, '").HasChildren: ', branchElement.HasChildren, sep='')

# Example output:
#
#BranchElements("Static").HasChildren: True
#BranchElements("Dynamic").HasChildren: True

##endregion Example
