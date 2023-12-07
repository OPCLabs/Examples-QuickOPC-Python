# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to all dataset messages on an OPC-UA PubSub connection with Ethernet UADP mapping.
#
# In order to produce network messages for this example, run the UADemoPublisher tool. For documentation, see
# http://kb.opclabs.com/UADemoPublisher_Basics . In some cases, you may have to specify the interface name to be used.
# The UADemoPublisher must be told to use the Ethernet transport: run it with the -eth switch on the command line.
#
# The OpcLabs.Pcap assembly needs to be referenced in your project (or otherwise made available, together with its
# dependencies) for the Ethernet transport to work, and additional software installation may be needed as well. Refer to
# the documentation for more information.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import opclabs_pcap
import time

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA.PubSub import *
from OpcLabs.EasyOpc.UA.PubSub.Extensions import *
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
# "opc.eth" is the scheme for OPC UA Ethernet. "FF-FF-FF-FF-FF-FF" is the Ethernet broadcast address.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.eth://FF-FF-FF-FF-FF-FF')
# In some cases you may have to set the interface (network adapter) name that needs to be used, similarly to
# the statement below. Your actual interface name may differ, of course.
#pubSubConnectionDescriptor.ResourceAddress.InterfaceName = 'Ethernet'

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber, pubSubConnectionDescriptor)

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
