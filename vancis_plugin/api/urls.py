from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'vancis-plugin'

router = NetBoxRouter()
router.register('cmdb-number', views.CMDBNumberViewSet)
router.register('virtual-machine-data', views.VirtualMachineDataViewSet)
router.register('network-device-data', views.NetworkDeviceDataViewSet)
router.register('software-package-data', views.SoftwarePackageDataViewSet)
router.register('software-package', views.SoftwarePackageViewSet)
router.register('storage-cluster', views.StorageClusterViewSet)
router.register('storage-volume', views.StorageVolumeViewSet)

urlpatterns = router.urls
