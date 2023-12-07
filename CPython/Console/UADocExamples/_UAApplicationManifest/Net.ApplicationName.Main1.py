# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example demonstrates how to set the application name for the client certificate.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Event handler for the LogEntry event.
# Print the loggable entry containing client certificate parameters.
def onLogEntry(sender, logEntryEventArgs):
    if logEntryEventArgs.EventId == 161:
        print(logEntryEventArgs)


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Hook static events.
EasyUAClient.LogEntry += onLogEntry

try:
    # Set the application name, which determines the subject of the client certificate.
    # Note that this only works once in each host process.
    EasyUAApplication.Instance.ApplicationParameters.ApplicationManifest.ApplicationName = \
        'QuickOPC - Python (.NET) example application'

    # Do something - invoke an OPC read, to trigger some loggable entries.
    client = EasyUAClient()
    try:
        value = IEasyUAClientExtension.ReadValue(client,
                                                 endpointDescriptor,
                                                 UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)

    # The certificate will be located or created in a directory similar to:
    # C:\ProgramData\OPC Foundation\CertificateStores\MachineDefault\certs
    # and its subject will be as given by the application name.

    print('Processing log entry events for 10 seconds...')
    time.sleep(10)

    print('Finished.')

finally:
    # Unhook static events.
    EasyUAClient.LogEntry -= onLogEntry

##endregion Example
