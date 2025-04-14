from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

# app_name = "vancis_plugin"

urlpatterns = (

    # Access lists
    path('cmdbnumber/', views.CMDBNumberListView.as_view(), name='cmdbnumber_list'),
    path('cmdbnumber/add/', views.CMDBNumberEditView.as_view(), name='cmdbnumber_add'),
    path('cmdbnumber/delete/', views.CMDBNumberBulkDeleteView.as_view(), name='cmdbnumber_bulk_delete'),
    path('cmdbnumber/<int:pk>/', views.CMDBNumberView.as_view(), name='cmdbnumber'),
    path('cmdbnumber/<int:pk>/edit/', views.CMDBNumberEditView.as_view(), name='cmdbnumber_edit'),
    path('cmdbnumber/<int:pk>/delete/', views.CMDBNumberDeleteView.as_view(), name='cmdbnumber_delete'),
    path('cmdbnumber/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='cmdbnumber_changelog', kwargs={
        'model': models.CMDBNumber
    }),

    # Access list rules
    path('virtualmachinedata/', views.VirtualMachineDataListView.as_view(), name='virtualmachinedata_list'),
    path('virtualmachinedata/add/', views.VirtualMachineDataEditView.as_view(), name='virtualmachinedata_add'),
    path('virtualmachinedata/delete/', views.VirtualMachineDataBulkDeleteView.as_view(), name='virtualmachinedata_bulk_delete'),
    path('virtualmachinedata/<int:pk>/', views.VirtualMachineDataView.as_view(), name='virtualmachinedata'),
    path('virtualmachinedata/<int:pk>/edit/', views.VirtualMachineDataEditView.as_view(), name='virtualmachinedata_edit'),
    path('virtualmachinedata/<int:pk>/delete/', views.VirtualMachineDataDeleteView.as_view(), name='virtualmachinedata_delete'),
    path('virtualmachinedata/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualmachinedata_changelog', kwargs={
        'model': models.VirtualMachineData
    }),

    # Access list rules
    path('networkdevicedata/', views.NetworkDeviceDataListView.as_view(), name='networkdevicedata_list'),
    path('networkdevicedata/add/', views.NetworkDeviceDataEditView.as_view(), name='networkdevicedata_add'),
    path('networkdevicedata/delete/', views.NetworkDeviceDataBulkDeleteView.as_view(), name='networkdevicedata_bulk_delete'),
    path('networkdevicedata/<int:pk>/', views.NetworkDeviceDataView.as_view(), name='networkdevicedata'),
    path('networkdevicedata/<int:pk>/edit/', views.NetworkDeviceDataEditView.as_view(), name='networkdevicedata_edit'),
    path('networkdevicedata/<int:pk>/delete/', views.NetworkDeviceDataDeleteView.as_view(), name='networkdevicedata_delete'),
    path('networkdevicedata/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='networkdevicedata_changelog', kwargs={
        'model': models.NetworkDeviceData
    }),

    # Access list rules
    path('softwarepackage/', views.SoftwarePackageListView.as_view(), name='softwarepackage_list'),
    path('softwarepackage/add/', views.SoftwarePackageEditView.as_view(), name='softwarepackage_add'),
    path('softwarepackage/delete/', views.SoftwarePackageBulkDeleteView.as_view(), name='softwarepackage_bulk_delete'),
    path('softwarepackage/<int:pk>/', views.SoftwarePackageView.as_view(), name='softwarepackage'),
    path('softwarepackage/<int:pk>/edit/', views.SoftwarePackageEditView.as_view(), name='softwarepackage_edit'),
    path('softwarepackage/<int:pk>/delete/', views.SoftwarePackageDeleteView.as_view(), name='softwarepackage_delete'),
    path('softwarepackage/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='softwarepackage_changelog', kwargs={
        'model': models.SoftwarePackage
    }),

    # Access list rules
    path('softwarepackagedata/', views.SoftwarePackageDataListView.as_view(), name='softwarepackagedata_list'),
    path('softwarepackagedata/add/', views.SoftwarePackageDataEditView.as_view(), name='softwarepackagedata_add'),
    path('softwarepackagedata/delete/', views.SoftwarePackageDataBulkDeleteView.as_view(), name='softwarepackagedata_bulk_delete'),
    path('softwarepackagedata/<int:pk>/', views.SoftwarePackageDataView.as_view(), name='softwarepackagedata'),
    path('softwarepackagedata/<int:pk>/edit/', views.SoftwarePackageDataEditView.as_view(), name='softwarepackagedata_edit'),
    path('softwarepackagedata/<int:pk>/delete/', views.SoftwarePackageDataDeleteView.as_view(), name='softwarepackagedata_delete'),
    path('softwarepackagedata/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='softwarepackagedata_changelog', kwargs={
        'model': models.SoftwarePackageData
    }),

    # Access list rules
    path('storagecluster/', views.StorageClusterListView.as_view(), name='storagecluster_list'),
    path('storagecluster/add/', views.StorageClusterEditView.as_view(), name='storagecluster_add'),
    path('storagecluster/delete/', views.StorageClusterBulkDeleteView.as_view(), name='storagecluster_bulk_delete'),
    path('storagecluster/<int:pk>/', views.StorageClusterView.as_view(), name='storagecluster'),
    path('storagecluster/<int:pk>/edit/', views.StorageClusterEditView.as_view(), name='storagecluster_edit'),
    path('storagecluster/<int:pk>/delete/', views.StorageClusterDeleteView.as_view(), name='storagecluster_delete'),
    path('storagecluster/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagecluster_changelog', kwargs={
        'model': models.StorageCluster
    }),

     # Access list rules
    path('storagevolume/', views.StorageVolumeListView.as_view(), name='storagevolume_list'),
    path('storagevolume/add/', views.StorageVolumeEditView.as_view(), name='storagevolume_add'),
    path('storagevolume/delete/', views.StorageVolumeBulkDeleteView.as_view(), name='storagevolume_bulk_delete'),
    path('storagevolume/<int:pk>/', views.StorageVolumeView.as_view(), name='storagevolume'),
    path('storagevolume/<int:pk>/edit/', views.StorageVolumeEditView.as_view(), name='storagevolume_edit'),
    path('storagevolume/<int:pk>/delete/', views.StorageVolumeDeleteView.as_view(), name='storagevolume_delete'),
    path('storagevolume/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='storagevolume_changelog', kwargs={
        'model': models.StorageVolume
    }),


)
