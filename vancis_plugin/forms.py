from django import forms

from virtualization.models import VirtualMachine
from dcim.models import Device
from tenancy.models import Tenant
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from .models import CMDBNumber, VirtualMachineData, NetworkDeviceData, SoftwarePackage, SoftwarePackageData, StorageCluster, StorageVolume

###############
# CMDB Number #
###############
class CMDBNumberForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = CMDBNumber
        fields = ('name', 'cmdb_number', 'comments', 'tags')


class CMDBNumberFilterForm(NetBoxModelFilterSetForm):
    model = CMDBNumber


###################
# Virtual Machine #
###################
class VirtualMachineDataForm(NetBoxModelForm):

    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all()
    )

    class Meta:
        model = VirtualMachineData
        fields = ('virtual_machine',)


class VirtualMachineDataFilterForm(NetBoxModelFilterSetForm):
    model = VirtualMachineData
    cmdb_number = forms.ModelMultipleChoiceField(
        queryset=CMDBNumber.objects.all(),
        required=False
    )


##################
# Network Device #
##################
class NetworkDeviceDataForm(NetBoxModelForm):
    network_device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )

    class Meta:
        model = NetworkDeviceData
        fields = ('network_device',)


class NetworkDeviceDataFilterForm(NetBoxModelFilterSetForm):
    model = NetworkDeviceData
    cmdb_number = forms.ModelMultipleChoiceField(
        queryset=CMDBNumber.objects.all(),
        required=False
    )


####################
# Software Package #
####################
class SoftwarePackageDataForm(NetBoxModelForm):
    software_package = DynamicModelChoiceField(
        queryset=SoftwarePackage.objects.all()
    )

    class Meta:
        model = SoftwarePackageData
        fields = ('software_package',)


class SoftwarePackageDataFilterForm(NetBoxModelFilterSetForm):
    model = SoftwarePackageData
    cmdb_number = forms.ModelMultipleChoiceField(
        queryset=CMDBNumber.objects.all(),
        required=False
    )


class SoftwarePackageForm(NetBoxModelForm):
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all()
    )

    dependency_servers = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all()
    )

    class Meta:
        model = SoftwarePackage
        fields = (
            'name',
            'version',
            'vendor',
            'status',
            'description',
            'documentatie',
            'ticket',
            'tenant',
            'dependency_servers'
        )


class SoftwarePackageFilterForm(NetBoxModelFilterSetForm):
    model = SoftwarePackage
    cmdb_number = forms.ModelMultipleChoiceField(
        queryset=CMDBNumber.objects.all(),
        required=False
    )


###########
# Storage #
###########
class StorageClusterForm(NetBoxModelForm):

    class Meta:
        model = StorageCluster
        fields = (
            'name',
            'totalSize',
        )

class StorageClusterFilterForm(NetBoxModelFilterSetForm):
    model = StorageCluster



class StorageVolumeForm(NetBoxModelForm):
    storageCluster = DynamicModelChoiceField(
        queryset=StorageCluster.objects.all()
    )

    class Meta:
        model = StorageVolume
        fields = (
            'storageCluster',
            'volumeID',
            'volName',
            'volSize',
            'tenant',
            'minIOPS',
            'scsiNAADeviceID',
        )


class StorageVolumeFilterForm(NetBoxModelFilterSetForm):
    model = StorageVolume