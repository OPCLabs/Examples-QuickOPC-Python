# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for an OPC Data Access item.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.DataAccess.Forms.Browsing import *


itemDialog = DAItemDialog()
itemDialog.ServerDescriptor.ServerClass = "OPCLabs.KitServer.2"

dialogResult = itemDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('NodeElement: ', itemDialog.NodeElement, sep='')

##endregion Example
