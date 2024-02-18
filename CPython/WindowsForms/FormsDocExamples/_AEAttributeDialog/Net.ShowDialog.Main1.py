# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to let the user browse for an OPC Alarms&Events attribute.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.AlarmsAndEvents.Forms.Browsing import *


attributeDialog = AEAttributeDialog()
attributeDialog.ServerDescriptor.ServerClass = "OPCLabs.KitEventServer.2"
attributeDialog.CategoryId = 0x00EC0001

dialogResult = attributeDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('AttributeElement: ', attributeDialog.AttributeElement, sep='')

##endregion Example
