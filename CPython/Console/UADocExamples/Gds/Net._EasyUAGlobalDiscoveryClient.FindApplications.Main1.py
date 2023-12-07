# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to find all registrations in the GDS.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Discovery import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.Gds import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')
gdsEndpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(gdsEndpointDescriptor,
                                                                           'appadmin', 'demo')

# Instantiate the global discovery client object.
globalDiscoveryClient = EasyUAGlobalDiscoveryClient()

# Find all (client or server) applications registered in the GDS.
try:
    _, _, _, applicationDescriptionArray = globalDiscoveryClient.QueryApplications(
        gdsEndpointDescriptor,
        0,  # startingRecordId
        0,  # maximumRecordsToReturn
        '', # applicationName
        '', # applicationUriString
        UAApplicationTypes.All, # applicationTypes
        '', # productUriString
        Array.Empty[String](),  # serverCapabilities
        DateTime(), # out lastCounterResetTime
        0,  # out nextRecordId
        Array.Empty[UAApplicationDescription]()) # out applications
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# For each application returned by the query, find its registrations in the GDS.
for applicationDescription in applicationDescriptionArray:
    print()
    print('Application URI string: ', applicationDescription.ApplicationUriString, sep='')

    try:
        applicationRecordArray = globalDiscoveryClient.FindApplications(
            gdsEndpointDescriptor,
            applicationDescription.ApplicationUriString)
    except UAException as uaException:
        print('  *** Failure: ' + uaException.GetBaseException().Message)
        continue

    # Display results.
    for applicationRecord in applicationRecordArray:
        print('  Application ID: ', applicationRecord.ApplicationId, sep='')

print()
print('Finished.')

##endregion Example
