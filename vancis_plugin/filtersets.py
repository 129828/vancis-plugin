from netbox.filtersets import NetBoxModelFilterSet
from .models import CMDBNumber, VirtualMachineData, NetworkDeviceData, SoftwarePackage, SoftwarePackageData, StorageCluster, StorageVolume



class CMDBNumberFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = CMDBNumber
        fields = ('id', 'name', 'cmdb_number')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class SoftwarePackageFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = SoftwarePackage
        fields = ('id', 'name', 'version', 'vendor', 'status', 'tenant', 'description', 'dependency_servers', 'documentatie', 'ticket')

    def search(self, queryset, name, value):
        return queryset.filter(
            name__icontains=value
        )


class VirtualMachineDataFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VirtualMachineData
        fields = ('id', 'cmdb_number', 'virtual_machine')

    def search(self, queryset, name, value):
        return queryset.filter(cmdb_number__icontains=value)


class NetworkDeviceDataFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = NetworkDeviceData
        fields = ('id', 'cmdb_number', 'network_device')

    def search(self, queryset, name, value):
        return queryset.filter(cmdb_number__icontains=value)


class SoftwarePackageDataFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = SoftwarePackageData
        fields = ('id', 'cmdb_number', 'software_package')

    def search(self, queryset, name, value):
        return queryset.filter(cmdb_number__icontains=value)

class StorageClusterFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageCluster
        fields = ('id', 'name')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class StorageVolumeFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StorageVolume
        fields = ('id', 'volName', 'storageCluster', 'volumeID')

    def search(self, queryset, name, value):
        return queryset.filter(volName__icontains=value)
