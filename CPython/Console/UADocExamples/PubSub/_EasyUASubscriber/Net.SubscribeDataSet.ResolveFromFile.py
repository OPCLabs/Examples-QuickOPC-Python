# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to dataset messages and specify a filter, resolving logical parameters to physical
# from an OPC-UA PubSub configuration file in binary format. The metadata obtained through the resolution is used to
# decode fixed layout messages with RawData field encoding.
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
from OpcLabs.BaseLib import *
from OpcLabs.EasyOpc.UA.PubSub import *
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


def resolverAccess(sender, e):
    # Display resolution information.
    print(e)


# Define the PubSub resolver. We want the information be resolved from a PubSub binary configuration file that
# we have. The file itself is in this script's directory.
pubSubResolverDescriptor = UAPubSubResolverDescriptor.File(ResourceDescriptor('UADemoPublisher-Default.uabinary'))

# Define the PubSub connection we will work with, using its logical name in the PubSub configuration.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor()
pubSubConnectionDescriptor.Name = 'FixedLayoutConnection'
# In some cases you may have to set the interface (network adapter) name that needs to be used, similarly to
# the statement below. Your actual interface name may differ, of course.
#pubSubConnectionDescriptor.ResourceAddress.InterfaceName = 'Ethernet'

# Define the filter. The writer group and the dataset writer are specified using their logical names in the
# PubSub configuration. The publisher Id in the filter will be taken from the logical PubSub connection.
filter = UASubscribeDataSetFilter(
    UAWriterGroupDescriptor('FixedLayoutGroup'),
    UADataSetWriterDescriptor('SimpleWriter'))

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage
subscriber.ResolverAccess += resolverAccess

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber,
                                            pubSubResolverDescriptor,
                                            pubSubConnectionDescriptor,
                                            filter)

print('Processing dataset message events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
subscriber.UnsubscribeAllDataSets()

print('Waiting for 1 second...')
# Unsubscribe operation is asynchronous, messages may still come for a short while.
time.sleep(1)

subscriber.DataSetMessage -= dataSetMessage
subscriber.ResolverAccess -= resolverAccess

print('Finished.')

##endregion Example
