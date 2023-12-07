# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for computers on the network.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.Forms.Browsing.Specialized import *


dialog = ComputerBrowserDialog()
print(dialog.ShowDialog())

# Display results.
print(dialog.SelectedName)

print('Finished.')

##endregion Example
