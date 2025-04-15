from rest_framework import serializers

# from ipam.api.serializers import NestedPrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import CMDBNumber, VirtualMachineData, NetworkDeviceData, SoftwarePackage, SoftwarePackageData, StorageCluster, StorageVolume

#
# Nested serializers
#
class NestedCMDBNumberSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:cmdbnumber-detail'
    )

    class Meta:
        model = CMDBNumber
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number'
        )


class NestedVirtualMachineDataSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:virtualmachinedata-detail'
    )

    class Meta:
        model = VirtualMachineData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'network_device',
        )


class NestedSoftwarePackageDataSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:softwarepackagedata-detail'
    )

    class Meta:
        model = SoftwarePackageData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'software_package',
        )


class NestedNetworkDeviceDataSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:networkdevicedata-detail'
    )

    class Meta:
        model = VirtualMachineData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'network_device',
        )


class NestedSoftwarePackageSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:softwarepackage-detail'
    )

    class Meta:
        model = SoftwarePackage
        fields = (
            'id',
            'url',
            'display',
            'name',
            'version',
            'vendor',
            'status',
            'description',
            'documentatie',
            'ticket',
            'tenant',
            'dependency_servers',
            'CMDB',
        )


#
# Regular serializers
#

class CMDBNumberSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:cmdbnumber-detail'
    )

    class Meta:
        model = CMDBNumber
        fields = (
            'id',
            'url',
            'display',
            'name',
            'cmdb_number',
            'comments',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )


class VirtualMachineDataSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:virtualmachinedata-detail'
    )
    cmdb_number = NestedCMDBNumberSerializer

    class Meta:
        model = VirtualMachineData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'virtual_machine',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )


class NetworkDeviceDataSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:networkdevicedata-detail'
    )
    cmdb_number = NestedCMDBNumberSerializer

    class Meta:
        model = NetworkDeviceData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'network_device',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )


class SoftwarePackageDataSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:softwarepackagedata-detail'
    )
    cmdb_number = NestedCMDBNumberSerializer

    class Meta:
        model = SoftwarePackageData
        fields = (
            'id',
            'url',
            'display',
            'cmdb_number',
            'software_package',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )


class SoftwarePackageSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:softwarepackage-detail'
    )
    # CMDB = NestedCMDBNumberSerializer()

    class Meta:
        model = SoftwarePackage
        fields = (
            'id',
            'url',
            'display',
            'name',
            'version',
            'vendor',
            'status',
            'description',
            'documentatie',
            'ticket',
            'tenant',
            'dependency_servers',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
            'CMDB',
        )

class StorageClusterSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:storagecluster-detail'
    )

    class Meta:
        model = StorageCluster
        fields = (
            'id',
            'url',
            'display',
            'name',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )

class StorageVolumeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vancis_plugin-api:storagevolume-detail'
    )

    class Meta:
        model = StorageVolume
        fields = (
            'id',
            'url',
            'display',
            'storageCluster',
            'volumeID',
            'volName',
            'volSize',
            'minIOPS',
            'scsiNAADeviceID',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )