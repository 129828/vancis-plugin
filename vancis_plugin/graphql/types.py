from typing import Annotated, List

import strawberry
import strawberry_django

from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.scalars import BigInt


from vancis_plugin.models import (
    CMDBNumber,
    SoftwarePackage,
    VirtualMachineData,
    NetworkDeviceData,
    SoftwarePackageData,
    StorageCluster,
    StorageVolume,
)

from .filters import (
    CMDBNumberFilter,
    SoftwarePackageFilter,
    VirtualMachineDataFilter,
    NetworkDeviceDataFilter,
    SoftwarePackageDataFilter,
    StorageClusterFilter,
    StorageVolumeFilter,
)


@strawberry_django.type(CMDBNumber, fields="__all__", filters=CMDBNumberFilter)
class CMDBNumberType(NetBoxObjectType):
    name: str
    cmdb_number: int


@strawberry_django.type(SoftwarePackage, fields="__all__", filters=SoftwarePackageFilter)
class SoftwarePackageType(NetBoxObjectType):
    name: str
    version: str
    vendor: str
    status: str
    klant: Annotated["TenantType", strawberry.lazy("tenancy.graphql.types")] | None
    description: str
    dependency_servers: Annotated["VirtualMachineType", strawberry.lazy("virtualization.graphql.types")] | None
    documentatie: str
    ticket: str


@strawberry_django.type(SoftwarePackageData, fields="__all__", filters=SoftwarePackageDataFilter)
class SoftwarePackageDataType(NetBoxObjectType):
    cmdb_number: Annotated["CMDBNumberType", strawberry.lazy("vancis_plugin.graphql.types")] | None
    software_package: Annotated["SoftwarePackageType", strawberry.lazy("vancis_plugin.graphql.types")] | None


@strawberry_django.type(NetworkDeviceData, fields="__all__", filters=NetworkDeviceDataFilter)
class NetworkDeviceDataType(NetBoxObjectType):
    cmdb_number: Annotated["CMDBNumberType", strawberry.lazy("vancis_plugin.graphql.types")] | None
    network_device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None


@strawberry_django.type(VirtualMachineData, fields="__all__", filters=VirtualMachineDataFilter)
class VirtualMachineDataType(NetBoxObjectType):
    cmdb_number: Annotated["CMDBNumberType", strawberry.lazy("vancis_plugin.graphql.types")] | None
    virtual_machine: Annotated["VirtualMachineType", strawberry.lazy("virtualization.graphql.types")] | None


@strawberry_django.type(StorageCluster, fields="__all__", filters=StorageClusterFilter)
class StorageClusterType(NetBoxObjectType):
    name: str
    totalSize: BigInt


@strawberry_django.type(StorageVolume, fields="__all__", filters=StorageVolumeFilter)
class StorageVolumeType(NetBoxObjectType):
    storageCluster: Annotated["VirtualMachineType", strawberry.lazy("vancis_plugin.graphql.types")] | None
    volumeID: int
    volName: str
    volSize: BigInt
    minIOPS: int
    tenant: Annotated["TenantType", strawberry.lazy("tenancy.graphql.types")] | None
    scsiNAADeviceID: str
