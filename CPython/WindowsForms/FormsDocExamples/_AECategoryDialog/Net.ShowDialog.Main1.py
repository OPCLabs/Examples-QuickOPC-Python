# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for OPC Alarms&Events categories.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.AlarmsAndEvents.Forms.Browsing import *


categoryDialog = AECategoryDialog()
categoryDialog.ServerDescriptor.ServerClass = "OPCLabs.KitEventServer.2"

dialogResult = categoryDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print()
for categoryElement in categoryDialog.CategoryElements:
    print(categoryElement)

##endregion Example
