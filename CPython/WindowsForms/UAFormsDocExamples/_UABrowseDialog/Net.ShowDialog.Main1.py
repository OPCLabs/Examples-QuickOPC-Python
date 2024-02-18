# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to let the user browse for an OPC-UA node.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


browseDialog = UABrowseDialog()
browseDialog.InputsOutputs.CurrentNodeDescriptor.EndpointDescriptor.Host = 'opcua.demo-this.com'
browseDialog.Mode.AnchorElementType = UAElementType.Host

dialogResult = browseDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print(browseDialog.Outputs.CurrentNodeElement.NodeElement)

print('Finished.')

##endregion Example
