# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to all dataset messages with specific publisher Id, on an OPC-UA PubSub connection
# with UDP UADP mapping.
#
# In order to produce network messages for this example, run the UADemoPublisher tool. For documentation, see
# https://kb.opclabs.com/UADemoPublisher_Basics . In some cases, you may have to specify the interface name to be used.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA.PubSub import *
from OpcLabs.EasyOpc.UA.PubSub.Configuration import *
from OpcLabs.EasyOpc.UA.PubSub.OperationModel import *


def dataSetMessage(sender, e):
    # Display the dataset.
    if e.Succeeded:
        # An event with null DataSetData just indicates a successful connection.
        if e.DataSetData is not None:
            print('')
            print('Dataset data: ', e.DataSetData, sep='')
            for pair in e.DataSetData.FieldDataDictionary:
                print(pair)
    else:
        print('')
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


# Define the PubSub connection we will work with. Uses implicit conversion from a string.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.udp://239.0.0.1')
# In some cases you may have to set the interface (network adapter) name that needs to be used, similarly to
# the statement below. Your actual interface name may differ, of course.
#pubSubConnectionDescriptor.ResourceAddress.InterfaceName = 'Ethernet'

# Define the arguments for subscribing to the dataset, where the filter is (unsigned 64-bit) publisher Id 31.
subscribeDataSetArguments = UASubscribeDataSetArguments(
    pubSubConnectionDescriptor,
    UASubscribeDataSetFilter(UAPublisherId.CreateUInt64(Decimal(31))))

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber, subscribeDataSetArguments)

print('Processing dataset message events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
subscriber.UnsubscribeAllDataSets()

print('Waiting for 1 second...')
# Unsubscribe operation is asynchronous, messages may still come for a short while.
time.sleep(1)

subscriber.DataSetMessage -= dataSetMessage

print('Finished.')

##endregion Example
