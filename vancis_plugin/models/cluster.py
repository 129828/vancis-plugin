from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class StorageCluster(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    totalSize = models.BigIntegerField()

    class Meta:  # noqa: D106
        ordering = ('name',)

    @property
    def utilization(self):
        used_size = 0
        for volume in self.storageVolumes.all():
            used_size += volume.volSize
        return (used_size / self.totalSize) * 100

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:storagecluster', args=[self.pk])


class StorageVolume(NetBoxModel):
    storageCluster = models.ForeignKey(
        StorageCluster,
        related_name="storageVolumes",
        on_delete=models.CASCADE
    )
    volumeID = models.IntegerField()
    volName = models.CharField(max_length=100, unique=True)
    volSize = models.BigIntegerField()
    minIOPS = models.IntegerField()
    tenant = models.ForeignKey(
        'tenancy.Tenant',
        on_delete=models.CASCADE,
        help_text='Netbox: Tenant'
    )
    scsiNAADeviceID = models.CharField(max_length=100)

    class Meta:  # noqa: D106
        ordering = ('volName',)

    def __str__(self):
        return f"{self.volName} ({self.storageCluster.name})"

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:storagevolume', args=[self.pk])