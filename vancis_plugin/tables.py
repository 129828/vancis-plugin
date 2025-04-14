from django_tables2.utils import A
import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns
from .models import CMDBNumber, VirtualMachineData, NetworkDeviceData, SoftwarePackage, SoftwarePackageData, StorageCluster, StorageVolume


class CMDBNumberTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    connected_object = tables.Column(
        linkify=True,
        accessor=A('linked_object')
    )

    class Meta(NetBoxTable.Meta):
        model = CMDBNumber
        fields = (
            'pk', 'id', 'name', 'connected_object', 'cmdb_number'
        )
        default_columns = (
            'name', 'connected_object', 'cmdb_number'
        )


class VirtualMachineDataTable(NetBoxTable):
    cmdb_number = tables.Column(
        linkify=True
    )
    virtual_machine = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = VirtualMachineData
        fields = (
            'pk', 'id', 'cmdb_number', 'virtual_machine'
        )
        default_columns = (
            'cmdb_number', 'virtual_machine'
        )


class NetworkDeviceDataTable(NetBoxTable):
    cmdb_number = tables.Column(
        linkify=True
    )
    network_device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = NetworkDeviceData
        fields = (
            'pk', 'id', 'cmdb_number', 'network_device'
        )
        default_columns = (
            'cmdb_number', 'network_device'
        )


class SoftwarePackageDataTable(NetBoxTable):
    cmdb_number = tables.Column(
        linkify=True
    )
    software_package = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwarePackageData
        fields = (
            'pk', 'id', 'cmdb_number', 'software_package'
        )
        default_columns = (
            'cmdb_number', 'software_package'
        )


DPENDENCY_SERVERS_HTML = """
{% for server in value.all %}
    <a href="{{ server.get_absolute_url }}">{{ server }}</a><br />
{% endfor %}
"""

class SoftwarePackageTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    tenant = tables.Column(
        linkify=True
    )
    dependency_servers = columns.TemplateColumn(
        template_code=DPENDENCY_SERVERS_HTML,
        orderable=False,
        verbose_name='Dependency Servers'
    )
    CMDB = tables.Column(
        verbose_name='CMDB'
    )

    class Meta(NetBoxTable.Meta):
        model = SoftwarePackage
        fields = (
            'pk', 'id', 'name',
            'version',
            'vendor',
            'status',
            'description',
            'documentatie',
            'ticket',
            'tenant',
            'dependency_servers',
            'CMDB'
        )
        default_columns = (
            'name', 'version', 'tenant', 'dependency_servers',
            'CMDB'
        )


class PrefixUtilizationColumn(columns.UtilizationColumn):
    """
    Extend UtilizationColumn to allow disabling the warning & danger thresholds for prefixes
    marked as fully utilized.
    """
    template_code = """
    {% load helpers %}
    {% utilization_graph value %}
    """

class StorageClusterTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    utilization = PrefixUtilizationColumn(
        accessor='utilization',
        orderable=False
    )
    class Meta(NetBoxTable.Meta):
        model = StorageCluster
        fields = (
            'pk', 
            'id', 
            'name', 
            'utilization',
            'totalSize',
        )
        default_columns = (
            'name', 
            'utilization',
            'totalSize',
        )


class StorageVolumeTable(NetBoxTable):
    storageCluster = tables.Column(
        linkify=True
    )
    volName = tables.Column(
        linkify=True
    )
    tenant = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StorageVolume
        fields = (
            'pk', 'id', 
            'storageCluster',
            'tenant',
            'volumeID',
            'volName',
            'volSize',
            'minIOPS',
            'scsiNAADeviceID'
        )
        default_columns = (
            'volName', 'storageCluster' , 'volSize', 'tenant'
        )
