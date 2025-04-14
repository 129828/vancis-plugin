from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


#
# CMDBNumber views
#

class CMDBNumberView(generic.ObjectView):
    queryset = models.CMDBNumber.objects.all()


class CMDBNumberListView(generic.ObjectListView):
    queryset = models.CMDBNumber.objects.annotate()
    table = tables.CMDBNumberTable
    filterset = filtersets.CMDBNumberFilterSet
    filterset_form = forms.CMDBNumberFilterForm


class CMDBNumberEditView(generic.ObjectEditView):
    queryset = models.CMDBNumber.objects.all()
    form = forms.CMDBNumberForm


class CMDBNumberDeleteView(generic.ObjectDeleteView):
    queryset = models.CMDBNumber.objects.all()


class CMDBNumberBulkDeleteView(generic.BulkDeleteView):
    queryset = models.CMDBNumber.objects.annotate()
    filterset = filtersets.CMDBNumberFilterSet
    table = tables.CMDBNumberTable

#
# VirtualMachineData views
#

class VirtualMachineDataView(generic.ObjectView):
    queryset = models.VirtualMachineData.objects.all()


class VirtualMachineDataListView(generic.ObjectListView):
    queryset = models.VirtualMachineData.objects.all()
    table = tables.VirtualMachineDataTable
    filterset = filtersets.VirtualMachineDataFilterSet
    filterset_form = forms.VirtualMachineDataFilterForm


class VirtualMachineDataEditView(generic.ObjectEditView):
    queryset = models.VirtualMachineData.objects.all()
    form = forms.VirtualMachineDataForm


class VirtualMachineDataDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualMachineData.objects.all()

class VirtualMachineDataBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualMachineData.objects.annotate()
    filterset = filtersets.VirtualMachineDataFilterSet
    table = tables.VirtualMachineDataTable


#
# NetworkDeviceData views
#

class NetworkDeviceDataView(generic.ObjectView):
    queryset = models.NetworkDeviceData.objects.all()


class NetworkDeviceDataListView(generic.ObjectListView):
    queryset = models.NetworkDeviceData.objects.all()
    table = tables.NetworkDeviceDataTable
    filterset = filtersets.NetworkDeviceDataFilterSet
    filterset_form = forms.NetworkDeviceDataFilterForm


class NetworkDeviceDataEditView(generic.ObjectEditView):
    queryset = models.NetworkDeviceData.objects.all()
    form = forms.NetworkDeviceDataForm


class NetworkDeviceDataDeleteView(generic.ObjectDeleteView):
    queryset = models.NetworkDeviceData.objects.all()

class NetworkDeviceDataBulkDeleteView(generic.BulkDeleteView):
    queryset = models.NetworkDeviceData.objects.annotate()
    filterset = filtersets.NetworkDeviceDataFilterSet
    table = tables.NetworkDeviceDataTable


#
# SoftwarePackageData views
#

class SoftwarePackageDataView(generic.ObjectView):
    queryset = models.SoftwarePackageData.objects.all()


class SoftwarePackageDataListView(generic.ObjectListView):
    queryset = models.SoftwarePackageData.objects.all()
    table = tables.SoftwarePackageDataTable
    filterset = filtersets.SoftwarePackageDataFilterSet
    filterset_form = forms.SoftwarePackageDataFilterForm


class SoftwarePackageDataEditView(generic.ObjectEditView):
    queryset = models.SoftwarePackageData.objects.all()
    form = forms.SoftwarePackageDataForm


class SoftwarePackageDataDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwarePackageData.objects.all()

class SoftwarePackageDataBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwarePackageData.objects.annotate()
    filterset = filtersets.SoftwarePackageDataFilterSet
    table = tables.SoftwarePackageDataTable

#
# SoftwarePackage views
#

class SoftwarePackageView(generic.ObjectView):
    queryset = models.SoftwarePackage.objects.all()


class SoftwarePackageListView(generic.ObjectListView):
    queryset = models.SoftwarePackage.objects.all()
    table = tables.SoftwarePackageTable
    filterset = filtersets.SoftwarePackageFilterSet
    filterset_form = forms.SoftwarePackageFilterForm


class SoftwarePackageEditView(generic.ObjectEditView):
    queryset = models.SoftwarePackage.objects.all()
    form = forms.SoftwarePackageForm


class SoftwarePackageDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwarePackage.objects.all()

class SoftwarePackageBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwarePackage.objects.annotate()
    filterset = filtersets.SoftwarePackageFilterSet
    table = tables.SoftwarePackageTable



#
# StorageCluster views
#
class StorageClusterView(generic.ObjectView):
    queryset = models.StorageCluster.objects.all()
    
    def get_extra_context(self, request, instance):
        table = tables.StorageVolumeTable(instance.storageVolumes.all())
        table.configure(request)
        return {
            'storageVolumes_table': table,
        }


class StorageClusterListView(generic.ObjectListView):
    queryset = models.StorageCluster.objects.annotate()
    table = tables.StorageClusterTable
    filterset = filtersets.StorageClusterFilterSet
    filterset_form = forms.StorageClusterFilterForm


class StorageClusterEditView(generic.ObjectEditView):
    queryset = models.StorageCluster.objects.all()
    form = forms.StorageClusterForm


class StorageClusterDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageCluster.objects.all()


class StorageClusterBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageCluster.objects.annotate()
    filterset = filtersets.StorageClusterFilterSet
    table = tables.StorageClusterTable


#
# Storage Volume views
#
class StorageVolumeView(generic.ObjectView):
    queryset = models.StorageVolume.objects.all()


class StorageVolumeListView(generic.ObjectListView):
    queryset = models.StorageVolume.objects.annotate()
    table = tables.StorageVolumeTable
    filterset = filtersets.StorageVolumeFilterSet
    filterset_form = forms.StorageVolumeFilterForm


class StorageVolumeEditView(generic.ObjectEditView):
    queryset = models.StorageVolume.objects.all()
    form = forms.StorageVolumeForm


class StorageVolumeDeleteView(generic.ObjectDeleteView):
    queryset = models.StorageVolume.objects.all()


class StorageVolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.StorageVolume.objects.annotate()
    filterset = filtersets.StorageVolumeFilterSet
    table = tables.StorageVolumeTable