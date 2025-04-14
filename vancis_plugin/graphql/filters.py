import strawberry_django
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

from vancis_plugin.models import (
    CMDBNumber,
    SoftwarePackage,
    VirtualMachineData,
    NetworkDeviceData,
    SoftwarePackageData,
    StorageCluster,
    StorageVolume,
)

from vancis_plugin.fitlersets import (
    CMDBNumberFilterSet,
    SoftwarePackageFilterSet,
    VirtualMachineDataFilterSet,
    NetworkDeviceDataFilterSet,
    SoftwarePackageDataFilterSet,
    StorageClusterFilterSet,
    StorageVolumeFilterSet,
)

__all__ = (
    "CMDBNumberFilter",
    "SoftwarePackageFilter",
    "VirtualMachineDataFilter",
    "NetworkDeviceDataFilter",
    "SoftwarePackageDataFilter",
    "StorageClusterFilter",
    "StorageVolumeFilter",
)


@strawberry_django.filter(CMDBNumber, lookups=True)
@autotype_decorator(CMDBNumberFilterSet)
class CMDBNumberFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(SoftwarePackage, lookups=True)
@autotype_decorator(SoftwarePackageFilterSet)
class SoftwarePackageFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(VirtualMachineData, lookups=True)
@autotype_decorator(VirtualMachineDataFilterSet)
class VirtualMachineDataFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(NetworkDeviceData, lookups=True)
@autotype_decorator(NetworkDeviceDataFilterSet)
class NetworkDeviceDataFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(SoftwarePackageData, lookups=True)
@autotype_decorator(SoftwarePackageDataFilterSet)
class SoftwarePackageDataFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(StorageCluster, lookups=True)
@autotype_decorator(StorageClusterFilterSet)
class StorageClusterFilter(BaseFilterMixin):
    pass


@strawberry_django.filter(StorageVolume, lookups=True)
@autotype_decorator(StorageVolumeFilterSet)
class StorageVolumeFilter(BaseFilterMixin):
    pass
