from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


#
# Object types
#

class CMDBNumberType(NetBoxObjectType):

    class Meta:
        model = models.CMDBNumber
        fields = '__all__'


class VirtualMachineDataType(NetBoxObjectType):

    class Meta:
        model = models.VirtualMachineData
        fields = '__all__'
        filterset_class = filtersets.VirtualMachineDataFilterSet


class NetworkDeviceDataType(NetBoxObjectType):

    class Meta:
        model = models.NetworkDeviceData
        fields = '__all__'
        filterset_class = filtersets.NetworkDeviceDataFilterSet


#
# Queries
#

class Query(ObjectType):
    cmdbnumber = ObjectField(CMDBNumberType)
    cmdbnumber_list = ObjectListField(CMDBNumberType)

    virtualmachinedata = ObjectField(VirtualMachineDataType)
    virtualmachinedata_list = ObjectListField(VirtualMachineDataType)

    NetworkDeviceData = ObjectField(NetworkDeviceDataType)
    NetworkDeviceData_list = ObjectListField(NetworkDeviceDataType)


schema = Query
