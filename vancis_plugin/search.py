from netbox.search import SearchIndex, register_search
from .models import CMDBNumber, VirtualMachineData, NetworkDeviceData, SoftwarePackage, SoftwarePackageData, StorageCluster, StorageVolume


@register_search
class CMDBNumberIndex(SearchIndex):
    model = CMDBNumber
    fields = (
        ('name', 100),
        ('comments', 5000),
    )


@register_search
class VirtualMachineDataIndex(SearchIndex):
    model = VirtualMachineData
    fields = (
        ('cmdb_number', 100),
    )


@register_search
class NetworkDeviceDataIndex(SearchIndex):
    model = NetworkDeviceData
    fields = (
        ('cmdb_number', 100),
    )


@register_search
class SoftwarePackageDataIndex(SearchIndex):
    model = SoftwarePackageData
    fields = (
        ('cmdb_number', 100),
    )


@register_search
class SoftwarePackageIndex(SearchIndex):
    model = SoftwarePackage
    fields = (
        ('name', 100),
        ('CMDB', 100),
    )

@register_search
class StorageClusterIndex(SearchIndex):
    model = StorageCluster
    fields = (
        ('name', 100),
    )

@register_search
class StorageVolumeIndex(SearchIndex):
    model = StorageVolume
    fields = (
        ('volName', 100),
    )
