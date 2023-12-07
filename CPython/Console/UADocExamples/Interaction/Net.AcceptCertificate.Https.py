# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how in a console application, the user is asked to accept a server HTTPS certificate.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Do not implicitly trust any endpoint URLs. We want the user be asked explicitly.
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustedEndpointUrlStrings.Clear()

# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('https://opcua.demo-this.com:51212/UA/SampleServer/')

# Instantiate the client object.
client = EasyUAClient()

try:
    # Obtain attribute data.
    # The component automatically triggers the necessary user interaction during the first operation.
    attributeData = IEasyUAClientExtension.Read(client,
                                                endpointDescriptor,
                                                UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('Value: ', attributeData.Value)
print('ServerTimestamp: ', attributeData.ServerTimestamp)
print('SourceTimestamp: ', attributeData.SourceTimestamp)
print('StatusCode: ', attributeData.StatusCode)

print()
print('Finished.')

##endregion Example
