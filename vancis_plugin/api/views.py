
from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import CMDBNumberSerializer, VirtualMachineDataSerializer, NetworkDeviceDataSerializer, SoftwarePackageSerializer, SoftwarePackageDataSerializer, StorageVolumeSerializer, StorageClusterSerializer  # noqa: E501


class CMDBNumberViewSet(NetBoxModelViewSet):
    queryset = models.CMDBNumber.objects.prefetch_related(
        'tags'
    )
    serializer_class = CMDBNumberSerializer


class VirtualMachineDataViewSet(NetBoxModelViewSet):
    queryset = models.VirtualMachineData.objects.prefetch_related(
        'tags'
    )
    serializer_class = VirtualMachineDataSerializer
    filterset_class = filtersets.VirtualMachineDataFilterSet


class NetworkDeviceDataViewSet(NetBoxModelViewSet):
    queryset = models.NetworkDeviceData.objects.prefetch_related(
       'tags'
    )
    serializer_class = NetworkDeviceDataSerializer
    filterset_class = filtersets.NetworkDeviceDataFilterSet


class SoftwarePackageDataViewSet(NetBoxModelViewSet):
    queryset = models.SoftwarePackageData.objects.prefetch_related(
        'tags'
    )
    serializer_class = SoftwarePackageDataSerializer
    filterset_class = filtersets.SoftwarePackageDataFilterSet


class SoftwarePackageViewSet(NetBoxModelViewSet):
    queryset = models.SoftwarePackage.objects.prefetch_related(
        'tags'
    )
    serializer_class = SoftwarePackageSerializer
    filterset_class = filtersets.SoftwarePackageFilterSet


class StorageClusterViewSet(NetBoxModelViewSet):
    queryset = models.StorageCluster.objects.prefetch_related(
        'tags'
    )
    serializer_class = StorageClusterSerializer
    filterset_class = filtersets.StorageClusterFilterSet


class StorageVolumeViewSet(NetBoxModelViewSet):
    queryset = models.StorageVolume.objects.prefetch_related(
        'tags'
    )
    serializer_class = StorageVolumeSerializer
    filterset_class = filtersets.StorageVolumeFilterSet
